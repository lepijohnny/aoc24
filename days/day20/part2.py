from heapq import heapify, heappop, heappush
import sys
from collections import defaultdict


def distances(
    point, cheat, max, grid
) -> defaultdict[tuple[int | None, int | None], int]:

    w, h = len(grid), len(grid[0])
    x, y = point

    heap = [(0, x, y)]
    heapify(heap)
    seen = {}

    distances = defaultdict(lambda: sys.maxsize)
    distances[(x, y)] = 0
    while len(heap) > 0:
        cost, x, y = heappop(heap)

        if (x, y) in seen and seen[(x, y)] <= cost:
            continue

        seen[(x, y)] = cost

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy

            if nx < 0 or nx >= w or ny < 0 or ny >= h:
                continue

            if grid[nx][ny] in "#" and not cheat:
                continue

            next = cost + 1

            if next > max:
                continue

            distances[(nx, ny)] = min(distances[(nx, ny)], next)

            heappush(heap, (next, nx, ny))

    return distances


def find(search: str, grid: list[list[str]]) -> tuple[int | None, int | None]:
    w, h = len(grid), len(grid[0])

    for r in range(h):
        for c in range(w):
            if grid[r][c] == search:
                return (r, c)

    return None, None


def main() -> None:
    data = sys.stdin.read().strip()
    grid = list(list(x for x in line) for line in data.splitlines())

    h, w = len(grid), len(grid[0])

    start = find("S", grid)
    end = find("E", grid)

    dist_to_start = distances(start, cheat=False, max=sys.maxsize, grid=grid)
    dist_to_end = distances(end, cheat=False, max=sys.maxsize, grid=grid)

    base = dist_to_end[start]

    t = 0
    for r in range(w):
        for c in range(h):
            if grid[r][c] in "#":
                continue

            dist_to_20 = distances((r, c), cheat=True, max=20, grid=grid)

            for (kx, ky), v in dist_to_20.items():
                if grid[kx][ky] == "#":
                    continue

                d = dist_to_start[(r, c)] + dist_to_end[(kx, ky)] + v

                if base - d >= 100:
                    t += 1

    print(t)


if __name__ == "__main__":
    main()
