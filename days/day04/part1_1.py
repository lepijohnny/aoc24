import sys
from itertools import product


def scan(grid: list[str], r: int, c: int) -> int:
    n, m = len(grid), len(grid[0])
    word = "XMAS"

    t = 0
    for dx, dy in product([-1, 0, 1], [-1, 0, 1]):
        if not dx and not dy:
            continue

        bingo = True
        for k in range(len(word)):
            i = r + k * dx
            j = c + k * dy

            if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] != word[k]:
                bingo = False
                break

        if bingo:
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
