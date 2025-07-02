import mysql.connector
from dotenv import load_dotenv
import os
from uuid import uuid4
import csv

load_dotenv()

def connect_db():
    "connects to mysql database server"
    return mysql.connector.connect(
        host=os.getenv("HOST", "localhost"),
        user=os.getenv("DBUSERNAME", "root"),
        password=os.getenv("PASSWORD"),
    )

def create_database(connection):
    "creates database"
    database_name = os.getenv("DBNAME", "ALX_prodev")
    cursor = connection.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
    cursor.close()

def connect_to_prodev():
    "connects to the ALX_prodev database"
    return mysql.connector.connect(
        host=os.getenv("HOST", "localhost"),
        user=os.getenv("DBUSERNAME", "root"),
        password=os.getenv("PASSWORD"),
        database=os.getenv("DBNAME", "ALX_prodev")
    )

def create_table(connection):
    """creates a table user_data if it does not exists with the required fields"""
    database_name = os.getenv("DBNAME", "ALX_prodev")
    user_data_schema = """
    CREATE TABLE IF NOT EXISTS user_data (
    user_id VARCHAR(60) PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL ,
    age DECIMAL(3, 0) NOT NULL )
    """
    cursor = connection.cursor()
    cursor.execute(f"USE {database_name}")
    cursor.execute(user_data_schema)
    cursor.close()

def insert_data(connection, data):
    """inserts data(csv file) in the database if it does not exist"""
    with open(data, 'r') as file:
        reader = csv.DictReader(file)
        cursor = connection.cursor()
        for row in reader:
            user_id = str(uuid4())
            name = row['name']
            email = row['email']
            age = int(row['age'])
            cursor.execute(
                "INSERT IGNORE INTO user_data (user_id, name, email, age) VALUES (%s, %s, %s, %s)",
                (user_id, name, email, age)
            )
        cursor.close()
        connection.commit()
