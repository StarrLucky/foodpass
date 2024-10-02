import config
import order
import datetime


now = datetime.datetime.now()


if 14 < now.hour < 22:
    for u in config.userList:
        order.login(u.username, u.password)
        order.make_order(u.meals)
else:
    print("Current time {} is out  of order hours (14:00 - 22:00)".format(now)  )
