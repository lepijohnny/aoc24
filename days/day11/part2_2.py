import sys


def blink(item: int, step: int, steps: int, seen: dict[tuple[int, int], int]) -> int:
    next = []

    if (item, step) in seen:
        return seen[(item, step)]

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
        t += blink(n, step + 1, steps, seen)
        seen[(item, step)] = t
    return t


def main() -> None:
    data = sys.stdin.read().strip()

    nums = list(map(int, data.split()))

    seen: dict[tuple[int, int], int] = {}
    t = 0
    for n in nums:
        t += blink(n, 0, 75, seen)
    print(t)


if __name__ == "__main__":
    main()
