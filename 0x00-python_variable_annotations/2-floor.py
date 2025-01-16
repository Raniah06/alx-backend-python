#!/usr/bin/env python3
"""
This module contains a type-annotated function `floor` that takes a float
and returns the floor of the float as an integer.
"""

import math


def floor(n: float) -> int:
    """Takes a float argument and returns its floor as an integer."""
    return math.floor(n)
