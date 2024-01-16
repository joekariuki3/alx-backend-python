#!/usr/bin/env python3
"""Async Comprehension"""

import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """using  async comprehension return random list of int form
    a generator funtion"""
    return [num async for num in async_generator()]
