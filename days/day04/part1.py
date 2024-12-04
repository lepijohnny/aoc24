import sys
from itertools import repeat


def scan(grid: list[str], r: int, c: int) -> int:
    n, m = len(grid), len(grid[0])

    t = 0
    for dx, dy in [
        ([i for i in repeat(r, 4)], [c + i for i in range(4)]),  # r
        ([i for i in repeat(r, 4)], [c - i for i in range(4)]),  # l
        ([r - i for i in range(4)], [i for i in repeat(c, 4)]),  # t
        ([r + i for i in range(4)], [i for i in repeat(c, 4)]),  # b
        ([r - i for i in range(4)], [c + i for i in range(4)]),  # tr
        ([r - i for i in range(4)], [c - i for i in range(4)]),  # tl
        ([r + i for i in range(4)], [c + i for i in range(4)]),  # br
        ([r + i for i in range(4)], [c - i for i in range(4)]),  # bl
    ]:
        if all(0 <= i < n for i in dx) and all(0 <= i < m for i in dy):
            f = ""
            for rr, cc in zip(dx, dy):
                f += grid[rr][cc]

            if f == "XMAS":
                t += 1

    return t


def main() -> None:
    data = sys.stdin.read().strip()

    grid = []
    for line in data.split("\n"):
        grid.append(line)

    n, m = len(grid), len(grid[0])

    t = 0
    for r in range(n):
        for c in range(m):
            if grid[r][c] == "X":
                t += scan(grid, r, c)

    print(t)


if __name__ == "__main__":
    main()
