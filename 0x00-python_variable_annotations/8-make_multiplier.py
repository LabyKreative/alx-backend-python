#!/usr/bin/env python3
'''
make_multiplier that takes a float multiplier.
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    Creates a multiplier function.
    '''
    return lambda x: x * multiplier
