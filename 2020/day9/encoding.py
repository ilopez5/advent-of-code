#!/bin/python3
import sys
import time

window = set()

def parse(filename):
    with open(filename, "r") as fd:
        data = [int(x) for x in fd.readlines()]
    return data

def partOne(data, wsize):
    # add initial window
    for idx in range(wsize):
        window.add(data[idx])

    for idx,num in enumerate(data[wsize:], wsize):
        # check window values
        for i, wnum in enumerate(window):
            if num-wnum in window and num-wnum != wnum:
                break
        if i == wsize-1:
            return num
        else:
            window.remove(data[idx-wsize])
            window.add(num)

def partTwo(data, total):
    start = 0
    end   = 1
    while True:
        currentSum = sum(data[start:end])
        if currentSum == total:
            return min(data[start:end]) + max(data[start:end])
        elif currentSum < total:
            end += 1
        else:
            start += 1

if __name__ == '__main__':
    # parse data
    data = parse(sys.argv[1])

    # part 1
    start = time.perf_counter()
    solution1 = partOne(data, int(sys.argv[2]))

    # part 2
    solution2 = partTwo(data, solution1)
    end = time.perf_counter()
    # results
    print("Part 1:\n{0}".format(solution1))
    print("Part 2:\n{0}".format(solution2))
    print("Time: {0} seconds".format(round(end-start,4)))
