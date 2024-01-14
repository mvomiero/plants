import docker
import psycopg2

import subprocess
result = subprocess.run(['ping', '-c', '4', '172.17.0.2'], capture_output=True, text=True)
print(result.stdout)


# Function to get container's IP address by its name
def get_container_ip(container_name):
    client = docker.from_env()
    container = client.containers.get(container_name)
    return container.attrs['NetworkSettings']['IPAddress']

# Establish a connection to the PostgreSQL database using the container's IP address
def connect_to_database():
    container_name = "postgres-database-container"  # Replace with your container's name
    container_ip = get_container_ip(container_name)
    conn = psycopg2.connect(
        host=container_ip,
        port="5432",
        database="postgres",
        user="postgres",
        password="postgres",  # Replace with your PostgreSQL password
        connect_timeout=10,
    )
    return conn

# Connect to the database
connection = connect_to_database()


# Create a new database
def create_database(conn, db_name):
    try:
        cursor = conn.cursor()
        cursor.execute(f"CREATE DATABASE {db_name};")
        conn.commit()
        print(f"Database '{db_name}' created successfully.")
    except psycopg2.Error as e:
        print("Error creating database:", e)

# Replace "new_database" with your desired database name
create_database(connection, "plants")
