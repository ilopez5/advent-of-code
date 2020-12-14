#!/bin/python3
import sys
import time

def parse(file):
    with open(file, "r") as fd:
        data = [int(x) for x in fd.read().split()]
    return data

def twoEntries(data):
    for num1 in data:
        num2 = 2020 - num1
        if num2 in data:
            print("{0}+{1}=2020\n{0}*{1}={2}".format(num1, num2, num1 * num2))
            break

def threeEntries(data):
    for num1 in data:
        for num2 in data:
            num3 = 2020 - num1 - num2
            if num3 in data:
                print("{0}*{1}*{2}={3}".format(num1,num2,num3,num1*num2*num3))
                return

if __name__ == '__main__':
    # parse
    data = parse(sys.argv[1])

    start = time.perf_counter()
    print("Part 1:")
    twoEntries(data)
    print("Part 2:")
    threeEntries(data)
    end = time.perf_counter()
    print("Time: {0:2} seconds".format(round(end-start, 4)))

