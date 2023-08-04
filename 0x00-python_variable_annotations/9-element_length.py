#!/usr/bin/env python3
"""Defines the element_length function"""
from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[SyntaxWarning, int]]:
    """Returns the elements inside the itereable, where each value is the
    element it self and its length"""
    return [(i, len(i)) for i in lst]
