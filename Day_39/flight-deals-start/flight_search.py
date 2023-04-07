import requests
import json
from flight_data import *

api_id = "KtlGvZ1N_gif5IprgwA-SmZTSRuLQcya"
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def location_data(city_name=''):
        url = "https://api.tequila.kiwi.com/locations/query"
        params = dict()
        params['term'] = city_name
        params['locale'] = "en-US"
        params['location_types'] = "airport"
        params['limit'] = "1"
        params['active_only'] = True
        header = dict()
        header['accept'] = "application/json"
        header['apikey'] = api_id
        response = requests.get(url, params=params, headers=header)
        response = response.json()
        print("\n response", response)
        city_code = response["locations"][0]["city"]["code"]
        return city_code

    def search_flight(origin_city_code = '',destination_city_code='',from_date='',to_date='',price_to =''):
        url = "https://api.tequila.kiwi.com/v2/search"
        params =dict()
        params['fly_from'] = f"city:{origin_city_code}"
        params['fly_to'] = f"city:{destination_city_code}"
        params['date_from '] = from_date.strftime("%d/%m/%Y")
        params['date_to '] = to_date.strftime("%d/%m/%Y")
        params['price_to'] = price_to
        params['nights_in_dst_from'] = 7
        params['nights_in_dst_to'] = 28
        params['one_for_city'] = 1
        params['max_stopovers'] = 0
        params['curr'] = "GBP"
        params['flight_type'] = 'round'
        header = dict()
        header['accept'] = "application/json"
        header['apikey'] =  api_id
        response = requests.get(url,headers=header,params=params)
        #response =response.json()
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None
        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        #response = json.dumps(response,indent=4)
        #print("\n flight response",response)
        return flight_data

#FS = FlightSearch
#FS.search_flight(origin_city_code="LON",destination_city_code="PAR",from_date="16/03/2023",to_date="18/03/2023",price_to ='54')