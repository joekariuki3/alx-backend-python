#!/usr/bin/env python3
# This script creates a SQLite database named 'users.db' and populates it with a list of users.

import sqlite3

def connect_to_db():
    """
    Connects to the SQLite database named 'users.db' and returns a connection object.

    Returns:
        Connection object
    """
    conn = sqlite3.connect('users.db')
    return conn

def create_users_db():
    """
    Creates a SQLite database named 'users.db' and creates a table named 'users' within it.
    The table has three columns: 'id', 'username', and 'password'.
    The 'id' column is an auto-incrementing integer primary key.
    The 'username' and 'password' columns are both TEXT types.
    """

    conn = connect_to_db()
    c = conn.cursor()
    c.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, email TEXT, age INTEGER, password TEXT)")
    conn.commit()
    conn.close()


def populate_users_db():
    """
    Populates the 'users' table in the SQLite database named 'users.db' with a list of users.

    The users are:
        - Alice with password 'password123'
        - Bob with password 'qwerty'
        - Charlie with password 'letmein'
        - Dave with password '12345678'
        - Eve with password 'iloveyou'
        - Frank with password 'admin123'
        - Grace with password 'welcome'
        - Heidi with password 'password1'
        - Ivan with password 'secret'
        - Jack with password 'passw0rd'
    """

    conn = connect_to_db()
    c = conn.cursor()
    users = [
        ('alice','alice@example.com', 22 , 'password123'),
        ('bob', 'bob@example.com', 41 , 'qwerty'),
        ('charlie', 'charlie@example.com', 7, 'letmein'),
        ('dave', 'dave@example.com', 33, '12345678'),
        ('eve', 'eve@example.com', 12, 'iloveyou'),
        ('frank', 'frank@example.com', 55, 'admin123'),
        ('grace', 'grace@example.com', 10, 'welcome'),
        ('heidi', 'heidi@example.com', 55, 'password1'),
        ('ivan', 'ivan@example.com', 88, 'secret'),
        ('jack', 'jack@example.com', 17, 'passw0rd'),
    ]
    c.executemany("INSERT INTO users (username, email, age, password) VALUES (?, ?, ?, ?)", users)
    conn.commit()
    conn.close()

def check_db_exists():
    """
    Checks if the SQLite database named 'users.db' exists.

    Returns:
        True if the database exists, False otherwise.
    """
    try:
        connect_to_db()
        return True
    except sqlite3.OperationalError:
        return False

def check_table_exists():
    """
    Checks if the 'users' table exists in the SQLite database named 'users.db'.

    Returns:
        True if the table exists, False otherwise.
    """
    try:
        conn = connect_to_db()
        c = conn.cursor()
        c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
        return c.fetchone() is not None
    except sqlite3.OperationalError:
        return False
    finally:
        conn.close()

def check_table_empty():
    """
    Checks if the 'users' table in the SQLite database named 'users.db' is empty.

    Returns:
        True if the table is empty, False otherwise.
    """
    try:
        conn = connect_to_db()
        c = conn.cursor()
        c.execute("SELECT COUNT(*) FROM users")
        count = c.fetchone()[0]
        return count == 0
    except sqlite3.OperationalError:
        return True
    finally:
        conn.close()

def main():
    """
    Main function to check if the database and table exist, and if the table is empty.
    If the database does not exist, it creates the database and populates it with users.
    """
    if not check_db_exists():
        print("Database does not exist. Creating database.")
        create_users_db()

    if not check_table_exists():
        print("Table does not exist. Creating table.")
        create_users_db()

    if check_table_empty():
        print("Table is empty. Populating table with users.")
        populate_users_db()
    else:
        print("Table already populated with users.")

if __name__ == "__main__":
    main()