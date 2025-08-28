from selenium import webdriver
from selenium.webdriver.common.by import By
from  time import  sleep
from selenium.webdriver.common.keys import Keys
PROMISED_DOWN=150
PROMISED_UP=10
TWITTER_EMAIL="rumiruba.10@gmail.com"
TWITTER_PASSWORD="Nida@123"
class InternetSpeedTwitterBot:


    def __init__(self):
        self.chrome_option=webdriver.ChromeOptions()
        self.chrome_option.add_experimental_option("detach",True)
        self.driver=webdriver.Chrome(options=self.chrome_option)
        self.down=0
        self.up=0
    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        go=self.driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[2]/a/span[4]')
        go.click()
        sleep(60)
        self.down=self.driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        print("down:",self.down)
        self.up=self.driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        print("up:",self.up)

    def tweet_at_provider(self):
        self.driver.get("https://x.com/")
        self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[4]/a/div/span/span').click()
        sleep(3)
        email=self.driver.find_element(By.NAME,"text")
        email.send_keys(TWITTER_EMAIL,Keys.ENTER)
        sleep(3)
        self.driver.find_element(By.NAME,"text").send_keys("@10Rumiruba",Keys.ENTER)
        sleep(3)
        self.driver.find_element(By.NAME,"password").send_keys(TWITTER_PASSWORD,Keys.ENTER)
        sleep(5)
        tweet=self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        tweet.send_keys(f"Hey Internet Provider,why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?")
        post=self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button/div/span/span')
        post.click()
        print("successful")
        # self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div/button[2]/div').click()

bot=InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()