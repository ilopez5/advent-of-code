#!/bin/python3
import sys
import time
from functools import wraps

memory = dict()

def parse(filename):
    with open(filename, "r") as fd:
        data = [int(x) for x in fd.readlines()]
    return data

def partOne(data):
    jolts = set(data)
    diffs = dict()
    currentJolt = 0
    for i,joltage in enumerate(jolts):
        difference = joltage - currentJolt
        if difference in diffs:
            diffs[difference].append(joltage)
        else:
            diffs[difference] = [joltage]
        currentJolt = joltage

    # add phone adapter
    diffs[(joltage+3) - currentJolt].append(joltage+3)
    return len(diffs[1]) * len(diffs[3])

def traverse(jolts, idx):
    # check if we have done this idx before
    if idx in memory:
        return memory[idx]

    # safety check
    if idx+1 == len(jolts):
        return 1

    routes = 0
    for i in range(1,4):
        if idx+i < len(jolts) and jolts[idx+i]-jolts[idx] <= 3:
            # follow this route before moving on to the next
            routes += traverse(jolts, idx+i)

    # store answer in case we redo this idx later
    memory[idx] = routes
    return routes


def partTwo(data):
    # sort and add plug + phone adapter
    jolts = [0] + sorted(data)
    jolts.append(jolts[-1]+3)
    return traverse(jolts, 0)
    
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
