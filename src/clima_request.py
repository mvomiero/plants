from dotenv import load_dotenv
import os
import json
import time
from colorama import Fore, Back, Style, init

# Initialize colorama
init()

import requests

load_dotenv()

API_KEY = os.getenv("API_KEY")

def get_climatic_data_for_location(latitude, longitude):
    #print(f"{Fore.RED}get_climatic_data_for_location.{Style.RESET_ALL}")
    all_month_data = []

    for month in range(1, 13):
        # OpenWeatherMap Aggregated Monthly Historical Weather API endpoint
        endpoint = 'https://history.openweathermap.org/data/2.5/aggregated/month'

        # Construct the API URL for the current month
        url = f'{endpoint}?month={month}&lat={latitude}&lon={longitude}&appid={API_KEY}'

        # Make the API request
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            weather_data = response.json()
            all_month_data.append(weather_data)  # Store data for the current month
        else:
            print ("error!")
            #print(f'Error for month {month}: {response.status_code}, {response.text}')
        #print("month %d retrieved" % month)

    return all_month_data


# # Example usage:
# latitude = 52.52  # Replace with your desired latitude
# longitude = 13.4  # Replace with your desired longitude

# data_for_location = get_climatic_data_for_location(latitude, longitude)
# print(data_for_location)
