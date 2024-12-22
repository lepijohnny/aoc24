import sys


def mix(x: int, y: int) -> int:
    return x ^ y


def prune(x: int) -> int:
    return int(x % 16777216)


def main() -> None:
    data = sys.stdin.read().strip()

    secrets = list(map(int, data.splitlines()))

    t = 0
    for s in secrets:
        s3 = s
        for i in range(2000):
            s = s3
            s1 = prune(mix(s, s * 64))
            s2 = prune(mix(s1, int(s1 / 32)))
            s3 = prune(mix(s2, s2 * 2048))

            if i == 1999:
                t += s3
    print(t)


if __name__ == "__main__":
    main()
