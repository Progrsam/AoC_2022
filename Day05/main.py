"""
    [G]         [P]         [M]
    [V]     [M] [W] [S]     [Q]
    [N]     [N] [G] [H]     [T] [F]
    [J]     [W] [V] [Q] [W] [F] [P]
[C] [H]     [T] [T] [G] [B] [Z] [B]
[S] [W] [S] [L] [F] [B] [P] [C] [H]
[G] [M] [Q] [S] [Z] [T] [J] [D] [S]
[B] [T] [M] [B] [J] [C] [T] [G] [N]
 1   2   3   4   5   6   7   8   9
"""
from pprint import pprint

one = ['B', 'G', 'S', 'C']
two = ['T', 'M', 'W', 'H', 'J', 'N', 'V', 'G']
three = ['M', 'Q', 'S']
four = ['B', 'S', 'L', 'T', 'W', 'N', 'M']
five = ['J', 'Z', 'F', 'T', 'V', 'G', 'W', 'P']
six = ['C', 'T', 'B', 'G', 'Q', 'H', 'S']
seven = ['T', 'J', 'P', 'B', 'W']
eight = ['B', 'D', 'C', 'Z', 'F', 'T', 'Q', 'M']
nine = ['N', 'S', 'H','B', 'P', 'F']

stacks = [one, two, three, four, five, six, seven, eight, nine]


def move(amount, move_from, move_to):
    for i in range(0, amount):
        stacks[move_to - 1].append(stacks[move_from - 1].pop())


def move_second(amount, move_from, move_to):
    stack_from = stacks[move_from - 1]
    stack_to = stacks[move_to - 1]

    to_insert = []
    for i in range(0, amount):
        to_insert.append(stack_from.pop())

    to_insert.reverse()
    for i in to_insert:
        stack_to.append(i)


with open("input", "r") as file:
    lines = [line.strip().split(" ") for line in file]
    for line in lines:
        amount = line[1]
        move_from = line[3]
        move_to = line[5]
        move(int(amount), int(move_from), int(move_to))
        # move_second(int(amount), int(move_from), int(move_to))

    for stack in stacks:
        print(stack.pop())
