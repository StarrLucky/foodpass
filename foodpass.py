from xml.dom import NotFoundErr
from selenium.webdriver.common.by import By
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
import requests

def check_url(url):
    request_response = requests.head(url)
    status_code = request_response.status_code
    if status_code == 200:
        print("Meal {0} is available for order.".format(url))
        return True
    else:
        print("Meal {0} is not available".format(url))
        return False

class FoodPass:
    driver = None
    def __init__(self) -> None:
        self.new_window()

    def new_window(self):
        service = Service()
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(service=service, options=options)

    def login(self, username, password):
        try:
            self.driver.get('https://foodpassonline.com/menuorder/')
            input_username = self.driver.find_element(By.XPATH, '//*[@id="username"]')
            input_username.send_keys(username)
            input_password = self.driver.find_element(By.XPATH, '//*[@id="password"]')
            input_password.send_keys(password)
            login_btn = self.driver.find_element(By.XPATH, '//*[@id="customer_login"]/div[1]/form/p[3]/button')
            login_btn.click()
            if len(self.driver.page_source) > 0:
                return True
            else:
                return False
        except NoSuchElementException: 
            return False

    def is_order_free(self):
            if "0.00" in self.driver.page_source:
                return True
            else:
                print("The order cost more than 0 lari. Check sum of the order, it should be <= 15 lari to apply coupon.")
                return False

    def clear_cart(self):
        try:
            self.driver.get('https://foodpassonline.com/%D0%BA%D0%BE%D1%80%D0%B7%D0%B8%D0%BD%D0%B0/')
            hrefs = self.driver.find_elements(By.CLASS_NAME , "remove")
            print(hrefs)
            try:
                for u in hrefs:
                    url = self.driver.find_elements(By.CLASS_NAME , "remove")[0].get_attribute('href')
                    self.driver.get(url)
                    print("An item was removed from the cart.")
            except StaleElementReferenceException:
                return False

        except NoSuchElementException:
            return False

    def add_item_in_cart(self, url):
        try:
            if check_url(url):
                self.driver.get(url)
                self.driver.find_element(By.XPATH, '//*[@id="wp--skip-link--target"]/div/div/div[1]/div[3]/div[2]/div[3]/form/button').click()
                return  True
        except NoSuchElementException:
            pass
        return False

    def order_meals(self, meals):
        for url in meals:
            self.add_item_in_cart(url)
            print("Meal {0} has been added to the cart.".format(url))
        return  True

    def order_lunchboxes(self, lunchboxes):
        for url in lunchboxes:
            try:
                if check_url(url):
                    self.driver.get(url)
                    self.add_item_in_cart(url)
                    print("Lunchbox {0} has been added to the cart".format(url))
                    return  True
            except NotFoundErr:
                pass
        return False

    def submit_order(self):
        self.driver.get("https://foodpassonline.com/checkout-2/")  # Go to Cart
        if self.is_order_free():
            order_btn = self.driver.find_element(By.XPATH, '//*[@id="place_order"]')
            self.driver.execute_script("arguments[0].click();", order_btn)
            return  True
        return False

    def form_order(self, meals, lunchboxes):
        self.driver.get('https://foodpassonline.com/login-2/orders/')
        current_date = datetime.datetime.now().strftime("%d %B %Y").lstrip('0')

        if current_date in self.driver.page_source:
            print("The user has already ordered today.")
            return False
        else:
            # add any of the lunchboxes to the cart. If nothing is present, then adding a list of meals to the cart.
            if self.order_lunchboxes(lunchboxes):
                return  True
            elif self.order_meals(meals):
                return  True
            else:
                return  False

