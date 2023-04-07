#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import *
from flight_data import *
from flight_search import *
from notification_manager import *
from datetime import datetime,timedelta


data = DataManager
flight_data = FlightData
flight_search = FlightSearch
flight_data_csv = data.get_data()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for j,i in enumerate(flight_data_csv['prices']):
    if i['iataCode'] == '':
        city_name = i['city']
        print("\n city_name",city_name)
        city_code = flight_search.location_data(city_name=city_name)
        data.update_data(row_number=j+2,city_code=city_code)

flight_data_csv = data.get_data()
for destination in flight_data_csv['prices']:
    flight = flight_search.search_flight(
        origin_city_code="LON",
        destination_city_code = destination["iataCode"],
        from_date=tomorrow,
        to_date=six_month_from_today,
        price_to=destination['lowestPrice']
    )
    try:
        print(f"\n Flight {destination['city']}:-",flight.destination_airport)
    except:
        pass
