# Python Decorators

## Collection of decorators that can be used to simplify and improve code

### Available Decorators

#### 1. Create Users Database

- **[create_users_db](create_users_db.py)**: Script creates a SQLite database named `users.db` and populates it with a list of users.

#### 2. Log Queries

- **[log_queries](0-log_queries.py)**: Decorator that logs SQL query before executing it.

#### 3. Database Connection Management

- **[with_db_connection](1-with_db_connection.py)**: Decorator to manage database connections for functions that require a connection.
- **[transactional](2-transactional.py)**: Decorator to manage database connections for functions that require a connection.

#### 4. Error Handling

- **[retry_on_failure](3-retry_on_failure.py)**: Decorator that retries a function call on failure.

#### 5. Query Caching

- **[cache_query.py](4-cache_query.py)**: Decorator that caches query results based on the SQL query string.
