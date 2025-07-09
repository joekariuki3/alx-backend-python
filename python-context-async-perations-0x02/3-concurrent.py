import aiosqlite
from sqlite3 import Error
import asyncio

DATABASE_NAME = "users.db"

async def connect_to_database():
    """connects to the database and returns connection"""
    try:
        connection = await aiosqlite.connect(DATABASE_NAME)
        return connection
    except Error as e:
        print(e)
async def close_connection(connection):
    """closes the database connection"""
    await connection.close()

async def async_fetch_users():
    """fetches all users from database"""
    query = "SELECT * FROM users;"

    connection = await connect_to_database()
    cursor = await connection.execute(query)
    results = await cursor.fetchall()
    await close_connection(connection)
    return results

async def async_fetch_older_users():
    """fetches all users older than 40"""
    query = "SELECT * FROM users WHERE age > 40;"

    connection = await connect_to_database()
    cursor = await connection.execute(query)
    result = await cursor.fetchall()
    await close_connection(connection)
    return result

async def fetch_concurrently():
    """uses asyncio.gather to execute async_fetch_users and async_fetch_old_users"""
    results = await asyncio.gather(async_fetch_users(), async_fetch_older_users())

    for result in results:
        print(result)

if __name__ == "__main__":
    asyncio.run(fetch_concurrently())