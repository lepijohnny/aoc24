import re
import sys


def main() -> None:
    data = sys.stdin.read().strip()

    grid = list(data.splitlines())

    n, m = n, m = len(grid), len(grid[0])

    me = "^"
    x, y = -1, -1
    for i in range(n):
        for j in range(m):
            if grid[i][j] == me:
                x, y = i, j

    turn = {(-1, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0)}

    route = set()
    dx, dy = (-1, 0)

    while True:
        nX, nY = x + dx, y + dy

        if nX < 0 or nX >= n or nY < 0 or nY >= m:
            break

        if grid[nX][nY] == "#":
            dx, dy = turn[(dx, dy)]
            nX, nY = x + dx, y + dy

        x, y = nX, nY
        route.add((x, y))

    print(len(route))


if __name__ == "__main__":
    main()
