import psycopg2

# PostgreSQL container's IP address
container_ip = "172.17.0.2"  # Replace this with your container's actual IP

# PostgreSQL connection parameters
conn_params = {
    "host": container_ip,
    "port": "5432",
    "database": "postgres",  # Replace with your database name
    "user": "postgres",      # Replace with your username
    "password": "postgres",   # Replace with your password
    "connect_timeout": 5     # Timeout in seconds (adjust as needed)

}

try:
    # Establish connection to PostgreSQL
    conn = psycopg2.connect(**conn_params)
    
    # If connection is successful
    print("Connection to PostgreSQL container successful!")
    
    # Perform operations or execute SQL queries here if needed
    
    # Remember to close the connection when finished
    conn.close()
    
except psycopg2.Error as e:
    # If connection fails, print the error message
    print("Error connecting to PostgreSQL container:", e)
