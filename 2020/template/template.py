#!/bin/python3
import sys
import time

def parse(filename):
    with open(filename, "r") as fd:
        data = fd.read().split()
    return data

def partOne(data):
    pass

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
    print("Time: {0} seconds".format(round(end-start,4)))
