import psycopg2
import matplotlib.pyplot as plt

# Function to fetch data from the database for all months for each instance
def fetch_all_monthly_climate_data():
    conn = psycopg2.connect(
        host="localhost",
        database="plants",
        user="marco",
        # password="your_password"  # Replace with your actual password
    )
    cursor = conn.cursor()

    query = "SELECT * FROM plant_climate_data;"
    cursor.execute(query)
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data

# Extract temperatures for each month for a specific instance and convert to Celsius
def extract_instance_temperatures(data):
    instance_temperatures = []

    for row in data:
        instance_data = []
        for month_idx in range(1, 13):
            month_key = f'{month_idx:02}_climate'  # Generate column name like '01_climate', '02_climate', ..., '12_climate'
            month_data = row[month_idx]
            avg_temp_kelvin = month_data['result']['temp']['mean']
            avg_temp_celsius = avg_temp_kelvin - 273.15  # Convert from Kelvin to Celsius
            instance_data.append(avg_temp_celsius)
        instance_temperatures.append(instance_data)

    return instance_temperatures

# Main function to orchestrate the process
def main():
    instances_data = fetch_all_monthly_climate_data()
    instances_temperatures = extract_instance_temperatures(instances_data)
    num_instances = len(instances_temperatures)

    plt.figure(figsize=(12, 8))

    for i in range(num_instances):
        plt.plot(range(1, 13), instances_temperatures[i], marker='o', linestyle='-', label=f'Instance {i + 1}')

    plt.xlabel('Months')
    plt.ylabel('Average Temperature (K)')
    plt.title('Temperature Progression Throughout the Year for Different Instances')
    plt.xticks(range(1, 13), ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
