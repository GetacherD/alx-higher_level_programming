#!/bin/bash
# Get content  from request
curl -s -I "$1" |grep Allow|cut -d" " -f2,3,4,5,6,7,8
