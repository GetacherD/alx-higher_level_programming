#!/usr/bin/bash
curl "$1" |grep Content-Length|awk '{print $2}'
