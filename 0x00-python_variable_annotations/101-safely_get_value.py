#!/usr/bin/env python3
"""
This module contains a function `safely_get_value` that retrievesfrom a dictionary using a given key. If not found returns default value."""

from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(
    dct: Mapping, key: Any, default: Union[T, None] = None
) -> Union[Any, T]:
    """Returns the value associated with `key` in `dct`, or `default` if the key is not found."""
    if key in dct:
        return dct[key]
    else:
        return default
