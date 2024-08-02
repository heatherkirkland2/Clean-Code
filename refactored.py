class WeatherDataFetcher:
    def fetch_weather_data(self, city):
        # Simulated function to fetch weather data for a given city
        print(f"Fetching weather data for {city}...")
        # Simulated data based on city
        weather_data = {
            "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50, "city": "New York"},
            "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65, "city": "London"},
            "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70, "city": "Tokyo"}
        }
        return weather_data.get(city, {})

class DataParser:
    def parse_weather_data(self, data):
        # Function to parse weather data
        if not data:
            return "Weather data not available"
        city = data["city"]
        temperature = data["temperature"]
        condition = data["condition"]
        humidity = data["humidity"]
        return f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%"

class UserInterface:
    def get_user_input(self):
        city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
        detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
        return city, detailed

    def display_weather(self, forecast):
        print(forecast)

    def run(self):
        weather_fetcher = WeatherDataFetcher()
        data_parser = DataParser()

        while True:
            city, detailed = self.get_user_input()
            if city.lower() == 'exit':
                break

            data = weather_fetcher.fetch_weather_data(city)
            parsed_data = data_parser.parse_weather_data(data)

            if detailed == 'yes':
                forecast = f"Detailed forecast for {city}:\n{parsed_data}"
            else:
                forecast = parsed_data

            self.display_weather(forecast)



if __name__ == "__main__":
    user_interface = UserInterface()
    user_interface.run()