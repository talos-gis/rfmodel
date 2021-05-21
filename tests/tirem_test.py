from numpy.testing import assert_almost_equal

from rfmodel.read_profile import read_profile
from rfmodel.rfmodel_types import RFModelPolarization, RFModelReturn
from tirem.tirem3 import calc_tirem_loss


def test_tirem():
    filename = 'data/ELEV3.DAT'
    dist, elev = read_profile(filename)
    assert len(dist) == len(elev) == 250

    base = dict(
        refractivity=301,
        conductivity=0.028,
        permittivity=15,
        humidity=10,
    )
    io = [
        (
            dict(
                tx_antenna_height=2,
                rx_antenna_height=2,
                frequency=300,
                polarization=RFModelPolarization.V,
            ),
            RFModelReturn(
                fresnel_clearance=0.0,
                total_loss=179.916,
                free_space_loss=123.894,
                version='TIREM-5.',
                propagation_mode='DIF')
        ),
        (
            dict(
                tx_antenna_height=2,
                rx_antenna_height=2,
                frequency=300,
                polarization=RFModelPolarization.H,
            ),
            RFModelReturn(
                fresnel_clearance=0.0,
                total_loss=179.916,
                free_space_loss=123.894,
                version='TIREM-5.',
                propagation_mode='DIF')
        ),
        (
            dict(
                tx_antenna_height=1000,
                rx_antenna_height=1000,
                frequency=300,
                polarization=RFModelPolarization.V,
            ),
            RFModelReturn(
                fresnel_clearance=0.510532,
                total_loss=124.16,
                free_space_loss=123.894,
                version='TIREM-5.',
                propagation_mode='LOS')
        ),
    ]
    for i, o in io:
        res = calc_tirem_loss(num_profile_points=len(elev), profile_elevation=elev, profile_distance=dist, **i, **base)
        o.assert_equal(res, decimal=3)
