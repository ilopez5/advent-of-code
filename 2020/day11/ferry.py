#!/bin/python3
import sys
import time

def parse(filename):
    with open(filename, "r") as fd:
        data = fd.read().splitlines()
    return data

def adjacentSeatsEmpty(grid, row, col):
    seatsTaken = 0
    # up  | down | left | right | up/left | down/left | up/right | down/right
    adjSeats = [(-1,0), (1,0), (0,-1), (0,1), (-1,-1), (1,-1), (-1,1), (1,1)]
    for r,c in adjSeats:
        if row+r in range(len(grid)) and col+c in range(len(grid[0])):
            if grid[row+r][col+c] == '#':
                seatsTaken += 1
    return seatsTaken == 0, seatsTaken

def adjacentDirectionsEmpty(grid, row, col):
    seatsTaken = 0
    # up  | down | left | right | up/left | down/left | up/right | down/right
    adjSeats = [(-1,0), (1,0), (0,-1), (0,1), (-1,-1), (1,-1), (-1,1), (1,1)]
    for r,c in adjSeats:
        rstep, cstep = r, c
        # everywhere else done with while loop
        while row+r in range(len(grid)) and col+c in range(len(grid[0])):
            if grid[row+r][col+c] == 'L':
                seatsTaken += 0
                break
            elif grid[row+r][col+c] == '#':
                seatsTaken += 1
                break
            r += rstep
            c += cstep
    #  if row == 0 and col == 3:
        #  breakpoint()
    return seatsTaken == 0, seatsTaken

# debugging only
def printGrid(grid):
    for r in range(len(grid)):
        print("".join(grid[r]))

# debugging only
def slowCount(grid):
    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "#":
                count += 1
    return count

def partOne(data):
    # assemble a 2D grid
    tempgrid = list()
    grid     = list()

    # initialize 2D grid
    for row in data:
        r = [s for s in row]
        grid.append(r.copy())
        tempgrid.append(r.copy())
    
    seatCount = 0
    changes = 1 
    while changes > 0:
        changes = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                current = grid[r][c]
                if current != '.':
                    # only consider non-floor spots
                    allEmpty, count = adjacentSeatsEmpty(grid, r, c)
                    if allEmpty and current == 'L':
                        # occupy the empty seat
                        tempgrid[r][c] = '#'
                        changes   += 1
                        seatCount += 1
                    elif count>=4 and current == '#':
                        # empty the occupied seat
                        tempgrid[r][c] = 'L'
                        changes   += 1
                        seatCount -= 1
        # copy over all modifications at once
        for row in range(len(grid)):
            grid[row] = tempgrid[row].copy()
    return seatCount

def partTwo(data):
    # assemble a 2D grid
    tempgrid = list()
    grid     = list()

    # initialize 2D grid
    for row in data:
        r = [s for s in row]
        grid.append(r.copy())
        tempgrid.append(r.copy())
    
    seatCount = 0
    changes = 1 
    while changes > 0:
        #  printGrid(grid)
        #  print("\n")
        changes = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                current = grid[r][c]
                if current != '.':
                    # only consider non-floor spots
                    allEmpty, count = adjacentDirectionsEmpty(grid, r, c)
                    if allEmpty and current == 'L':
                        # occupy the empty seat
                        tempgrid[r][c] = '#'
                        changes   += 1
                        seatCount += 1
                    elif count>=5 and current == '#':
                        # empty the occupied seat
                        tempgrid[r][c] = 'L'
                        changes   += 1
                        seatCount -= 1
        # copy over all modifications at once
        for row in range(len(grid)):
            grid[row] = tempgrid[row].copy()
    return seatCount


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
