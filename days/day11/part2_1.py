from functools import cache
import sys


@cache
def blink(item: int, step: int, steps: int) -> int:
    next = []
    if step == steps:
        return 1
    elif item == 0:
        next.append(1)
    elif len(str(item)) % 2 == 0:
        s, c = str(item), len(str(item))
        next.append(int(s[: c // 2]))
        next.append(int(s[c // 2 :]))
    else:
        next.append(item * 2024)

    t = 0
    for n in next:
        t += blink(n, step + 1, steps)
    return t


def main() -> None:
    data = sys.stdin.read().strip()

    nums = list(map(int, data.split()))

    t = 0
    for n in nums:
        t += blink(n, 0, 75)
    print(t)


if __name__ == "__main__":
    main()
