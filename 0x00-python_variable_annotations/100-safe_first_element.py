#!/usr/bin/env python3
"""Augment the following code with the correct duck-typed annotations:"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Retrieves the first element."""
    if lst:
        return lst[0]
    else:
        return None
