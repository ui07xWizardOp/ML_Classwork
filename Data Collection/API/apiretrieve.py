import requests
import csv
import os

def fetch_weather_data():
    API_URL = "https://archive-api.open-meteo.com/v1/archive?latitude=52.52&longitude=13.41&start_date=2025-11-15&end_date=2025-11-29&hourly=temperature_2m"
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()
        
        times = data["hourly"]["time"]
        temps = data["hourly"]["temperature_2m"]
        
        output_file = os.path.join(os.path.dirname(__file__), "weather_api.csv")
        with open(output_file, "w", newline="") as wcsv:
            csv_writer = csv.writer(wcsv)
            csv_writer.writerow(["time", "temperature"])
            for t, temp in zip(times, temps):
                csv_writer.writerow([t, temp])
        print(f"Weather data saved to {output_file}")
        
        # Display the data
        print("\nFetched Weather Data (First 5 rows):")
        with open(output_file, "r") as rcsv:
            reader = csv.reader(rcsv)
            for i, row in enumerate(reader):
                print(row)
                if i >= 5: break
        
        print("\nNote: To fetch data from a different source, modify the 'API_URL' variable in this script.")
    except Exception as e:
        print(f"Error fetching API data: {e}")

if __name__ == "__main__":
    fetch_weather_data()
