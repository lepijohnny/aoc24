import sys


def walk_the_edge(edges: set[tuple[int, int, int]]) -> int:

    # for up, down walk left or right, for left, right walk up or down
    move = [[(0, 1), (0, -1)], [(0, -1), (0, 1)], [(1, 0), (-1, 0)], [(1, 0), (-1, 0)]]

    count = 0
    used = set()
    while len(edges) > 0:
        edge = edges.pop()

        if edge in used:
            continue

        side = [edge]

        while len(side) > 0:
            x, y, dir = side.pop()
            for dx, dy in move[dir]:
                xx, yy = x + dx, y + dy
                if (xx, yy, dir) in edges and (xx, yy, dir) not in used:
                    side.append((xx, yy, dir))
                    used.add((xx, yy, dir))

        count += 1
    return count


def main() -> None:
    data = sys.stdin.read().strip()

    grid = list(list(line) for line in data.splitlines())

    n, m = len(grid), len(grid[0])

    # up, down, left, right
    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    t = []

    seen = set()
    for r in range(n):
        for c in range(m):
            if (r, c) in seen:
                continue

            R = grid[r][c]
            explore = [(r, c)]
            edges = []
            area = 0

            while len(explore) > 0:
                px, py = explore.pop()

                if (px, py) in seen:
                    continue

                area += 1

                for i in range(len(move)):
                    dx, dy = move[i]
                    x, y = px + dx, py + dy

                    if x < 0 or x >= n or y < 0 or y >= m:
                        edges.append((px, py, i))
                        continue

                    if grid[x][y] != R:
                        edges.append((px, py, i))
                        continue

                    explore.append((x, y))
                seen.add((px, py))

            s = walk_the_edge(set(edges))

            t.append((area, s))

    print(sum(x * y for x, y in t))


if __name__ == "__main__":
    main()
