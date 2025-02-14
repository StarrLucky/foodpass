from selenium.webdriver.common.by import By

class LoginPageLocators(object):
    LOGIN_PAGE_URL = 'https://foodpassonline.com/login-2/'
    USERNAME       = (By.XPATH, '/html/body/div[1]/div/div/div/main/div/article/div/div/div[2]/div/div[1]/div/div/div[2]/div[2]/div/form/div[1]/div[1]/div/input')
    PASSWORD       = (By.XPATH, '/html/body/div[1]/div/div/div/main/div/article/div/div/div[2]/div/div[1]/div/div/div[2]/div[2]/div/form/div[1]/div[2]/div/input')
    LOGIN_BUTTON   = (By.XPATH, '/html/body/div[1]/div/div/div/main/div/article/div/div/div[2]/div/div[1]/div/div/div[2]/div[2]/div/form/button')

class CheckoutPageLocators(object):
    CHECKOUT_PAGE_URL = 'https://foodpassonline.com/checkout-2/'
    AMOUNT_TEXT       = (By.XPATH, '//*[@id="order_review"]/table/tfoot/tr[3]/td/strong/span')
    ORDER_BUTTON      = (By.XPATH, '//*[@id="place_order"]')

class CartPageLocators(object):
    CART_PAGE_URL      = 'https://foodpassonline.com/checkout-2/'
    ADD_TO_CART_BUTTON = (By.XPATH, '//*[@id="wp--skip-link--target"]/div/div/div[1]/div[3]/div[2]/div[3]/form/button')
    REMOVE_BUTTON      = (By.CLASS_NAME, "remove")

class OrdersPageLocators(object):
    ORDERS_PAGE_URL      = 'https://foodpassonline.com/login-2/orders/'
