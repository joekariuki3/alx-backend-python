import sqlite3
import functools
from datetime import datetime

### decorator to log SQL queries
def log_queries(func):
    """
    decorator that logs sql query before executing it
    :param func: function to be decorated
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        query = args[0] if args else kwargs.get('query', None)
        if query:
            print(f"{datetime.now()}: Executing query: {query}")
        return func(*args, **kwargs)
    return wrapper

@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

#### fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")