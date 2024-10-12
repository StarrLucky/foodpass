from selenium.webdriver.common.by import By
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class order:
    driver = None
    def __init__(self) -> None:
        service = Service()
        options = webdriver.ChromeOptions()
        # options.add_argument("--headless")
        self.driver = webdriver.Chrome(service=service, options=options)
        
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
        self.driver.get('https://foodpassonline.com/login-2/orders/')
        current_date = datetime.datetime.now().strftime("%d %B %Y").lstrip('0')

        if current_date not in self.driver.page_source:
            for url in meals:
                self.add_item_in_cart(url)
            
            self.driver.get("https://foodpassonline.com/checkout-2/") # Go to Cart
        
            order_btn = self.driver.find_element(By.XPATH, '//*[@id="place_order"]')
            self.driver.execute_script("arguments[0].click();", order_btn)
            return True
        else: 
            print("Today, the user has already placed an order.")
            return False

        self.driver.quit()