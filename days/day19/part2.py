import sys
from functools import cache


@cache
def count(d: str, idx: int, avl: frozenset[str]) -> int:
    if idx == len(d):
        return 1

    if idx > len(d):
        return 0

    found = 0

    i = len(d)
    for i in range(len(d), idx, -1):
        if d[idx:i] in avl:
            found += count(d, i, avl)

    return found


def main() -> None:
    data = sys.stdin.read().strip()

    p, d = data.split("\n\n")

    patterns = set()
    for pattern in p.split(","):
        patterns.add(pattern.strip())

    designs = d.splitlines()

    t = 0
    for d in designs:
        t += count(d, 0, frozenset(patterns))
    print(t)


if __name__ == "__main__":
    main()
