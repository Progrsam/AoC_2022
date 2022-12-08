def first_part():
    with open("input", "r") as file:
        lines = [line.strip() for line in file]

        sum = len(lines) * 2 + (len(lines[1]) - 2) * 2

        for j in range(1, len(lines) -1):
            for k in range(1, len(lines[j]) -1):
                visible_top = True
                visible_bottom = True
                visible_left = True
                visible_right = True

                # Check up
                for i in range(0, j):
                    if lines[i][k] >= lines[j][k]:
                        visible_top = False

                # Check Down
                for i in range(j + 1, len(lines)):
                    if lines[i][k] >= lines[j][k]:
                        visible_bottom = False

                # Check left
                for i in range(0, k):
                    if lines[j][i] >= lines[j][k]:
                        visible_left = False

                # Check right
                for i in range(k + 1, len(lines[1])):
                    if lines[j][i] >= lines[j][k]:
                        visible_right = False

                if visible_left or visible_right or visible_top or visible_bottom:
                    sum += 1

    print(sum)


def second_part():
    with open("input", "r") as file:
        lines = [line.strip() for line in file]

        max = 0

        for j in range(1, len(lines) -1):
            for k in range(1, len(lines[j]) -1):
                amount_of_trees_top = j
                amount_of_trees_bottom = len(lines) - j - 1
                amount_of_trees_left = k
                amount_of_trees_right = len(lines[1]) - k - 1


                # Check up
                for i in range(0, j):
                    if lines[i][k] >= lines[j][k]:
                        amount_of_trees_top = j-i

                # Check Down
                for i in range(j + 1, len(lines)):
                    if lines[i][k] >= lines[j][k]:
                        amount_of_trees_bottom = i-j
                        break

                # Check left
                for i in range(0, k):
                    if lines[j][i] >= lines[j][k]:
                        amount_of_trees_left = k-i

                # Check right
                for i in range(k + 1, len(lines[1])):
                    if lines[j][i] >= lines[j][k]:
                        amount_of_trees_right = i-k
                        break

                combined_amount = amount_of_trees_top * amount_of_trees_bottom * amount_of_trees_left * amount_of_trees_right
                if combined_amount > max:
                    max = combined_amount

    print(max)


first_part()
second_part()
