import sys


def loop(x: int, y: int, grid: list[str], vx: int, vy: int) -> bool:
    turn = {(-1, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0)}

    n, m = len(grid), len(grid[0])

    turns = {}
    dx, dy = (-1, 0)

    while True:
        nX, nY = x + dx, y + dy

        if nX < 0 or nX >= n or nY < 0 or nY >= m:
            break

        while grid[nX][nY] == "#" or (nX, nY) == (vx, vy):
            dx, dy = turn[(dx, dy)]
            nX, nY = x + dx, y + dy

            if (x, y, dx, dy) in turns:
                return True

            turns[(x, y, dx, dy)] = True

        x, y = nX, nY

    return False


def main() -> None:
    data = sys.stdin.read().strip()

    grid = list(data.splitlines())

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
            if loop(x, y, grid, i, j):
                t += 1

    print(t)


if __name__ == "__main__":
    main()
