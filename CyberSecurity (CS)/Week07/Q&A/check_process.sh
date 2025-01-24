#!/bin/bash

if ! pgrep -x "Web Content" > /dev/null
then
	echo "$(date) - Process Web Content is not running!" >>  ~/Documents/QA/web_process.txt
else
	echo "$(date) - Process Web Content is running!" >> ~/Documents/QA/web_process.txt
fi

