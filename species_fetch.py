import psycopg2
from psycopg2 import extras
import requests
import json
from clima_request import get_climatic_data_for_location

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="plants",
    user="marco",
    # password="your_password"  # Replace with your actual password
)

# Create a cursor with a dictionary cursor factory
cur = conn.cursor(cursor_factory=extras.DictCursor)

# Execute a query to select specific fields (ID, species, latitude, longitude) of observations of a specific plant
query = """
    SELECT *
    FROM plantnet_observations 
    WHERE species = 'Cistus creticus' 
        AND decimalLatitude IS NOT NULL 
        AND decimalLongitude IS NOT NULL;
"""
cur.execute(query)

observations = cur.fetchall()  # Fetch all observations for the plant

drop_table_query = "DROP TABLE IF EXISTS plant_climate_data;"
cur.execute(drop_table_query)
conn.commit()

# Create a new table in the same database to store plant observations and climate data
create_table_query = """
CREATE TABLE IF NOT EXISTS plant_climate_data (
    observation_id SERIAL PRIMARY KEY,
    species VARCHAR(100),  -- Column to store species
    january_climate JSONB,  -- Fields for January climate data
    february_climate JSONB,  -- Fields for February climate data
    march_climate JSONB,  -- Fields for March climate data
    april_climate JSONB,  -- Fields for April climate data
    may_climate JSONB,  -- Fields for May climate data
    june_climate JSONB,  -- Fields for June climate data
    july_climate JSONB,  -- Fields for July climate data
    august_climate JSONB,  -- Fields for August climate data
    september_climate JSONB,  -- Fields for September climate data
    october_climate JSONB,  -- Fields for October climate data
    november_climate JSONB,  -- Fields for November climate data
    december_climate JSONB  -- Fields for December climate data
);
"""
cur.execute(create_table_query)
conn.commit()  # Commit the table creation query

# Insert observation data with corresponding climate data into the new table
commit_limit = 1  # Set the limit to 1 for testing the first observation
commit_count = 0   # Initialize a counter to track the number of commits

for observation in observations:
    if commit_count >= commit_limit:
        break  # Stop the loop after reaching the commit limit

    species = observation['species']
    latitude = observation['decimallatitude']
    longitude = observation['decimallongitude']

    # Get climatic data for the observation's location
    climate_data = get_climatic_data_for_location(latitude, longitude)
    print("climatic data retrieved")

    # Remove unnecessary keys from the observation dictionary
    #observation.pop('decimallatitude')
    #observation.pop('decimallongitude')

    # Convert observation dictionary to JSON string
    #observation_json = json.dumps(observation)

    # Build the INSERT query for the new table with observation and climate data for all months
    insert_query = """
    INSERT INTO plant_climate_data (
        species, january_climate, february_climate, march_climate, april_climate,
        may_climate, june_climate, july_climate, august_climate, september_climate,
        october_climate, november_climate, december_climate
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """

    # Execute the INSERT query, passing species, observation details as JSON, and climate data for all months
    cur.execute(insert_query, (
        species, json.dumps(climate_data[0]), json.dumps(climate_data[1]), json.dumps(climate_data[2]),
        json.dumps(climate_data[3]), json.dumps(climate_data[4]), json.dumps(climate_data[5]), json.dumps(climate_data[6]),
        json.dumps(climate_data[7]), json.dumps(climate_data[8]), json.dumps(climate_data[9]), json.dumps(climate_data[10]),
        json.dumps(climate_data[11])
    ))
    conn.commit()  # Commit the insertion for each observation
    print ("done!")
    commit_count += 1  # Increment the commit count

# Close the cursor and connection
cur.close()
conn.close()
