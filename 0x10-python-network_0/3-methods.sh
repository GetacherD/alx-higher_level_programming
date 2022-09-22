#!/bin/bash
# Get content  from request
curl -s -I -L -X OPTIONS "$1" |grep -i allow:|awk '{print $2 $3}'
