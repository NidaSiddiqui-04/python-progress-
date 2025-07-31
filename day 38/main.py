import requests
import os
from datetime import datetime
NUTRITIONIX_ID=os.environ.get("NUTRITIONIX_ID")
NUTRITIONIX_KEY=os.environ.get("NUTRITIONIX_KEY")

API_ENDPOINT="https://trackapi.nutritionix.com/v2/natural/exercise"
parameters={
    "query":input("enter you routine:"),
    "weight_kg":55,
    "height_cm":124.36,
    "age":22

}
header={
    "x-app-id":NUTRITIONIX_ID,
    "x-app-key":NUTRITIONIX_KEY,
    "Content-Type": "application/json"
}
response=requests.post(url=API_ENDPOINT,json=parameters,headers=header)
print(response.status_code)
result=response.json()

print(result)
SHEETY_USERNAME=os.environ.get("SHEETY_USERNAME")
SHEETY_PASSWORD=os.environ.get("SHEETY_PASSWORD")
SHEETY_BEAERER_TOKEN  = os.environ.get("SHEETY_BEAERER_TOKEN")
headers={
    "Authorization":SHEETY_BEAERER_TOKEN,
}
SHEETY_ENDPOINT=os.environ.get("SHEETY_ENDPOINT")
today=datetime.now()
time=today.time()
print(time)
for exercise in result["exercises"] :
    parameters={
    "sheet1":{
    "date":today.strftime("%Y-%m-%d"),
    "time":time.strftime("%X"),
    "exercise":exercise["name"].title(),
    "duration":exercise["duration_min"],
    "calories":exercise["nf_calories"]
        }
    }

    response=requests.post(url=SHEETY_ENDPOINT,json=parameters,headers=headers)
    print(response.text)