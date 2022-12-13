import json
from functools import cmp_to_key


def compare_one_index(first, second):
    if type(first) is int and type(second) is int:
        comparison_result = (first - second) // abs(first - second) if (first - second) != 0 else 0
        return comparison_result
    elif type(first) is list and type(second) is list:
        if len(first) == 0 and len(second) == 0:
            return 0
        elif len(first) == 0:
            return -1
        elif len(second) == 0:
            return 1
        else:
            return compare_each_index(first, second)
    elif type(first) is int:

        return compare_one_index([first], second)
    elif type(second) is int:
        return compare_one_index(first, [second])


def compare_each_index(list1, list2):
    for i in range(min(len(list1), len(list2))):
        result = compare_one_index(list1[i], list2[i])

        if result != 0:
            return result

    if len(list1) < len(list2):
        return -1
    elif len(list1) == len(list2):
        return 0
    else:
        return 1


def solve(part, use_example):
    filename = "exampleinput.txt" if use_example else "input"

    if part == 1:
        score_part1 = 0
        with open(filename) as openfileobject:
            raw = openfileobject.read()

        chunks = raw.split('\n\n')

        for chunk_index in range(len(chunks)):
            rows = [json.loads(r.strip()) for r in chunks[chunk_index].split()]

            result = compare_each_index(rows[0], rows[1])
            if result != 1:  # (-1 == left smaller, 0 == left and right equal, which is fine)
                score_part1 += chunk_index + 1
                # print(f"chunk {chunk_index + 1}: True  (score: {score_part1})")
            # else:
            # print(f"chunk {chunk_index + 1}: False  (s

        return score_part1

    with open(filename) as openfileobject:
        packets = [json.loads(l.strip()) for l in openfileobject.readlines() if l != '\n']

    packets.append([[2]])
    packets.append([[6]])
    packets.sort(key=cmp_to_key(compare_each_index))

    decoder_key = (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)

    return decoder_key


print(f'Part 1: {solve(1, False)}')
print(f'Part 2: {solve(2, False)}')
