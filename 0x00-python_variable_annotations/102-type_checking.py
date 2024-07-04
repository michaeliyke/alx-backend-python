#!/usr/bin/env python3
"""Python Variable Annotations module"""
from typing import Tuple, List, Any


def zoom_array(lst: Tuple, factor: int = 2) -> List[Any]:
    """The zoom_array function takes a list and a float factor as arguments"""
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
