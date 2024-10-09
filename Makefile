install:
	python3 -m venv venv
<<<<<<< HEAD
	source venv/bin/activate
	pip3 install -r requirements.txt 
	apt-get install firefox-esr -y
=======
	pip3 install -r requirements.txt 
	sudo apt-get install chromium

make orders:
	source venv/bin/activate
	python3 makeOrders.py
>>>>>>> 45053667e3d3abd3305e13f2f8f061df981cc32e
