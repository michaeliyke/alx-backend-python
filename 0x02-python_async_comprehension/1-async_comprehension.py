#!/usr/bin/env python3
"""Module: Async Comprehension lessons"""

from typing import List, AsyncGenerator
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Loop through async generator and return list of results"""
    asyncGen: AsyncGenerator[float, None] = async_generator()
    return [i async for i in asyncGen]
