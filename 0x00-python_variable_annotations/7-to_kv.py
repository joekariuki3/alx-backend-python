#!/usr/bin/env python3
"""function that takes a string and an int or float
and returns a tuple(k: str, squre of v int or float)
"""
from typing import Tuple, Union
"""import requred types from typing module"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """takes in k as string and v as either int or float,
    then returns a tuple of k and v"""
    result: tuple = (k, v * v)
    return result
