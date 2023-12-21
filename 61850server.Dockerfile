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


RUN cd /tmp/libiec61850/examples/server_example_basic_io && cp server_example_basic_io /srv

# Create and set the working directory
WORKDIR /srv

ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib


