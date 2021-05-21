from typing import Tuple

import numpy as np


def read_profile(filename: str) -> Tuple[np.ndarray, np.ndarray]:
    with open(filename, 'r') as f:
        lines = f.readlines()
    count = int(lines[0].strip())
    dist = np.empty(count, dtype=np.float32)
    elev = np.empty(count, dtype=np.float32)
    for i in range(count):
        d, e = lines[i+1].strip().split()
        dist[i] = float(d)
        elev[i] = float(e)
    return dist, elev

