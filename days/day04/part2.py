import sys


def scan(grid: list[str], r: int, c: int) -> int:
    n, m = len(grid), len(grid[0])

    t = 0
    w = ""
    for dx, dy in [
        ([r - 1, r, r + 1], [c - 1, c, c + 1]),  # \
        ([r + 1, r, r - 1], [c - 1, c, c + 1]),  # /
    ]:
        if all(0 <= i < n for i in dx) and all(0 <= i < m for i in dy):
            for rr, cc in zip(dx, dy):
                w += grid[rr][cc]

    if w[:3] in ["MAS", "SAM"] and w[3:] in ["MAS", "SAM"]:
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
            if grid[r][c] == "A":
                t += scan(grid, r, c)

    print(t)


if __name__ == "__main__":
    main()
