import requests
def fetch_wether_data(location):
    api_key = 'bd5e378503939ddaee76f12ad7a97608'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    return data

def fetch_forecaste_data(location):
    api_key = 'bd5e378503939ddaee76f12ad7a97608'
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    return data

def display_wether(data):
    if 'main' in data and 'weather' in data:
        weather_dec = data['weather'][0]['description'].capitalize()
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        print("wind_speed",wind_speed)
        print("humidity",humidity)
        print("temperature",temp)
        print(weather_dec)
    else:
        print("unable to fetch data")

def display_forecast(data):
    if 'list' in data:
        print("Forecast:")
        for forecast in data['list']:
            date = forecast['dt_txt']
            temperature = forecast['main']['temp']
            weather_description = forecast['weather'][0]['description'].capitalize()
            print(f"- {date}: {weather_description}, {temperature}°C")
    else:
        print("Error: Unable to fetch forecast data.")


def main():
    print("welcome to wether forecast app"
          )
    location = input("please enter your location(city name or zip code)")

    print("\nfetching wether data...")

    weather_data = fetch_wether_data(location)

    print(weather_data)
    forcaste_data = fetch_forecaste_data(location)
    print("forcast_data",forcaste_data)

    print("\ncurrent wether:")
    display_wether(weather_data)

    print("\nforcast")
    display_forecast(forcaste_data)


if __name__ == "__main__":
    main()