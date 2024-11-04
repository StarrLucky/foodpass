FROM python:latest

ADD config.py .. 
ADD foodpass.py ..
ADD make_orders.py ..
ADD user.py ..
ADD requirements.txt .. 
ADD crontab /etc/cron.d/foodpass-cron
ADD Makefile ..

RUN apt-get update && apt-get install python3 cron nano -y
RUN pip3 install -r requirements.txt  --break-system-packages

# install google chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable
RUN wget --no-verbose -O /tmp/chrome.deb https://mirror.cs.uchicago.edu/google-chrome/pool/main/g/google-chrome-stable/google-chrome-stable_114.0.5735.106-1_amd64.deb \
  && apt install -y  /tmp/chrome.deb  --allow-downgrades\
  && rm /tmp/chrome.deb 
# install chromedriver
RUN apt-get install -yqq unzip
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/
# set display port to avoid crash
ENV DISPLAY=:99

RUN chmod 0644 /etc/cron.d/foodpass-cron
RUN crontab /etc/cron.d/foodpass-cron
RUN touch foodpass.log

CMD cron && tail -f /foodpass.log