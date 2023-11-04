#!/usr/bin/env python3


import requests


archive_url = "https://ipt.plantnet.org/archive.do?r=observations"

response = requests.get(archive_url)


if response.status_code == 200:
    print("status code is 200")
    # Define the filename for the downloaded archive
    file_name = "plant_observations.zip"  # You can use any filename you prefer

    # Save the response content (ZIP file) to a local file
    with open(file_name, 'wb') as f:
        f.write(response.content)

    print(f"Darwin Core Archive downloaded and saved as {file_name}")
else:
    print(f"Error: Unable to retrieve the Darwin Core Archive. Status code: {response.status_code}")


