from typing import Tuple, Optional, Union

from osgeo import osr
import numpy as np
from tirem.geod.geod_backport import Geod, GeodIntermediateReturn

from osgeo_utils.auxiliary.util import PathOrDS
from osgeo_utils.samples.gdallocationinfo import gdallocationinfo

g_wgs84 = Geod(ellps='WGS84')


def geod_profile(filename_or_ds: PathOrDS, band_nums=None, srs=4326, ovr_idx: Optional[Union[int, float]] = None,
                 g: Geod = None, only_geod: bool = False,
                 initial_idx: int = 0, terminus_idx: int = 0, **kwargs) -> \
        Tuple[GeodIntermediateReturn, Optional[np.ndarray]]:
    if g is None:
        g = g_wgs84
    geod_res = g.inv_intermediate(initial_idx=initial_idx, terminus_idx=terminus_idx, **kwargs)
    lons, lats = geod_res.lons, geod_res.lats
    if only_geod:
        raster_res = None
    else:
        pixels, lines, raster_res = gdallocationinfo(
            filename_or_ds, band_nums=band_nums, x=lons, y=lats, srs=srs,
            inline_xy_replacement=False, ovr_idx=ovr_idx,
            axis_order=osr.OAMS_TRADITIONAL_GIS_ORDER)
    return geod_res, raster_res
