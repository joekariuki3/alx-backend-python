#!/usr/bin/env python3
"""type checking validation"""

from typing import Tuple, Any, List, Union
"""import required methods from typing module"""


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """type checking validation"""
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
