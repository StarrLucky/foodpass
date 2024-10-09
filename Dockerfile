FROM python:latest

ADD config.py ..
ADD order.py ..
ADD makeOrders.py .. 
ADD user.py ..
ADD requirements.txt .. 

RUN apt-get update && apt-get install firefox-esr -y

RUN pip3 install -r requirements.txt  --break-system-packages

CMD  [python3, makeOrders.py]