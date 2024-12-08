import sys
from itertools import combinations
from collections import defaultdict


def main() -> None:
    data = sys.stdin.read().strip()

    grid = list(list(line) for line in data.splitlines())

    h, w = len(grid), len(grid[0])

    ants = defaultdict(list)
    for r in range(h):
        for c in range(w):
            a = grid[r][c]
            if a != ".":
                ants[a].append((r, c))

    unq = set()
    for _, v in ants.items():
        for a, b in combinations(v, 2):
            ax, ay = a
            bx, by = b
            dx, dy = bx - ax, by - ay

            unq.add(a)
            unq.add(b)

            while ax >= 0 and ax < w and ay >= 0 and ay < h:
                if grid[ax][ay] not in [ants.keys(), "#"]:
                    unq.add((ax, ay))
                    grid[ax][ay] = "#"
                ax, ay = ax - dx, ay - dy

            ax, ay = a
            bx, by = b

            while bx >= 0 and bx < w and by >= 0 and by < h:
                if grid[bx][by] not in [ants.keys(), "#"]:
                    unq.add((bx, by))
                    grid[bx][by] = "#"
                bx, by = bx + dx, by + dy

    print(len(unq))


if __name__ == "__main__":
    main()
