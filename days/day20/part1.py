from heapq import heapify, heappop, heappush
import sys
from collections import Counter


def walls(grid) -> list[tuple[int, int]]:

    w, h = len(grid), len(grid[0])

    wls = []
    for r in range(1, h - 1):
        for c in range(1, w - 1):
            if grid[r][c] in "#":
                wls.append((r, c))

    return wls


def search(start, end, cheat, grid) -> tuple[bool, int]:

    w, h = len(grid), len(grid[0])
    xx, yy = start
    fx, fy = end

    heap = [(0, xx, yy)]
    heapify(heap)
    seen = {}

    while len(heap) > 0:
        cost, x, y = heappop(heap)

        if x < 0 or x >= w or y < 0 or y >= h:
            print("out of bounds")
            continue

        if (fx, fy) == (x, y):
            return (True, cost)

        if (x, y) in seen and seen[(x, y)] <= cost:
            continue

        seen[(x, y)] = cost

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy

            if grid[nx][ny] in "#" and (nx, ny) != cheat:
                continue

            heappush(heap, (cost + 1, nx, ny))

    return (False, 0)


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

    start = find("S", grid)
    end = find("E", grid)
    cheat = (None, None)

    _, cost = search(start, end, cheat, grid)

    counter = Counter()
    for cht in walls(grid):
        done, c = search(start, end, cht, grid)
        if done:
            counter[cost - c] += 1

    print(sum(v for k, v in counter.items() if k >= 100))


if __name__ == "__main__":
    main()
