#!/usr/bin/env python3

from os import getenv
from seed import connect_to_prodev


"""fetch users data in batches using generator and process them"""
def stream_users_in_batches(batch_size: int):
    """    Generator that yields user data in batches from the database.

    Args:
        batch_size (int): The number of records to fetch in each batch.

    Yields:
        list: A list of user records from the database.
    """
    connection = connect_to_prodev()
    cursor = connection.cursor(dictionary=True)

    try:
        cursor.execute("SELECT * FROM user_data")
        while True:
            batch = cursor.fetchmany(batch_size)
            if not batch:
                break
            yield batch
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cursor.close()
        connection.close()
    return None


def batch_processing(batch_size: int):
    """Process user data in batches, to filter users over the age of 25

    Args:
        batch_size (int): The number of records to process in each batch.
    """
    age_limit = 25
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user['age'] > age_limit:
                print(user)

    return None