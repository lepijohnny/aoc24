import sys
import heapq


def not_blocked(x, y, grid) -> bool:
    return grid[x][y] in ".E"


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
    h, w = len(grid), len(grid[0])

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
    if (sx, sy) == (None, None):
        raise RuntimeError("Start doesn't exist")

    ex, ey = find("E", grid)
    if (sx, sy) == (None, None):
        raise RuntimeError("Finish doesn't exist")

    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    idx = 0

    cw_idx = clockwise(dirs, idx)
    ccw_idx = counterclockwise(dirs, idx)

    explore = [
        (RUN, sx, sy, idx, [(sx, sy, idx)]),
        (TURN, sx, sy, cw_idx, [(sx, sy, cw_idx)]),
        (TURN, sx, sy, ccw_idx, [(sx, sy, ccw_idx)]),
    ]

    seen: dict[tuple[int | None, int | None, int], int] = {}
    best = set()
    finished = sys.maxsize

    while len(explore) > 0:
        cost, x, y, idx, path = heapq.heappop(explore)

        if (x, y, idx) in seen and seen[(x, y, idx)] < cost:
            continue

        seen[(x, y, idx)] = cost

        if cost > finished:
            continue

        # finish reached
        if (x, y) == (ex, ey):
            finished = cost if cost < finished else finished
            for x, y, _ in path:
                best.add((x, y))
            continue

        # try to move in the same direction
        dx, dy = dirs[idx]
        nx, ny = x + dx, y + dy
        if not_blocked(nx, ny, grid):
            heapq.heappush(explore, (cost + RUN, nx, ny, idx, [*path, (nx, ny, idx)]))

        # turn
        for t_idx in [clockwise(dirs, idx), counterclockwise(dirs, idx)]:
            dx, dy = dirs[t_idx]
            nx, ny = x + dx, y + dy
            if not_blocked(nx, ny, grid):
                heapq.heappush(
                    explore, (cost + TURN, x, y, t_idx, [*path, (x, y, t_idx)])
                )

    print(f"{finished}, {len(best)}")


if __name__ == "__main__":
    main()
