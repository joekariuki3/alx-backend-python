import sqlite3


class ExecuteQuery:
    """
    ExecuteQuery class in a context manager
    that takes a query and parameter and returns the result of the query
    """
    def __init__(self, query:str, param:list):
        self.query = query
        self.param = param
        self.result = None
        self.connection = None
        self.database = "users.db"

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.database)
            return self.connection
        except Exception as e:
            print(e)

    def __enter__(self):
        self.connection = self.connect()
        cursor = self.connection.cursor()
        cursor.execute(self.query, self.param)
        self.result = cursor.fetchall()
        return self.result

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()
        self.connection = None


with ExecuteQuery(query="SELECT * FROM users WHERE age > ?", param=[25]) as result:
    print(result)