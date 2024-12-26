import re
import sys


def main() -> None:
    data = sys.stdin.read().strip()

    locks = []
    keys = []

    for blk in data.split("\n\n"):
        g = list(list(line) for line in blk.splitlines())

        h, w = len(g), len(g[0])

        tmp = []
        for x in range(w):
            count = 0
            for y in range(h):
                if g[y][x] == "#":
                    count += 1
            tmp.append(count)

        if g[0][0] == "#":
            locks.append([x - 1 for x in tmp])
        else:
            keys.append([x - 1 for x in tmp])

    t = 0
    for lock in locks:
        for key in keys:
            if all(x + y < h - 1 for x, y in zip(lock, key)):
                t += 1
    print(t)


if __name__ == "__main__":
    main()
