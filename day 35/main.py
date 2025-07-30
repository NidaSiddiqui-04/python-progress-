import requests

from twilio.rest import Client
whatsapp_no="whatsapp:+14155238886"
no="+12513188030"
account_sid="AC261816a56dcff008b296f64e0db556dd"
auth_token="bea45fd7f803e9eead7b8ba518da8e19"
my_key="8e49f9286aaa9a04f7a255e7f0e81848"
response=requests.get(url="https://api.openweathermap.org/data/2.5/forecast?lat=23.486576&lon=80.106567&appid=8e49f9286aaa9a04f7a255e7f0e81848&cnt=4")
print(response.status_code)
data=response.json()
# print(data["list"][1]["weather"][0]["description"])
print(data)
will_rain=False
for waether_data in data["list"]:

    condition_code= waether_data["weather"][0]["id"]
    print(condition_code)
    if int(condition_code)<700:
        will_rain=True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(

        from_="+12513188030",
        body="It's going to rain today.remember to bring your☔",
        to="+987063"
    )

    print(message.status)
