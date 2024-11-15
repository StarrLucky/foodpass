install:
	python3 -m venv venv
	pip3 install -r requirements.txt --break-system-packages

make orders:
	. venv/bin/activate
	python3 make_orders.py

make tests:
	. venv/bin/activate
	python3 test.py