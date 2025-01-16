#!/usr/bin/env python3
"""
This module contains a function `safe_first_element` that takes a sequence and 
returns its first element, or None if the sequence is empty.
"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returns the first element of a sequence, or None if the sequence is empty."""
    if lst:
        return lst[0]
    else:
        return None
