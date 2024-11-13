import config
import foodpass
import datetime
import pytz

my_tz = pytz.timezone("Asia/Tbilisi")
time_now = datetime.datetime.now(my_tz)


def allowed_order():
    today = datetime.datetime.today().weekday()
    is_allowed = True
    if today > 5:
        is_allowed = False
        print("{0}: Current day of week {1} is out  of order days (MON - FRI)".format(time_now, today))
    elif 22 > time_now.hour < 14:
        is_allowed = False
        print("{0}: Current time is out of order hours (14:00 - 22:00 GMT+4)".format(time_now))
    return is_allowed


if allowed_order():
    food_pass = foodpass.FoodPass()
    for u in config.userList:
        print("{0}: Ordering for {1}".format(time_now, u.username))
        if not food_pass.login(u.username, u.password):
            print("{0} Login for {1} failed.".format(time_now, u.username))
            break
        if not food_pass.clear_cart():
            print("{0} Cannot clear cart.".format(time_now))
            break
        if not food_pass.form_order(u.meals, u.lunchboxes):
            break
        if food_pass.submit_order():
            print("{0}: Order for {1} is successfull".format(time_now, u.username))
        else:
            print("{0}: Failed to make an order for {1}".format(time_now, u.username))

    food_pass.driver.delete_all_cookies()
