import time
import sqlite3
import functools


query_cache = {}

def with_db_connection(func):
    """Decorator to manage database connections for functions that require a connection.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')
        try:
            result = func(conn, *args, **kwargs)
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            result = None
        finally:
            conn.close()
        return result
    return wrapper

def cache_query(func):
    """ Decorator that caches query results based on the SQL query string.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        query = kwargs.get('query')
        if query:
            if query in query_cache:
                print("Using cached result for query:", query)
                return query_cache[query]
            else:
                results = func(*args, **kwargs)
                query_cache[query] = results
                return results
        else:
            raise ValueError("Query string is required for caching. Use the 'query' keyword argument. ex: fetch_users(query='SELECT * FROM users')")
    return wrapper


@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

#### First call will cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")

#### Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")