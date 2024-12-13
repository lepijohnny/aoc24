import sys


def main() -> None:
    data = sys.stdin.read().strip()

    grid = list(list(line) for line in data.splitlines())

    n, m = len(grid), len(grid[0])

    move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    fence = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    t = []

    seen = set()
    for r in range(n):
        for c in range(m):
            if (r, c) in seen:
                continue

            R = grid[r][c]
            region = []
            explore = [(r, c)]

            while len(explore) > 0:
                px, py = explore.pop()

                # print(f"{px}, {py}")

                if grid[px][py] != R or (px, py) in seen:
                    continue

                region.append((px, py))
                seen.add((px, py))

                for dx, dy in move:
                    x, y = px + dx, py + dy

                    if x < 0 or x >= n or y < 0 or y >= m:
                        continue

                    explore.append((x, y))

            # count fence
            f = []
            for x, y in region:
                for dx, dy in fence:
                    fx, fy = x + dx, y + dy

                    if fx < 0 or fx >= n or fy < 0 or fy >= m:
                        f.append((fx, fy))
                        continue

                    if grid[fx][fy] != R:
                        f.append((fx, fy))
                        continue

            t.append((len(region), len(f)))

    print(sum(x * y for x, y in t))


if __name__ == "__main__":
    main()
