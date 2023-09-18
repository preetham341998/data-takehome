import psycopg2

# Define database connection parameters (move this to config.py)
db_params = {
    "dbname": "your_database_name",
    "user": "your_database_user",
    "password": "your_database_password",
    "host": "localhost",  # or the database host IP or domain
    "port": "5432"  # or your PostgreSQL port
}

def create_database_connection():
    try:
        # Create a database connection
        connection = psycopg2.connect(**db_params)
        return connection
    except psycopg2.Error as e:
        print(f"Error creating database connection: {e}")
        return None

def close_database_connection(connection):
    try:
        connection.close()
    except psycopg2.Error as e:
        print(f"Error closing database connection: {e}")

def write_to_postgres(data):
    # Connect to the PostgreSQL database
    conn = create_database_connection()
    if conn:
        try:
            cursor = conn.cursor()

            # Insert or update records in the 'user_logins' table
            for record in data:
                user_id = record['user_id']
                device_type = record['device_type']
                masked_ip = record['masked_ip']
                masked_device_id = record['masked_device_id']
                locale = record['locale']
                app_version = record['app_version']
                create_date = record['create_date']

                # Check if the user_id already exists in the table
                cursor.execute("SELECT user_id FROM user_logins WHERE user_id = %s", (user_id,))
                existing_user = cursor.fetchone()

                if existing_user:
                    # If user_id exists, update the record
                    cursor.execute(
                        "UPDATE user_logins SET device_type = %s, masked_ip = %s, masked_device_id = %s, "
                        "locale = %s, app_version = %s, create_date = %s WHERE user_id = %s",
                        (device_type, masked_ip, masked_device_id, locale, app_version, create_date, user_id)
                    )
                else:
                    # If user_id doesn't exist, insert a new record
                    cursor.execute(
                        "INSERT INTO user_logins (user_id, device_type, masked_ip, masked_device_id, "
                        "locale, app_version, create_date) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                        (user_id, device_type, masked_ip, masked_device_id, locale, app_version, create_date)
                    )

            # Commit changes and close connections
            conn.commit()
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            cursor.close()
            close_database_connection(conn)
