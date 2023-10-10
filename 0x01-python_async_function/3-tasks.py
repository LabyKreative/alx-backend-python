#!/usr/bin/env python3
"""A script that creates an asybchronus task."""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Creates an asynchronous function."""
    return asyncio.create_task(wait_random(max_delay))
