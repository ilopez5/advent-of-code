def smart_cooling(file):
    with open(file, 'r') as fd:
        opcodes = fd.read().split(',')
        opcodes = list(map(int, opcodes))

    pc = 0
    while pc < len(opcodes):
        if opcodes[pc] == 99: # Immediately search for end condition
            break

        op, m1, m2 = smart_parse(str(opcodes[pc])) # Parse opcode with parameter modes
        p1, p2 = opcodes[pc+1], opcodes[pc+2]      # default is immediate mode
        if not m1:
            p1 = opcodes[p1]
        if not m2:
            p2 = opcodes[p2]
        
        if op == 1:
            p3 = opcodes[pc+3]
            opcodes[p3] = p1 + p2
            pc += 4
        elif op == 2:
            p3 = opcodes[pc+3]
            opcodes[p3] = p1 * p2
            pc += 4
        elif op == 3:
            num = input("Enter instruction: ")
            opcodes[p1] = int(num)
            pc += 2
        elif op == 4:
            print(p1)
            pc += 2
        elif op == 5:
            if p1 != 0:
                pc = p2
            else:
                pc += 3
        elif op == 6:
            if p1 == 0:
                pc = p2
            else:
                pc += 3
        elif op == 7:
            p3 = opcodes[pc+3]
            if p1 < p2:
                opcodes[p3] = 1
            else:
                opcodes[p3] = 0
            pc += 4
        elif op == 8:
            p3 = opcodes[pc+3]
            if p1 == p2:
                opcodes[p3] = 1
            else:
                opcodes[p3] = 0
            pc += 4
    return

def smart_parse(inst):
    op = int(inst[len(inst)-2:])            # 2 Rightmost bits for cmd
    inst = '000' + inst[:-2]                # Padding
    if op in [1,2,5,6,7,8]:
        first, second = False, False
        if inst[-1] == '1':
            first = True
        if inst[-2] == '1':
            second = True
        return op, first, second
    elif op == 3:
        return op, True, True
    elif op == 4:
        if inst[-1] == '1':
            return op, True, True
        return op, False, True

if __name__ == "__main__":
    smart_cooling('day5input.txt')