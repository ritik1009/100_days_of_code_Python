import requests
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def get_data():
        url = "https://api.sheety.co/d48a0724d6289b81239e7d79266d44a9/flightDeals/prices"
        response = requests.get(url=url)
        response = response.json()
        return response
    