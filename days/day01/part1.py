import sys


def main() -> None:
    data = sys.stdin.read().strip()

    a = []
    b = []

    for line in data.splitlines():
        nums = line.split()
        a.append(int(nums[0]))
        b.append(int(nums[1]))

    a.sort()
    b.sort()

    r = 0
    for x, y in zip(a, b):
        r += abs(x - y)

    print(r)


if __name__ == "__main__":
    main()
