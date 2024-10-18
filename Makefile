install:
	wget http://launchpadlibrarian.net/361669488/chromium-chromedriver_65.0.3325.181-0ubuntu0.14.04.1_armhf.deb
	sudo dpkg -i chromium-chromedriver_65.0.3325.181-0ubuntu0.14.04.1_armhf.deb
	sudo apt-get install -f
	sudo apt-get install xvfb
	sudo pip install PyVirtualDisplay
	sudo pip install xvfbwrapper 

	sudo pip install selenium

	# sudo apt-get install python3-pip firefox-esr xvfb wget
	# pip3 install -r requirements.txt  --break-system-packages
	# wget "https://github.com/mozilla/geckodriver/releases/download/v0.33.0/geckodriver-v0.33.0-linux-aarch64.tar.gz"
	# tar -xvzf geckodriver-v0.33.0-linux-aarch64.tar.gz
	# mv geckodriver /usr/local/bin

make orders:
	python3 makeOrders.py

make tests:
	. venv/bin/activate
	python3 test.py