from heapq import heapify, heappop, heappush
import sys
from collections import defaultdict


def distances(point, cheat, max, grid) -> defaultdict[tuple[int, int], int]:

    w, h = len(grid), len(grid[0])
    x, y = point

    heap = [(0, x, y)]
    heapify(heap)
    seen = {}

    distances = defaultdict()
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

            if (nx, ny) not in distances:
                distances[(nx, ny)] = next

            if distances[(nx, ny)] > next:
                distances[(nx, ny)] = next

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

    dist_to_start_from = distances(start, False, sys.maxsize, grid)
    dist_to_end_from = distances(end, False, sys.maxsize, grid)

    base = dist_to_end_from[start]

    t = 0
    for (x, y), fs in dist_to_start_from.items():
        for (xx, yy), fe in dist_to_end_from.items():
            if abs(xx - x) + abs(yy - y) <= 20:
                if fs + fe + abs(xx - x) + abs(yy - y) <= base - 100:
                    t += 1

    print(t)


if __name__ == "__main__":
    main()
