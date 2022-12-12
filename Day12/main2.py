from collections import deque


def second_part():
    height_map = [[[i, j, char, 0] for i, char in enumerate(line.strip())] for j, line in enumerate(open("input", "r"))]
    start_pos = [0, 0, 'a', 0]
    end_pos = [0, 0, 'z', 0]
    for i, line in enumerate(height_map):
        for j, tup in enumerate(line):
            if "S" in tup:
                start_pos = [tup[0], tup[1], "a", 0]
                height_map[i][j] = start_pos
            if "E" in tup:
                end_pos = [tup[0], tup[1], "z", 0]
                height_map[i][j] = end_pos

    BFS(height_map, start_pos, end_pos)




def BFS(height_map, start_pos, end_pos):
    visited = []
    queue = deque([start_pos])
    min_val = 1000
    while queue:
        vertex = queue.pop()


        if vertex == end_pos:
            if vertex[3] < min_val:
                min_val = vertex[3]

        if vertex not in visited:
            visited.append(vertex)  # u, l, d, r
            if vertex[1] != 0 and ord(height_map[vertex[1] - 1][vertex[0]][2]) - ord(vertex[2]) <= 1:
                if height_map[vertex[1] - 1][vertex[0]][3] > height_map[vertex[1]][vertex[0]][3] + 1:
                    if height_map[vertex[1] - 1][vertex[0]][2] == "a":
                        height_map[vertex[1] - 1][vertex[0]][3] = 0
                    else:
                        height_map[vertex[1] - 1][vertex[0]][3] = height_map[vertex[1]][vertex[0]][3] + 1
                    queue.append(height_map[vertex[1] - 1][vertex[0]])
                    if height_map[vertex[1] - 1][vertex[0]] in visited:
                        visited.remove(height_map[vertex[1] - 1][vertex[0]])
                elif height_map[vertex[1] - 1][vertex[0]] not in visited and height_map[vertex[1] - 1][
                    vertex[0]] not in queue:
                    height_map[vertex[1] - 1][vertex[0]][3] = height_map[vertex[1]][vertex[0]][3] + 1
                    queue.append(height_map[vertex[1] - 1][vertex[0]])
            if vertex[0] != 0 and ord(height_map[vertex[1]][vertex[0] - 1][2]) - ord(vertex[2]) <= 1:
                if height_map[vertex[1]][vertex[0] - 1][3] > height_map[vertex[1]][vertex[0]][3] + 1:
                    if height_map[vertex[1]][vertex[0] - 1][2] == "a":
                        height_map[vertex[1]][vertex[0] - 1][3] = 0
                    else:
                        height_map[vertex[1]][vertex[0] - 1][3] = height_map[vertex[1]][vertex[0]][3] + 1
                    queue.append(height_map[vertex[1]][vertex[0] - 1])
                    if height_map[vertex[1]][vertex[0] - 1] in visited:
                        visited.remove(height_map[vertex[1]][vertex[0] - 1])
                elif height_map[vertex[1]][vertex[0] - 1] not in visited and height_map[vertex[1]][
                    vertex[0] - 1] not in queue:
                    height_map[vertex[1]][vertex[0] - 1][3] = height_map[vertex[1]][vertex[0]][3] + 1
                    queue.append(height_map[vertex[1]][vertex[0] - 1])
            if vertex[1] != len(height_map) - 1 and ord(height_map[vertex[1] + 1][vertex[0]][2]) - ord(vertex[2]) <= 1:
                if height_map[vertex[1] + 1][vertex[0]][3] > height_map[vertex[1]][vertex[0]][3] + 1:
                    if height_map[vertex[1] + 1][vertex[0]][2] == "a":
                        height_map[vertex[1] + 1][vertex[0]][3] = 0
                    else:
                        height_map[vertex[1] + 1][vertex[0]][3] = height_map[vertex[1]][vertex[0]][3] + 1
                    queue.append(height_map[vertex[1] + 1][vertex[0]])
                    if height_map[vertex[1] + 1][vertex[0]] in visited:
                        visited.remove(height_map[vertex[1] + 1][vertex[0]])
                elif height_map[vertex[1] + 1][vertex[0]] not in visited and height_map[vertex[1] + 1][
                    vertex[0]] not in queue:
                    height_map[vertex[1] + 1][vertex[0]][3] = height_map[vertex[1]][vertex[0]][3] + 1
                    queue.append(height_map[vertex[1] + 1][vertex[0]])
            if vertex[0] != len(height_map[0]) - 1 and ord(height_map[vertex[1]][vertex[0] + 1][2]) - ord(
                    vertex[2]) <= 1:
                if height_map[vertex[1]][vertex[0] + 1][3] > height_map[vertex[1]][vertex[0]][3] + 1:
                    if height_map[vertex[1]][vertex[0] + 1][2] == "a":
                        height_map[vertex[1]][vertex[0] + 1][3] = 0
                    else:
                        height_map[vertex[1]][vertex[0] + 1][3] = height_map[vertex[1]][vertex[0]][3] + 1
                    queue.append(height_map[vertex[1]][vertex[0] + 1])
                    if height_map[vertex[1]][vertex[0] + 1] in visited:
                        visited.remove(height_map[vertex[1]][vertex[0] + 1])
                elif height_map[vertex[1]][vertex[0] + 1] not in visited and height_map[vertex[1]][
                    vertex[0] + 1] not in queue:
                    height_map[vertex[1]][vertex[0] + 1][3] = height_map[vertex[1]][vertex[0]][3] + 1
                    queue.append(height_map[vertex[1]][vertex[0] + 1])
    print(min_val)
    return visited


second_part()