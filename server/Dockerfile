# Dockerfile for SP REST API

FROM ubuntu:18.04

RUN apt-get update && \
    apt-get install -y build-essential \
    python3 \
    python3-dev \
    python3-pip

COPY . app
RUN pip3 install uwsgi && \
    pip3 install -r app/requirements.txt

EXPOSE 9887

CMD ["uwsgi", "--ini", "app/uswgi.ini"]