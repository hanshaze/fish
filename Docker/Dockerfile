FROM python:3.7 as builder

WORKDIR /home/

RUN git clone https://github.com/DarkSecDevelopers/HiddenEye

FROM debian:10
LABEL maintaner="Equinockx moisestapia741@gmail.com"

WORKDIR /home/

RUN apt-get update

RUN apt-get install -y --no-install-recommends python3.7 && \
    apt-get install -y python3-pip && \
    apt-get install --no-install-recommends -y php && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /home/HiddenEye/

COPY --from=builder /home/HiddenEye/ .

RUN pip3 install -r requirements.txt