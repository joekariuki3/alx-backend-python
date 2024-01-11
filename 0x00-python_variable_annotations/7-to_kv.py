#!/usr/bin/env pyton3
from typing import Tuple, Union
"""function that takes a string and an int or float
and returns a tuple(k: str, squre of v int or float)
"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, Union[int, float]]:
    """returns a tuple of k and v"""
    return (k, v * v)
