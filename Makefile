install:
	sudo apt-get install python3-pip firefox-esr xvfb wget
	pip3 install -r requirements.txt  --break-system-packages
	wget "https://github.com/mozilla/geckodriver/releases/download/v0.33.0/geckodriver-v0.33.0-linux-aarch64.tar.gz"
	tar -xvzf geckodriver-v0.33.0-linux-aarch64.tar.gz
	mv geckodriver /usr/local/bin

make orders:
	python3 makeOrders.py
