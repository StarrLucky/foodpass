from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

from pages.locators import *

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.locator = LoginPageLocators

    def __wait_for_element(self, element):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(element)
        )

    def enter_username(self, username):
        self.__wait_for_element(self.locator.USERNAME)
        self.driver.find_element(*self.locator.USERNAME).send_keys(username)

    def enter_password(self, password):
        self.__wait_for_element(self.locator.PASSWORD)
        self.driver.find_element(*self.locator.PASSWORD).send_keys(password)

    def click_login(self):
        self.__wait_for_element(self.locator.LOGIN_BUTTON)
        self.driver.find_element(*self.locator.LOGIN_BUTTON).click()

    def is_logged_in(self):
        return "Hello" in self.driver.page_source or "successful" in self.driver.page_source

    def login(self, username, password):
        self.driver.get(self.locator.LOGIN_PAGE_URL)
        self.enter_username(username), self.enter_password(password)
        self.click_login()
        return  self.is_logged_in()

    def login_with_valid_user(self):
        self.login("foodguessr", "mtsvadiminda")
        return LoginPage(self.driver)
