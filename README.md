Thanks to @jelly549 the approach works on me too (Raspberry Pi 4 Model B Rev 1.2).
I'd like to provide some more detailed steps for future users to save time (it took me an hour to figure it out).
I take Firefox and its driver Gecko as an example. If you use others you need to make some minor changes and your browser and driver.
Find an appropriate release of driver for your Raspbery Pi.
i.e. https://github.com/mozilla/geckodriver/releases
an AARM64 version should be downloaded: https://github.com/mozilla/geckodriver/ ... h64.tar.gz
Unzip and movethe executable to PATH. I placed it in /usr/local/bin.
Install the browser. On debian: sudo apt install firefox-esr
Install selenium.
In python, use the following code to import selenium
Code: Select all

from selenium import webdriver
from selenium import webdriver

browser = webdriver.Firefox()
browser.get("<target url>")

should work. Creating a new browser might be very time consuming-on my Pi creating one request could be ~140 seconds