#!/usr/bin/env python3
"""a type-annotated function sum_mixed_list which takes a list mxd_lst"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """of integers and floats and returns their sum as a float."""
    return float(sum(mxd_lst))
