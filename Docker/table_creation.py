import psycopg2

# Connect to the PostgreSQL server
conn = psycopg2.connect(
    dbname='postgres',
    user='postgres',
    password='mysecretpassword',
    host='localhost',
    port='5432'
)

# Create a cursor object to interact with the database
cur = conn.cursor()

# Create a sample table
cur.execute('''
    CREATE TABLE IF NOT EXISTS example_table_2 (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL
    )
''')

# Commit the changes
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()

print("Table created successfully!")
