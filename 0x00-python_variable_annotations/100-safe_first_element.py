#!/usr/bin/env python3
"""Defines the safe_first_element"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Safely retrieves the first element from the given sequence.

    This function takes a sequence as input and returns the first element
    of the sequence if it is not empty. If the sequence is empty, the
    function returns None.

    Parameters:
        lst (Sequence[Any]): A sequence from which the first element will
            be retrieved.

    Returns:
        Union[Any, None]: The first element of the sequence if it is not
        empty, otherwise, returns None.

    Examples:
        >>> safe_first_element([1, 2, 3])
        1

        >>> safe_first_element([])
        None
    """
    if lst:
        return lst[0]
    else:
        return None
