from typing import Tuple, Optional, Union

from osgeo import osr
import numpy as np
import pyproj

from osgeo_utils.auxiliary.osr_util import get_srs
from rfmodel.util import version_tuple

pyproj_version = version_tuple(pyproj.__version__)
if pyproj_version >= (3, 1):
    from pyproj.geod import Geod, GeodIntermediateReturn
else:
    from rfmodel.geod.geod_backport import Geod, GeodIntermediateReturn

from osgeo_utils.auxiliary.util import PathOrDS, open_ds, get_pixel_size
from osgeo_utils.samples.gdallocationinfo import gdallocationinfo

g_wgs84 = Geod(ellps='WGS84')


def get_resolution_meters(filename_or_ds: PathOrDS):
    ds = open_ds(filename_or_ds)
    resolution, _ = get_pixel_size(ds)
    srs = get_srs(ds)
    if srs.IsGeographic():
        resolution *= 111_111  # deg to meter
    return resolution


def geod_profile(filename_or_ds: PathOrDS, band_nums=None, srs=4326, ovr_idx: Optional[Union[int, float]] = None,
                 g: Geod = None, only_geod: bool = False,
                 npts: int = 0, del_s: float = 0,
                 initial_idx: int = 0, terminus_idx: int = 0,
                 **kwargs) -> \
        Tuple[GeodIntermediateReturn, Optional[np.ndarray]]:
    if g is None:
        g = g_wgs84
    if npts == del_s == 0:
        filename_or_ds = open_ds(filename_or_ds)
        del_s = get_resolution_meters(filename_or_ds)
    geod_res = g.inv_intermediate(npts=npts, del_s=del_s,
                                  initial_idx=initial_idx, terminus_idx=terminus_idx, **kwargs)
    lons, lats = geod_res.lons, geod_res.lats
    if only_geod:
        raster_values = None
    else:
        pixels, lines, raster_values = gdallocationinfo(
            filename_or_ds, band_nums=band_nums, x=lons, y=lats, srs=srs,
            inline_xy_replacement=False, ovr_idx=ovr_idx,
            axis_order=osr.OAMS_TRADITIONAL_GIS_ORDER)
    return geod_res, raster_values
