#!/usr/bin/env python3
"""execute multiple coroutines at the same time with async"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """call wait_random n times returning a list of random
    delay time"""
    delay_time_list = []
    for _ in range(n-n, n):
        delay_time = await wait_random(max_delay)
        delay_time_list.append(delay_time)
    return sorted(delay_time_list)
