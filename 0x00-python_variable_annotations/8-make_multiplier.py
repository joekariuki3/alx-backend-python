#!/usr/bin/env python3
"""function that returnd a function that multiplies a value"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """return a funtion mult that produces a product of multiplier
    and multiplier2"""
    def mult(multiplier2: float):
        """returns product of multiplier and multiplier2"""
        return multiplier * multiplier2
    return mult
