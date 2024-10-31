import config
import order
import datetime
import time 

import pytz

my_tz = pytz.timezone("Asia/Tbilisi") 
time_now = datetime.datetime.now(my_tz)

if 14 <= time_now.hour < 22:
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
else:
    print("Current time {} is out  of order hours (14:00 - 22:00 GMT+4)".format(time_now)  )
