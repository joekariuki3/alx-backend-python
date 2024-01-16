#!/usr/bin/env python3
"""Run time for four parallel comprehensions"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """Run time for four parallel comprehensions"""
    start_time = asyncio.get_event_loop().time()
    task1 = asyncio.create_task(async_comprehension())
    task2 = asyncio.create_task(async_comprehension())
    task3 = asyncio.create_task(async_comprehension())
    task4 = asyncio.create_task(async_comprehension())
    await asyncio.gather(task1, task2, task3, task4)
    end_time = asyncio.get_event_loop().time()
    execute_time = end_time - start_time
    return execute_time
