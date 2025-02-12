from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    USERNAME     = (By.XPATH, '/html/body/div[1]/div/div/div/main/div/article/div/div/div[2]/div/div[1]/div/div/div[2]/div[2]/div/form/div[1]/div[1]/div/input')
    PASSWORD     = (By.XPATH, '/html/body/div[1]/div/div/div/main/div/article/div/div/div[2]/div/div[1]/div/div/div[2]/div[2]/div/form/div[1]/div[2]/div/input')
    LOGIN_BUTTON = (By.XPATH, '/html/body/div[1]/div/div/div/main/div/article/div/div/div[2]/div/div[1]/div/div/div[2]/div[2]/div/form/button')
