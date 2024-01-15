#!/usr/bin/env python3
"""function that takes an int and wait for randon time
then return tne number"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """receives and input then delays random seconds"""
    delay_time = random.uniform(0, max_delay)
    await asyncio.sleep(delay_time)
    return delay_time
