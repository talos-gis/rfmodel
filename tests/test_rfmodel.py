from rfmodel.rfmodel import calc_path_loss_lonlat
from rfmodel.rfmodel_types import RFModelPolarization, RFModelReturn
from tirem.tirem3 import calc_tirem_loss


def test_calc_loss_lonlat():
    filename = 'data/srtm_30k_global.tif'

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
    rfmodel_options = dict(
        frequency=3000.0, polarization=RFModelPolarization.H,
        refractivity=300.0, conductivity=0.003, permittivity=10.0, humidity=10.0)

    print_debug = False
    res = calc_path_loss_lonlat(
        calc_tirem_loss, filename,
        profile_options=profile_options, rfmodel_options=rfmodel_options,
        tx_antenna_height=5, rx_antenna_height=5, tx_msl=tx_msl, rx_msl=rx_msl,
        print_debug=print_debug)

    expected = RFModelReturn(
        fresnel_clearance=0.0, total_loss=655.2137451, free_space_loss=174.63401794433594,
        version='TIREM-5.', propagation_mode='TRO')

    expected.assert_equal(res)
