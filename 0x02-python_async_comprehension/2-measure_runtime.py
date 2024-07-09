#!/usr/bin/env async_comprehension
"""Module: Async Comprehension lessons"""

import asyncio
import time
from typing import Coroutine, List
async_comprehension: Coroutine[None, None, List[float]] =\
    __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure runtime of async_comprehension coroutine"""
    start = time.time()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    end = time.time()
    return end - start
