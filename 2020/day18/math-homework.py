#!/bin/python3
import sys
import time
import re
from stack import Stack

prec1 = {'*': 1, '+': 1}
prec2 = {'*': 1, '+': 2}

def parse(filename):
    with open(filename, "r") as fd:
        data = fd.read().splitlines()
    return data

def evaluate(tokens):
    operands = Stack()
    for tok in tokens:
        if tok in "0123456789":
            operands.push(int(tok))
        else:
            op2 = operands.pop()
            op1 = operands.pop()
            if tok == '*':
                result = op1 * op2
            else:
                result = op1 + op2
            operands.push(result)
    return operands.pop()

def infixToPostfix(expr, prec):
    """Returns the postfix form of the infix expression found in `expr`"""
    ops = Stack()
    postfix = []
    toks = expr.split()
    for t in toks:
        if t.isdigit():
            postfix.append(t)
        elif t == '(':
            ops.push('(')
        elif t == ')':
            op = ops.pop()
            while op != '(':
                postfix.append(op)
                op = ops.pop()
        else:
            while True:
                if ops.empty() or ops.peek() == '(':
                    ops.push(t)
                    break
                if prec[t] > prec[ops.peek()]:
                    ops.push(t)
                    break
                elif prec[t] == prec[ops.peek()]:
                    postfix.append(ops.pop())
                    ops.push(t)
                    break
                else:
                    postfix.append(ops.pop())
    while not ops.empty():
        postfix.append(ops.pop())
    return postfix

def partOne(data):
    result = 0
    for line in data:
        args = infixToPostfix(line, prec1)
        result += evaluate(args)
    return result

def partTwo(data):
    result = 0
    for line in data:
        args = infixToPostfix(line, prec2)
        result += evaluate(args)
    return result


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
