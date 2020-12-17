#!/bin/python3
import sys
import time
import re

def parse(filename):
    with open(filename, "r") as fd:
        data = fd.read().splitlines()
    return data

def partOne(data):
    mask = dict()
    mem  = dict()
    for line in data:
        # parse instruction
        cmd, value = line.split(" = ")

        if cmd == "mask":
            # populate the mask
            mask.clear()
            for bit in range(35, -1, -1):
                if value[bit] != 'X':
                    mask[bit] = value[bit]
        else:
            # determine memory index to store
            address = int(re.findall(r'\d+', cmd)[0])

            # convert number into binary string
            output = bin(int(value))[2:]
            output = '0'*(36-len(output)) + output
            
            # convert str into mutable list
            output = [char for char in output]

            # perform each mask modification
            for mod,val in mask.items():
                output[mod] = val

            # convert back to str
            output = ''.join(output)

            # store in memory location
            mem[address] = int(output, 2)
    return sum(mem.values())

def storePermutations(mem, floating, output, value):
    # run through each permutation
    for p in range(1<<(len(floating))):
        # create permutation
        bitstr = bin(p)[2:]
        bitstr = '0'*(len(floating)-len(bitstr)) + bitstr
        bitlst = [c for c in bitstr]

        # patch permutation into temp address
        for i,pos in enumerate(floating):
            output[pos] = bitlst[i]

        # convert address bit string to integer
        newidx = int(''.join(output), 2)
       
        # store value
        mem[newidx] = value
 
def partTwo(data):
    mask = dict()
    mem  = dict()

    # run program
    for line in data:
        # parse instruction
        cmd, value = line.split(" = ")

        if cmd == "mask":
            # populate the mask
            maskstr = value
            mask.clear()
            for b in range(35, -1, -1):
                mask[b] = value[b]
        else:
            # determine memory index to store
            address = int(re.findall(r'\d+', cmd)[0])

            # convert memory location into binary string
            address = bin(int(address))[2:]
            address = '0'*(36-len(address)) + address
            addrlst = [char for char in address]

            # perform each mask modification
            floating = list()
            for i in range(36):
                if   mask[i] == 'X':
                    # log indices for floating bits
                    floating.append(i)
                    addrlst[i] = 'X'
                elif mask[i] == '1':
                    # overwrite with '1'
                    addrlst[i] = '1'

            # store 'value' at every permutation
            storePermutations(mem, floating, addrlst, int(value))

    #  print(mem)
    return sum(mem.values())

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
