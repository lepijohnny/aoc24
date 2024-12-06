import sys


def loop(x: int, y: int, grid: list[list[str]]) -> bool:
    turn = {(-1, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0)}

    n, m = len(grid), len(grid[0])

    turns = {}
    dx, dy = (-1, 0)

    while True:
        nX, nY = x + dx, y + dy

        if nX < 0 or nX >= n or nY < 0 or nY >= m:
            break

        while grid[nX][nY] == "#":
            dx, dy = turn[(dx, dy)]
            nX, nY = x + dx, y + dy

            if (x, y, dx, dy) in turns:
                return True

            turns[(x, y, dx, dy)] = True

        x, y = nX, nY

    return False


def main() -> None:
    data = sys.stdin.read().strip()

    grid = list(list(line) for line in data.splitlines())

    n, m = n, m = len(grid), len(grid[0])

    x, y = -1, -1
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "^":
                x, y = i, j

    t = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "#" or grid[i][j] == "^":
                continue
            grid[i][j] = "#"
            if loop(x, y, grid):
                t += 1
            grid[i][j] = "."

    print(t)


if __name__ == "__main__":
    main()
