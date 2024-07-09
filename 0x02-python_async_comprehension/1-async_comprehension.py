#!/usr/bin/env python3
"""Module: Async Comprehension lessons"""

from typing import List, AsyncGenerator
async_generator: AsyncGenerator[float, None] =\
    __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Loop through async generator and return list of results"""
    return [i async for i in async_generator()]
