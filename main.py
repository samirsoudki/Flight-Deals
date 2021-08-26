#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import os
API_Tequila_Key = os.getenv("API_Tequila_Key")
SERVER_KIWI = "https://tequila-api.kiwi.com/v2/search"
IATA_CODE = "KBP"
sheety_url_data = "https://api.sheety.co/89f436d23e73b914073612e6bcb6d739/flightDeals/prices"
from pprint import pprint
import requests
response = requests.get(sheety_url_data)
data = response.json()
sheet_data = data.get("prices")
price = [x.get("lowestPrice") for x in sheet_data]
x = [x.get("iataCode") for x in sheet_data]
flight_list = []
flight_prices_list = []
min_price = 50
for n in range(0, len(x)):
    header = {
        "apikey": API_Tequila_Key
    }
    params = {
        "fly_from": IATA_CODE,
        "fly_to": x[n],
        "date_from": "01/09/2021",
        "data_to": "01/3/2022",
        "flight_type": "oneway",
        "curr": "USD",
    }
    r = requests.get(url=SERVER_KIWI, params=params, headers=header)
    data_flights = r.json()
    data_flight = data_flights.get("data")
    flight = data_flight[0]
    flight_from = flight.get("flyFrom")
    flight_to = flight.get("flyTo")
    flight_price = flight.get("price")
    flight_day_from_home = flight.get("local_departure").split("T")
    flight_day = flight_day_from_home[0]
    flight_day_to_destination = flight.get("local_arrival")
    from_country = flight.get("cityFrom")
    to_country = flight.get("cityTo")
    flight_prices_list.append(flight_price)
    statement = f"you will fly from {flight_from}, {from_country} to {flight_to}, {to_country}, for ${flight_price}, on {flight_day}"
    for number in flight_prices_list:
        if min_price > number:
            min_price = number
            flight_list.append(statement)

pprint(flight_list)










