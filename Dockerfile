FROM python:latest

ADD config.py .. 
ADD foodpass.py ..
ADD make_orders.py ..
ADD user.py ..
ADD requirements.txt .. 
ADD crontab /etc/cron.d/foodpass-cron
ADD Makefile ..

RUN apt-get update && apt-get install python3 cron nano jq unzip -y
RUN pip3 install -r requirements.txt  --break-system-packages

# Install Chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | tee /etc/apt/sources.list.d/google-chrome.list
apt update -y
apt install -y gconf-service libasound2 libatk1.0-0 libcairo2 libcups2 libfontconfig1 libgdk-pixbuf2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libxss1 fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils
apt install -y google-chrome-stable \

# Install chromedriver
RUN CHROMEDRIVER_URL='https://storage.googleapis.com/chrome-for-testing-public/132.0.6833.0/linux64/chromedriver-linux64.zip' \
    && curl -sSLf --retry 3 --output /tmp/chromedriver-linux64.zip "$CHROMEDRIVER_URL" \
    && unzip -o /tmp/chromedriver-linux64.zip -d /tmp \
    && rm -rf /tmp/chromedriver-linux64.zip \
    && mv -f /tmp/chromedriver-linux64/chromedriver "/usr/local/bin/chromedriver" \
    && chmod +x "/usr/local/bin/chromedriver"

# set display port to avoid crash
ENV DISPLAY=:99

RUN chmod 0644 /etc/cron.d/foodpass-cron
RUN crontab /etc/cron.d/foodpass-cron
RUN touch foodpass.log

CMD cron && tail -f /foodpass.log