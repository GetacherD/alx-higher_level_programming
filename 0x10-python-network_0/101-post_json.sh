#!/bin/bash
# post json data
curl "$1" -sX POST -H 'Content-Type: application/json' -d '{"name": "John Doe","age": 33}'
