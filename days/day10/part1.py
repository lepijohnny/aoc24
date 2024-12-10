import sys


def main() -> None:
    data = sys.stdin.read().strip()

    grid = list(list(map(int, line)) for line in data.splitlines())

    h, w = len(grid), len(grid[0])

    d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    trails = []
    for r in range(w):
        for c in range(h):
            if grid[r][c] == 0:
                path = [(r, c)]
                while len(path) > 0:
                    x, y = path.pop()

                    if grid[x][y] == 9:
                        trails.append((r, c, x, y))
                        continue

                    for dx, dy in d:
                        nx, ny = x + dx, y + dy

                        if nx < 0 or nx >= w or ny < 0 or ny >= h:
                            continue

                        if grid[nx][ny] != grid[x][y] + 1:
                            continue

                        path.append((nx, ny))

    print(len(set(trails)))


if __name__ == "__main__":
    main()
