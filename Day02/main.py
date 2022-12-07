def rps(first, second):
    to_add = 0
    if second == 'X':
        to_add = 1
    elif second == 'Y':
        to_add = 2
    elif second == 'Z':
        to_add = 3

    if first == 'A' and second == 'X':
        return 3 + to_add
    if first == 'B' and second == 'Y':
        return 3 + to_add
    if first == 'C' and second == 'Z':
        return 3 + to_add
    elif first == 'A' and second == 'Y':
        return 6 + to_add
    elif first == 'A' and second == 'Z':
        return 0 + to_add
    elif first == 'B' and second == 'X':
        return 0 + to_add
    elif first == 'B' and second == 'Z':
        return 6 + to_add
    elif first == 'C' and second == 'X':
        return 6 + to_add
    elif first == 'C' and second == 'Y':
        return 0 + to_add
    else:
        return 0

print(rps('A','Z'))

with open("input", "r") as file:
    lines = file.readlines()
    result = 0
    for game in lines:
        splitted = game.strip().split(" ")
        if splitted[0] == 'A' and splitted[1] == 'X':
            result += rps(splitted[0], 'Z')
        elif splitted[0] == 'B' and splitted[1] == 'X':
            result += rps(splitted[0], 'X')
        elif splitted[0] == 'C' and splitted[1] == 'X':
            result += rps(splitted[0], 'Y')
        elif splitted[0] == 'A' and splitted[1] == 'Y':
            result += rps(splitted[0], 'X')
        elif splitted[0] == 'B' and splitted[1] == 'Y':
            result += rps(splitted[0], 'Y')
        elif splitted[0] == 'C' and splitted[1] == 'Y':
            result += rps(splitted[0], 'Z')
        elif splitted[0] == 'A' and splitted[1] == 'Z':
            result += rps(splitted[0], 'Y')
        elif splitted[0] == 'B' and splitted[1] == 'Z':
            result += rps(splitted[0], 'Z')
        elif splitted[0] == 'C' and splitted[1] == 'Z':
            result += rps(splitted[0], 'X')

    print(result)
