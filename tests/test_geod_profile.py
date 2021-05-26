import timeit

import numpy as np
from numpy.testing import assert_almost_equal

from rfmodel.geod.geod_profile import Geod, geod_profile


def test_profile(do_print=False):
    filename = 'data/srtm_30k.tif'
    boston_lat = 42. + (15. / 60.)
    boston_lon = -71. - (7. / 60.)
    portland_lat = 45. + (31. / 60.)
    portland_lon = -123. - (41. / 60.)
    lon1 = boston_lon
    lat1 = boston_lat
    lon2 = portland_lon
    lat2 = portland_lat

    g = Geod(ellps='WGS84')

    exp_lons = np.array([-71.11666667, -83.34059574, -96.62663201, -110.34290056, -123.68333333])
    exp_lats = np.array([42.25, 45.35040408, 47.01585593, 47.07341669, 45.51666667])
    exp_alts = np.array([56, 181, 278, 1767, 495])

    for npts, del_s in [(5, 0), (0, 1_000_000)]:
        geod_res, alts = geod_profile(
            filename, g=g,
            lon1=lon1, lat1=lat1, lon2=lon2, lat2=lat2, npts=npts, del_s=del_s)
        lons, lats = geod_res.lons, geod_res.lats

        lons = np.array(lons)
        lats = np.array(lats)
        alts = np.array(alts[0])

        if do_print:
            for x, y, z in list(zip(lons, lats, alts)):
                print(f"{x:8.3f} {y:8.3f} {z:12.3f}")

        assert_almost_equal(lons, exp_lons)
        assert_almost_equal(lats, exp_lats)
        assert_almost_equal(alts, exp_alts)


if __name__ == '__main__':
    do_time = False
    bench_count = 1
    repeat_count = 10
    if do_time:
        t = timeit.timeit(
            'test_profile()',
            setup='from __main__ import test_profile',
            number=repeat_count)
        print(t)
    else:
        test_profile(do_print=True)
