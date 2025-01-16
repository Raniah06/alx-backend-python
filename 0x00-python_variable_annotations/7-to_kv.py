#!/usr/bin/env python3
"""
This module contains a type-annotated function `to_kv` that takes a string
and an int or float, and returns a tuple with the string and the square of
the number as a float.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Takes a string and an int or float and returns a tuple.

    The first element of the tuple is the string `k`, and the second element
    is the square of the int/float `v`, returned as a float.
    """
    return (k, float(v**2))
