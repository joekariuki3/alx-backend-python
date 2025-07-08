import time
import sqlite3
import functools

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

def retry_on_failure(retries=3, delay=1):
    """
    decorator that retries a function call on failure
    :param retries: number of retries
    :param delay: delay between retries
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Error: {e}. Retrying in {delay} seconds...")
                    time.sleep(delay)
            raise Exception(f"Function {func.__name__} failed after {retries} retries")
        return wrapper
    return decorator


@with_db_connection
@retry_on_failure(retries=3, delay=1)
def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

#### attempt to fetch users with automatic retry on failure

users = fetch_users_with_retry()
print(users)