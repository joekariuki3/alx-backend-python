import sqlite3
import functools

with_db_connection = __import__("1-with_db_connection").with_db_connection

def transactional(func):
    """Decorator that ensures a function running a database operation is wrapped inside a transaction.
    If the function completes successfully, the transaction is committed; if an exception occurs, it is rolled back.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = args[0]
        conn.execute("BEGIN TRANSACTION")
        try:
            result = func(*args, **kwargs)
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise e
        return result
    return wrapper

@with_db_connection
@transactional
def update_user_email(conn, user_id, new_email):
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id))
#### Update user's email with automatic transaction handling

update_user_email(user_id=1, new_email='Crawford_Cartwright@hotmail.com')