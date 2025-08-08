import os

import requests



SHEETY_API="https://api.sheety.co/a0657c080fff492f2e35bee1e62097aa/flightDeals/sheet1"

class DataManager:
    def __init__(self):
        self.username=os.environ.get("USER_NAME")
        self.password=os.environ.get("PASS_WORD")
        self.data={}
        
        self.user_endpoint=os.environ.get("USERS_ENDPOINT")
    def get_datasheet(self):
        response=requests.get(url=SHEETY_API,auth=(self.username,self.password))
        result=response.json()
        self.data=result["sheet1"]
        return self.data
    def update_sheety(self):
        for city in self.data:
            params={
                "sheet1":
                    {
                        "iataCode":city["iataCode"]
                    }
            }
            response=requests.put(url=f"{SHEETY_API}/{city["id"]}",json=params,auth=(self.username,self.password))
            print(response.text)
    def get_customer_emails(self):
        
        response=requests.get(url=self.user_endpoint,auth=(self.username,self.password))
        print(response.status_code)
        data=response.json()
        print(data)
        self.costumer_data=data["users"]

        return self.costumer_data