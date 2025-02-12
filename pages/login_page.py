from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

from pages.locators import *

class LoginPage(webdriver):
    def __init__(self, driver):
        self.driver = driver
        self.locator = LoginPageLocators

    def wait_for_element(self, element):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(element)
        )

    def enter_username(self, username):
        self.wait_for_element(self.locator.USERNAME)
        self.driver.find_element(*self.locator.USERNAME).send_keys(username)

    def enter_password(self, password):
        self.wait_for_element(self.locator.PASSWORD)
        self.driver.find_element(*self.locator.PASSWORD).send_keys(password)

    def click_login(self):
        self.wait_for_element(self.locator.LOGIN_BUTTON)
        self.driver.find_element(*self.locator.LOGIN_BUTTON).click()


    def login(self, username, password):
        self.driver.get('https://foodpassonline.com/login-2/')
        self.enter_username(username), self.enter_password(password)
        self.click_login()
        if "Hello" or "successful" in self.driver.page_source:
            return True
        else:
            return False

    def login_with_valid_user(self):
        self.login("foodguessr", "mtsvadiminda")
        return LoginPage(self.driver)
