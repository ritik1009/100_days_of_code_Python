import requests
import json
from datetime import datetime
#import json
#response =requests.get(url='http://api.open-notify.org/iss-now.json')
#response.raise_for_status()
#longitude = response.json()['iss_position']['longitude']
#latitude = response.json()['iss_position']['latitude']
#position = (longitude,latitude)
##response = response.json()
##resonse = json.dumps(response,indent=4)
#print(position)

url = "https://api.sunrise-sunset.org/json"
param = {
    "lat": 18.667089,
    "lng":73.732094,
    "formatted":0
}
response = requests.get(url=url,params=param)
response.raise_for_status()
response = response.json()

sunrise =response["results"]["sunrise"]

sunset =response["results"]["sunset"]
sunrise = sunrise.split("T")[1].split(':')[0]
sunset = sunset.split("T")[1].split(':')[0]
#response = json.dumps(response,indent=4)
now = datetime.now()
hour = now.hour
print(sunrise)