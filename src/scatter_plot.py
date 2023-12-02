import psycopg2
import json
import matplotlib.pyplot as plt

# Function to fetch data from the database
def fetch_climate_data():
    conn = psycopg2.connect(
        host="localhost",
        database="plants",
        user="marco",
        # password="your_password"  # Replace with your actual password
    )
    cursor = conn.cursor()

    query = "SELECT may_climate FROM plant_climate_data;"
    cursor.execute(query)
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data

# Extract average temperature for May from each observation
def extract_average_temperature_may(data):
    may_avg_temp = []

    for row in data:
        month_data = row[0]  # Assuming data is already in dictionary format
        avg_temp_may = month_data['result']['temp']['mean']
        may_avg_temp.append(avg_temp_may)

    return may_avg_temp

# Plot scatter diagram for average temperature in May for each observation
def plot_average_temperature_may_vertical_line(may_avg_temp):
    plt.figure(figsize=(8, 6))
    plt.plot([1] * len(may_avg_temp), may_avg_temp, marker='o', linestyle='', label='May Average Temperature')

    plt.xlabel('Observations')
    plt.ylabel('Average Temperature in May (K)')
    plt.title('Average Temperature in May for Different Observations')
    plt.legend()
    plt.tight_layout()
    plt.show()

# Main function to orchestrate the process
def main():
    climate_data = fetch_climate_data()
    may_avg_temp = extract_average_temperature_may(climate_data)
    plot_average_temperature_may_vertical_line(may_avg_temp)

if __name__ == "__main__":
    main()
