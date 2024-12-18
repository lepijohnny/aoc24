from heapq import heapify, heappop, heappush
import sys
import time


def can_reach_finish(fx, fy, blocked) -> bool:

    heap = [(0, 0, 0)]
    heapify(heap)
    seen = set()
    finish = False
    while len(heap) > 0:
        cost, x, y = heappop(heap)

        # print(f"x={x}, y={y}, cost={cost}")
        # time.sleep(0.5)

        if (fx, fy) == (x, y):
            finish = True
            break

        if (x, y) in seen:
            continue

        seen.add((x, y))

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy

            if nx < 0 or nx > fx or ny < 0 or ny > fy or (nx, ny) in blocked:
                continue

            heappush(heap, (cost + 1, nx, ny))

    return finish


def main() -> None:
    data = sys.stdin.read().strip()

    corrupt = [tuple(map(int, line.split(","))) for line in data.splitlines()]

    if len(corrupt) == 25:
        fx, fy = 6, 6
        min_idx = 12
    else:
        fx, fy = 70, 70
        min_idx = 1024

    max_idx = len(corrupt)
    idx = min_idx + (max_idx - min_idx) // 2
    while min_idx < max_idx - 1:
        can = can_reach_finish(fx, fy, set(corrupt[:idx]))

        if can:
            min_idx = idx
            idx = min_idx + (max_idx - min_idx) // 2
        else:
            max_idx = idx
            idx = min_idx + (max_idx - min_idx) // 2

    print(f"{corrupt[idx]}")


if __name__ == "__main__":
    main()
