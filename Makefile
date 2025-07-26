install:
	python3 -m venv venv
	pip3 install -r requirements.txt --break-system-packages

orders:
	python3 make_orders.py

tests:
	python3 test.py
