import colors as c
import math as m

# part one
def count_asteroids(file):
    print("\nParsing",c.y(file)+"...")
    puzzle = parse_input(file)
    print(c.g("Parsed."))

    print("Marking asteroids...")
    coords = mark_asteroids(puzzle)
    print(c.g("Asteroids marked."))

    print("Counting detectable planets...")
    count = {}
    best_count = 0
    for asteroid in coords:
        count[asteroid] = detect_neighbors(asteroid, coords)
        if count[asteroid] > best_count:
            best_count = count[asteroid]
            best_asteroid = asteroid
    print(c.g("Count complete."))
    return best_asteroid, best_count

def mark_asteroids(puzzle):
    output = []
    for y in range(len(puzzle)):
        for x in range(len(puzzle[0])):
            if puzzle[y][x] == '#':
                output.append((x,y))
    return output

def detect_neighbors(asteroid, coords):
    x1, y1 = asteroid
    count = 0
    done_up, done_down, done_left, done_right = False, False, False, False
    left, right = {}, {}

    for ast2 in coords:
        if asteroid == ast2:
            continue

        x2, y2 = ast2
        if y1 == y2:                            # Horizontal
            if x1 > x2 and not done_left:
                count += 1
                done_left = True
            elif x1 < x2 and not done_right:
                count += 1
                done_right = True
        elif x1 == x2:                          # Vertical
            if y1 > y2 and not done_up:
                count += 1
                done_up = True
            elif y1 < y2 and not done_down:
                count += 1
                done_down = True
        else:
            m = (y2-y1) / (x2-x1)
            if x2 > x1 and m not in right:
                right[m] = True
                count += 1
            elif x2 < x1 and m not in left:
                left[m] = True
                count += 1
    return count

def parse_input(file):
    with open(file, 'r') as fd:
        puzzle = fd.read().splitlines()
    return puzzle

# part two
def obliterate(asteroid, file):
	# read input file
	print("Parsing {0}...".format(c.y(file)), end="")
	puzzle = parse_input(file)
	print("Done.")

	print("Marking asteroids........", end="")
	coords = mark_asteroids(puzzle)
	print("Done.")

	print("Firing lasers............", end="")
	count = 0
	while count < 200:
		# record current 360 degrees of neighbors
		up, right, down, left = recordNeighbors(asteroid, coords)


	print("Done.")
	return (9,2)

def recordNeighbors(best_asteroid, coords):
	x1, y1 = best_asteroid
	up = right = down = left = {}

	for asteroid in coords:
		# ignore source asteroid
		if asteroid == best_asteroid:
			continue

		x2, y2 = asteroid
		dist = distance(best_asteroid, asteroid)

		if x1 == x2:
			# vertically aligned asteroids
			if y1 > y2:
				# asteroid is below us
				if down[0]:
					# already marked a neighbor below us, must check
					existing_dist = down[0][0]
					if dist < existing_dist:
						# our current asteroid is closer than the existing one
						down[0] = (dist, asteroid)
				else:
					# first asteroid below us encountered
					down[0] = (dist, asteroid)
			elif y1 < y2:
				# asteroid is above us
				if up[0]:
					# already marked a neighbor above us, must check
					existing_dist = up[0][0]
					if dist < existing_dist:
						# our current asteroid is closer than the existing one
						up[0] = (dist, asteroid)
				else:
					# first asteroid above us encountered
					up[0] = (dist, asteroid)
		else:
			# asteroid is some degree left or right to us

			# calculate slope
			slope = slope(best_asteroid, asteroid)

			if x1 > x2:
				# asteroid is to our left
				if slope in left:
					# there is an existing asteroid at this slope


def distance(one, two):
	x1, y1 = one
	x2, y2 = two
	return m.sqrt(((x2-x1)**2) + ((y2-y1)**2))

def slope(one, two):
	x1, y1 = one
	x2, y2 = two
	return (y2 - y1) / (x2 - x1)

if __name__ == "__main__":
	# determine input file
	input_file = 'day10test5.txt'

	# part one
	print(c.b("Part One:"))
	loc, count = count_asteroids(input_file)
	print("Received {0} with count {1}".format(loc,count))

	# part two
	print(c.b("Part Two:"))
	solution = obliterate(loc, input_file)
	try:
		assert(solution[0]*100 + solution[1] == 802)
	except:
		print("Expected: {0}\nReceived: {1}".format(802, solution[0]*100 + solution[1]))