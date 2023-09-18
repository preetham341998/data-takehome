import psycopg2

# database connection parameters 
db_params = {
    "dbname": "your_database_name",
    "user": "your_database_user",
    "password": "your_database_password",
    "host": "localhost", 
    "port": "5432"  
}

def create_database_connection():
    try:
        # database connection creation
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
    # Connecting to PostgreSQL database
    conn = create_database_connection()
    if conn:
        try:
            cursor = conn.cursor()

            # Inserting/updating records in the 'user_logins' table
            for record in data:
                user_id = record['user_id']
                device_type = record['device_type']
                masked_ip = record['masked_ip']
                masked_device_id = record['masked_device_id']
                locale = record['locale']
                app_version = record['app_version']
                create_date = record['create_date']

                # Check  user_id already exists or not
                cursor.execute("SELECT user_id FROM user_logins WHERE user_id = %s", (user_id,))
                existing_user = cursor.fetchone()

                if existing_user:
                    # If  exists, update  record
                    cursor.execute(
                        "UPDATE user_logins SET device_type = %s, masked_ip = %s, masked_device_id = %s, "
                        "locale = %s, app_version = %s, create_date = %s WHERE user_id = %s",
                        (device_type, masked_ip, masked_device_id, locale, app_version, create_date, user_id)
                    )
                else:
                    # doesn't exist, insert  new record
                    cursor.execute(
                        "INSERT INTO user_logins (user_id, device_type, masked_ip, masked_device_id, "
                        "locale, app_version, create_date) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                        (user_id, device_type, masked_ip, masked_device_id, locale, app_version, create_date)
                    )

            # Commit the changes and close connections
            conn.commit()
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            cursor.close()
            close_database_connection(conn)
