#!/usr/bin/env python3
"""Defines the floor function"""


def floor(n: float) -> int:
    """Floors a number that is a float to the nearest integer

    Parameters:
    n (float): the number that is going to be floored

    Returns:
    int: the floor of the number passed as a parameter
    """
    return int(str(n).split('.')[0])
