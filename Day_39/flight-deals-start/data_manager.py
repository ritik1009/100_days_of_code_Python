import requests
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def get_data():
        url = "https://api.sheety.co/d48a0724d6289b81239e7d79266d44a9/flightDeals/prices"
        response = requests.get(url=url)
        response = response.json()
        return response
    
    def update_data(row_number = '',city_code = ''):
        url = f"https://api.sheety.co/d48a0724d6289b81239e7d79266d44a9/flightDeals/prices/{row_number}"
        params = {
            "price":{
            "iataCode":city_code
            }
        }
        response = requests.put(url,json=params)
        repsonse = response.json()
        return response


dd = DataManager

print(dd.get_data())
    