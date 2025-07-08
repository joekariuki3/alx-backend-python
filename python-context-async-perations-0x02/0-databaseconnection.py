import sqlite3

class DatabaseConnection:
    """DatabaseConnection class is a context manager that handles opening and closing database connections automatically
        - use __enter__ and __exit__ methods to manage the connection lifecycle
    """
    def __init__(self, db_file):
        self.db_file = db_file
        self.connection = None

    def __enter__(self):
        """Open the database connection."""
        try:
            self.connection = sqlite3.connect(self.db_file)
            return self.connection
        except sqlite3.Error as e:
            print(f"An error occurred while connecting to the database: {e}")
            self.connection = None
            raise

    def __exit__(self, exc_type, exc_value, traceback):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            self.connection = None
            print(f"Database connection closed to {self.db_file}")



with DatabaseConnection('users.db') as conn:
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()
    for row in rows:
        print(row)