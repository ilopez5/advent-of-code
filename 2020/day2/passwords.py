#!/bin/python3
import sys
import time

# for parsing
def parse(file):
    with open(file, "r") as fd:
        data = fd.read().splitlines()[:-1]
    return data

def coundValidPasswords(data):
    validPasswords = 0
    for entry in data:
        # parse record
        record = entry.split()
        minChars, maxChars  = [int(x) for x in record[0].split("-")]
        char                = record[1][0]
        pcount              = record[2].count(char)

        # check validity
        if pcount <= maxChars and pcount >= minChars:
            validPasswords += 1
    return validPasswords

def countValidNew(data):
    validPasswords = 0
    for entry in data:
        # parse record
        record = entry.split()
        idx1, idx2 = [int(x) for x in record[0].split("-")]
        char       = record[1][0]
        pcount     = record[2]

        # check validity
        appearances = 0
        if char == pcount[idx1-1]:
            appearances += 1
        if char == pcount[idx2-1]:
            appearances += 1
        if appearances == 1:
            validPasswords += 1

    return validPasswords


if __name__ == '__main__':
    # parse input data
    data = parse(sys.argv[1])

    # part 1
    start = time.perf_counter()
    pcount1 = coundValidPasswords(data)

    # part 2
    pcount2 = countValidNew(data)
    end = time.perf_counter()

    # results
    print("Test 1:\n{0} valid passwords".format(pcount1))
    print("Test 2:\n{0} valid passwords".format(pcount2))
    print("Time: {0} seconds".format(round(end-start,4)))


