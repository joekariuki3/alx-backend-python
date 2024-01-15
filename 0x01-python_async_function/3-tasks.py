#!/usr/bin/env python3
"""a funtion that create a task and return it"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """a function that create a task
    using an async funtion wait_random then returns it"""
    task1 = asyncio.create_task(wait_random(max_delay))
    return task1
