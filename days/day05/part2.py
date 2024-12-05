import re
import sys


def main() -> None:
    data = sys.stdin.read().strip()
    rules = []
    orders = []

    br = True
    for line in data.splitlines():
        if not line.strip():
            br = False
            continue

        if br:
            p = line.split("|")
            rules.append((int(p[0]), int(p[1])))
        else:
            orders.append(list(map(int, line.split(","))))

    t = 0
    for order in orders:
        v = True
        for i in range(len(order)):
            for j in range(i + 1, len(order)):
                if not (order[i], order[j]) in rules:
                    order[i], order[j] = order[j], order[i]
                    v = False

        if not v:
            t += order[len(order) // 2]

    print(t)


if __name__ == "__main__":
    main()
