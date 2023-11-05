#!/usr/bin/env python3

import requests

# Define the base URL for the GBIF Occurrence endpoint
occurrence_base_url = "https://api.gbif.org/v1/occurrence/search"

# Define your query parameters
params = {
    #"scientificName": "Tilia cordata",  # Replace with the plant species you want to search for
    "scientificName": "Cistus creticus",  # Replace with the plant species you want to search for
    "limit": 100,  # You can adjust the limit to control the number of results per request
    "offset": 0  # Start with an offset of 0 to retrieve the first page of results
}

# Make the API request
response = requests.get(occurrence_base_url, params=params)

if response.status_code == 200:
    data = response.json()

    # Loop through the results
    for result in data.get("results", []):
        # Process the occurrence data as needed
        # Example: Print the occurrence ID and location
        occurrence_id = result.get("key")
        location = result.get("decimalLatitude"), result.get("decimalLongitude")
        print(f"Occurrence ID: {occurrence_id}, Location: {location}")

    # Check for pagination and retrieve more results if available
    if data.get("offset", 0) + data.get("limit", 0) < data.get("count", 0):
        params["offset"] = data.get("offset", 0) + data.get("limit", 0)
        # You can put the code to make additional requests here to retrieve more results
else:
    print(f"Error: Unable to retrieve plant occurrences. Status code: {response.status_code}")
