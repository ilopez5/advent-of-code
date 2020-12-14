def intprogram():
    with open('day2input.txt','r') as fd:
        opcodes = fd.read().lower().split(',')

    opcodes = list(map(int, opcodes))
    opcodes[1], opcodes[2] = 12, 2
    for op in range(0,len(opcodes),4):
        if opcodes[op] == 1:
            idx_one, idx_two, idx_dest = opcodes[op+1], opcodes[op+2], opcodes[op+3]
            opcodes[idx_dest] = opcodes[idx_one] + opcodes[idx_two]
        elif opcodes[op] == 2:
            idx_one, idx_two, idx_dest = opcodes[op+1], opcodes[op+2], opcodes[op+3]
            opcodes[idx_dest] = opcodes[idx_one] * opcodes[idx_two]
        elif opcodes[op] == 99:
            break
    return opcodes[0]

def intprogram_two(one, two):
    with open('day2input.txt','r') as fd:
        opcodes = fd.read().lower().split(',')
        opcodes = list(map(int, opcodes))

    opcodes[1], opcodes[2] = one, two
    for op in range(0, len(opcodes), 4):
        if opcodes[op] == 1:
            idx_one, idx_two, idx_dest = opcodes[op+1], opcodes[op+2], opcodes[op+3]
            opcodes[idx_dest]= opcodes[idx_one] + opcodes[idx_two]
        elif opcodes[op] == 2:
            idx_one, idx_two, idx_dest = opcodes[op+1], opcodes[op+2], opcodes[op+3]
            opcodes[idx_dest] = opcodes[idx_one] * opcodes[idx_two]
        elif opcodes[op] == 99:
            break
    return opcodes[0]

if __name__ == "__main__":
    for i in range(100):
        for j in range(100):
            if intprogram_two(i,j) == 19690720:
                print(100*i+j)
                break