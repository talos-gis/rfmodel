from numpy.testing import assert_almost_equal

from tirem.tirem import calc_tirem_loss_lonlat
from tirem.tirem_types import TiremPolarization, TiremReturn


def test_calc_tirem_loss_lonlat():
    filename = '../data/srtm_lowres.tif'

    boston_lat = 42. + (15. / 60.)
    boston_lon = -71. - (7. / 60.)
    portland_lat = 45. + (31. / 60.)
    portland_lon = -123. - (41. / 60.)
    lon1 = boston_lon
    lat1 = boston_lat
    lon2 = portland_lon
    lat2 = portland_lat

    del_s = 500
    tx_msl = False
    rx_msl = False

    profile_options = dict(lon1=lon1, lat1=lat1, lon2=lon2, lat2=lat2, del_s=del_s)
    tirem_options = dict(
        frequency=3000.0, polarization=TiremPolarization.H,
        refractivity=300.0, conductivity=0.003, permittivity=10.0, humidity=10.0)

    print_debug = True
    res = calc_tirem_loss_lonlat(
        filename,
        profile_options=profile_options, tirem_options=tirem_options,
        tx_antenna_height=5, rx_antenna_height=5, tx_msl=tx_msl, rx_msl=rx_msl,
        print_debug=print_debug)

    expected = TiremReturn(fresnel_clearance=0.0, total_loss=670.5097045898438, free_space_loss=174.6343536376953,
                           version='TIREM-5.', propagation_mode='TRO ')

    assert_almost_equal(res[0:2], expected[0:2])
    assert res[2:] == expected[2:]
