import config
import order
import datetime
import time 

from datetime import datetime
import pytz

my_tz = pytz.timezone("Asia/Tbilisi") 
time_now = datetime.now(my_tz)

if 10 <= time_now.hour < 24:
    for u in config.userList:
        print("Ordering for {}".format(u.username))
        newOrder = order.order()
        newOrder.login(u.username, u.password)
        if newOrder.make_order(u.meals):
            print("Order for {} is successfull".format(u.username))
        else:
            print("Failed to make an order for {}".format(u.username))
else:
    print("Current time {} is out  of order hours (14:00 - 22:00 GMT+4)".format(time_now)  )