#!/bin/python3
import sys
import time

luggage      = "shiny gold"
ancestors    = dict()
successor    = dict()
memoization  = set()
allbags      = list()

def isInt(string):
    try:
        int(string)
        return True
    except:
        return False

def logAncestor(parent, child, amount):
    if child in ancestors:
        ancestors[child].append((parent, amount))
    else:
        ancestors[child] = [(parent, amount)]

def logSuccessor(parent, child, amount):
    if parent in successor:
        successor[parent].append((child, amount))
    else:
        successor[parent] = [(child, amount)]

def __mapBags(data):
    for line in data:
        toks     = line.split()
        parent   = " ".join(toks[:2])
        contains = toks[4:]
        if len(contains) < 4:
            # contains no bag
            successor[parent] = list()
        elif len(contains) == 4:
            # contains one bag
            child  = " ".join(contains[1:3])
            amount = int(contains[0])
            logAncestor(parent, child, amount)
            logSuccessor(parent, child, amount)
        else:
            # contains several
            for i in range(len(contains)):
                if isInt(contains[i]):
                    amount = int(contains[i])
                    child  = " ".join(contains[i+1:i+3])
                    logAncestor(parent, child, amount)
                    logSuccessor(parent, child, amount)
    return

def __countPaths(bag, desc=False):
    if not desc:
        memoization.add(bag)
        if bag in ancestors:
            for parent, cnt in ancestors[bag]:
                __countPaths(parent)
    else:
        count = 0
        for child, cnt in successor[bag]:
            count += cnt + cnt * __countPaths(child, desc=True)
        return count

def parse(filename):
    with open(filename, "r") as fd:
        data = fd.read().splitlines()
    return data

def partOne(data):
    for parent,cnt in ancestors[luggage]:
        __countPaths(parent)
    return len(memoization)

def partTwo(data):
    count = 0
    for child,cnt in successor[luggage]:
        count += cnt + cnt * __countPaths(child, desc=True)
    return count

if __name__ == '__main__':
    # parse data
    data = parse(sys.argv[1])

    # part 1
    start = time.perf_counter()
    
    # map ancestors for both parts
    __mapBags(data)
    solution1 = partOne(data)

    # part 2
    solution2 = partTwo(data)
    end = time.perf_counter()
    # results
    print("Part 1:\n{0}".format(solution1))
    print("Part 2:\n{0}".format(solution2))
    print("Time: {0} seconds".format(round(end-start,4)))
