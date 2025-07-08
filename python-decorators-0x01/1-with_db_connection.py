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

@with_db_connection
def get_user_by_id(conn, user_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return cursor.fetchone()

#### Fetch user by ID with automatic connection handling

user = get_user_by_id(user_id=1)
print(user)