#!/usr/bin/env python3
"""Defines the make_multiplier function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by multiplier"""

    def f(n: float) -> float:
        """Returns a float multiplied by multiplier"""
        return n * multiplier

    return f
