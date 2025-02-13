from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

from pages.locators import *

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.locator = CheckoutPageLocators

    def __wait_for_element(self, element):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(element)
        )

    def __get_amount(self):
        self.__wait_for_element(self.locator.AMOUNT_TEXT)
        return self.driver.find_element(*self.locator.AMOUNT_TEXT).text()

    def get_order_price(self):
        self.driver.get(self.locator.CHECKOUT_PAGE_URL)
        return self.__get_amount()

