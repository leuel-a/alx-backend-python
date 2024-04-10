#!/usr/bin/env python3
"""Defines the task_wait_n function"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Asynchronously waits for 'n' random delays up to 'max_delay'
    and returns a list of the delays."""
    tasks = []

    for _ in range(n):
        tasks.append(asyncio.create_task(wait_random(max_delay)))

    results = []
    for coroutine in asyncio.as_completed(tasks):
        result = await coroutine
        results.append(result)
    return results
