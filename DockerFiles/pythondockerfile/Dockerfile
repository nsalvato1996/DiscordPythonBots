FROM ubuntu:latest
WORKDIR /usr/src/
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

RUN apt-get update -y && \
    apt-get install -y software-properties-common && \
    add-apt-repository ppa:saiarcot895/chromium-beta && \
    apt-get update -y && \
    apt-get install -y chromium-browser && \
    apt-get -y install python3-pip && \
    pip3 install pyyaml requests_html selenium datetime discord asyncio bs4 requests && \
    python3 -m pip install --upgrade requests && \
    source ~/.bashrc
