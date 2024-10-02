import config
import order
import datetime
import time 

now = datetime.datetime.now()


if 14 < now.hour < 22:
    for u in config.userList:
        print("Ordering for {}".format(u.username))
        newOrder = order.order()
        newOrder.login(u.username, u.password)
        newOrder.make_order(u.meals)

else:
    print("Current time {} is out  of order hours (14:00 - 22:00)".format(now)  )
