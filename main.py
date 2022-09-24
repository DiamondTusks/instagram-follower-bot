from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time

CHROME_DRIVER_PATH = "/Users/me/Documents/development/chromedriver"
SERVICE = Service(CHROME_DRIVER_PATH)
SIMILAR_ACCOUNT = "python.learning"
USERNAME = ""
PASSWORD = ""

class InstaFollower:

    def __init__(self, service):
        self.driver = webdriver.Chrome(service=service)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")

        time.sleep(3)
        username_field = self.driver.find_element(By.NAME, 'username')
        username_field.send_keys(USERNAME)

        time.sleep(3)
        password_field = self.driver.find_element(By.NAME, 'password')
        password_field.send_keys(PASSWORD)
        password_field.send_keys(Keys.ENTER)

        time.sleep(3)
        save_info = self.driver.find_element(By.CLASS_NAME, 'o9w3sbdw')
        save_info.click()

        time.sleep(3)
        notification = self.driver.find_element(By.CLASS_NAME, '_a9--')
        notification.click()


    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/")

        time.sleep(3)
        followers = self.driver.find_element(By.XPATH, '//*[@id="mount_0_0_EN"]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div/div/button')
        followers.click()

        time.sleep(3)
        # follower_popup = self.driver.find_element(By.CLASS_NAME, '_anno')
        scrollable_popup = self.driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_popup)
            time.sleep(2)



    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, "li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()

insta_follower = InstaFollower(SERVICE)
insta_follower.login()
insta_follower.find_followers()
insta_follower.follow()
