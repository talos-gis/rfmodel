from collections import namedtuple

from rfmodel.rfmodel_types import RFModelPolarization, RFModelReturn

include "base.pxi"
from libc.string cimport memset
from tirem cimport _tirem3  # Import the pxd "header"
cimport cython

_TiremReturn = namedtuple("RFModelReturn", ['fresnel_clearance', 'total_loss', 'free_space_loss', 'version', 'propagation_mode'])

cdef char[17] _activation
memset(_activation, 0x20, 16)
_activation[16] = 0

def tirem_set_activation_key(key: str):
    c = min(len(key), 16)
    for i in range(c):
        _activation[i] = key[i]
    _activation[c] = 0

@cython.boundscheck(False)
@cython.wraparound(False)
def calc_tirem_loss(
        tx_antenna_height: float, rx_antenna_height: float, frequency: float,
        num_profile_points: int, profile_elevation: object, profile_distance: object,
        refractivity: float, conductivity: float, permittivity: float, humidity: float,
        polarization: RFModelPolarization,
        extension: bool = False,
    ) -> RFModelReturn:

    cdef PyBuffWriteManagerF profile_elevation_buff = PyBuffWriteManagerF(profile_elevation)
    cdef PyBuffWriteManagerF profile_distance_buff = PyBuffWriteManagerF(profile_distance)

    cdef float fresnel_clearance, total_loss, free_space_loss

    cdef char[5] _polarization
    cdef char[9] version
    cdef char[5] propagation_mode

    _polarization[0] = 'V' if polarization == RFModelPolarization.V else 'H'
    _polarization[1] = 0

    _tirem3.CalcTiremLoss(
        tx_antenna_height=tx_antenna_height,
        rx_antenna_height=rx_antenna_height,
        frequency=frequency,
        num_profile_points=num_profile_points,
        profile_elevation=profile_elevation_buff.data, profile_distance=profile_distance_buff.data,
        extension=extension,
        refractivity=refractivity, conductivity=conductivity, permittivity=permittivity, humidity=humidity,
        polarization=_polarization, version=version, propagation_mode=propagation_mode,
        fresnel_clearance=&fresnel_clearance, total_loss=&total_loss, free_space_loss=&free_space_loss,
        activation_key=_activation,
    )
    return _TiremReturn(fresnel_clearance, total_loss, free_space_loss,
                        version.decode().strip(), propagation_mode.decode().strip())
