import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv

load_dotenv()

TWITTER_EMAIL = os.getenv("TWITTER_EMAIL")
TWITTER_PASS = os.getenv("TWITTER_PASS")


class InternetSpeedTwitterBot:

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(chrome_options)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get(url="https://www.speedtest.net")
        cookie_button = self.driver.find_element(By.ID, value="onetrust-accept-btn-handler")
        cookie_button.click()
        go_button = (self.driver.find_element(By.CSS_SELECTOR, value=".start-button a"))
        time.sleep(3)
        go_button.click()
        time.sleep(45)
        self.down = self.driver.find_element(By.CLASS_NAME, value="download-speed").text
        self.up = self.driver.find_element(By.CLASS_NAME, value="upload-speed").text

    def tweet_at_provider(self, message: str):
        self.driver.get(url="https://x.com/")
        time.sleep(4)
        cross_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@data-testid="xMigrationBottomBar"]'))
        )
        cross_button.click()

        sign_in_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main'
                                                  '/div/div/div[1]/div[1]/div/div[3]/div[4]/a'))
        )
        sign_in_button.click()

        email_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "text"))
        )
        email_input.send_keys(f"{TWITTER_EMAIL}")

        next_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(., "Next")]'))
        )

        next_button.click()

        unusual_activity = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//input[@name="text" and @type="text"]'))
        )

        unusual_activity.send_keys("AbotforP")

        next_button2 = WebDriverWait(self.driver, 3).until(
            EC.element_to_be_clickable((By.XPATH, '//div[@dir="ltr" and .//span[contains(text(), "Next")]]'))
        )
        next_button2.click()

        password_box = (WebDriverWait(self.driver, 10).until
        (
            EC.element_to_be_clickable((By.XPATH, "//input[@name='password']"))
        ))

        password_box.send_keys(f"{TWITTER_PASS}")

        log_in = (WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='LoginForm_Login_Button']"))
        ))

        log_in.click()

        cross_button2 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="layers"]/div/div[1]/div/div/div/button'))
        )

        cross_button2.click()


        tweet_label = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-testid='tweetTextarea_0RichTextInputContainer'] "
                                                         "div[contenteditable='true']"))
        )
        time.sleep(3)
        tweet_label.send_keys(f"{message}")

        time.sleep(2)

        post_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]'
                                                  '/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/'
                                                  'div/div/button'))
        )

        post_button.click()


obj = InternetSpeedTwitterBot()

obj.get_internet_speed()

if float(obj.down) < 150.00 or float(obj.up) < 150.00:
    msg = f"Why is my download speed {obj.down} and upload speed {obj.up} when it should be 150 down and 150 up?"
    obj.tweet_at_provider(msg)
