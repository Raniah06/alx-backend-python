#!/usr/bin/env python3
"""
Contains a function to zoom in on nos of a tuple by a given factor"""

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Function to zoom in on each item in the tuple by a factor.

    Parameters:
    - lst: Tuple of items to zoom in on.
    - factor: The factor by which to zoom in (default is 2).

    Returns:
    - A list with each item in lst repeated factor times.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

# Ensure the factor is an integer, so passing a float should be invalid
zoom_3x = zoom_array(array, 3)
