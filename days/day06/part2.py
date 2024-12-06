import sys


def main() -> None:
    data = sys.stdin.read().strip()

    grid = list(data.splitlines())

    n, m = n, m = len(grid), len(grid[0])

    x, y = -1, -1
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "^":
                x, y = i, j

    turn = {(-1, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0)}

    xx, yy = x, y
    t = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] == "#" or grid[i][j] == "^":
                continue

            loop = False
            turns = {}
            x, y = xx, yy
            dx, dy = (-1, 0)

            while True:
                nX, nY = x + dx, y + dy

                if nX < 0 or nX >= n or nY < 0 or nY >= m:
                    break

                while grid[nX][nY] == "#" or (nX, nY) == (i, j):
                    dx, dy = turn[(dx, dy)]
                    nX, nY = x + dx, y + dy

                    if (x, y, dx, dy) in turns:
                        loop = True
                        break

                    turns[(x, y, dx, dy)] = True

                if loop:
                    break

                x, y = nX, nY

            if loop:
                t += 1

    print(t)


if __name__ == "__main__":
    main()
