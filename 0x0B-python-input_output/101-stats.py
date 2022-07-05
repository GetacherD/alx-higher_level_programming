#!/usr/bin/python3
"""
stats
"""
import sys


total = 0
count = 0
stats = [200, 301, 400, 401, 403, 404, 405, 500]
stat_counts = [0] * 8

try:
    for line in sys.stdin:
        total += int(line.split(" ")[-1])
        count += 1
        for s in stats:
            if s == int(line.split(" ")[-2]):
                stat_counts[stats.index(s)] += 1
        if count == 10:
            print("File size: {}".format(total))
            count = 0
            for i in range(len(stats)):
                if stat_counts[i]:
                    print("{}: {}".format(stats[i], stat_counts[i]))
except KeyboardInterrupt:
    print("File size: {}".format(total))
    for i in range(len(stats)):
        if stat_counts[i]:
            print("{}: {}".format(stats[i], stat_counts[i]))
    raise
