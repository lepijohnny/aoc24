import sys
from collections import Counter
from itertools import repeat


def blick(item: int) -> list[int]:
    if item == 0:
        return [1]

    s = str(item)
    if len(s) % 2 == 0:
        return [int(s[: len(s) // 2]), int(s[len(s) // 2 :])]

    return [item * 2024]


def main() -> None:
    data = sys.stdin.read().strip()

    stones = list(map(int, data.split()))

    count = Counter(stones)

    for i in range(75):
        next = Counter()
        for val, x in count.items():
            for k in blick(val):
                next[k] += x
        count = Counter(next)

    print(sum(count.values()))


if __name__ == "__main__":
    main()
