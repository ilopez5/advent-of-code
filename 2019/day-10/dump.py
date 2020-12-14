done = False
    while not done:
		# obtain first 360 degrees of neighbouring asteroids
        left, right, vert = record_neighbors(asteroid, coords)

        rslopes = sorted(list(right.keys()),reverse=True)
        lslopes = sorted(list(left.keys()),reverse=True)

        # print(vert[0])
        # print(rslopes)
        # print(right[rslopes[0]])
        # print(vert[1])
        # print(lslopes)

        _, ast = vert[0]
        if count == 200:
            return ast
        count += 1
        del coords[coords.index(ast)]

        for slope in rslopes:
            _, ast = right[slope]
            if count == 200:
                return ast
            del coords[coords.index(ast)]
            count += 1

        _, ast = vert[1]
        if count == 200:
            return ast
        count += 1
        del coords[coords.index(ast)]

        for slope in lslopes:
            _, ast = left[slope]
            if count == 200:
                return ast
            del coords[coords.index(ast)]
            count += 1


def record_neighbors(asteroid, coords):
    x1, y1 = asteroid
    vert, left, right = {}, {}, {}

    for ast2 in coords:
        if asteroid == ast2:
            continue

        x2, y2 = ast2
        d = (((x2-x1)**2) + ((y2-y1)**2))**(1/2)

        if x1 == x2:                          # Vertical
            if y1 > y2 and 0 not in vert:
                vert[0] = [d, ast2]
            elif y1 > y2 and 0 in vert:
                if vert[0][0] > d:
                    vert[0] = [d, ast2]
            elif y1 < y2 and 1 not in vert:
                vert[1] = [d, ast2]
            elif y1 < y2 and 1 in vert:
                if vert[1][0] > d:
                    vert[1] = d
        else:
            m = 0
            if y1 != y2:
                m = (y2-y1) / (x2-x1)

            if x2 > x1 and m not in right:
                right[m] = [d, ast2]            # store the distance
            elif x2 > x1 and m in right:
                if right[m][0] > d:
                    right[m] = [d, ast2]
            elif x2 < x1 and m not in left:
                left[m] = [d, ast2]
            elif x2 < x1 and m in left:
                if left[m][0] > d:
                    left[m] = [d, ast2]
    return left, right, vert
