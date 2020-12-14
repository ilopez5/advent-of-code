# Part 1
def main():
    max_output = 0
    for a in range(5):
        for b in range(5):
            for c in range(5):
                for d in range(5):
                    for e in range(5):
                        output, inputs, valid = 0, [a,b,c,d,e], True
                        for phase_setting in inputs:
                            if inputs.count(phase_setting) > 1:
                                valid = False
                                break
                            output = max_thruster([phase_setting, output])
                        if output > max_output and valid:
                            max_output = output
                            max_phase = [a,b,c,d,e]
    return max_output, max_phase

def max_thruster(inputs):
    with open('day7input.txt', 'r') as fd:              # fresh program each time
        opcodes = fd.read().split(',')
        opcodes = list(map(int, opcodes))
    track = pc = 0
    while pc < len(opcodes):
        if opcodes[pc] == 99:                      # Immediately search for end condition
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
            num = inputs[track]
            opcodes[p1] = int(num)
            track += 1
            pc += 2
        elif op == 4:
            inputs.append(opcodes[pc])
            if opcodes[pc+2] == 99:
                final_output = p1
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
    
    return final_output

# Part 2
def feedback_loop(file):
    max_output = 0
    with open(file, 'r') as fd:
        opcodes = fd.read().split(',')
        opcodes = list(map(int, opcodes))

    for f in range(5,10):
        for g in range(5,10):
            for h in range(5,10):
                for i in range(5,10):
                    for j in range(5,10):
                        if check_valid([f,g,h,i,j]):
                            phase, output = [f,g,h,i,j], 0
                            memory = {f:[0,opcodes], g:[0,opcodes], h:[0,opcodes], i:[0,opcodes], j:[0,opcodes]}

                            while True:
                                for setting in phase:
                                    output, memory = max_thruster_feed(setting, memory, [output])
                                if check_end(j, memory):
                                    break
                            if output > max_output:
                                max_output = output
                                max_phase = phase
    return max_output, max_phase

def max_thruster_feed(phase, memory, inputs):
    pc, opcodes = memory[phase][0], memory[phase][1]

    while pc < len(opcodes):
        if opcodes[pc] == 99:                       # Immediately search for end condition
            break
        op, m1, m2 = smart_parse(str(opcodes[pc]))  # Parse opcode with parameter modes
        p1, p2 = opcodes[pc+1], opcodes[pc+2]       # default is immediate mode
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
            num = inputs[0]
            if pc == 0:
                num = phase
            opcodes[p1] = num
            pc += 2
        elif op == 4:
            pc += 2
            memory[phase] = [pc, opcodes]         # update memory space
            return p1, memory
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

    return inputs[0]

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

def check_valid(lst):
    for x in lst:
        if lst.count(x) > 1:
            return False
    return True

def check_end(phase, memory):
    pc = memory[phase][0]
    opcodes = memory[phase][1]
    cmd = opcodes[pc]
    if cmd == 99:
        return True
    return False


if __name__ == "__main__":
    #max_output, max_phase = main()
    max_output, max_phase = feedback_loop('day7input.txt')
    print("Max Output: ", max_output)
    print("Phase Settings: ", max_phase)