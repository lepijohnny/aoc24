from heapq import heapify, heappop, heappush
import sys
import time


def main() -> None:
    data = sys.stdin.read().strip()

    corrupt = [tuple(map(int, line.split(","))) for line in data.splitlines()]

    if len(corrupt) == 25:
        fx, fy = 6, 6
        blocked = set(corrupt[:12])
    else:
        fx, fy = 70, 70
        blocked = set(corrupt[:1024])

    heap = [(0, 0, 0)]
    heapify(heap)
    seen = set()
    while len(heap) > 0:
        cost, x, y = heappop(heap)

        # print(f"x={x}, y={y}, cost={cost}")
        # time.sleep(0.5)

        if (fx, fy) == (x, y):
            print(cost)
            break

        if (cost, x, y) in seen:
            continue

        seen.add((cost, x, y))

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy

            if nx < 0 or nx > fx or ny < 0 or ny > fy or (nx, ny) in blocked:
                continue

            heappush(heap, (cost + 1, nx, ny))


if __name__ == "__main__":
    main()
