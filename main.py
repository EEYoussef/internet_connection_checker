from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#PROMISED_DOWN =50
PROMISED_DOWN =150
PROMISED_up =20

CHROME_DRIVER_PATH = ""
# Enter Your CHROME DRIVER PATH
TWITTER_EMAIL=""
#Enter your email address for Twitter
TWITTER_PASSWORD=""
#Twitter password
TWITTER_USERNAME=""
#Twitter Username
INTERNET_SPEED = 100
#Internet Speed


class InternetSpeedTwitterBot:
    def __init__(self,driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.down =0
        self.up=0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        start_test =self.driver.find_element_by_class_name("start-text")
        start_test.click()
        time.sleep(60)
        self.up = self.driver.find_element_by_class_name("upload-speed")
        self.down = self.driver.find_element_by_class_name("download-speed")



    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/i/flow/login?input_flow_data=%7B%22requested_variant%22%3A%22eyJsYW5nIjoiZW4ifQ%3D%3D%22%7D")
        sign_in = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/a[2]/div/span/span')
        sign_in.click()
        # sign_in_by_google = self.driver.find_element_by_xpath('//*[@id="gsi_544379_503772"]')
        # sign_in_by_google.click()
        time.sleep(3)
        email = self.driver.find_element_by_css_selector("input")
        email.send_keys(TWITTER_EMAIL)
        email.send_keys(Keys.ENTER)
    #if extra security was  needed
        # time.sleep(3)
        # verify_email_username = self.driver.find_element_by_css_selector("input")
        # verify_email_username.send_keys(TWITTER_USERNAME)
        # verify_email_username.send_keys(Keys.ENTER)
        # # next_button = self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div')
        # # next_button.click()

        time.sleep(3)
        password = self.driver.find_element_by_css_selector("input")
        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)
        # next_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div[2]/div[3]/div/div/span/span')
        # next_button.click()

        time.sleep(5)
        tweet_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]')
        tweet_button.click()

        if (PROMISED_DOWN > INTERNET_SPEED):
            tweet_text = "Internet service is down"
            tweet = self.driver.find_element_by_css_selector('[data-block="true"]')
            tweet.click()
            tweet.send_keys(tweet_text)
            self.driver.find_element_by_css_selector('[data-testid="tweetButton"]').click()



speed_twitter_bot= InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
speed_twitter_bot.get_internet_speed()
speed_twitter_bot.tweet_at_provider()