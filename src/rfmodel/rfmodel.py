from typing import Any, Callable, Sequence, Dict

import numpy as np

from osgeo_utils.auxiliary.util import PathOrDS
from rfmodel.geod.geod_profile import geod_profile
from rfmodel.rfmodel_types import RFModelReturn


def calc_path_loss_lonlat(
        calc_loss: Callable[[Any], RFModelReturn],
        filename_or_ds: PathOrDS,
        profile_options: dict, rfmodel_options: dict,
        tx_antenna_height: float, rx_antenna_height: float,
        tx_msl: bool = False, rx_msl: bool = False,
        print_debug: bool = False) -> RFModelReturn:

    geod_res, raster_res = geod_profile(filename_or_ds=filename_or_ds, **profile_options)
    npts = geod_res.npts
    dtype = np.float32
    profile_distance = np.arange(npts, dtype=dtype)
    profile_distance *= geod_res.del_s
    profile_elevation = np.array(raster_res[0], dtype=dtype)

    if not tx_msl:
        tx_antenna_height += profile_elevation[0]
    if not rx_msl:
        rx_antenna_height += profile_elevation[-1]

    res = calc_loss(tx_antenna_height=tx_antenna_height, rx_antenna_height=rx_antenna_height,
                    num_profile_points=npts, profile_elevation=profile_elevation,
                    profile_distance=profile_distance, **rfmodel_options)

    if print_debug:
        print(f'Profile options: {profile_options}')
        print(f'RfModel options: {rfmodel_options}')
        print(geod_res)
        print(f'Profile Elevation: {profile_elevation}')
        print(f'Profile Distance: {profile_distance}')
        print(res)

    return res


def get_dict_of_items_from_dict_of_sequences(d: Dict[Any, Sequence], index: int) -> Dict[Any, Any]:
    return {k: (v[index % len(v)] if isinstance(v, Sequence) else v) for k, v in d.items()}


def calc_path_loss_lonlat_multi(
        calc_loss: Callable[[Any], RFModelReturn],
        filename_or_ds: PathOrDS,
        count: int, main_options: dict,
        profile_options: dict, rfmodel_options: dict,
        **kwargs) -> np.ndarray:

    a = np.empty((3, count), dtype=np.float32)
    for i in range(count):
        res = calc_path_loss_lonlat(
            calc_loss=calc_loss,
            filename_or_ds=filename_or_ds,
            **get_dict_of_items_from_dict_of_sequences(main_options, i),
            profile_options=get_dict_of_items_from_dict_of_sequences(profile_options, i),
            rfmodel_options=get_dict_of_items_from_dict_of_sequences(rfmodel_options, i), **kwargs)
        a[:, i] = res[0:3]

    return a

