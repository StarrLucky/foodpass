install:
	python3 -m venv venv
	pip3 install -r requirements.txt --break-system-packages

orders:
	. venv/bin/activate
	python3 make_orders.py

tests:
	. venv/bin/activate
	python3 test.py
