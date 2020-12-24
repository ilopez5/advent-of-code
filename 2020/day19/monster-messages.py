#!/bin/python3
import sys
import time
import re

memoization = dict()

depth = dict()

def parse(filename):
    with open(filename, "r") as fd:
        data = fd.read().splitlines()
    return data

def ruleReplace(data, ruleNum, part=1):
    # parse line
    rules = re.findall(r'([\d]+|\||[a-z])', data[ruleNum])
    main  = int(rules[0])

    # see if this has been done before
    if main in memoization:
        return memoization[main]


    rules = rules[1:]
    if re.match(r'[a-z]', rules[0]):
        # reached char endpoint (leaf)
        memoization[main] = rules[0]
        return rules[0]
    else:
        # assume input data won't go past 3 levels of recursion
        if part == 2 and ruleNum in [8,11]:
            if depth[ruleNum] > 3:
                return memoization[42]
            else:
                depth[ruleNum] += 1

        # more rules (non-leaf)
        for r, rule in enumerate(rules):
            if rules[r] != '|':
                rules[r] = ruleReplace(data, int(rule), part)
        # wrap this group
        if '|' in rules and main > 0:
            rules = ['('] + rules + [')']
        # log for later reuse
        memoization[main] = ''.join(rules)
        return memoization[main]
 
def partOne(data):
    # recursively create regular expression pattern
    pattern = re.compile(ruleReplace(data, 0))

    # run each monster message through regex
    count = 0
    for line in data[max(memoization.keys())+2:]:
        if pattern.fullmatch(line):
            count += 1
    return count

def partTwo(data):
    # apply part two patches
    data[8]  = "8: 42 | 42 8"
    data[11] = "11: 42 31 | 42 11 31"
    memoization.clear()
    depth[8] = 0
    depth[11] = 0
    pattern = re.compile(ruleReplace(data, 0, 2))
    
    # run each monster message through regex
    count = 0
    for line in data[max(memoization.keys())+2:]:
        if pattern.fullmatch(line):
            count += 1
    return count

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
