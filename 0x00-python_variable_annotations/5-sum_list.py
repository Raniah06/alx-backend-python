#!/usr/bin/env python3
"""
This module contains a type-annotated function `sum_list` that takes a list
of floats as input and returns their sum as a float.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """Takes a list of floats and returns their sum as a float."""
    return sum(input_list)
