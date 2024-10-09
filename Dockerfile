FROM python:latest

ADD config.py ..
ADD order.py ..
ADD makeOrders.py .. 
ADD user.py ..
ADD requirements.txt .. 

RUN apt-get update && apt-get install firefox-esr cron -y
RUN pip3 install -r requirements.txt  --break-system-packages


RUN touch /foodpass.log


RUN (crontab -l ; echo "00 15 * * * python3 makeOrders.py  >> foodpass.log 2>&1") | crontab


# CMD  [python3, makeOrders.py]
CMD ["tail", "-f", "foodpass.log"]

