FROM debian:10
LABEL maintaner="Equinockx moisestapia741@gmail.com"

WORKDIR /home/

RUN apt-get update

RUN apt-get install -y git
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN apt-get install -y php
RUN apt-get update

RUN git clone https://github.com/DarkSecDevelopers/HiddenEye

WORKDIR /home/HiddenEye/

RUN pip3 install -r requirements.txt