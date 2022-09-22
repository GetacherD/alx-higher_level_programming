#!/bin/bash
# post request
curl "$1" -sX POST -F "email=test@gmail.com&subject=I will always be here for PLD"
