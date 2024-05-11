import requests


def get_wether(city,api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    responce = requests.get(url)

    if responce.status_code == 200:
        data = responce.json()
        tem = data["main"]["temp"]
        dec = data["weather"][0]["description"]
        print(f"the chennai wether is{tem} and the desc {dec}")
    else:
        print("you cant access the data",responce.status_code)



def main():
    api_key = "bd5e378503939ddaee76f12ad7a97608"
    city = input("enter the city name")

    get_wether(city, api_key)


if __name__ == "__main__":
    main()