import requests
from datetime import datetime

API_KEY = "fe7c51be8ac1418aa19140414251609"
WEATHER_URL = " http://api.weatherapi.com/v1/current.json"

def get_weather(city):
    params = {
        "key": API_KEY,
        "q": city,
        "aqi": "no"
    }
    response = requests.get(WEATHER_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code)
        return None

def parse_weather(data, city):
    if not data or "error" in data:
        print("Could not get weather for", city)
        return None
    temp_c = data["current"]["temp_c"]
    humidity = data["current"]["humidity"]
    condition = data["current"]["condition"]["text"]
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Timestamp: {timestamp}")
    print(f"City: {city}")
    print(f"Weather: {condition}")
    print(f"Temperature: {temp_c}°C")
    print(f"Humidity: {humidity}%")
    return {
        "timestamp": timestamp,
        "city": city,
        "condition": condition,
        "temperature": temp_c,
        "humidity": humidity
    }

def log_weather(entry, filename="weather_log.txt"):
    with open(filename, "a") as f:
        f.write(
            f"Timestamp: {entry['timestamp']}\n"
            f"City: {entry['city']}\n"
            f"Weather: {entry['condition']}\n"
            f"Temperature: {entry['temperature']}°C\n"
            f"Humidity: {entry['humidity']}%\n"
            f"{'-'*40}\n"
        )
    print(f"Weather info appended to {filename}")


city = input("Enter city name: ")
data = get_weather(city)
entry = parse_weather(data, city)
if entry:
    log_weather(entry)