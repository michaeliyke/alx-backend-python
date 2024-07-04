#!/usr/bin/env python3
"""Python Variable Annotations module"""
from typing import List, Union, Any, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return first element of list if exists, None otherwise"""
    if lst:
        return lst[0]
    else:
        return None
