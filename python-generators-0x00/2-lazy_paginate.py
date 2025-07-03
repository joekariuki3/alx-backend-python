from seed import connect_to_prodev

def paginate_users(page_size: int, offset: int):
    """
    Fetch user data in batches from the database using pagination.
    Args:
        page_size (int): The number of records to fetch in each batch.
        offset (int): The number of records to skip before fetching the batch.
    Returns:
        list: A list of user records from the database.
    """
    connection = connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM user_data LIMIT %s OFFSET %s", (page_size, offset))
        batch = cursor.fetchall()
        return batch
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cursor.close()
        connection.close()
    return None

def lazy_paginate(page_size):
    """
    Generator that yields user data in batches from the database using pagination.
    Args:
        page_size (int): The number of records to fetch in each batch.
    Yields:
        list: A list of user records from the database.
    """
    offset = 0
    while True:
        batch = paginate_users(page_size, offset)
        if not batch:
            break
        yield batch
        offset += page_size

    return None