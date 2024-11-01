from time import sleep

import config
import order
import datetime
import time 

from datetime import datetime
import pytz


def allowed_order():
    my_tz = pytz.timezone("Asia/Tbilisi")
    time_now = datetime.now(my_tz)
    today = datetime.today().weekday()
    is_allowed = True
    if today > 5:
        is_allowed = False
        print("Current day of week {} is out  of order days (MON - FRI)".format(today))
    elif 22 > time_now.hour < 14:
        print("Current time {} is out  of order hours (14:00 - 22:00 GMT+4)".format(time_now))

if allowed_order():
    for u in config.userList:
        print("Ordering for {}".format(u.username))
        newOrder = order.order()
        newOrder.login(u.username, u.password)
        newOrder.clear_cart()
        if newOrder.form_order(u.meals, u.lunchboxes):
            if  newOrder.submit_order():
                print("Order for {} is successfull".format(u.username))
            else:
                print("Failed to make an order for {}".format(u.username))
        newOrder.driver.delete_all_cookies()
