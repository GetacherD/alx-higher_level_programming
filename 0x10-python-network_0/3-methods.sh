#!/bin/bash
# Get content  from request
curl -s -i -L -X OPTIONS "$1" |grep -i allow:|awk '{print $2 $3}'
