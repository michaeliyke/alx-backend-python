#!/usr/bin/env python3
"""Module on Async/await lessons"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> float:
    """
    Spawn wait_random n times with max_delay. Return the list of all delays.
    """
    delays = [wait_random(max_delay) for _ in range(n)]
    return [await delay for delay in asyncio.as_completed(delays)]
