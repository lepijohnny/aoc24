import re
import sys


def is_possible(d: str, idx: int, avl: set[str]) -> bool:
    if idx == len(d):
        return True

    if idx > len(d):
        return False

    # found = False

    i = len(d)
    for i in range(len(d), idx, -1):
        if d[idx:i] != "" and d[idx:i] in avl and is_possible(d, i, avl):
            return True

    return False


def main() -> None:
    data = sys.stdin.read().strip()

    p, d = data.split("\n\n")

    patterns = set()
    for pattern in p.split(","):
        patterns.add(pattern.strip())

    designs = d.splitlines()

    t = 0
    for d in designs:
        if is_possible(d, 0, patterns):
            print(f"Possible: {d}")
            t += 1
    print(t)


if __name__ == "__main__":
    main()
