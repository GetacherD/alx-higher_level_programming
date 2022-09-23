#!/usr/bin/python3
"""
search with get
"""
import sys
import requests


if __name__ == "__main__":
    payload = {'q': len(sys.argv) >= 3 ? sys.argv[2]: ""}
    resp = requests.post(sys.argv[1], data=payload)
    data = resp.json()
    if resp.headers.get("Content-Type") != 'application/json':
        print("Not a valid JSON")
    elif dict(data) == {}:
        print("No result")
    else:
        print("[{}] {}".format(dict(data)["id"], (dict(data))["name"]))
