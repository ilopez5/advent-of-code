import time as t

def part_one():
    start = t.perf_counter()
    with open('day3input.txt', 'r') as fd:
        moves = fd.readlines()

    wire1 = moves[0].split(',')
    wire1[-1] = wire1[-1][:-1]
    wire2 = moves[1].split(',')
    wire2[-1] = wire2[-1][:-1]

    euclid = []                                                         # store coordinates
    origin = current = (0,0)                                            # init
    for move in wire1:
        direction, distance = move[0], int(move[1:])
        if direction == 'U':
            for _ in range(distance):
                current = (current[0], current[1]+1)                    # take a step up
                if current not in euclid:
                    euclid.append(current)
        elif direction == 'R':
            for _ in range(distance):
                current = (current[0]+1, current[1])                    # take a step right
                if current not in euclid:
                    euclid.append(current)
        elif direction == 'D':
            for _ in range(distance):
                current = (current[0], current[1]-1)                    # take a step down
                if current not in euclid:
                    euclid.append(current)
        else:
            for _ in range(distance):
                current = (current[0]-1, current[1])                    # take a step left
                if current not in euclid:
                    euclid.append(current)
    
    current = origin                                                    # reset current to origin
    intersections = []
    for move in wire2:
        direction, distance = move[0], int(move[1:])
        if direction == 'U':
            for _ in range(distance):
                current = (current[0], current[1]+1)                    # take a step up
                if current in euclid:
                    intersections.append(current)
        elif direction == 'R':
            for _ in range(distance):
                current = (current[0]+1, current[1])                    # take a step right
                if current in euclid:
                    intersections.append(current)
        elif direction == 'D':
            for _ in range(distance):
                current = (current[0], current[1]-1)                    # take a step down
                if current in euclid:
                    intersections.append(current)
        else:
            for _ in range(distance):
                current = (current[0]-1, current[1])                    # take a step left
                if current in euclid:
                    intersections.append(current)

    closest = abs(intersections[0][0]) + abs(intersections[0][1])
    for x in intersections[1:]:
        d = abs(x[0]) + abs(x[1])
        if d < closest:
            closest = d
    
    end = t.perf_counter()
    print(closest)
    print("Took {0} seconds".format(end-start))
    return

def part_two():
    start = t.perf_counter()
    with open('day3input.txt', 'r') as fd:
        moves = fd.readlines()

    wire1 = moves[0].split(',')
    wire1[-1] = wire1[-1][:-1]
    wire2 = moves[1].split(',')
    wire2[-1] = wire2[-1][:-1]

    euclid = []                                                   # store coordinates
    origin = current = (0,0)                                      # init
    steps1, steps2 = {}, {}
    step = 0

    for move in wire1:                                            # about 240 seconds
        direction, distance = move[0], int(move[1:])
        if direction == 'U':
            for _ in range(distance):
                step += 1
                current = (current[0], current[1]+1)              # take a step up
                if current not in euclid:
                    euclid.append(current)
                if current not in steps1:
                    steps1[current] = step
        elif direction == 'R':
            for _ in range(distance):
                step += 1
                current = (current[0]+1, current[1])              # take a step right
                if current not in euclid:
                    euclid.append(current)
                if current not in steps1:
                    steps1[current] = step
        elif direction == 'D':
            for _ in range(distance):
                step += 1
                current = (current[0], current[1]-1)              # take a step down
                if current not in euclid:
                    euclid.append(current)
                if current not in steps1:
                    steps1[current] = step
        else:
            for _ in range(distance):
                step += 1
                current = (current[0]-1, current[1])              # take a step left
                if current not in euclid:
                    euclid.append(current)
                if current not in steps1:
                    steps1[current] = step
    
    current = origin                                              # reset current to origin
    intersections = []
    step = 0
    for move in wire2:
        direction, distance = move[0], int(move[1:])
        if direction == 'U':
            for _ in range(distance):
                step += 1
                current = (current[0], current[1]+1)              # take a step up
                if current in euclid:
                    if current not in steps2:
                        steps2[current] = steps1[current] + step
                    intersections.append(current)
        elif direction == 'R':
            for _ in range(distance):
                step += 1
                current = (current[0]+1, current[1])              # take a step right
                if current in euclid:
                    if current not in steps2:
                        steps2[current] = steps1[current] + step
                    intersections.append(current)
        elif direction == 'D':
            for _ in range(distance):
                step += 1
                current = (current[0], current[1]-1)              # take a step down
                if current in euclid:
                    if current not in steps2:
                        steps2[current] = steps1[current] + step
                    intersections.append(current)
        else:
            for _ in range(distance):
                step += 1
                current = (current[0]-1, current[1])              # take a step left
                if current in euclid:
                    if current not in steps2:
                        steps2[current] = steps1[current] + step
                    intersections.append(current)

    closest = steps2[intersections[0]]
    for x in intersections[1:]:
        if steps2[x] < closest:
            closest = steps2[x]
    
    end = t.perf_counter()
    print(closest)
    print("Took {0} seconds".format(end-start))
    return

if __name__ == "__main__":
    part_two()