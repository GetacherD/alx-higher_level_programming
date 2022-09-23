#!/usr/bin/python3
"""
Fetch URL Data
"""
import urllib.request

with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as resp:
    print("Body response:")
    data = resp.read()
    print("    - type: {}".format(type(data)))
    print("    - content: {}".format(data))
    print("    - utf8 content: {}".format(data.decode("ascii")))
