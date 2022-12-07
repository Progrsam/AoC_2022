with open("input", "r") as input:
    lines = input.readlines()
    sum_value = 0
    values = []
    for line in lines:
        if line == "\n":
            values.append(sum_value)
            sum_value = 0
        else:
            sum_value += int(line)

    print("Maximaler Wert: " + str(max(values)))


    #Part 2
    values.sort()
    result = 0
    for i in range(1,4):
        result += values[len(values) - i]
    print("Die drei maximalen Werte als Summe: " + str(result))
