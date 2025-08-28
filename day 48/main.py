

from selenium.webdriver.common.by import By

from selenium import webdriver
#to keep the Chrome browser open
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")
# price=driver.find_element(By.CLASS_NAME,"a-price-whole").text
#
# price_paise=driver.find_element(By.CLASS_NAME,"a-price-fraction").text
# print(f"The price is :{price}.{price_paise}")
# element=driver.find_element(By.NAME,"field-keywords")
# print(element.get_attribute("id"))
# print(element.get_attribute("class"))
# print(element.tag_name)
# print(element.get_attribute("placeholder"))
# print(element.get_attribute("autocomplete"))
# go_button=driver.find_element(By.ID,"nav-search-submit-button")
# print(go_button.tag_name)
# print(go_button.get_attribute("type"))
# print(go_button.get_attribute("class"))
# print(go_button.size)
# link=driver.find_element(By.CSS_SELECTOR,".a-spacing-base span")
# print(link.text)
# print(driver.find_element(By.XPATH,'//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[3]/span[2]/span[2]').tag_name)
# list1=driver.find_elements(By.CLASS_NAME,"a-price-whole")
# for element in list1:
#     print(element.text)
event_time=driver.find_elements(By.CSS_SELECTOR,".event-widget time")
event_name=driver.find_elements(By.CSS_SELECTOR,".event-widget li a")
events={}
for n in range(len(event_time)):
    events[n]={
        "time":event_time[n].text,
        "name":event_name[n].text
    }
print(events)
# l2=driver.find_element(By.XPATH,'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[2]').text
# l3=driver.find_element(By.XPATH,'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[3]').text
# l4=driver.find_element(By.XPATH,'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[4]').text
# l5=driver.find_element(By.XPATH,'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[5]').text
# dict1={
#     "time":l1[0:10],
#     "name":l1[11:33]
# }
# dict2={"time":l2[0:10],
#        "name":l2[11:26]}
# dict3={
#     "time":l3[0:10],
#     "name":l3[11:100]
# }
# dict4={
#     "name":l4[0:10],
#     "time":l4[11:30]
# }
# dict5={
#     "time":l5[0:10],
#     "name":l5[11:35]
# }
# events={0:dict1,1:dict2,2:dict3,3:dict4,4:dict5}
# print(events  )
driver.quit()