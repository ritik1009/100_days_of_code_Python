import requests
import json

api_key = "0e21bfb00f9826fac72c406f8a42e218"
api_url = "https://api.openweathermap.org/data/2.5/weather"
lat = 28.632429
lon = 77.218788
params = dict()
params['lat'] = lat
params['lon'] = lon
params['appid'] = api_key
response = requests.get(url = api_url,params=params)
response =response.json()
weather_slice = response["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an Umbrella")
#weather = response['weather'][0]['main']
#icon = response['weather'][0]['icon']
#id = response['weather'][0]['id']
#response = json.dumps(response,indent = 4)

print(response)

