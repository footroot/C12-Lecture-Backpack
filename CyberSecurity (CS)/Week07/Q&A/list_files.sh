#!/bin/bash

output_file="file_data.txt"
directory="${1:-.}"

echo "Listing files in directory: $directory" > "$output_file"
echo "--------------------------------------" >> "$output_file"

for file in "$directory"/*; do
	if [ -f "$file" ]; then
		size=$(stat -c%s "$file")
		echo "$(basename "$file") - $size bytes" >> "$output_file"
	fi
done

echo "Files listed in $output_file"
