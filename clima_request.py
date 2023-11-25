from dotenv import load_dotenv
import os

import requests

load_dotenv()

API_KEY = os.getenv("API_KEY")
print(API_KEY)


# Replace these coordinates with the latitude and longitude of your plant location
latitude = 52.52  # Example latitude (Berlin)
longitude = 13.4  # Example longitude (Berlin)

# Replace with the desired month (1 for January, 2 for February, etc.)
month = 2

# OpenWeatherMap Aggregated Monthly Historical Weather API endpoint
endpoint = 'https://history.openweathermap.org/data/2.5/aggregated/month'

# Construct the API URL
url = f'{endpoint}?month={month}&lat={latitude}&lon={longitude}&appid={API_KEY}'

# Make the API request
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse and work with the response data (which is typically in JSON format)
    weather_data = response.json()
    print(weather_data)
else:
    # Print an error message if the request was not successful
    print(f'Error: {response.status_code}, {response.text}')
