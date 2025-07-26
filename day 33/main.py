import requests
import datetime as dt
# current=requests.get(url="http://api.open-notify.org/iss-now.json")
# print(current.raise_for_status())
# print(current.status_code )
# data=current.json()["iss_position"]
# print(data)
# longitude=current.json()["iss_position"]["longitude"]
# print(longitude)
# latitude=current.json()["iss_position"]["latitude"]
# iss_position=(longitude,latitude)
# print(iss_position)
parameters={
    "lat":20.593683,
    "lng":78.962883
}
response=requests.get(" https://api.sunrise-sunset.org/json?lat=23.486576&lng=80.106567&formatted=0")
data=response.json()
print(data)
sunrise=data["results"]["sunrise"]

sunset=data["results"]["sunset"]
print(sunrise)
print(sunrise.split("T")[1].split(":")[2])

print(sunset)
current_time=dt.datetime.now()
print(current_time)