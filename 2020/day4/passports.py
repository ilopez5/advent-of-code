#!/bin/python3
import sys
import time

rules = {}
def checkValid(f):
    rules[f.__name__] = f
    return f

@checkValid
def byr(x): return len(x)==4 and int(x) in range(1920, 2002+1)

@checkValid
def iyr(x): return len(x)==4 and int(x) in range(2010, 2020+1)

@checkValid
def eyr(x): return len(x)==4 and int(x) in range(2020, 2030+1)

@checkValid
def hgt(x):
    number, unit = x[:-2], x[-2:]
    if number and unit and unit == 'cm': return int(number) in range(150,198+1)
    if number and unit and unit == 'in': return int(number) in range(59,76+1)
    else: return False

@checkValid
def hcl(x): return len(x)==7 and x[0]=='#' and x[1:].isalnum()

@checkValid
def pid(x): return len(x)==9

@checkValid
def ecl(x): return x in {'amb','blu','brn','gry','grn','hzl','oth'}

# for parsing the input data
def parse(filename):
    with open(filename, "r") as fd:
        data = fd.read().splitlines()
    return data

def partOne(data):
    fnames = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']
    valid = count = 0
    for line in data:
        if not line:
            # passport parsed
            if count == len(fnames): 
                valid += 1
            count = 0
        else:
            for field in fnames:
                if field in line: 
                    count += 1
    return valid

def partTwo(data):
    valid = count = 0
    for line in data:
        if not line:
            # passport parsed
            if count == len(rules):
                valid += 1
            count = 0
        else:
            # parse current line
            for field in line.split():
                fName, fValue = field.split(":")
                if fName != 'cid' and rules[fName](fValue): 
                    count += 1
    return valid

if __name__ == '__main__':
    # parse data
    data = parse(sys.argv[1])

    #  part 1
    start = time.perf_counter()
    solution1 = partOne(data)

    # part 2
    solution2 = partTwo(data)
    end = time.perf_counter()
    # results
    print("Part 1:\n{0}".format(solution1))
    print("Part 2:\n{0}".format(solution2))
    print("Time: {0} seconds".format(round(end-start,4)))
