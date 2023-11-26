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

# Execute a query to get the count
query = """
    SELECT COUNT(*) 
    FROM plantnet_observations 
    WHERE species = 'Cistus creticus' 
        AND decimalLatitude IS NOT NULL 
        AND decimalLongitude IS NOT NULL;
"""
cur.execute(query)

# Fetch the count
count = cur.fetchone()[0]

# Print the result
print(f"Number of instances: {count}")

# Close the cursor and connection
cur.close()
conn.close()


# # Execute a query
# cur.execute("SELECT * FROM plantnet_observations LIMIT 10;")
# rows = cur.fetchall()

# # Print the results
# for row in rows:
#     print(row)

