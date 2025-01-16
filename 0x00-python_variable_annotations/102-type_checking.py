#!/usr/bin/env python3
from typing import List

def zoom_array(lst: List[int], factor: int = 2) -> List[int]:
    """
    Function to zoom in on each item in the list by a factor.
    
    Parameters:
    - lst: List of integers to zoom in on.
    - factor: The factor by which to zoom in (default is 2).
    
    Returns:
    - A list with each item in lst repeated factor times.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

# Ensure the factor is an integer, so passing a float should be invalid
zoom_3x = zoom_array(array, 3)
