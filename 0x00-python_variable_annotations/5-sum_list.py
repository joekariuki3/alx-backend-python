#!/usr/bin/env python3
"""function that sums up floats in a list"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """sums up float in input_list
    and return the float total"""
    total: float = 0
    for num in input_list:
        total = total + num
    return total
