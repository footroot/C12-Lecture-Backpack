#!/bin/bash

if [ -z "$1" ]; then
	echo "Usage: $0 <file>"
	exit 1
fi

file="$1"

if [ ! -f "$file" ]; then
	echo "File not found"
	exit 1
fi

tr -s '[:space:][:punct:]' '\n' < "$file" | sort | uniq -c | sort -nr
