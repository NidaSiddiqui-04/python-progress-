import os
import requests
from dotenv import load_dotenv
load_dotenv()
IATA_ENDPOINT="https://test.api.amadeus.com/v1/reference-data/locations/cities"
FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"
class FlightSearch:
    def __init__(self):
        self.api_key=os.environ.get("API_KEY")
        self.api_password=os.environ.get("API_SECRET")
        self.token=self.get_token()

    def get_token(self):
        api_url="https://test.api.amadeus.com/v1/security/oauth2/token"
        header={
            "Content-Type": "application/x-www-form-urlencoded"
        }
        body={
            "grant_type":"client_credentials",
            "client_id":self.api_key,
            "client_secret":self.api_password
        }
        response=requests.post(url=api_url,headers=header,data=body)
        return response.json()["access_token"]

    def get_destination_code(self, city_name):
        headers = {"Authorization": f"Bearer {self.token}"}
        query = {
            "keyword": city_name,
            "max": 2,
            "include":"AIRPORTS",

        }
        response = requests.get(
            url=IATA_ENDPOINT,
            headers=headers,
            params=query
        )

        print(f"Status code {response.status_code}. Airport IATA: {response.text}")
        try:
            code = response.json()["data"][0]['iataCode']
        except KeyError:
            print(f"KeyError: No airport code found for {city_name}.")
            return ""
        return code
    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time,is_direct=True):
        headers = {"Authorization": f"Bearer {self.token}"}
        query = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true"if is_direct else "false",
            "currencyCode": "GBP",
            "max": "10",
        }

        response = requests.get(
            url=FLIGHT_ENDPOINT,
            headers=headers,
            params=query,
        )

        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            
            return None
        return response.json()