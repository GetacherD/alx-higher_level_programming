#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys


def main():

    n = len(sys.argv)
    ops = [add, sub, mul, div]
    if (n != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operator = sys.argv[2]
    if operator not in ["+", "-", "*", "/"]:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    for i, op in enumerate(["+", "-", "*", "/"]):
        if op is operator:
            print("{} {} {} = {}".format(a, operator, b, ops[i](a, b)))


if __name__ == "__main__":
    main()
