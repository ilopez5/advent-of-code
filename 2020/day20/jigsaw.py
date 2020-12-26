#!/bin/python3
import sys
import time
import re
from collections import defaultdict

# globals
puzzle    = dict()
ops       = dict(top='bottom',left='right',right='left',bottom='top')
allTiles  = set()
checked   = set()
corners   = set()

class Tile:
    def __init__(self, tid):
        self.id        = tid
        self.edges     = defaultdict(lambda: list())
        self.neighbors = dict(top=False,right=False,bottom=False,left=False)
        self.checked   = dict(top=False,right=False,bottom=False,left=False)
        self.perms     = set()
    
    def isFullyChecked(self):
        return all(self.checked.values())

    def setFullyChecked(self):
        for edge in ops:
            self.checked[edge] = True

    def isCorner(self):
        assert(self.isFullyChecked())

        if not self.neighbors['top']    and not self.neighbors['right']:
            return True
        if not self.neighbors['top']    and not self.neighbors['left']:
            return True
        if not self.neighbors['bottom'] and not self.neighbors['right']:
            return True
        if not self.neighbors['bottom'] and not self.neighbors['left']:
            return True
        return False

    def __str__(self):
        return "{{id={0}}}".format(self.id)


def parse(filename):
    with open(filename, "r") as fd:
        data = fd.read().splitlines()

    for line in data:
        if re.match(r'Tile [\d]+:', line):
            # new tile
            tid  = int(re.findall(r'[\d]+', line)[0])
            tile = Tile(tid=tid)
            allTiles.add(tid)
        elif line:
            # tile being parsed
            if not tile.edges['top']:
                # first line
                tile.edges['top'] = [c for c in line]
                tile.edges['left'].append(line[0])
                tile.edges['right'].append(line[-1])
            elif len(tile.edges['left']) == len(tile.edges['top'])-1:
                # last line
                tile.edges['bottom'] = [c for c in line]
                tile.edges['left'].append(line[0])
                tile.edges['right'].append(line[-1])
            else:
                # middle tiles
                tile.edges['left'].append(line[0])
                tile.edges['right'].append(line[-1])
        else:
            # finished parsing a tile
            tile.edges['top']    = ''.join(tile.edges['top'])
            tile.edges['right']  = ''.join(tile.edges['right'])
            tile.edges['bottom'] = ''.join(tile.edges['bottom'])
            tile.edges['left']   = ''.join(tile.edges['left'])
            
            # store permutations
            for edge in ops:
                tile.perms.add(tile.edges[edge])
                tile.perms.add(tile.edges[edge][::-1])

            puzzle[tile.id] = tile
    return data

def compare(main):
    global allTiles

    # compare with all other tiles
    for tid in allTiles:
        other = puzzle[tid]

        if other == main:
            continue

        # check all sides
        for edge in ops:
            # check if this edge matches 'other' in any way
            if main.edges[edge] in other.perms:
                # mark as checked
                main.neighbors[edge] = True

    # mark as checked
    main.setFullyChecked()
    checked.add(main.id)

    # check if it is a corner
    if main.isCorner():
        corners.add(main.id)
    return


def partOne(data):
    global allTiles, corners

    while len(checked) < len(allTiles):
        # obtain a tile to work on
        main = puzzle[allTiles.pop()]
       
        # compares with all other tiles
        compare(main)

        # copy over changes to allTiles
        allTiles.add(main.id)

        # short circuit
        if len(corners) == 4:
            break

    result = 1
    for tid in corners:
        result *= tid
    return result

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
