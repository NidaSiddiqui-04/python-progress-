import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# --- CONFIG ---
USERNAME = "rumiruba.10"
PASSWORD = "Nida@123"
MAX_FOLLOWS = 10  # keep this low to avoid restriction
class InstaFollowers:
     def __init__(self):
        self.driver = webdriver.Chrome()




     def login(self):
        self.driver.get("https://www.instagram.com/")
        WebDriverWait(self.driver, 20).until(
        EC.presence_of_element_located((By.NAME, "username"))
        )
        self.driver.find_element(By.NAME, "username").send_keys(USERNAME)
        self.driver.find_element(By.NAME, "password").send_keys(PASSWORD)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(random.randint(8,12))
        save_login_prompt = self.driver.find_element(By.XPATH, "//div[contains(text(),'Not now')]")
        if save_login_prompt:
            save_login_prompt.click()
        time.sleep(random.randint(5,9))
        print("✅ Logged in")
     def find_follower(self):
         self.driver.get("https://www.instagram.com/art__and__craft.__/")
         time.sleep(random.randint(5,8))
         followers = self.driver.find_element(By.XPATH, "//a[contains(@href, '/followers/')]")
         followers.click()
         print("✅ Followers pop-up opened")
         time.sleep(random.randint(3,8))
         popup = self.driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]')

         # scroll loop
         for i in range(8):  # increase range for more scrolling
             self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", popup)
             time.sleep(random.randint(5,10))  # wait to load new followers

     def follow(self):
         buttons=self.driver.find_elements(By.CLASS_NAME,"_ap3a _aaco _aacw _aad6 _aade")
         for follow in buttons:
                follow.click()
                time.sleep(random.randint(1,3))
                print("followed")

         self.driver.quit()
bot=InstaFollowers()
bot.login()
bot.find_follower()
bot.follow()
# # ---- GO TO TARGET PROFILE ----
# driver.get("https://www.instagram.com/instagram/")  # example profile
# time.sleep(random.randint(5, 10))
#
# # ---- OPEN FOLLOWERS POP-UP ----
# followers_link = WebDriverWait(driver, 20).until(
#     EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/followers/')]"))
# )
# followers_link.click()
#
# popup = WebDriverWait(driver, 20).until(
#     EC.presence_of_element_located((By.XPATH, "//div[@role='dialog']//div[@class='_aano']"))
# )
#
# print("✅ Followers pop-up opened")
#
# # ---- SCROLL AND FOLLOW SAFELY ----
# followed = 0
# while followed < MAX_FOLLOWS:
#     buttons = driver.find_elements(By.XPATH, "//button[text()='Follow']")
#
#     for btn in buttons:
#         try:
#             driver.execute_script("arguments[0].scrollIntoView(true);", btn)
#             time.sleep(random.uniform(2, 5))  # wait like a human
#             btn.click()
#             followed += 1
#             print(f"👉 Followed {followed} users")
#
#             if followed >= MAX_FOLLOWS:
#                 break
#
#             # random extra wait
#             time.sleep(random.uniform(5, 12))
#
#         except Exception as e:
#             print("⚠️ Error:", e)
#
#     # scroll popup a bit more
#     driver.execute_script("arguments[0].scrollTop += 300", popup)
#     time.sleep(random.uniform(4, 8))
#
# print("✅ Done, followed safely!")
# driver.quit()
