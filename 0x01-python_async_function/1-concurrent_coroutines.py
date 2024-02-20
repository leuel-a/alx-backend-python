#!/usr/bin/env python3
"""Defines the wait_n function"""
import asyncio
from typing import List


wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay) -> List[float]:
    tasks = [wait_random(max_delay) for _ in range(n)]

    results = []
    for coroutine in asyncio.as_completed(tasks):
        result = await coroutine
        results.append(result)
    return results
