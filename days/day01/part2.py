import sys
from collections import Counter


def main() -> None:
    data = sys.stdin.read().strip()

    a = []
    b = []

    for line in data.splitlines():
        nums = line.split()
        a.append(int(nums[0]))
        b.append(int(nums[1]))

    counter = Counter(b)

    r = 0
    for i in a:
        r += i * counter[i]

    print(r)


if __name__ == "__main__":
    main()
