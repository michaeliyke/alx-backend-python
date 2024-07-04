#!/usr/bin/env python3
"""Python Variable Annotations module"""
from typing import List, Tuple, Iterable


def element_length(lst: List[Iterable]) -> List[Tuple[Iterable, int]]:
    """Return a list of the length of each element in the input list"""
    return [(i, len(i)) for i in lst]
