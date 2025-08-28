from time import sleep

from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
option=webdriver.ChromeOptions()
option.add_experimental_option("detach",True)
# driver=webdriver.Chrome(options=option)
# driver.get("https://simple.wikipedia.org/wiki/Main_Page")
#
# # value=driver.find_element(By.LINK_TEXT,'272,233')
# # value.click()
# #
# #
# # value=driver.find_element(By.XPATH,'//*[@id="EnWpMpBook2"]/div[4]/a[2]')
# # value.click()
# search_text=driver.find_element(By.ID,"bodySearchInputMP")
# search_text.send_keys("python",Keys.ENTER)
# driver=webdriver.Chrome(options=option)
# driver.get("https://secure-retreat-92358.herokuapp.com/")
#
# first_name=driver.find_element(By.XPATH,'/html/body/form/input[1]')
# first_name.send_keys("Nida")
# last_name=driver.find_element(By.XPATH,'/html/body/form/input[2]')
# last_name.send_keys("Siddiqui")
# e_mail=driver.find_element(By.XPATH,'/html/body/form/input[3]')
# e_mail.send_keys("rubarumi.0404@gmail.com")
# button=driver.find_element(By.XPATH,'/html/body/form/button')
# button.click()
driver=webdriver.Chrome(options=option)
driver.get("https://ozh.github.io/cookieclicker/")
cookie=driver.find_element(By.XPATH,'//*[@id="bigCookie"]')
while True:
    cookie.click()
