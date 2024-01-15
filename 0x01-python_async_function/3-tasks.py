#!/usr/bin/env python3
"""create a task and return it"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_dely: int) -> asyncio.Task:
    """create a task and return it"""
    task1 = asyncio.create_task(wait_random(max_dely))
    return task1
