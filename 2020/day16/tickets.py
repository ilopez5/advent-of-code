#!/bin/python3
import sys
import time
import re
from collections import defaultdict

def parse(filename):
    with open(filename, "r") as fd:
        data = list(filter(lambda x: x != '', fd.read().splitlines()))
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
    fields = defaultdict(lambda: set())
    pool   = set()
    guess  = dict()
    for l,line in enumerate(data):
        if 'ticket' in line:
            continue
        elif l>0 and data[l-1] == "your ticket:":
            # our ticket values
            ourticket = [int(x) for x in line.split(',')]
            
            for i in range(len(ourticket)):
                guess[i] = set(fields.keys())
        elif ':' in line and 'ticket' not in line:
            # rule
            toks   = line.split(':')
            fname  = toks[0]
            values = [int(x) for x in re.findall(r'[\d]+', line)]

            # update global pool of valid numbers
            pool.update(range(values[:2][0], values[:2][1]+1))
            pool.update(range(values[2:][0], values[2:][1]+1))

            # update specific field range of valid numbers
            fields[fname].update(range(values[:2][0], values[:2][1]+1))
            fields[fname].update(range(values[2:][0], values[2:][1]+1))
        else:
            # actual tickets
            # parse values into list
            ticket = [int(x) for x in line.split(',')]
            
            # check if number is valid globally
            valid = True
            for val in ticket:
                if val not in pool:
                    valid = False
                    break

            if valid:
                # valid ticket, time to learn/guess
                for i,val in enumerate(ticket):
                    for fname, frange in fields.items():
                        if val not in frange:
                            guess[i].remove(fname)

    # narrow down guesses to one per index
    alreadyPruned = set()
    while True:
        total = 0
        for idx, options in guess.items():
            toPrune = options.copy()
            if len(options) == 1:
                # this index has been narrowed down
                total += 1
                if not toPrune.issubset(alreadyPruned):
                    # new field to be pruned
                    for i in range(len(guess)):
                        if i != idx:
                            guess[i].difference_update(toPrune)
                    # log as pruned so we don't repeat
                    alreadyPruned.add(toPrune.pop())
        if total == len(guess):
            break

    result = 1
    for idx in range(len(ourticket)):
        if 'departure' in guess[idx].pop():
            result *= ourticket[idx]
    return result

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
