import re
import sys


def maybe_tree(w, h, robots, split=True, rsym="*", esym=".", width=8) -> bool:

    maybe = False

    grid = [[0 for _ in range(w)] for _ in range(h)]

    for x, y, _, _ in robots:
        grid[y][x] += 1

    lines = []
    for c in range(h):
        line = ""
        for r in range(w):
            if split and (r == w // 2 or c == h // 2):
                line += " "
            else:
                if grid[c][r] > 0:
                    line += rsym
                else:
                    line += esym

        lines.append(line)

        if (rsym * width) in line:
            maybe = True

    if maybe:
        print("\n".join(lines))

    return maybe


def teleport(move, position, velocity, bound):
    return (position + move * velocity) % bound


def main() -> None:
    data = sys.stdin.read().strip()

    robots = []
    for line in data.splitlines():
        x, y, vx, vy = re.findall(r"-?\d+", line)
        robots.append((int(x), int(y), int(vx), int(vy)))

    h, w = 103, 101

    for i in range(1, h * w):
        for j in range(len(robots)):
            x, y, vx, vy = robots[j]

            x = teleport(1, x, vx, w)
            y = teleport(1, y, vy, h)

            robots[j] = (x, y, vx, vy)

        if maybe_tree(w, h, robots, split=False, width=8):
            print(i)
            break


if __name__ == "__main__":
    main()
