# Dockerfile for SP REST API

FROM ubuntu:18.04

RUN apt-get update && \
    apt-get install -y build-essential \
    python3 \
    python3-dev \
    sqlite3 \
    python3-pip \
    python-setuptools 

COPY . app

RUN apt-get install -y software-properties-common

RUN pip3 install uwsgi && \
    pip3 install -r requirements.txt

EXPOSE 9887

CMD ["uwsgi", "--ini", "app/uswgi.ini"]