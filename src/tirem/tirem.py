import numpy as np

from osgeo_utils.auxiliary.base import PathLikeOrStr
from tirem.geod.geod_profile import geod_profile
from tirem.tirem3 import calc_tirem_loss


def calc_tirem_loss_lonlat(
        filename: PathLikeOrStr,
        profile_options: dict, tirem_options: dict,
        tx_antenna_height: float, rx_antenna_height: float,
        tx_msl: bool = False, rx_msl: bool = False,
        print_debug: bool = False):

    geod_res, raster_res = geod_profile(filename_or_ds=filename, **profile_options)
    npts = geod_res.npts
    dtype = np.float32
    profile_distance = np.arange(npts, dtype=dtype)
    profile_distance *= geod_res.del_s
    profile_elevation = np.array(raster_res[0], dtype=dtype)

    if not tx_msl:
        tx_antenna_height += profile_elevation[0]
    if not rx_msl:
        rx_antenna_height += profile_elevation[-1]

    res = calc_tirem_loss(tx_antenna_height=tx_antenna_height, rx_antenna_height=rx_antenna_height,
                          num_profile_points=npts, profile_elevation=profile_elevation,
                          profile_distance=profile_distance, **tirem_options)

    if print_debug:
        print(f'profile options: {profile_options}')
        print(f'tirem options: {tirem_options}')
        print(geod_res)
        print(f'Profile Elevation: {profile_elevation}')
        print(f'Profile Distance: {profile_distance}')
        print(res)

    return res

