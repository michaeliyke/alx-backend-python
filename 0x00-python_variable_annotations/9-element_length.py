#!/usr/bin/env python3
"""Python Variable Annotations module"""
from typing import List, Tuple, Sequence


def element_length(lst: List[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of the length of each element in the input list"""
    return [(i, len(i)) for i in lst]
