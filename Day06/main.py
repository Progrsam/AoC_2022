def find_start_of_message(line, amount):
    for j in range(0, len(line) - amount):
        amount_to_find = amount
        for i in range(0, amount):
            if amount_to_find == 1:
                print(j+amount, line[j: j+amount])
            if line[j: j + amount].count(line[j + i]) == 1:
                amount_to_find -= 1


with open('input', "r") as file:
    line = file.readline()
    find_start_of_message(line, 4)
    find_start_of_message(line, 14)

