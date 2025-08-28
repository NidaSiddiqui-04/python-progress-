import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep


load_dotenv()
email = os.environ.get("EMAIL")
password = os.environ.get("PASSWORD")
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
print(user_data_dir)
chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument("--disable-extensions")
chrome_option.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36")
chrome_option.add_experimental_option("detach", True)
# :white_tick: Correct flag
chrome_option.add_argument(f"--user-data-dir={user_data_dir}")
chrome_option.add_argument("--profile-directory=Profile 1")

chrome_option.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_option.add_experimental_option("useAutomationExtension", False)
driver = webdriver.Chrome(options=chrome_option)
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined});"
})
driver.get("https://appbrewery.github.io/gym/")
element = WebDriverWait(driver, 10)
login_button = element.until(ec.element_to_be_clickable((By.ID, "login-button")))
login_button.click()
email_input = element.until(ec.presence_of_element_located((By.ID, "email-input")))
email_input.clear()
email_input.send_keys(email)
password_input = element.until(ec.presence_of_element_located((By.ID, "password-input")))
password_input.clear()
password_input.send_keys(password)
login = element.until(ec.element_to_be_clickable((By.ID, "submit-button")))
login.click()
booked=0
waitlisted=0
already_booked_waitlisted=0
total_classes=[]
element.until(ec.presence_of_element_located((By.ID,"schedule-page")))
class_=driver.find_elements(By.CLASS_NAME,"Schedule_dayGroup__y79__")
for classes in class_:
    day=classes.find_element(By.CLASS_NAME,"Schedule_dayTitle__YBybs").text

    if "Tue" in day:

        class_time=classes.find_elements(By.CSS_SELECTOR,".ClassCard_cardContent__WGvPp p[id^='class-time-']")
        time=[time.text for time in class_time]

        if "Time: 6:00 PM" in time:

            class_name=classes.find_element(By.CSS_SELECTOR,".ClassCard_cardContent__WGvPp h3[id^='class-name-spin-']").text
            print(class_name)

            button = classes.find_element(By.XPATH, '//*[@id="book-button-spin-2025-08-26-1800"]')





            class_info=f"{class_name} on {day}"

            if button.text=="Booked":
                   print(f"✔️ Already Booked: {class_info}")
                   booked+=1
                   total_classes.append(f"[booked] {class_info}")
            elif button.text=="Waitlisted":
                 print(f"✔️Already on Waitlist:{class_info}")
                 already_booked_waitlisted+=1
                 total_classes.append(f"[waitlisted] {class_info}")
            elif button.text=="Join Waitlist":

                 button.click()
                 sleep(1)
                 print(f"😊Joined waitlist for: {class_info}")
                 waitlisted+=1
                 total_classes.append(f"[new waitlist] {class_info}")
            else:

                 button.click()
                 sleep(1)

                 print(f"🌼Booked:{class_info}")
                 booked+=1
                 total_classes.append(f"[new bookings] {class_info}")
    elif  "Thu" in day:

        class_time = classes.find_elements(By.CSS_SELECTOR, ".ClassCard_cardContent__WGvPp p[id^='class-time-']")
        time = [time.text for time in class_time]
        print(time)
        if "Time: 6:00 PM" in time:

            class_name = classes.find_element(By.CSS_SELECTOR, ".ClassCard_cardContent__WGvPp h3[id^='class-name-spin-']").text
            print(class_name)
            button2=classes.find_element(By.XPATH, '//*[@id="book-button-spin-2025-08-28-1800"]')


            class_info = f"{class_name} on {day}"

            if button2.text == "Booked":
                print(f"✔️ Already Booked: {class_info}")
                already_booked_waitlisted += 1
                total_classes.append(f"[booked] {class_info}")
            elif button2.text == "Waitlisted":
                print(f"✔️Already on Waitlist:{class_info}")
                already_booked_waitlisted += 1
                total_classes.append(f"[waitlisted] {class_info}")
            elif button2.text == "Join Waitlist":

                button2.click()
                sleep(1)
                print(f"😊Joined waitlist for: {class_info}")
                waitlisted += 1
                total_classes.append(f"[new waitlist] {class_info}")
            else:

                button2.click()
                sleep(1)

                print(f"🌼Booked:{class_info}")
                booked += 1
                total_classes.append(f"[new bookings] {class_info}")








print("---------BOOKING SUMMARY----------")
print(f"New bookings:{booked}")
print(f"Waitlisted joined:{waitlisted}")
print(f"Already booked/waitlisted:{already_booked_waitlisted}")
total=booked+waitlisted+already_booked_waitlisted
print(f"Total Tuesday and Thursday 6pm classes processsed:{total}")


print("------DETAILED CLASS LIST-------")
for details in total_classes:
    print(f" ♦️{details}")
