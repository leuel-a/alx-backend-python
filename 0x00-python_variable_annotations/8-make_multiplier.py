#!/usr/bin/env python3
"""Defines the make_multiplier function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by multiplier

    Parameters:
    multiplier (float): the number to multiply by

    Returns:
    function: a function that multiplies a float by multiplier
    """
    def function(n: float) -> float:
        """Multiplies a float by multiplier

        Parameters:
        n (float): the number to multiply by multiplier

        Returns:
        float: the product of n and multiplier
        """
        return n * multiplier
    return function
