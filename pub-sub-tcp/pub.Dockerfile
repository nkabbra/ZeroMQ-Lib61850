# Use an official debian runtime as a parent image
FROM debian:latest

# Create and set the working directory
WORKDIR /app

# Install ZeroMQ dependencies and tools
RUN apt-get update && \
    apt-get install -y libzmq3-dev  gcc libczmq-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


# Copy the C source code into the container
COPY . /app/

RUN gcc -o wuserver wuserver.c -lczmq -lzmq

# Run the ZeroMQ server
CMD ["./wuserver"]
