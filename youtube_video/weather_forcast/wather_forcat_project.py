#    api_key = 'bd5e378503939ddaee76f12ad7a97608'
#     url = f'http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={api_key}&units=metric'
#     response = requests.get(url)
#     data = response.json()
#     return data

import requests

def wether_function(data):
    api_key = 'bd5e378503939ddaee76f12ad7a97608'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={data}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    return data
def display_function_weather(wether):
    if  "weather" in wether and  "main" in wether:
        dec = wether["weather"][0]["description"]
        temp = wether["main"]["temp"]
        wind = wether["wind"]["speed"]

        print("dec",dec)
        print("temp",temp)
        print("wind speed",wind)


def main():

    data = input("please enter your city name")
    # print("data",data)

    wether = wether_function(data)
    # print("wether",wether)

    display_function_weather(wether)





if __name__ == "__main__":
    main()
