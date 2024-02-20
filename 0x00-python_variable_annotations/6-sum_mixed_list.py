#!/usr/bin/env python3
"""Defines the sum_mixed_list function"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns the sum of the numbers in the list"""
    return sum(mxd_lst)
