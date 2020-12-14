import colors as c

def intcodeComputer(file):
    print("Parsing",c.y(file)+"...")
    with open(file, 'r') as fd:
        opcodes = fd.read().split(',')
        opcodes = list(map(int, opcodes))
    print(c.g("Parsed."))

    print("Running Intcode computer...")
    rb = pc = 0
    while pc < len(opcodes):
        if opcodes[pc] == 99: break

        op, p1, p2, p3, opcodes = obtain_params(pc, rb, opcodes)
        
        if op == 1:   # adds params
            opcodes[p3] = p1 + p2
            pc += 4
        elif op == 2: # multiplies params
            opcodes[p3] = p1 * p2
            pc += 4
        elif op == 3: # prompts for input
            num = input("Enter instruction: ")
            opcodes[p1] = int(num)
            pc += 2
        elif op == 4: # outputs
            out = p1
            pc += 2
        elif op == 5: # jump if non-zero
            if p1 != 0:
                pc = p2
            else:
                pc += 3
        elif op == 6: # Jump if zero
            if p1 == 0:
                pc = p2
            else:
                pc += 3
        elif op == 7: # Less than
            if p1 < p2:
                opcodes[p3] = 1
            else:
                opcodes[p3] = 0
            pc += 4
        elif op == 8: # Equal to
            if p1 == p2:
                opcodes[p3] = 1
            else:
                opcodes[p3] = 0
            pc += 4
        elif op == 9: # Modify RB
            rb += p1
            pc += 2
    print(c.g("Complete."))
    return out

def obtain_params(pc, rb, opcodes):
    op, m1, m2, m3 = smart_parse(str(opcodes[pc]))  # Parse instruction
    p1, p2, p3 = opcodes[pc+1], opcodes[pc+2], pc+3 # Default to Immediate mode

    if m1 == 0:                                     # Param 1: Positional
        if p1 < len(opcodes):                       # Within bounds?
            if op != 3:                             # Yes, command 3?
                p1 = opcodes[p1]                    # No, return arg
        else:                                       # Out of bounds
            diff = p1 - len(opcodes) + 1            # Find difference
            opcodes.extend([0]*diff)                # Extend said difference
            if op != 3:
                p1 = 0
    elif m1 == 2:                                   # Param 2: Relative
        p1 = p1 + rb
        if p1 < len(opcodes):
            if op != 3:
                p1 = opcodes[p1]
        else:
            diff = p1 - len(opcodes) + 1
            opcodes.extend([0]*diff)
            if op != 3:
                p1 = 0
    
    if m2 == 0:                                     # Param 2: Positional
        if p2 < len(opcodes):
            p2 = opcodes[p2]
        else:
            diff = p2 - len(opcodes) + 1
            opcodes.extend([0]*diff)
            p2 = 0 
    elif m2 == 2:                                   # Param 2: Relative
        if (p2+rb) < len(opcodes):
            p2 = opcodes[p2+rb]
        else:
            diff = (p2+rb) - len(opcodes) + 1
            opcodes.extend([0]*diff)
            p2 = 0

    if op in [1,2,7,8]:                             # Param 3 Parse Necessary?
        p3 = opcodes[pc+3]
        if m3 == 0:
            if p3 >= len(opcodes):
                diff = p3 - len(opcodes) + 1
                opcodes.extend([0]*diff)
        elif m3 == 2:                               # Param 3: Relative
            p3 = p3 + rb
            if p3 >= len(opcodes):
                diff = p3 - len(opcodes) + 1
                opcodes.extend([0]*diff)
    return op, p1, p2, p3, opcodes

def smart_parse(inst):
    op = int(inst[len(inst)-2:])                    # 2 Rightmost bits for cmd
    inst = '000' + inst[:-2]                        # Padding to avoid idx errors
    return op, int(inst[-1]), int(inst[-2]), int(inst[-3])

if __name__ == "__main__":
    print(c.b("Part One:"))
    solution4 = intcodeComputer('day9input.txt')
    if solution4 != 'error':
        print(c.g("Output:"), solution4)
    print(c.b("\nPart Two:"))
    solution5 = intcodeComputer('day9input.txt')
    print(c.g("Output:"),solution5)
