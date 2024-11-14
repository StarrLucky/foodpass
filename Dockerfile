FROM python:latest

ADD config.py .. 
ADD foodpass.py ..
ADD make_orders.py ..
ADD user.py ..
ADD requirements.txt .. 
ADD crontab /etc/cron.d/foodpass-cron
ADD Makefile ..
ADD bin bin

RUN apt-get update && apt-get install cron nano unzip -y
RUN pip3 install -r requirements.txt  --break-system-packages

# Install chrome 114 chrome that supports webdriver and selenuim withoud headache
RUN apt-get install -y ./bin/google-chrome-stable_114.0.5735.106-1_amd64.deb
# Install chromedriver
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip
RUN unzip /bin/chromedriver_linux64.zip chromedriver -d /usr/local/bin/

# set display port to avoid crash
ENV DISPLAY=:99

RUN chmod 0644 /etc/cron.d/foodpass-cron
RUN crontab /etc/cron.d/foodpass-cron
RUN touch foodpass.log

CMD cron && tail -f /foodpass.log