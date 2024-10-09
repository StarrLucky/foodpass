from selenium.webdriver.common.by import By
import datetime
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
class order:
    driver = None
    def __init__(self) -> None:
        opts = Options()
        opts.add_argument("--headless")
        self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()),options=opts)
        
    def login(self, username, password):
        self.driver.get('https://foodpassonline.com/menuorder/')
        input_username = self.driver.find_element(By.XPATH, '//*[@id="username"]')
        input_username.send_keys(username)
        input_password = self.driver.find_element(By.XPATH, '//*[@id="password"]')
        input_password.send_keys(password)
        self.driver.find_element(By.XPATH, '//*[@id="customer_login"]/div[1]/form/p[3]/button').click()

    def add_item_in_cart(self, url):
        self.driver.get(url)
        self.driver.find_element(By.XPATH, '//*[@id="wp--skip-link--target"]/div/div/div[1]/div[3]/div[2]/div[3]/form/button').click()

    def make_order(self, meals):
        self.driver.get('https://foodpassonline.m/login-2/orders/')
        current_date = datetime.datetime.now().strftime("%d %B %Y").lstrip('0')

        if current_date not in self.driver.page_source:
            for url in meals:
                self.add_item_in_cart(url)
            self.driver.find_element(By.XPATH, '//*[@id="place_order"]').click() 
        else:
            print("Today, the user has already placed an order.")

        self.driver.quit()