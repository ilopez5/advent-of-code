#!/bin/python3
import sys
import time
import re
from collections import defaultdict

def parse(filename):
    with open(filename, "r") as fd:
        data = fd.read().splitlines()
    return data

recorded        = dict()
recordedList    = defaultdict(lambda: list())
allIngredients  = set()
safeIngredients = set()
iCounts = defaultdict(lambda: 0)

def partOne(data):
    global allIngredients
    for food in data:
        # parse ingredients and allergens
        ingredients, allergies = food.split(' (contains ')
        ingredients   = ingredients.split()
        allergies     = allergies.split(', ')
        allergies[-1] = allergies[-1][:-1]

        # add ingredients to relevant sets
        options = set(ingredients)
        allIngredients = allIngredients.union(options)

        # log appearance
        for i in ingredients:
            iCounts[i] += 1

        for allergen in allergies:
            if allergen not in recorded:
                recorded[allergen] = options
            else:
                recorded[allergen] = recorded[allergen].intersection(options)
    # find dangerous foods
    dangerous = set()
    for v in recorded.values():
        dangerous = dangerous.union(v)
    safeIngredients = allIngredients.difference(dangerous)

    # determine final counts
    result = 0
    for i in safeIngredients:
        result += iCounts[i]
    return result

def partTwo(data):
    # narrow down guesses to one per index
    alreadyPruned = set()
    while True:
        total = 0
        for allergen, ingredients in recorded.items():
            toPrune = ingredients.copy()
            if len(ingredients) == 1:
                # this index has been narrowed down
                total += 1
                if not toPrune.issubset(alreadyPruned):
                    # new field to be pruned
                    for i in recorded:
                        if i != allergen:
                            recorded[i].difference_update(toPrune)
                    # log as pruned so we don't repeat
                    alreadyPruned.add(toPrune.pop())
        if total == len(recorded):
            break

    print(recorded)
    result = list()
    for k in sorted(recorded):
        result.append(recorded[k].pop())
    return ','.join(result) 

def main():
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
    return

if __name__ == '__main__':
    main()
