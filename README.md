# ZeroMQ-Lib61850

Pay attention to Dockerfile: the version with no delay works with
- FROM debian:stable-20211115-slim  and
- RUN git clone -b v1.5 https://github.com/mz-automation/libiec61850.git /tmp/libiec61850
- The cyclic error problem was indeed a library version problem. Only use v1.5 in dockerfile ! The 1.5 version adds a delay between each subscription treatment ( average 60*s each). v1.4 is  cyclic at a rate of 1000µs.



