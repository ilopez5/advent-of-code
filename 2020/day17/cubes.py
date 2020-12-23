#!/bin/python3
import sys
import time

allCubes    = set()
activeCubes = set()
pointMap    = dict()

class Point():
    def __init__(self, x, y, z, active=False):
        self.x = x
        self.y = y
        self.z = z
        self.active = active
        self.neighbors = self.generateNeighbors()

    def generateNeighbors(self):
        n = set()
        for x in range(self.x-1, self.x+2):
            for y in range(self.y-1, self.y+2):
                for z in range(self.z-1, self.z+2):
                    if (x,y,z) != self.coords():
                        n.add((x,y,z))
        return n

    def coords(self):
        return (self.x, self.y, self.z)

    def isActive(self):
        return self.active

    def prettyPrint(self):
        print("{{coords={0}, active={1}}}".format(self.coords(), self.active))


def countActiveNeighbors(point):
    count = 0
    for neighbor in point.neighbors:
        if neighbor not in allCubes:
            # first appearance, inactive but leg work required
            new = Point(neighbor[0], neighbor[1], neighbor[2])
            allCubes.add(neighbor)
            pointMap[new.coords()] = new
        elif neighbor in activeCubes:
            count += 1
    return count

def countAndCheck(active, cube):
    point = pointMap[cube]
    count = countActiveNeighbors(point)

    # determine if point needs to change state
    if point.isActive() and count not in [2,3]:
        point.active = False
        active.discard(point.coords())
    elif not point.isActive() and count == 3:
        point.active = True
        active.add(point.coords())


def parse(filename):
    with open(filename, "r") as fd:
        data = fd.read().splitlines()
    return data

def partOne(data):
    global activeCubes
    # parse initial layout
    for y in range(len(data)): # y-axis
        for x in range(len(data[y])): # x-axis
            # create new point obj
            p = Point(x=x, y=y, z=0, active=(data[y][x] == '#'))

            # store in respective sets/dicts
            pointMap[p.coords()] = p
            allCubes.add(p.coords())
            if p.isActive():
                activeCubes.add(p.coords())

    # run boot sequence (6 cycles)
    for cycle in range(6):
        # copy state of points for simultaneous modifications
        tempActive = activeCubes.copy()
        instance   = allCubes.copy()

        # run through all existing cubes (at this instance)
        for cube in instance:
            # perform check on ourself
            countAndCheck(tempActive, cube)
            
            # perform check on all our neighbors
            for neighbor in pointMap[cube].neighbors:
                countAndCheck(tempActive, neighbor)
       # store all results simulatenously
        activeCubes = tempActive.copy()
    return len(activeCubes)
    
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
