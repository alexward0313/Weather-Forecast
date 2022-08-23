import requests
import sched
import time




API_KEY = "e51c515295f6492e9a70ae58d1639e64"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("What city would you like to monitor?\n")
requests_url = f"{BASE_URL}?appid={API_KEY}&q={city}"

response = requests.get(requests_url)

if response.status_code == 200:
    print("\n" + city)
    time.sleep(2)
    data = response.json()
    weather = data["weather"][0]["description"]
    print("Weather:", weather)
    time.sleep(2)
    temperature = round(data["main"]["temp"] - 273.15)*1.8 + 32
    print("Temperature:", temperature, "Fahrenheit")
    time.sleep(15)
else:
    print("An error occurred.")
    time.sleep(10)








