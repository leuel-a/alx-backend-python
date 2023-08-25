#!/usr/bin/env python3
"""This is the first task of the Python - Async project"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """This function waits a random value and returns its value"""
    random_number: float = random.uniform(0, max_delay)
    await asyncio.sleep(random_number)
    return random_number
