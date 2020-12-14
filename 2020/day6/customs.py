#!/bin/python3
import sys
import time

groups = set()

def parse(filename):
    with open(filename, "r") as fd:
        data = fd.read().splitlines()
    return data

def partOne(data):
    ySum  = 0
    group = set()
    for line in data:
        if not line:
            # group complete
            ySum += len(group)
            group = set()
        else:
            for question in line:
                group.add(question)
    return ySum


def partTwo(data):
    gSum  = 0
    group = list()
    for line in data:
        if not line:
            # group complete
            agreedVotes = group[0]
            for person in group[1:]:
                agreedVotes = agreedVotes.intersection(person)
            gSum += len(agreedVotes)
            group.clear()
        else:
            groupTally = set()
            for yesVote in line:
                groupTally.add(yesVote)
            group.append(groupTally)
    return gSum

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
