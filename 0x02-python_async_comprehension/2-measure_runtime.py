#!/usr/bin/env python3
"""Module: Async Comprehension lessons"""

import asyncio
import time
from typing import Coroutine, List
async_comprehension: Coroutine[None, None, List[float]] =\
    __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure runtime of async_comprehension coroutine"""
    start = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    return time.time() - start
