from enum import IntEnum
from typing import NamedTuple

from numpy.testing import assert_almost_equal


class RFModelReturn(NamedTuple):
    """
    fresnel_clearance: The ratio of the minimum clearance of the ray path to the first Fresnel zone radius
    total_loss: Total Path loss (Basic transmission loss) [dB]
    free_space_loss: Free space loss [dB]
    version: Model version number
    propagation_mode: Mode indicator
    """
    fresnel_clearance: float
    total_loss: float
    free_space_loss: float
    version: str
    propagation_mode: str

    def assert_equal(self: 'RFModelReturn', other: 'RFModelReturn', decimal=7):
        assert_almost_equal(self[0:3], other[0:3], decimal=decimal)
        assert self[3:] == other[3:]


class RFModelPolarization(IntEnum):
    H = 0
    V = 1
