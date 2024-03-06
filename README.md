# ZeroMQ-Lib61850

Pay attention to Dockerfile: the version with no delay works with
- FROM debian:stable-20211115-slim  and
- RUN git clone -b v1.5 https://github.com/mz-automation/libiec61850.git /tmp/libiec61850
- The cyclic error problem was indeed a library version problem. Only use v1.5 in dockerfile ! The 1.5 version adds a delay between each subscription treatment ( average 60*s each). v1.4 is  cyclic at a rate of 1000µs.


-'sudo apt-get install git'
- install docker: https://docs.docker.com/engine/install/ubuntu/
- install docker compose: 'https://docs.docker.com/compose/install/linux/#install-using-the-repository'
- 'git clone https://github.com/mz-automation/libiec61850.git'
   - ' cmake . \
        && make \
        && make install \
        && make examples '
- 'snap install code'
-  ' apt-get update && \
    apt-get install -y libzmq3-dev  gcc libczmq-dev \
        git \
        build-essential \   
        cmake \  
        iputils-ping \  
        python3.11 python3.11-dev \'

- 'git clone https://github.com/booksbyus/zguide'
- 'gcc -o wuserver wuserver.c -lczmq -lzmq'
- 
