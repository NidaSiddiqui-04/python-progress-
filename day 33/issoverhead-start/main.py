import time

import requests
from datetime import datetime
import smtplib


MY_EMAIL="nidasiddiquui.0404@gmail.com"
PASSWORD="yhkqxtepguqfjknh"

MY_LAT = 23.4890237 # Your latitude
MY_LONG = 80.093248 # Your longitude
def iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])


#Your position is within +5 or -5 degrees of the ISS position
    if MY_LAT-5<=iss_latitude>=MY_LAT+5 and MY_LONG-5<=iss_longitude>=MY_LONG+5:
         return True


def nighttime():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
      }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    print(sunset)

    time_now = datetime.now().hour

    print(time_now)

    if time_now>=sunset or time_now<=sunrise:
        return True

while True:
    time.sleep(60)

    if iss_overhead() and nighttime():
        with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL,password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,to_addrs="rubarumi.0404@gmail.com",msg="Subject:Look up😊😋\n\n The iss is above you")
#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.


