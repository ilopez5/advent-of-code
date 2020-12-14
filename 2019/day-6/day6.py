# Part 1
def verify_orbits(file):
    with open(file, 'r') as fd:
        data = fd.read().splitlines()
    num_orbits = {'COM': 0}

    to_find = ['COM']
    while data:
        for planet in to_find:
            for idx, orbit in enumerate(data):
                if planet == orbit[:3]:
                    sat = orbit[4:]
                    num_orbits[sat] = 1 + num_orbits[planet]
                    del data[idx]
                    to_find.append(sat)
            to_find = to_find[1:]
    
    sum = 0
    for count in num_orbits.values():
        sum += count
    return sum

# Part 2
def min_path(file):
    with open(file, 'r') as fd:
        data = fd.read().splitlines()

    path1 = ['YOU']                                 # Start at YOU, build path to COM
    while path1[-1] != 'COM':
        path1.append(find_parent(path1[-1], data))
    
    path2 = ['SAN']                                 # Start at SAN, build path to COM
    while path2[-1] != 'COM':
        path2.append(find_parent(path2[-1], data))

    for pos in range(-1, -len(path1), -1):          # Find where paths diverge
        if path1[pos] != path2[pos]:
            intersection = abs(pos) - 1
            break
    return (len(path1[1:]) + len(path2[1:])) - (2 * intersection)

def find_parent(planet, data):
    for orbit in data:
        if orbit[4:] == planet:
            return orbit[:3]


if __name__ == "__main__":
    import time
    start = time.perf_counter()
    print("Total Orbits: ", verify_orbits('day6input.txt'))
    print("Minimum Path: ", min_path('day6input.txt'))
    end = time.perf_counter()
    print("Took", end-start, "seconds")