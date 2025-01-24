#!/bin/bash

echo "Monitoring CPU usage for 5 seconds..."
cpu_usage=$(mpstat 1 5 | awk '/Average/ {print $3}')
echo "Average CPU usage: $cpu_usage%"
