import requests
from  datetime import datetime
import os


os.environ['api_id'] = ''
os.environ['api_key'] = ''
os.environ['bearrer_token'] = ''
api_url = "https://trackapi.nutritionix.com/"

api_id = os.environ.get('api_id')
api_key = os.environ.get('api_key')
bearrer_token = os.environ.get('bearrer_token')
def get_natural_exercies(query=''):
    url = api_url +"v2/natural/exercise"
    param = {"query":query}
    header = {
        'x-app-id':api_id,
        'x-app-key':api_key,
        'x-remote-user-id':"0"}
    response = requests.post(url,json= param,headers=header)
    response =response.json()
    exercise = response['exercises'][0]['name']
    duration = response['exercises'][0]['duration_min']
    calories = response['exercises'][0]['nf_calories']
    response = posting_in_sheet(exercise=exercise,Duration= duration,Calories=calories)
    return response

def posting_in_sheet(exercise="",Duration= "",Calories=""):
    now = datetime.now()
    today = now.strftime("%d/%m/%Y")
    time = now.strftime("%I:%M:%S")
    header = {"Authorization": f"Bearer {bearrer_token}"}
    url = "https://api.sheety.co/d48a0724d6289b81239e7d79266d44a9/myWorkouts/workouts"
    body = {
        "workout":{
            "date":today,
            "time":time,
            "exercise": exercise.title(),
            "duration":Duration,
            "calories":Calories,
        }
    }
    response = requests.post(url,json=body,headers=header)
    response = response.json()
    return response

print(get_natural_exercies(query = 'ran 2km'))