
def first_part():
    lines = [line.strip() for line in open("input", "r") if line.strip() != ""]
    monkeys = [lines[i*6:i*6+6] for i in range(0, int(len(lines)/6))]

    items = [[] for monkey in monkeys]
    inspected_items = [0 for monkey in monkeys]
    operations = []
    tests = [[] for monkey in monkeys]
    for j, monkey in enumerate(monkeys):
        # Items
        elements = monkey[1].replace(",", "").split(" ")
        for i in range(2, len(elements)):
            items[j].append(int(elements[i]))

        # Operations to worry level
        elements = monkey[2].split(" ")

        def mult(n):
            return lambda a: a * n if n != -1 else a * a

        def add(n):
            return lambda a: a + n if n != -1 else a + a

        if elements[5] == "old":
            if elements[4] == "+":
                x = add(-1)
            elif elements[4] == "*":
                x = mult(-1)
        elif elements[4] == "+":
            x = add(int(elements[5]))
        elif elements[4] == "*":
            x = mult(int(elements[5]))
        operations.append(x)

        # Tests
        elements = monkey[3].split(" ")

        def mod(n):
            return lambda a: a % n

        x = mod(int(elements[3]))
        tests[j].append(x)

        # Give to
        #True
        elements = monkey[4].split(" ")
        tests[j].append(int(elements[5]))

        #False
        elements = monkey[5].split(" ")
        tests[j].append(int(elements[5]))

    # Rounds
    for i in range(0, 20):
        for x, monkey in enumerate(monkeys):
            for item in items[x]:
                worry_level = item
                worry_level = operations[x](worry_level)
                worry_level = int(worry_level / 3)

                # Test
                if tests[x][0](worry_level) == 0:
                    items[tests[x][1]].append(worry_level)
                else:
                    items[tests[x][2]].append(worry_level)

                inspected_items[x] += 1

            items[x] = []

    inspected_items.sort()
    print("Ergebnis Teil 1: " + str(inspected_items[-1] * inspected_items[-2]))


def second_part():
    lines = [line.strip() for line in open("input", "r") if line.strip() != ""]
    monkeys = [lines[i*6:i*6+6] for i in range(0, int(len(lines)/6))]

    supermod = 1

    items = [[] for monkey in monkeys]
    inspected_items = [0 for monkey in monkeys]
    operations = []
    tests = [[] for monkey in monkeys]
    for j, monkey in enumerate(monkeys):
        # Items
        elements = monkey[1].replace(",", "").split(" ")
        for i in range(2, len(elements)):
            items[j].append(int(elements[i]))

        # Operations to worry level
        elements = monkey[2].split(" ")

        def mult(n):
            return lambda a: a * n if n != -1 else a * a

        def add(n):
            return lambda a: a + n if n != -1 else a + a

        if elements[5] == "old":
            if elements[4] == "+":
                x = add(-1)
            elif elements[4] == "*":
                x = mult(-1)
        elif elements[4] == "+":
            x = add(int(elements[5]))
        elif elements[4] == "*":
            x = mult(int(elements[5]))
        operations.append(x)

        # Super Modulo
        elements = monkey[3].split(" ")
        supermod *= int(elements[3])


        # Tests
        elements = monkey[3].split(" ")

        def mod(n):
            return lambda a: a % n

        x = mod(int(elements[3]))
        tests[j].append(x)

        # Give to
        #True
        elements = monkey[4].split(" ")
        tests[j].append(int(elements[5]))

        #False
        elements = monkey[5].split(" ")
        tests[j].append(int(elements[5]))


    # Rounds
    for i in range(0, 10000):
        for x, monkey in enumerate(monkeys):
            for item in items[x]:
                worry_level = item
                worry_level = operations[x](worry_level)
                worry_level = worry_level % supermod

                # Test
                if tests[x][0](worry_level) == 0:
                    items[tests[x][1]].append(worry_level)
                else:
                    items[tests[x][2]].append(worry_level)

                inspected_items[x] += 1

            items[x] = []
    inspected_items.sort()
    print("Ergebnis Teil 2: " + str(inspected_items[-1] * inspected_items[-2]))


first_part()
second_part()
