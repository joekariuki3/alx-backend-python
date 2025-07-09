# Python Context and Asynchronous Operations

This project demonstrates the implementation and usage of Python context managers and asynchronous operations with a focus on database connections and queries.

## Overview

The project showcases:

1. Context managers for database connections
2. SQL query execution within context managers
3. Asynchronous database operations with `aiosqlite`
4. Concurrent execution using `asyncio.gather`

## Files

- **0-databaseconnection.py**: Implements a context manager for handling SQLite database connections using the `__enter__` and `__exit__` methods.
- **1-execute.py**: Demonstrates a context manager for executing database queries with parameter binding.
- **3-concurrent.py**: Shows how to perform concurrent asynchronous database operations using `asyncio` and `aiosqlite`.

## Prerequisites

- Python 3.10.12
- SQLite3
- Virtual environment with required packages

## Installation

```bash
# Create a virtual environment
python -m virtualenv venv

# Activate virtual environment
source venv/bin/activate  # On Unix/macOS
# OR
.\venv\Scripts\activate  # On Windows

# Install required packages
pip install aiosqlite
```

## Usage

### 1. Database Connection Context Manager

The `DatabaseConnection` class provides a context manager for automatically handling database connections:

```python
with DatabaseConnection('users.db') as conn:
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()
```

### 2. Query Execution Context Manager

The `ExecuteQuery` class simplifies executing queries with parameters:

```python
with ExecuteQuery(query="SELECT * FROM users WHERE age > ?", param=[25]) as result:
    print(result)
```

### 3. Concurrent Asynchronous Operations

Use `asyncio.gather` to execute multiple database operations concurrently:

```python
async def fetch_concurrently():
    results = await asyncio.gather(async_fetch_users(), async_fetch_older_users())
    for result in results:
        print(result)
```

## Learning Objectives

- Understanding and implementing Python context managers
- Handling database connections safely and efficiently
- Working with asynchronous database operations
- Executing concurrent tasks with `asyncio`
- Managing resources properly with automatic cleanup

## Database Structure

The project uses a SQLite database named `users.db` with a `users` table containing:
- id (INTEGER PRIMARY KEY)
- username (TEXT)
- email (TEXT)
- age (INTEGER)
- password (TEXT)

## Running the Examples

```bash
# Run the database connection context manager example
python 0-databaseconnection.py

# Run the query execution context manager example
python 1-execute.py

# Run the concurrent operations example
python 3-concurrent.py
```