from enum import IntEnum
from typing import NamedTuple


class TiremReturn(NamedTuple):
    fresnel_clearance: float
    total_loss: float
    free_space_loss: float
    version: str
    propagation_mode: str


class TiremPolarization(IntEnum):
    H = 0
    V = 1
