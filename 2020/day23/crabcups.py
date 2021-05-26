#!/bin/python3
import sys
import time

def parse(filename):
    with open(filename, "r") as fd:
        data = fd.read().splitlines()
    return data

def partOne(data):
    cups    = [int(c) for c in data[0]]
    current = 0

    for move in range(1, 11):
        print("-- move {0} --".format(move))
        print("cups ({0}): {1}".format(cups[current], cups))
        currCup = cups[current]
        temp = current
        crabCups = list()
        for _ in range(3):
            crabCups.append(cups[(temp + 1) % len(cups)])
            del cups[(temp + 1) % len(cups)]

        print("pick up:", crabCups)

        temp = currCup - 1
        destination = -1
        while destination == -1:
            if temp in crabCups:
                temp -= 1
            elif temp < 1:
                destination = max(cups)
                break
            else:
                destination = temp
                break

        print("destination: {0}\n".format(destination))

        destIdx = cups.index(destination) + 1

        for i in range(0,3):
            cups.insert(destIdx+i, crabCups[i])

        crabCups.clear()
        current = (current + 1) % len(cups)

    output = list()
    
    for cup in cups:
        if cup == 1

        

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
