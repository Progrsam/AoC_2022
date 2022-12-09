def first_part():

    lines = [line.strip() for line in open("input", "r")]

    head = [0, 0]
    tail = [0, 0]
    marked_pos = []

    # Read Input
    for movement in lines:
        direction = movement.split(" ")[0]
        amount = movement.split(" ")[1]
        for i in range(0, int(amount)):
            old_position_head = head.copy()

            if direction == "U":
                head[1] += 1
            if direction == "D":
                head[1] -= 1
            if direction == "L":
                head[0] -= 1
            if direction == "R":
                head[0] += 1

            # First knot moves around Head
            if abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1:
                tail = old_position_head
                marked_pos.append((tail[0], tail[1]))

    print("Ergebnis Teil 1: " + str(len(list(dict.fromkeys(marked_pos))) + 1))


def second_part():

    lines = [line.strip() for line in open("input", "r")]

    head = [0, 0]
    knots = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
    marked_pos = []

    # Read Input
    for movement in lines:
        direction = movement.split(" ")[0]
        amount = movement.split(" ")[1]
        for i in range(0, int(amount)):
            old_position_head = head.copy()

            if direction == "U":
                head[1] += 1
            if direction == "D":
                head[1] -= 1
            if direction == "L":
                head[0] -= 1
            if direction == "R":
                head[0] += 1

            #First knot moves around Head
            if abs(head[0] - knots[0][0]) > 1 or abs(head[1] - knots[0][1]) > 1:
                knots[0] = old_position_head

            for j in range(1, len(knots)):
                if abs(knots[j-1][0] - knots[j][0]) > 1 or abs(knots[j-1][1] - knots[j][1]) > 1:
                    x = knots[j - 1][0] - knots[j][0]
                    y = knots[j - 1][1] - knots[j][1]

                    if x != 0 and y != 0:
                        to_add_x = 1 if x > 0 else -1
                        to_add_y = 1 if y > 0 else -1
                        knots[j] = [knots[j][0] + to_add_x, knots[j][1] + to_add_y]
                    else:
                        if x == 0:
                            to_add = 1 if y > 0 else -1
                            knots[j] = [knots[j][0], knots[j][1] + to_add]
                        elif y == 0:
                            to_add = 1 if x > 0 else -1
                            knots[j] = [knots[j][0] + to_add, knots[j][1]]

                if j == 8:
                    marked_pos.append((knots[8][0], knots[8][1]))

    print("Ergebnis Teil 2: " + str(len(list(dict.fromkeys(marked_pos)))))


first_part()
second_part()
