# Use an official debian runtime as a parent image
FROM debian:latest


ENV DEBIAN_FRONTEND=noninteractive




# Install ZeroMQ,IEC61850 dependencies and tools
RUN apt-get update && \
    apt-get install -y libzmq3-dev  gcc libczmq-dev \
        git \
        build-essential \   
        cmake \  
        iputils-ping \    
        iproute2 \   
        net-tools \
        telnet \
        telnetd \
        iperf \
        wireshark \
        vim nano \    
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*


RUN git clone -b v1.4 https://github.com/mz-automation/libiec61850.git /tmp/libiec61850

RUN cd /tmp/libiec61850 && cmake . \
        && make \
        && make install \
        && make examples 

# Create and set the working directory
WORKDIR /srv


# Copy the C source code into the container
COPY . /tmp/app
RUN cd /tmp/app && cmake . \
    && make 

RUN cd /tmp/app && cp client_sub /srv/client_sub 
RUN cd /srv && mkdir logs

ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib


