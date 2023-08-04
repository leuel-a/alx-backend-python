#!/usr/bin/env python3
"""Defines the element_length function"""
from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[SyntaxWarning, int]]:
    return [(i, len(i)) for i in lst]
