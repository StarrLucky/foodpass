from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

from pages.locators import *

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.locator = CartPageLocators

    def __wait_for_element(self, element):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(element))

    def add_to_cart(self, url):
        self.driver.get(url)
        self.__wait_for_element(self.locator.ADD_TO_CART_BUTTON)
        self.driver.find_element(self.locator.ADD_TO_CART_BUTTON).click()