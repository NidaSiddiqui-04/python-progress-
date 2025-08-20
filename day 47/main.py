import os
from dotenv import load_dotenv
import requests
import smtplib
import lxml
load_dotenv()
from bs4 import BeautifulSoup
EMAIL=os.environ.get("MY_EMAIL")
PASSWORD=os.environ.get("PASSWORD")

live_url="https://www.amazon.in/Paitsco-Kitten-Adults-Indoor-Interior/dp/B0DYYNB5HV/ref=sr_1_6?crid=2TH1Z63Y7BRQ9&dib=eyJ2IjoiMSJ9.uvmh8QimHrxq5dwsqNelg3bv8vYv-A5XfIrz3zmCk_xGxmSSedNXs0v_7bHz5wU2UoWZXxTqnQvzvkFQdA_i4C-MANmmIK5ijTd0nWfBl-V9odhZ9vHtOsGI7DhPWGBypmqRhKKRF0Z9mIVxfNy_F98_fpYk0JWC8M8CgSRhGNeQQm_-O237-joobTqgUsQhHDROyviXoA2yT9SYYznHYvyZBcA_Fdk-iSY2FRozg6U15Xy9nOcQQAYSUgnT95F4mS4lZMuuy1M7z22F6wB7Dui9AmHzbHTmthOtf0v1evQ._2Dds-EBa9NI8MZ42S8e8tv6naO1C2VftxwuOSBh1Gw&dib_tag=se&keywords=cat%2Bhouse%2Bfor%2Badult%2Bcat&qid=1755584341&sprefix=cat%2Bho%2Caps%2C301&sr=8-6&th=1"
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
    "Accept-Language":"en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,"
}
response=requests.get(url=live_url,headers=headers)
content=response.text
soup=BeautifulSoup(content,"lxml")
price=soup.find_all(name="span",class_="a-price aok-align-center")
item_price=""
for rate in price:
    item_price+=rate.select_one(selector="span",class_="a-offscreen").getText()

price_without_currency=item_price.split("₹")[1]
floating_price=float(price_without_currency)
print(floating_price)
message=f"Paitsco Cat House for Cat and Small Dogs Cat and Dog House, Kitten Home Adults Cat Bed Indoor Pet Bed Soft Interior, Design (Grey, Small) is now Rs{floating_price}\n{live_url}"

if floating_price<1100:
    print("yes")
    with smtplib.SMTP("smtp.gmail.com",port=587) as mail:
        mail.starttls()
        mail.login(user=EMAIL,password=PASSWORD)
        mail.sendmail(from_addr=EMAIL,to_addrs=os.environ.get("MAIL"),msg=f"subject:Amazon Price Alert!\n\n{message}")
        print("send")
else:
    print("no")