#!/usr/bin/env python3
"""An async_generator that takes no arguments."""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Creates a sequence of 10 nums."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
