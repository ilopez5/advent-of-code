#!/bin/python3
import sys
import time
import queue

instructions = set()
suspects     = queue.Queue()

def parse(filename):
    with open(filename, "r") as fd:
        data = fd.readlines()
    return data

def parseInstruction(string):
    op, arg = string.split()
    return op, int(arg)

def serializeInstr(op, arg):
    return "{0} {1}".format(op, arg)

def runBoot(data, sus=True):
    accumulator = pc = 0
    while pc < len(data):
        # check if this instruction has been executed
        if pc in instructions:
            return accumulator, True
        instructions.add(pc)

        # parse intruction and execute
        op, arg = parseInstruction(data[pc])
        if   op == "nop":
            if sus: suspects.put(pc)
            pc += 1
        elif op == "acc":
            accumulator += arg
            pc += 1
        else:
            if sus: suspects.put(pc)
            pc += arg
    return accumulator, False

def partOne(data):
    acc, _ = runBoot(data)
    return acc

def partTwo(data):
    while not suspects.empty():
        instructions.clear() 
        mdata       = data.copy()
        mpc         = suspects.get()
        
        # patch suspicious instruction
        op, arg = parseInstruction(mdata[mpc])
        if op == "nop":
            mdata[mpc] = serializeInstr("jmp", arg)
        else:
            mdata[mpc] = serializeInstr("nop", arg)

        # test boot
        accumulator, error = runBoot(mdata, sus=False)
        if not error:
            return accumulator
 
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
