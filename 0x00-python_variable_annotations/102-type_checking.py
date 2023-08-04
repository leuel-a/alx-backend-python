#!/usr/bin/env python3
"""Defines the zoom_array function and some examples"""
from typing import Tuple, List, Union


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Returns a list with tuples of the same type and zoomed in"""
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
