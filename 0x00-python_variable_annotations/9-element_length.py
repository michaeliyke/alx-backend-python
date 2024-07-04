#!/usr/bin/env python3
"""Python Variable Annotations module"""
from typing import Iterable, Tuple, Sequence, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of the length of each element in the input list"""
    return [(i, len(i)) for i in lst]
