#!/bin/python3
import sys
import time
from collections import defaultdict

def parse(filename):
    with open(filename, "r") as fd:
        data = fd.read().split(',')
    return data

def play(data, end):
    mem = defaultdict(lambda: list())
    # run through initial turns phase
    for turn,num in enumerate(data, 1):
        # [spoken list, first time?]
        mem[int(num)] = [turn]
        last = int(num)
   
    # increment turn once before beginning
    turn += 1
    while turn <= end:
        gap = turn - mem[last][-1]
        if gap == 1 and len(mem[last]) == 1:
            # first time being spoken
            mem[0].append(turn)
            last = 0
        else:
            diff = mem[last][-1] - mem[last][-2]
            mem[diff].append(turn)
            last = diff
        turn += 1
    return last


def partOne(data):
    return play(data, 2020)


def partTwo(data):
    return play(data, 30000000)

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
