#!/usr/bin/python3
"""
Send mail with POST Request
"""
import sys
import urllib.request
import urllib.error


if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as resp:
            pass
    except urllib.error.HTTPError as e:
        print(e.reason)
    else:
        print(resp.read().decode("utf-8"))
