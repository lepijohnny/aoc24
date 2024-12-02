import sys


def check(a: list[int]) -> bool:
    is_inc = all(1 <= (a[i + 1] - a[i]) <= 3 for i in range(len(a) - 1))
    is_dec = all(1 <= (a[i] - a[i + 1]) <= 3 for i in range(len(a) - 1))
    return is_inc or is_dec


def main() -> None:
    data = sys.stdin.read().strip()

    r = 0
    for line in data.splitlines():
        a = list(map(int, line.split()))

        options = [a]
        for i in range(len(a)):
            opt = a.copy()
            opt.pop(i)
            options.append(opt)

        if any(check(opt) for opt in options):
            r += 1

    print(r)


if __name__ == "__main__":
    main()
