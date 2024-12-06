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

    route = {(x, y): True}
    dx, dy = (-1, 0)
    t = 0
    while True:
        nX, nY = x + dx, y + dy

        if nX < 0 or nX >= n or nY < 0 or nY >= m:
            break

        if grid[nX][nY] == "#":
            dx, dy = turn[(dx, dy)]
            nX, nY = x + dx, y + dy
            t += 1

        x, y = nX, nY
        route[(x, y)] = True

    print(len(route))
    print(t)


if __name__ == "__main__":
    main()
