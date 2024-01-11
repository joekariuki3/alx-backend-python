#!/usr/bin/env python3
"""functions that takes list of mixed types int and float
and sum them up"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """returns sum of values in mxd_list"""
    total: float = 0
    for num in mxd_lst:
        total = total + num

    return total
