FROM debian:10
LABEL maintaner="Equinockx moisestapia741@gmail.com"

WORKDIR /home/

RUN apt-get update

RUN apt-get install --no-install-recommends -y git && \
    apt-get install --no-install-recommends -y python3.7 && \
    apt-get install -y python3-pip && \
    apt-get install --no-install-recommends -y php && \
    apt-get update && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/DarkSecDevelopers/HiddenEye

WORKDIR /home/HiddenEye/

RUN pip3 install -r requirements.txt