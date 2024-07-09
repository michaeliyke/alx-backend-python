#!/usr/bin/env async_comprehension
"""Module: Async Comprehension lessons"""

import asyncio
import time
from typing import Coroutine, List
async_comprehension: Coroutine[None, None, List[float]] =\
    __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """Measure runtime of async_comprehension coroutine"""
    start = time.time()
    await async_comprehension()
    end = time.time()
    return end - start
