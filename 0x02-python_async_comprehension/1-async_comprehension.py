#!/usr/bin/env python3
"""Import async_generator from the previous task and then write a coroutine"""
from typing import List
from importlib import import_module as using


async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Generate a list of 10 nums from a 10-num generator."""
    return [num async for num in async_generator()]
