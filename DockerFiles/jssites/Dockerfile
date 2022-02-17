FROM ubuntu@sha256:9d6a8699fb5c9c39cf08a0871bd6219f0400981c570894cd8cbea30d3424a31f
WORKDIR /usr/src/
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

RUN apt-get update -y
RUN apt-get install -y software-properties-common
RUN add-apt-repository ppa:saiarcot895/chromium-beta
RUN apt-get update -y
RUN apt-get install -y chromium-browser
# RUN apt-get install -y unzip
# RUN apt-get install wget -y
# RUN wget http://launchpadlibrarian.net/554114603/chromium-codecs-ffmpeg-extra_92.0.4515.159-0ubuntu0.18.04.1_arm64.deb
# RUN dpkg -i chromium-codecs-ffmpeg-extra_92.0.4515.159-0ubuntu0.18.04.1_arm64.deb
# RUN wget http://launchpadlibrarian.net/554114601/chromium-browser_92.0.4515.159-0ubuntu0.18.04.1_arm64.deb
# RUN dpkg -i chromium-browser_92.0.4515.159-0ubuntu0.18.04.1_arm64.deb
# RUN wget http://launchpadlibrarian.net/554114602/chromium-chromedriver_92.0.4515.159-0ubuntu0.18.04.1_arm64.deb 
# RUN dpkg -i chromium-chromedriver_92.0.4515.159-0ubuntu0.18.04.1_arm64.deb
# RUN apt --fix-broken install -y
RUN apt-get -y install python3-pip
RUN pip3 install pyyaml requests_html selenium datetime discord asyncio bs4 requests nest-asyncio
RUN python3 -m pip install --upgrade requests
RUN source ~/.bashrc

RUN mkdir -p /root/.local/share/pyppeteer/local-chromium/588429/chrome-linux/
RUN ln -s /usr/bin/chromium-browser /root/.local/share/pyppeteer/local-chromium/588429/chrome-linux/chrome
    



    
