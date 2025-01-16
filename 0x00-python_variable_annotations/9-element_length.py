#!/usr/bin/env python3
"""
This module contains a function `element_length` that takes an iterable object
and returns a list of tuples, where each tuple consists of an element of the
iterable and its length.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples with each element and its length."""
    return [(i, len(i)) for i in lst]
