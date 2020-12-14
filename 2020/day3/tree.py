#!/bin/python3
import sys
import time

def parse(filename):
    with open(filename, "r") as fd:
        data = fd.read().splitlines()[:-1]
    return data

def partOne(data):
    treeCount = col = 0
    for row in data[1:-1]:
        col += 3
        if row[col % len(row)] == "#":
            treeCount += 1
    return treeCount

def partTwo(data):
    solution = 1
    slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
    N = len(data[0])
    # iterate for every slope
    for x,y in slopes:
        # init
        col = row = treeCount = 0
        # iterate rows
        while row+y < len(data):
            row += y
            col += x
            if data[row][col % N] == "#":
                treeCount += 1
        # multiply the count for this slope
        solution *= treeCount
   return solution

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
