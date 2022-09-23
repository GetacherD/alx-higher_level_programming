#!/usr/bin/python3
"""
search with get
"""
import sys
import requests


if __name__ == "__main__":
    payload = {'q': len(sys.argv) >= 2 ? sys.argv[1]: ""}
    resp = requests.post('http://0.0.0.0:5000/search_user', data=payload)
    data = resp.json()
    if resp.headers.get("Content-Type") != 'application/json':
        print("Not a valid JSON")
    elif dict(data) == {}:
        print("No result")
    else:
        print("[{}] {}".format(dict(data)["id"], (dict(data))["name"]))
