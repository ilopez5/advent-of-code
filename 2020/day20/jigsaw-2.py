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
        self.neighbors = defaultdict(lambda: list())
        self.image     = list()

    def rotate(self):
        # store current values as temp
        _top    = self.edges['top']
        _right  = self.edges['right']
        _bottom = self.edges['bottom']
        _left   = self.edges['left']

        self.edges['top']    = _left[::-1]
        self.edges['right']  = _top
        self.edges['bottom'] = _right[::-1]
        self.edges['left']   = _bottom

        # rotate actual image
        new = [[] for _ in range(len(self.image))]
        for row in self.image[::-1]:
            for i in range(len(row)):
                new[i].append(row[i])
        for r in range(len(new)):
            new[r] = ''.join(new[r])
        self.image = new

    def flip(self, horizontal=True):
        if horizontal:
            _left  = self.edges['left']
            _right = self.edges['right']

            self.edges['top']    = self.edges['top'][::-1]
            self.edges['right']  = _left
            self.edges['left']   = _right
            self.edges['bottom'] = self.edges['bottom'][::-1]

            # flip actual image
            for r in range(len(self.image)):
                self.image[r] = self.image[r][::-1]
        else:
            # vertical flip
            _top    = self.edges['top']
            _bottom = self.edges['bottom']

            self.edges['top']    = _bottom
            self.edges['bottom'] = _top
            self.edges['left']   = self.edges['left'][::-1]
            self.edges['right']  = self.edges['right'][::-1]

            # flip actual image
            self.image = self.image[::-1]

    def isCorner(self):
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
        return "id={0}\n{1}".format(self.id, "\n".join(self.image))


def parse(filename):
    with open(filename, "r") as fd:
        for line in fd:
            line = line[:-1]
            if re.match(r'Tile [\d]+', line):
                # new tile
                tid  = int(re.findall(r'[\d]+', line)[0])
                tile = Tile(tid=tid)
                allTiles.add(tid)
            elif line:
                # need entire tile
                tile.image.append(line)

                # parse edges for neighbor matching
                if not tile.edges['top']:
                    # first line
                    tile.edges['top'] = line
                    tile.edges['left'].append(line[0])
                    tile.edges['right'].append(line[-1])
                elif len(tile.edges['left']) == len(tile.edges['top'])-1:
                    # last line
                    tile.edges['bottom'] = line
                    tile.edges['left'].append(line[0])
                    tile.edges['right'].append(line[-1])
                else:
                    # middle tiles
                    tile.edges['left'].append(line[0])
                    tile.edges['right'].append(line[-1])
            else:
                # finished parsing a tile
                tile.edges['right']  = ''.join(tile.edges['right'])
                tile.edges['left']   = ''.join(tile.edges['left'])
                puzzle[tile.id]      = tile
    return

def solve():
    for tid in puzzle:
        tile = puzzle[tid]

        for oid in allTiles:
            if oid == tid
                continue
            other = puzzle[oid]

            # comparison


    return 0

if __name__ == '__main__':
    # parse data
    parse(sys.argv[1])

    # run
    start     = time.perf_counter()
    solution  = solve()
    end       = time.perf_counter()
    # results
    print("Part 2:\n{0}".format(solution))
    print("Time: {0} ms".format(round((end-start) * 1000,4)))
