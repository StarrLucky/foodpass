install:
	python3 -m venv venv
	pip3 install -r requirements.txt 
	sudo apt-get install chromium

make orders:
	source venv/bin/activate
	python3 makeOrders.py
