from time import sleep
from xml.dom import NotFoundErr
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from pages.login_page import LoginPage
from pages.checkout_page import CheckoutPage
from pages.cart_page import CartPage
import requests
import datetime
import pytz


my_tz = pytz.timezone("Asia/Tbilisi")
time_now = datetime.datetime.now(my_tz)

def check_url(url):
    request_response = requests.head(url)
    status_code = request_response.status_code
    if status_code == 200:
        print("{0}: Meal {1} is available for order.".format(time_now, url))
        return True
    else:
        print("{0}: Meal {1} is not available".format(time_now, url))
        return False


class FoodPass:
    driver        = None
    cart_page     = None
    checkout_page = None

    def __init__(self) -> None:
        self.new_window()
        cart_page     = CartPage(self.driver)
        checkout_page = CheckoutPage(self.driver)

    def new_window(self):
        service = Service()
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(service=service, options=options)

    def login(self, username, password):
        try:
            login_page = LoginPage(self.driver)
            return login_page.login(username = username, password = password)
        except NoSuchElementException:
            return False

    def is_order_free(self):
        try:

            amount = self.checkout_page.get_order_price()
            if "0.00" in amount:
                return True
            else:
                print(
                    "{0}: The order cost is {1}. Check sum of the order, it should be <= 15 lari to apply coupon.".format(
                        time_now, amount))
                return False
        except NoSuchElementException:
            return False

    def clear_cart(self):
        try:
            self.driver.get('https://foodpassonline.com/%D0%BA%D0%BE%D1%80%D0%B7%D0%B8%D0%BD%D0%B0/')
            sleep(5)
            hrefs = self.driver.find_elements(By.CLASS_NAME, "remove")
            try:
                for u in hrefs:
                    url = self.driver.find_elements(By.CLASS_NAME, "remove")[0].get_attribute('href')
                    self.driver.get(url)
                    sleep(1)
                    print("{0} An item was removed from the cart.".format(time_now))
            except StaleElementReferenceException:
                return False
        except NoSuchElementException:
            return False
        return True

    def add_item_in_cart(self, url):
        try:
            if check_url(url):
                self.cart_page.add_to_cart(url) # TODO: check status
                return True
        except NoSuchElementException:
            pass
        return False

    def order_meals(self, meals):
        for url in meals:
            self.add_item_in_cart(url)
            print("{0}: Meal {1} has been added to the cart.".format(time_now, url))
        return True

    def order_lunchboxes(self, lunchboxes):
        for url in lunchboxes:
            try:
                if check_url(url):
                    self.driver.get(url)
                    self.add_item_in_cart(url)
                    print("{0}: Lunchbox {1} has been added to the cart".format(time_now, url))
                    return True
            except NotFoundErr:
                pass
        return False

    def submit_order(self):
        if self.is_order_free():
            order_btn = self.driver.find_element(By.XPATH, '//*[@id="place_order"]')
            self.driver.execute_script("arguments[0].click();", order_btn)
            return True
        return False

    def form_order(self, meals, lunchboxes):
        self.driver.get('https://foodpassonline.com/login-2/orders/')
        current_date = datetime.datetime.now().strftime("%d %B %Y").lstrip('0')
        if current_date in self.driver.page_source:
            print("{0}: The user has already ordered today.".format(time_now))
            return False
        else:
            if self.order_lunchboxes(lunchboxes):
                return True
            elif self.order_meals(meals):
                return True
            else:
                return False
