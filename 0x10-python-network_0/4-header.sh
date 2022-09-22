#!/bin/bash
# Get content  from request
curl -s "$1" -X GET -L -H "X-School-User-Id=98"
