#!/usr/bin/env python3
"""Defines the safely_get_value function"""
from typing import Any, Mapping, TypeVar, Union


def safely_get_value(dct: Mapping, key: Any,
        default: Union[TypeVar('T'), None]) -> Union[Any, TypeVar('T')]:
    """Return the value linked to key in dct if exists, otherwise return default"""
    if key in dct:
        return dct[key]
    else:
        return default
