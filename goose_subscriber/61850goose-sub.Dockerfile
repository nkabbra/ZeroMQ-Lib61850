FROM debian:stable-20211115-slim

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y \
              git \
              build-essential \
              cmake \
              python3.11 python3.11-dev \
         && rm -rf /var/lib/apt/lists/*
ENV DEBIAN_FRONTEND=

RUN git clone -b v1.5 https://github.com/mz-automation/libiec61850.git /tmp/libiec61850

RUN cd /tmp/libiec61850 && cmake . \
        && make \
        && make install

# Copy the C source code into the container
COPY . /tmp/app
RUN cd /tmp/app && cmake . \
    && make 

RUN cd /tmp/app && cp goose_subscriber_example /srv/goose_sub 

WORKDIR /srv

ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib
 