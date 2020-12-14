#!/bin/python3
import sys
import time

filledSeats = set(range(1024))
seats = set()

def parse(filename):
    with open(filename, "r") as fd:
        data = fd.read().splitlines()[:-1]
    return data

def _findGlobalSeat(record):
    row  = _findRowNum(record)
    seat = _findColNum(record)
    return row * 8 + seat

def _findRowNum(record):
    _min, _max = 0, 127
    for x in record[:-3]:
        if x == 'F':
            _max -= ((_max - _min) // 2) + 1
        else:
            _min += ((_max - _min) // 2) + 1
    return _min if x == 'F' else _max

def _findColNum(record):
    _min, _max = 0, 7
    for x in record[-3:]:
        if x == 'L':
            _max -= ((_max - _min) // 2) + 1
        else:
            _min += ((_max - _min) // 2) + 1
    return _min if x == 'R' else _max

def partOne(data):
    for line in data:
        globalSeat = _findGlobalSeat(line)
        filledSeats.remove(globalSeat)
        seats.add(globalSeat)
    return max(seats)

def partTwo(data):
    for x in filledSeats:
        if x-1 not in filledSeats and x+1 not in filledSeats:
            return x

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
