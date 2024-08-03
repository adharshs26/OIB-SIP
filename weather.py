import requests

# Replace 'YOUR_API_KEY' with your actual API key from Weatherbit
API_KEY = '8670257443944dccb7da07374af4c6ae'

def get_weather(location):
    url = "https://api.weatherbit.io/v2.0/current"
    params = {
        'city': location,
        'key': API_KEY
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data

def display_weather(data):
    if 'data' not in data or len(data['data']) == 0:
        print("Error: Weather data not available.")
        return

    weather = data['data'][0]
    temp = weather['temp']
    humidity = weather['rh']
    weather_description = weather['weather']['description']

    print(f"Location: {weather['city_name']}")
    print(f"Temperature: {temp}°C")
    print(f"Humidity: {humidity}%")
    print(f"Weather: {weather_description.capitalize()}")

def main():
    location = input("Enter the location (city name or ZIP code): ")
    data = get_weather(location)
    display_weather(data)

if __name__ == "__main__":
    main()
