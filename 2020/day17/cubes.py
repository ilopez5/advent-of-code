#!/bin/python3
import sys
import time

allCubes    = set()
activeCubes = set()
pointMap    = dict()

class Point():
    def __init__(self, coords, dim=3, active=False):
        self.x = coords[0]
        self.y = coords[1]
        self.z = coords[2]
        self.w = 0 if dim == 3 else coords[3]
        self.dimensions = dim
        self.active = active
        self.neighbors = self.generateNeighbors()

    def generateNeighbors(self):
        n = set()
        for x in range(self.x-1, self.x+2):
            for y in range(self.y-1, self.y+2):
                for z in range(self.z-1, self.z+2):
                    if self.dimensions == 4:
                        # four dimensions
                        for w in range(self.w-1, self.w+2):
                            if (x,y,z,w) != self.coords():
                                n.add((x,y,z,w))
                    else:
                        # three dimensions
                        if (x,y,z) != self.coords():
                            n.add((x,y,z))
        return n

    def coords(self):
        if self.dimensions == 4:
            return (self.x, self.y, self.z, self.w)
        return (self.x, self.y, self.z)

    def isActive(self):
        return self.active

    def prettyPrint(self):
        print("{{coords={0}, active={1}}}".format(self.coords(), self.active))


def countActiveNeighbors(point, dim):
    count = 0
    for neighbor in point.neighbors:
        if neighbor not in allCubes:
            # first appearance, inactive but leg work required
            new = Point(neighbor, dim=dim)
            allCubes.add(neighbor)
            pointMap[new.coords()] = new
        elif neighbor in activeCubes:
            count += 1
    return count

def countAndCheck(active, cube, dim=3):
    point = pointMap[cube]
    count = countActiveNeighbors(point, dim)

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

def initialize(data, dim):
    global activeCubes, allCubes, pointMap
    activeCubes.clear()
    allCubes.clear()
    pointMap.clear()
    for y in range(len(data)): # y-axis
        for x in range(len(data[y])): # x-axis
            # create new point obj
            p = Point((x,y,0,0), dim=dim, active=(data[y][x] == '#'))

            # store in respective sets/dicts
            pointMap[p.coords()] = p
            allCubes.add(p.coords())
            if p.isActive():
                activeCubes.add(p.coords())

def boot(dims=3):
    global activeCubes
    # run boot sequence (6 cycles)
    for cycle in range(6):
        # copy state of points for simultaneous modifications
        tempActive = activeCubes.copy()

        # run through all existing cubes (at this instance)
        for cube in activeCubes:
            # perform check on ourself
            countAndCheck(tempActive, cube, dims)
            
            # perform check on all our neighbors
            for neighbor in pointMap[cube].neighbors:
                countAndCheck(tempActive, neighbor, dims)
        # store all results simulatenously
        activeCubes = tempActive.copy()


def partOne(data):
    # parse and initialize
    initialize(data, dim=3)
    boot()
    return len(activeCubes)
    
def partTwo(data):
    # parse and initialize
    initialize(data, dim=4)
    boot(dims=4)
    return len(activeCubes)


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
