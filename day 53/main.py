


from bs4 import BeautifulSoup
from selenium  import webdriver
from selenium.webdriver.common.by import By
import requests
from time import sleep
FORM_LINK="https://docs.google.com/forms/d/e/1FAIpQLSd6-57Q0b1kRaxmZkd5dZvNB19f5X4l83IflKMmBFaYK7qtig/viewform?usp=header"
response=requests.get("https://appbrewery.github.io/Zillow-Clone/")
print(response.status_code)
content=response.text
soup=BeautifulSoup(content,"lxml")
price_list=[]
address_list=[]

links_list=[]
rent_house=soup.find_all(name="li",class_="ListItem-c11n-8-84-3-StyledListCardWrapper")

for home in rent_house:
     prices=home.select_one(name="span",selector=".PropertyCardWrapper__StyledPriceLine").getText().split("+")[0].split("/")[0]
     price_list.append(prices)
     address=home.find(name="address").getText()
     address_list.append(address)
     link=home.find(name="a").get("href")
     links_list.append(link)
address_list=[l1.strip().strip("|") for l1 in address_list]
print(address_list)

def fill_form_and_submit(driver,address,price,link):

       sleep(3)
       driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(address)

       sleep(4)
       driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(price)


       sleep(2)
       driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(link)
       sleep(1)
       driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()
chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_option)
driver.get(FORM_LINK)
for address,price,link in zip(address_list,price_list,links_list):
        fill_form_and_submit(driver,address, price, link)
        sleep(4)
        driver.find_element(By.LINK_TEXT,"Submit another response").click()
driver.get("https://docs.google.com/spreadsheets/d/1kWLPGrmShvuB-i1L2uVwstumL9gEUp6RXTX-QhjN00w/edit?resourcekey=&gid=346699481#gid=346699481")
