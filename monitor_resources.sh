#!/bin/bash

CONTAINER_ID="$1"
OUTPUT_FILE="$2"

echo "Timestamp, ContainerID, CPU(%),Memory Usage (MiB),Network I/O" > "$OUTPUT_FILE"

while true; do
    STATS=$(docker stats --no-stream --format "{{.Container}}; {{.CPUPerc}}; {{.MemUsage}}; {{.NetIO}}" "$CONTAINER_ID")
    TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")
    echo "$TIMESTAMP,$STATS" >> "$OUTPUT_FILE"    
    sleep 1

done
