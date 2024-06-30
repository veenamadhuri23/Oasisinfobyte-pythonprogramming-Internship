import requests

    def get_weather(api_key, location):
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            'q': location,
            'appid': api_key,
            'units': 'metric'
        }
        response = requests.get(base_url, params=params)
        return response.json()

    def display_weather(weather_data):
        if weather_data.get('cod') != 200:
            print(f"Error: {weather_data.get('message')}")
            return

        city = weather_data.get('name')
        country = weather_data.get('sys', {}).get('country')
        temperature = weather_data.get('main', {}).get('temp')
        humidity = weather_data.get('main', {}).get('humidity')
        weather_condition = weather_data.get('weather', [])[0].get('description')

        print(f"City: {city}, {country}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather Condition: {weather_condition}")

    def main():
        api_key = '30d4741c779ba94c470ca1f63045390a'  # Replace with your actual OpenWeatherMap API key
        location = input("Enter the city name or ZIP code: ")
        weather_data = get_weather(api_key, location)
        display_weather(weather_data)

    if __name__ == "__main__":
        main()
