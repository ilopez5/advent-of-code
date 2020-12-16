#!/bin/python3
import sys
import time
from math import radians, cos, sin

def parse(filename):
    with open(filename, "r") as fd:
        data = fd.read().splitlines()
    return data

def partOne(data):
    direction = 1 # index in compass
    shipPos   = [0,0] # origin
    compass   = ['N', 'E', 'S', 'W'] # for direction
    cmdPos    = {'N':1, 'E':0, 'S':1, 'W':0} # shipPos offset
        
    for instr in data:
        cmd, amt = instr[0], int(instr[1:])

        # movements
        if cmd in ['N', 'E']:
            # move north or east
            shipPos[cmdPos[cmd]] += amt
        elif cmd in ['S', 'W']:
            # move south or west
            shipPos[cmdPos[cmd]] -= amt
        elif cmd == 'F':
            # forward
            currDirection = compass[direction]
            dirIdx = cmdPos[currDirection]
            if currDirection in ['N', 'E']:
                shipPos[dirIdx] += amt
            else:
                shipPos[dirIdx] -= amt
        # turns
        elif cmd == 'L':
            # turn left
            turn = amt
            while turn > 0:
                direction += 1
                turn -= 90
            direction %= 4
        elif cmd == 'R':
            # turn right
            turn = amt
            while turn > 0:
                direction += 1
                turn -= 90
            direction %= 4
        else:
            raise Exception
    return abs(shipPos[0]) + abs(shipPos[1])

def partTwo(data):
    direction = 1 # index in compass
    waypoint  = [10,1]
    shipPos   = [0,0] # origin
    compass   = ['N', 'E', 'S', 'W'] # for direction
    cidx      = {'N':1, 'E':0, 'S':1, 'W':0} # shipPos offset
    
    # run every instruction
    for instr in data:
        # parse command and amount
        cmd, amt  = instr[0], int(instr[1:])
        
        # movements: N/E/S/W move waypoint, F moves ship
        if   cmd in ['N', 'E']:
            # move waypoint north or east
            waypoint[cidx[cmd]] += amt
        elif cmd in ['S', 'W']:
            # move waypoint south or west
            waypoint[cidx[cmd]] -= amt
        elif cmd == 'F':
            # move ship forward
            shipPos[0] += amt * waypoint[0]
            shipPos[1] += amt * waypoint[1]
        # turns
        elif cmd == 'L':
            # rotate waypoint left
            #  waypoint = rotate(waypoint, shipPos, amt)
            while amt > 0:
                tX = -1 * waypoint[1]
                tY = waypoint[0]
                waypoint = [tX, tY]
                amt -= 90

        elif cmd == 'R':
            # rotate waypoint right
            while amt > 0:
                tX = waypoint[1]
                tY = -1 * waypoint[0]
                waypoint = [tX, tY]
                amt -= 90
        else:
            raise Exception
    return abs(shipPos[0]) + abs(shipPos[1])



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
