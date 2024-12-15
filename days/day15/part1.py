import sys


def print_grid(grid):
    print("\n".join("".join(r) for r in grid))


def main() -> None:
    data = sys.stdin.read().strip()

    g, m = data.split("\n\n")
    grid = list(list(line) for line in g.splitlines())
    moves = list(x for x in m if x != "\n")

    h, w = len(grid), len(grid[0])

    dirs = {"<": (0, -1), ">": (0, 1), "^": (-1, 0), "v": (1, 0)}

    rx, ry = None, None
    for r in range(h):
        for c in range(w):
            if grid[r][c] == "@":
                rx, ry = r, c
                break

    print(f"{rx}, {ry}")
    print_grid(grid)
    print(moves)

    for move in moves:
        dx, dy = dirs[move]

        coords = [(rx, ry)]
        can_move = False

        x, y = rx, ry
        while True:
            x, y = x + dx, y + dy

            if grid[x][y] == "#":
                break
            if grid[x][y] == ".":
                coords.append((x, y))
                can_move = True
                break
            coords.append((x, y))

        if can_move:
            for i in range(len(coords) - 1, 0, -1):
                x1, y1 = coords[i]
                x2, y2 = coords[i - 1]
                grid[x1][y1], grid[x2][y2] = grid[x2][y2], grid[x1][y1]

            rx, ry = rx + dx, ry + dy

    print_grid(grid)

    t = 0
    for r in range(h):
        for c in range(w):
            if grid[r][c] == "O":
                t += r * 100 + c
    print(t)


if __name__ == "__main__":
    main()
