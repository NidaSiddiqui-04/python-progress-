from datamanager import DataManager
from flightsearch import FlightSearch
from datetime import timedelta,datetime
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager



flight_search=FlightSearch()
data=DataManager()
sheet_data=data.get_datasheet()

notification=NotificationManager()



for code in sheet_data:
        if code["iataCode"]=="":
            code["iataCode"]=flight_search.get_destination_code(code["city"])
            print(sheet_data)

data.data=sheet_data
data.update_sheety()
costumer_data=data.get_customer_emails()
costomer_email_list=[row ["emailAddress"] for row in costumer_data]
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))
ORIGIN_CITY="DEL"

for destination in sheet_data:
    print(f"Getting flights for {destination['city']}...")
    flights = flight_search.check_flights(
        ORIGIN_CITY,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
        
    )
    cheapest_flight = find_cheapest_flight(flights)
    print(f"{destination['city']}: £{cheapest_flight.price}")

    if  cheapest_flight.price =="N/A":
         stopover_flights=flight_search.check_flights(
              ORIGIN_CITY,
              destination["iataCode"],
              from_time=tomorrow,
              to_time=six_month_from_today,
              is_direct=False
         )
         cheapest_flight=find_cheapest_flight(stopover_flights)
         print(f"Cheapest indirect flight price is:{cheapest_flight.price}")
    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        
        if cheapest_flight.stops == 0:
            message = f"Low price alert! Only GBP {cheapest_flight.price} to fly direct "\
                      f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "\
                      f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
        else:
            message = f"Low price alert! Only GBP {cheapest_flight.price} to fly "\
                      f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "\
                      f"with {cheapest_flight.stops} stop(s) "\
                      f"departing on {cheapest_flight.out_date} and returning on {cheapest_flight.return_date}."
    
        notification.send_emails(message_body=message,email_list=costomer_email_list)



