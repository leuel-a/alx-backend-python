#!/usr/bin/env python3
"""Defines the sum_mixed_list function"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns the sum of the list of floats and integers

    Parameters:
    mxd_lst (List[Union[int, float]]): the list of floats and integers

    Returns:
    float: the sum of the list of floats and integers
    """
    return sum(mxd_lst)
