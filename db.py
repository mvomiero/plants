import psycopg2

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="plants",
    user="marco",
    #password="your_password"  # Replace with your actual password
)

# Create a cursor
cur = conn.cursor()

# Execute a query
cur.execute("SELECT * FROM plantnet_observations LIMIT 10;")
rows = cur.fetchall()

# Print the results
for row in rows:
    print(row)

# Close the cursor and connection
cur.close()
conn.close()
