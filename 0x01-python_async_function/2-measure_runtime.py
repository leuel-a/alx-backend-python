#!/usr/bin/env python3
"""Defines the measure_time function"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """Measures the runtime of wait_n"""
    start_time = time.time()
    await wait_n(n, max_delay)
    end_time = time.time()
    return (end_time - start_time) / n
