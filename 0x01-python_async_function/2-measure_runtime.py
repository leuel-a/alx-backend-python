#!/usr/bin/env python3
"""Defines the measure_time function"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures the total execution time for wait_n(n, max_delay)"""
    start_time = time.time()

    # The only way to run an async function is to use asyncio.run() in python
    asyncio.run(wait_n(n, max_delay))

    end_time = time.time()

    total_time = end_time - start_time
    return total_time / n
