#!/bin/python3
import sys
import time
import re

def parse(filename):
    with open(filename, "r") as fd:
        data = fd.read().splitlines()
    return data

def partOne(data):
    valid = set()
    count = 0
    for line in data:
        if ':' in line and 'ticket' not in line:
            # rule with valid ranges
            toks = [int(x) for x in re.findall(r'[\d]+', line)]
            valid.update(range(toks[:2][0],toks[:2][1]+1))
            valid.update(range(toks[2:][0],toks[2:][1]+1))
        elif line and 'ticket' not in line:
            # actual tickets to verify
            tokens = [int(x) for x in line.split(',')]
            for num in tokens:
                if num not in valid:
                    count += num
    return count 

def partTwo(data):
    pass

if __name__ == '__main__':
    # parse data
    data = parse(sys.argv[1])

    # part 1
    start = time.perf_counter()
    solution1 = partOne(data)

    # part 2
    solution2 = partTwo(data)
    end = time.perf_counter()
    # results
    print("Part 1:\n{0}".format(solution1))
    print("Part 2:\n{0}".format(solution2))
    print("Time: {0} ms".format(round((end-start) * 1000,4)))
