#!/usr/bin/python3
"""
Fetch Header Data
"""
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as resp:
        data = dict(resp.headers)
        print(data.get('X-Request-Id'))
