#!/usr/bin/python3
"""
search with get
"""
import sys
import requests


if __name__ == "__main__":
    payload = {'q': len(sys.argv) >= 3 ? sys.argv[2]: ""}
    resp = requests.post(sys.argv[1], data=payload)
    try:
        data = resp.json()
        if data:
            for key, value in (dict(data)).items():
                print("[{}] {}".format(key, value))
        else:
            print("No result")
    except BaseException:
        print("Not a valid JSON")
