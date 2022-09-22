#!/bin/bash
# post json data
curl -sX POST "$1" -H 'Content-Type: application/json' -d '{"name": "John Doe","age": 33}'
