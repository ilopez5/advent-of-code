#!/bin/python3
import sys
import time
from sympy.ntheory.modular import crt

class Node():
    def __init__(self, id=None, idx=None, prev=None, next=None):
        self.id   = id
        self.idx  = idx
        self.next = next
        self.prev = prev

def parse(filename):
    with open(filename, "r") as fd:
        data = fd.read().splitlines()
    return data

def partOne(data):
    depart   = int(data[0])
    shuttles = [int(x) for x in filter(lambda x: x!='x', data[1].split(','))]
    options  = dict()
    
    for bus in shuttles:
        options[bus] = bus - (depart % bus)

    bestTime = 9999
    for bus,time in options.items():
        if time < bestTime:
            bestBus  = bus
            bestTime = time
    return bestBus * bestTime

def partTwo(data):
    # apparently, my clever solution was not so clever. advent of code
    # forums suggest a more intelligent, mathematical approach, by
    # using the chinese remainder theorem. by installing the sympy
    # library, we set up the bus ids and their remainders and run it
    # through the crt() function.
    buses      = data[1].split(',')
    divisors   = list()
    remainders = list()
    # set up
    for i in range(len(buses)):
        if buses[i] != 'x':
            divisors.append(int(buses[i]))
            remainders.append((int(buses[i])-i)%int(buses[i]))
    return crt(divisors, remainders)[0]


# sad this wasn't great for the input data. worked fine for examples
def inefficientPartTwo(data):
    shuttles = data[1].split(',')

    # assemble 'linked list' with bus ids
    order = {None: Node()}
    prev  = None
    step  = int(shuttles[0])
    for i,bus in enumerate(shuttles):
        if bus != 'x':
            bus = int(bus)
            order[bus] = Node(id=bus, idx=i, prev=order[prev])
            order[prev].next = order[bus]
            prev = bus
            if step < bus:
                step = bus

    # prune placeholder
    order[None].next.prev = None
    del order[None]

    time = step
    done = False
    while not done:
        done = True
        t   = time
        bus = order[step]
        # check left busses for correctness
        while bus.prev:
            # calculate previous bus expected time
            prevTime = t - (bus.idx - bus.prev.idx)

            # check if expected time matches actual time
            if t != (t % bus.prev.id) + prevTime:
                done = False
                break
            # move to the 'next' previous bus
            t   = prevTime
            bus = bus.prev

        # store earliest bus time in case this is the solution
        result = t

        if done:
            # check right busses for correctness
            t   = time
            bus = order[step]
            while bus.next:
                # calculate next bus expected time
                nextTime = t + (bus.next.idx - bus.idx)

                # check if expected time matches actual time
                if 0 != (nextTime % bus.next.id):
                    done = False
                    break
                bus = bus.next
                t   = nextTime
       
        # take big step
        time += step

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
