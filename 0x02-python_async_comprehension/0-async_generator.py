#!/usr/bin/env python3
"""Async Generator"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator:
    """ loop 10 times sleep for a second then yield
    a random number"""
    for _ in range(1, 11):
        await asyncio.sleep(1)
        yield random.uniform(1, 9)
