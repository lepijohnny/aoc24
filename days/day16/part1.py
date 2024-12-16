import sys
import heapq
import time


def compact_grid_print(x, y, grid):
    w, h = len(grid), len(grid[0])

    lines = []
    for r in range(h):
        line = ""
        for c in range(w):
            if (r, c) == (x, y):
                line += "X"
            else:
                line += grid[r][c]
        lines.append(line)

    print("\n".join(lines))


def clockwise(dirs, idx) -> int:
    return (idx + 1) % len(dirs)


def counterclockwise(dirs, idx) -> int:
    return (idx - 1) % len(dirs)


def find(search: str, grid: list[list[str]]) -> tuple[int | None, int | None]:
    w, h = len(grid), len(grid[0])

    for r in range(h):
        for c in range(w):
            if grid[r][c] == search:
                return (r, c)

    return None, None


RUN = 1
TURN = 1000


def main() -> None:
    data = sys.stdin.read().strip()

    grid = list(list(x for x in line) for line in data.splitlines())

    sx, sy = find("S", grid)
    ex, ey = find("E", grid)

    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    idx = 0

    cw_idx = clockwise(dirs, idx)
    ccw_idx = counterclockwise(dirs, idx)

    explore = [
        (RUN, sx, sy, idx, [(sx, sy, idx)]),
        (TURN, sx, sy, cw_idx, [(sx, sy, cw_idx)]),
        (TURN, sx, sy, ccw_idx, [(sx, sy, ccw_idx)]),
    ]

    finished = sys.maxsize
    seen = set()
    while len(explore) > 0:
        cost, x, y, idx, path = heapq.heappop(explore)

        if (x, y, idx) in seen:
            continue

        seen.add((x, y, idx))

        # end reached
        if (x, y) == (ex, ey):
            finished = cost
            break

        # try to move in the same direction
        dx, dy = dirs[idx]
        nx, ny = x + dx, y + dy
        if grid[nx][ny] in ".E":
            heapq.heappush(explore, (cost + RUN, nx, ny, idx, [*path, (nx, ny, idx)]))

        # turn clockwise
        cw_idx = clockwise(dirs, idx)
        dx, dy = dirs[cw_idx]
        nx, ny = x + dx, y + dy
        if grid[nx][ny] == ".":
            heapq.heappush(
                explore, (cost + TURN, x, y, cw_idx, [*path, (x, y, cw_idx)])
            )

        # turn counterclockwise
        ccw_idx = counterclockwise(dirs, idx)
        dx, dy = dirs[ccw_idx]
        nx, ny = x + dx, y + dy
        if grid[nx][ny] == ".":
            heapq.heappush(
                explore, (cost + TURN, x, y, ccw_idx, [*path, (x, y, ccw_idx)])
            )

    print(f"{finished}")


if __name__ == "__main__":
    main()
