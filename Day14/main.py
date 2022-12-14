from pathlib import Path
from typing import Generator

DATA = Path("input").read_text().splitlines()


def parse(data: list[str]) -> tuple[set[complex], int]:
    cave: set[complex] = set()
    ymax = 0
    for line in data:
        if not line:
            continue
        points = [[int(a) for a in coord.split(",")] for coord in line.split(" -> ")]
        for s, e in zip(points, points[1:]):
            x0, y0 = s
            x1, y1 = e
            if x0 == x1:
                for y in range(min(y0, y1), max(y0, y1) + 1):
                    cave.add(x0 + y * 1j)
            else:
                for x in range(min(x0, x1), max(x0, x1) + 1):
                    cave.add(x + y0 * 1j)
            ymax = max(ymax, y0, y1)

    return cave, ymax


def sand(cave: set[complex], ymax: int) -> bool:
    pos = 500 + 0j
    down, left, right = 1j, -1 + 1j, 1 + 1j
    while pos.imag < ymax and 500 + 0j not in cave:
        if pos + down not in cave:
            pos += down
        elif pos + left not in cave:
            pos += left
        elif pos + right not in cave:
            pos += right
        else:
            cave.add(pos)
            return True
    return False


def score_1(data: list[str]) -> int:
    cave, ymax = parse(data)
    count = 0
    while sand(cave, ymax):
        count += 1
    return count

print("Teil  1", score_1(DATA))

def quicksand(
    cave: set[complex], ymax: int, pos: complex = 500 + 0j
) -> Generator[complex, None, None]:
    cave.add(pos)
    yield pos
    down, left, right = 1j, -1 + 1j, 1 + 1j

    if pos + down not in cave:
        yield from quicksand(cave, ymax, pos + down)
    if pos + left not in cave:
        yield from quicksand(cave, ymax, pos + left)
    if pos + right not in cave:
        yield from quicksand(cave, ymax, pos + right)


def score_2(data: list[str]) -> int:
    cave, ymax = parse(data)
    for x in range(500 - ymax - 4, 500 + ymax + 4):
        cave.add(x + (ymax + 2) * 1j)

    return len(list(quicksand(cave, ymax + 3)))


print("Teil 2", score_2(DATA))