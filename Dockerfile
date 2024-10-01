FROM ubuntu:24.04
# FROM seleniarm/standalone-chromium:latest

ADD config.py ..
ADD order.py ..
ADD requirements.txt .. 

RUN apt update && apt install -y  \
    python3 \ 
    python3-pip \
    chromium

RUN pip3 install -r requirements.txt  --break-system-packages


RUN python3 order.py


