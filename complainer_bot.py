from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv

SPEED_TEST = "https://www.speedtest.net/"
TWITTER = "https://twitter.com/i/flow/login"
load_dotenv("G:\My Drive\Programming\Python\EnvironmentVariables\.env.txt")
TWITTER_UN = os.getenv("TWITTER_UN")
TWITTER_PW = os.getenv("TWITTER_PW")


class InternetSpeedTwitterBot:

    def __init__(self, chrome_driver_path):
        # initialize selenium
        super().__init__()
        self.down = 0
        self.up = 0
        self.service = Service(chrome_driver_path)
        self.driver = webdriver.Chrome(service=self.service)


    def get_internet_speed(self):
        # open speedtest.net and get current download/upload speeds
        self.driver.get(SPEED_TEST)
        self.driver.find_element(By.CLASS_NAME, "start-button").click()
        time.sleep(60)
        self.down = int(float(self.driver.find_element(By.CLASS_NAME, "download-speed").text))
        self.up = int(float(self.driver.find_element(By.CLASS_NAME, "upload-speed").text))

    def tweet_at_provider(self, PROMISED_DOWN, PROMISED_UP):
        # tweet at comcast if speeds are below promised rate
        # login with username and password
        self.driver.get(TWITTER)
        time.sleep(2)
        username = self.driver.find_element(By.NAME, "text")
        username.send_keys(TWITTER_UN)
        username.send_keys(Keys.ENTER)
        time.sleep(2)
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(TWITTER_PW)
        password.send_keys(Keys.ENTER)
        time.sleep(5)

        # click tweet button
        tweet_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
        tweet_button.click()
        time.sleep(1)

        # enter text
        text = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div')
        text.send_keys(f"Hey Comcast, why is my Internet speed {self.down}mpbs down/{self.up}mbps up when I pay for {PROMISED_DOWN}mbps down/{PROMISED_UP}mbps up?")

        # submit tweet
        tweet = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]/div/span/span')
        tweet.click()

        self.driver.quit()