#!/usr/bin/env python3
"""Module on Async/await lessons"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Return an asyncio.Task type object"""
    return asyncio.create_task(wait_random(max_delay))
