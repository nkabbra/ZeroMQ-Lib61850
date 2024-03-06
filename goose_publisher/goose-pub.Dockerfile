# Use an official debian runtime as a parent image
FROM debian:stable-20211115-slim


ENV DEBIAN_FRONTEND=noninteractive




# Install ZeroMQ,IEC61850 dependencies and tools
RUN apt-get update && \
    apt-get install -y   gcc \
        git \
        build-essential \   
        cmake \  
        iputils-ping \  
        python3.11 python3.11-dev \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*


RUN git clone -b v1.5 https://github.com/mz-automation/libiec61850.git /tmp/libiec61850

RUN cd /tmp/libiec61850 && cmake . \
        && make \
        && make install \
        && make examples 

# Copy the C source code into the container
COPY . /tmp/app
RUN cd /tmp/app && cmake . \
    && make 

# Create and set the working directory
WORKDIR /srv
RUN cd /tmp/app && cp goose_publisher_example /srv/pub-gse
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib


