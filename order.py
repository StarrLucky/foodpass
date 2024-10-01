from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
import time
import datetime
import config


options = Options()

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def login(id, password):
    driver.get('https://foodpassonline.com/menuorder/')
    input_username = driver.find_element(By.XPATH, '//*[@id="username"]')
    input_username.send_keys(id)
    input_password = driver.find_element(By.XPATH, '//*[@id="password"]')
    input_password.send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="customer_login"]/div[1]/form/p[3]/button').click()


def addItemInCart(URL):
    driver.get(URL)
    driver.find_element(By.XPATH, '//*[@id="wp--skip-link--target"]/div/div/div[1]/div[3]/div[2]/div[3]/form/button').click()


def makeOrder(meals): 
    for url in meals:
        addItemInCart(url)

    # driver.get('https://foodpassonline.com/product/%d0%b3%d1%80%d0%b5%d1%87%d0%ba%d0%b0/')
    # driver.find_element(By.XPATH, '//*[@id="wp--skip-link--target"]/div/div/div[1]/div[3]/div[2]/div[3]/form/button').click()
    # driver.get('https://foodpassonline.com/product/%d0%ba%d1%83%d1%80%d0%b8%d0%bd%d1%8b%d0%b9-%d1%88%d0%bd%d0%b8%d1%86%d0%b5%d0%bb%d1%8c/')
    # driver.find_element(By.XPATH, '//*[@id="wp--skip-link--target"]/div/div/div[1]/div[3]/div[2]/div[3]/form/button').click()
    # driver.get('https://foodpassonline.com/checkout-2/')    
    driver.find_element(By.XPATH, '//*[@id="place_order"]').click()


login(config.LOGIN, config.PASSWORD)

driver.get('https://foodpassonline.com/login-2/orders/')
currentDate = datetime.datetime.now().strftime("%d %B %Y").lstrip('0')

if currentDate not in driver.page_source:
   makeOrder()
else:
    print("User have already ordered something today.")

driver.quit()

