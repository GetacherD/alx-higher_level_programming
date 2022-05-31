#!/usr/bin/python3
def uppercase(a):
    for c in a:
        if (ord(c) >= 97 and ord(c) <= 122):
            c = chr(ord(c) - 32)
        print("{}".format(c), end="")
    print("")
