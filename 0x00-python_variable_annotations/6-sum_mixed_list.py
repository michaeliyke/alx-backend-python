#!/usr/bin/env python3
"""Python Variable Annotations module"""
from typing import List, Union


def sum_mixed_list(mxd_lst: Union[int, float]) -> float:
    """Sums a list of floats and integers"""
    return sum(mxd_lst)
