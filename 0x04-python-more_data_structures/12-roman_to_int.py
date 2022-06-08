#!/usr/bin/python3
def roman_to_int(roman_string):

    if roman_string is None or (not isinstance(roman_string, str)):
        return 0
    digits = ["I", "V", "X", "L", "C", "D", "M"]
    val = [1, 5, 10, 50, 100, 500, 1000]
    sym = list(roman_string)
    tot = 0
    if sym.index("V") > sym.index("X"):
        return 0
    if sym.index("V") > sym.index("M"):
        return 0
    if sym.index("V") > sym.index("L"):
        return 0
    if sym.index("V") > sym.index("C"):
        return 0
    if sym.index("V") > sym.index("D"):
        return 0
    for c in sym:
        if c not in digits:
            return 0
        tot = tot + val[digits.index(c)]
    if "M" in sym and "C" in sym and sym.index("M") > sym.index("C"):
        tot = tot - 200
    if "X" in sym and "L" in sym and sym.index("L") > sym.index("X"):
        tot = tot - 20
    if "V" in sym and "I" in sym and sym.index("V") > sym.index("I"):
        tot = tot - 2
    if "X" in sym and "I" in sym and sym.index("X") > sym.index("I"):
        tot = tot - 2
    if "X" in sym and "C" in sym and sym.index("C") > sym.index("X"):
        tot = tot - 20
    if "C" in sym and "D" in sym and sym.index("D") > sym.index("C"):
        tot = tot - 200
    return tot
