#!/usr/bin/env python3
"""Module on Async/await lessons"""

import asyncio
from typing import List
from asyncio import Future
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Return the list of all the delays"""
    delays: List[Future] = [task_wait_random(max_delay) for _ in range(n)]
    return [await delay for delay in asyncio.as_completed(delays)]
