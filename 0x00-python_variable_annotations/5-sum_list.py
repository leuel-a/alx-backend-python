#!/usr/bin/env python3
"""Defines the sum_list function"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Sums a list of floats

    Parameters:
    input_list (List[float]): the list of floats

    Returns:
    float: the sum of the list of floats
    """
    return sum(input_list)
