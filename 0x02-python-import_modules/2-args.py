#!/usr/bin/python3
import sys


def main():

    n = len(sys.argv)
    if (n == 1):
        print("0 arguments.")
    elif n == 2:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(n - 1))
        for i, arg in enumerate(sys.argv[1:]):
            print("{}: {}".format(i + 1, arg))


if __name__ == "__main__":
    main()
