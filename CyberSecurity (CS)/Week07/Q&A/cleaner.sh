#!/bin/bash

THRESHOLD=15

USAGE=$(df / | grep / | awk '{ print $5 }' | sed 's/%//')

if [ "$USAGE" -gt "$THRESHOLD" ]; then
	echo "Disk space is above $THRESHOLD. Clearing package cache..."
	sudo apt clean
	echo "Cache cleared on $(date)." >> ~/Documents/Bash/cache.txt
else
	echo "Disk space is below $THRESHOLD. No action needed."
fi

