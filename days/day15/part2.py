import sys


def print_grid(grid):
    print("\n".join("".join(r) for r in grid))


def expand(line):
    return (
        line.replace("#", "##").replace("O", "[]").replace(".", "..").replace("@", "@.")
    )


def detect_wrong_move(grid) -> bool:
    for line in grid:
        if ".]" in "".join(line):
            return True
        if "[." in "".join(line):
            return True

    return False


def main() -> None:
    data = sys.stdin.read().strip()

    g, m = data.split("\n\n")
    grid = list(list(x for x in expand(line)) for line in g.splitlines())
    moves = list(x for x in m if x != "\n")

    h, w = len(grid), len(grid[0])

    dirs = {"<": (0, -1), ">": (0, 1), "^": (-1, 0), "v": (1, 0)}

    print(h)
    print(w)

    rx, ry = None, None
    for r in range(h):
        for c in range(w):
            if grid[r][c] == "@":
                rx, ry = r, c
                break

    for move in moves:
        dx, dy = dirs[move]

        can_push = True

        paths = []
        explore = [(rx, ry)]
        path = []
        seen = set()

        while len(explore) > 0 and can_push:
            if len(path) == 0:
                path.append(explore.pop())

            nx, ny = path[-1]
            while True:
                nx, ny = nx + dx, ny + dy

                seen.add((nx, ny))

                if grid[nx][ny] == "#":
                    can_push = False
                    break

                if grid[nx][ny] == ".":
                    path.append((nx, ny))
                    paths.append(path)
                    path = []
                    break

                # left/right
                if move in "<>":
                    if grid[nx][ny] in "[]":
                        path.append((nx, ny))
                        continue

                # up/down
                if move in "^v":
                    if grid[nx][ny] in "[":
                        path.append((nx, ny))
                        if (nx, ny + 1) not in seen:
                            explore.insert(0, (nx, ny + 1))
                        continue

                    if grid[nx][ny] in "]":
                        path.append((nx, ny))
                        if (nx, ny - 1) not in seen:
                            explore.insert(0, (nx, ny - 1))
                        continue

        # explore all paths
        # if any finish in # break
        # all paths have to finish in ., swap all paths
        if can_push:
            swapped = set()
            for p in paths:
                for i in range(len(p) - 1, 0, -1):
                    x1, y1 = p[i]
                    x2, y2 = p[i - 1]
                    if (x1, x2, y1, y2) not in swapped:
                        grid[x1][y1], grid[x2][y2] = grid[x2][y2], grid[x1][y1]
                        swapped.add((x1, x2, y1, y2))
            rx, ry = rx + dx, ry + dy

    print_grid(grid)

    t = 0
    for r in range(h):
        for c in range(w):
            if grid[r][c] == "[":
                t += r * 100 + c
    print(t)


if __name__ == "__main__":
    main()
