from seed import connect_to_prodev

def stream_user_ages():
    """
    Generator that yields user ages from the database.
    Yields:
        int: The age of each user from user_data table.
    """

    connection = connect_to_prodev()
    cursor = connection.cursor(dictionary=True)

    try:
        cursor.execute("SELECT age FROM user_data")
        for row in cursor:
            yield row['age']
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cursor.close()
        connection.close()
    return None

def users_average_age():
    """
    Calculate the average age of users from the database.
    Returns:
        float: The average age of users.
    """
    total_age = 0
    count = 0

    for age in stream_user_ages():
        total_age += age
        count += 1

    if count == 0:
        return 0.0

    average_age = total_age / count
    print(f"Average age of users: {average_age}")

    return average_age