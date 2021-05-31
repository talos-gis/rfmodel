from collections import namedtuple
from typing import NamedTuple

include "base.pxi"
from libc.string cimport memset
from tirem cimport _tirem3  # Import the pxd "header"
cimport cython

_TiremReturn = namedtuple("RFModelReturn", ['fresnel_clearance', 'total_loss', 'free_space_loss', 'version', 'propagation_mode'])

class TiremReturn(NamedTuple):
    """
    TIREM return value.
    Typed version of _TiremReturn (which we use because of a bug in Cython that doesn't work with NamedTuple)

    fresnel_clearance: The ratio of the minimum clearance of the ray path to the first Fresnel zone radius
    total_loss: Total Path loss (Basic transmission loss) [dB]
    free_space_loss: Free space loss [dB]
    version: TIREM version number
    propagation_mode: Mode indicator
        "LOS " - Line-of-sight,
        "DIF " - Diffraction,
        "TRO " - Troposcatter,
        "INVL" - Invalid license (Activation key)
    """
    fresnel_clearance: float
    total_loss: float
    free_space_loss: float
    version: str
    propagation_mode: str

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
        polarization: bool,
        extension: bool = False,
    ) -> TiremReturn:

    """

    :param tx_antenna_height: Transmitter structural antenna height in meters. Range: 0.0 to 30000.0 m
    :param rx_antenna_height: Receiver structural antenna height in meters. Range: 0.0 to 30000.0 m
    :param frequency: Transmitter frequency in MHz. Range: 1.0 to 40000.0 MHz
    :param num_profile_points: Total number of profile points for the entire path. Range: > 2
    :param profile_elevation: Array of profile terrain heights above mean sea level in meters. Range: -450.0 to 9000.0 m
    :param profile_distance: Array of great circle distances from the beginning of the profile to each profile point in meters. Range:> 0.0
    :param refractivity: Surface refractivity in N-units. Range: 200.0 to 450.0 N.
    :param conductivity: Conductivity of earth surface Siemans per meter. Range: 0.00001 to 100.0 S/m
    :param permittivity: permit Relative permittivity of earth surface. Range: 1.0 to 100.0
    :param humidity: humid Surface humidity at the transmitter site in grams per cubic meter. Range: 0.0 to 110.0 in g/m^3
    :param polarization: Transmitter antenna polarization, 'Vertical' if polarization else 'Horizontal'
    :param extension: Profile indicator flag: TRUE - Current profile is an extension of the last path along a radial FALSE- New profile
    :return: TiremReturn
    """

    cdef PyBuffWriteManagerF profile_elevation_buff = PyBuffWriteManagerF(profile_elevation)
    cdef PyBuffWriteManagerF profile_distance_buff = PyBuffWriteManagerF(profile_distance)

    cdef float fresnel_clearance, total_loss, free_space_loss

    cdef char[5] _polarization
    cdef char[9] version
    cdef char[5] propagation_mode

    _polarization[0] = 'V' if polarization else 'H'
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
