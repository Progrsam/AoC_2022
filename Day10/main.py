def first_part():
    lines = [line.strip() for line in open("input", "r")]

    x = 1
    to_add = []
    counter = 0
    sum = 0

    for line in lines:
        if "noop" in line:
            counter += 1
            if (counter + 20) % 40 == 0:
                print(counter, x)
                sum += counter * x
        else:
            amount = line.split(" ")[1]
            to_add.append([int(amount), 2])

            for i in range(0, 2):
                counter += 1
                if (counter + 20) % 40 == 0:
                    sum += counter * x

                for element in to_add:
                    element[1] -= 1

                for element in to_add:
                    if element[1] == 0:
                        x += element[0]

    print("Ergebnis Teil 1: " + str(sum))


def second_part():
    lines = [line.strip() for line in open("input", "r")]

    x = 1
    to_add = []
    counter = 0

    # CRT
    crt = [["#" for i in range(0, 40)] for j in range(0, 6)]
    line_crt = 0
    sprite_pos = range(0, 3)

    for line in lines:
        if "noop" in line:
            if counter % 40 in sprite_pos:
                crt[line_crt][counter % 40] = "#"
            else:
                crt[line_crt][counter % 40] = "."

            counter += 1
            if counter % 40 == 0:
                line_crt += 1

        else:
            amount = line.split(" ")[1]
            to_add.append([int(amount), 2])

            for i in range(0, 2):
                if counter % 40 in sprite_pos:
                    crt[line_crt][counter % 40] = "#"
                else:
                    crt[line_crt][counter % 40] = "."

                counter += 1
                if counter % 40 == 0:
                    line_crt += 1

                for element in to_add:
                    element[1] -= 1

                for element in to_add:
                    if element[1] == 0:
                        x += element[0]
                        sprite_pos = range(x-1, x + 2)

    print("Ergebnis Teil 2")
    for i in range(0, len(crt)):
        print(*crt[i])


first_part()
second_part()