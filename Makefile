install:
	python3 -m venv venv
	pip3 install -r requirements.txt --break-system-packages
	sudo apt-get install chromium

make orders:
	. venv/bin/activate
	python3 makeOrders.py

make tests:
	. venv/bin/activate
	python3 test.py