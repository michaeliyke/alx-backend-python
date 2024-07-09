#!/usr/bin/env python3
"""Module: Async Comprehension lessons"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Loops 10 times, wait a sec, yields a random number between 0 and 10."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield round(random.uniform(0, 10), 15)
