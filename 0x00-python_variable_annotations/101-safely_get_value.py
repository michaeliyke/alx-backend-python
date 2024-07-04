#!/usr/bin/env python3
"""Python Variable Annotations module"""
from typing import Union, Any, Mapping, TypeVar


T = TypeVar('T')


def safely_get_value(
    dct: Mapping,
    key: Any,
    default: Union[T, None] = None
) -> Union[Any, T]:
    """Return value of key in dictionary if exists, None otherwise"""
    if key in dct:
        return dct[key]
    else:
        return default
