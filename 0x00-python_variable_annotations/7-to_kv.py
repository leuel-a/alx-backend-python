#!/usr/bin/python3
"""Defines the to_kv function"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Accepts a string and an int or float and returns a tuple"""
    return (k, v ** 2)
