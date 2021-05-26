from typing import Tuple


def version_tuple(version: str) -> Tuple[int]:
    return tuple(int(s) for s in str(version).split('.') if s.isdigit())[:3]
