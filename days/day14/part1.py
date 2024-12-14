import re
import sys


def quadrant(grid, wspan, hspan) -> int:
    h, w = len(grid), len(grid[0])

    # q1
    q = 0
    h, hh = hspan
    w, ww = wspan

    for y in range(h, hh):
        for x in range(w, ww):
            q += grid[y][x]

    return q


def print_grid(grid, robots, split=True) -> None:
    # print("\n".join(["".join(map(str, x)) for x in grid]))

    h, w = len(grid), len(grid[0])

    for x, y, _, _ in robots:
        grid[y][x] += 1

    for c in range(h):
        line = ""
        for r in range(w):
            if split and (r == w // 2 or c == h // 2):
                line += " "
            else:
                line += str(grid[c][r])
        print(line)


def teleport(move, position, velocity, bound):
    p = position + move * velocity

    if 0 <= p < bound:
        return p

    if p < 0:
        rem = -p % bound
        return rem if rem == 0 else bound - rem

    if p >= bound:
        return p % bound


def main() -> None:
    data = sys.stdin.read().strip()

    robots = []
    for line in data.splitlines():
        x, y, vx, vy = re.findall(r"-?\d+", line)
        robots.append((int(x), int(y), int(vx), int(vy)))

    h, w = 103, 101
    grid = [[0 for _ in range(w)] for _ in range(h)]

    move = 100
    for i in range(len(robots)):
        x, y, vx, vy = robots[i]

        x = teleport(move, x, vx, w)
        y = teleport(move, y, vy, h)

        robots[i] = (x, y, vx, vy)

    print_grid(grid, robots, split=True)

    q1 = quadrant(grid, (0, w // 2), (0, h // 2))
    q2 = quadrant(grid, (w // 2 + 1, w), (0, h // 2))
    q3 = quadrant(grid, (0, w // 2), (h // 2 + 1, h))
    q4 = quadrant(grid, (w // 2 + 1, w), (h // 2 + 1, h))

    print((q1, q2, q3, q4))

    print(q1 * q2 * q3 * q4)


if __name__ == "__main__":
    main()
