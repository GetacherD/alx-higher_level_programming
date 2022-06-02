#!/usr/bin/python3
import sys


def add():

    s = 0
    for i in sys.argv[1:]:
        s += int(i)
    print(s)


if __name__ == "__main__":
    add()
