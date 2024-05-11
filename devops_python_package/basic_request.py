# very simple module


import requests

url = "https://facebook.com"


response = requests.get(url)

if response.status_code == 200:
    print(response.raise_for_status)
else:
    print("you cant access the server",response.status_code)


print(response)





