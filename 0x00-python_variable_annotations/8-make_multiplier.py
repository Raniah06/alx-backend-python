#!/usr/bin/env python3
"""
This module contains a type-annotated function `make_multiplier` that takes
a float multiplier as an argument and returns a function that multiplies a
float by that multiplier.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Takes a float `multiplier` and returns a function that multiplies a float by `multiplier`."""
    
    def multiplier_function(x: float) -> float:
        """Multiplies the input `x` by the `multiplier`."""
        return x * multiplier
    
    return multiplier_function
