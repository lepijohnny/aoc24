import sys
from collections import deque


def mix(x: int, y: int) -> int:
    return x ^ y


def prune(x: int) -> int:
    return int(x % 16777216)


def last(x: int) -> int:
    return int(str(x)[-1])


def main() -> None:
    data = sys.stdin.read().strip()

    secrets = list(map(int, data.splitlines()))

    gtrend = {}
    for s in secrets:
        s3 = s
        queue = deque(maxlen=5)
        ltrend = {}
        for i in range(2000):
            s = s3
            s1 = prune(mix(s, s * 64))
            s2 = prune(mix(s1, int(s1 / 32)))
            s3 = prune(mix(s2, s2 * 2048))

            queue.append(s3)

            if len(queue) == 5:
                seq = (
                    last(queue[-4]) - last(queue[-5]),
                    last(queue[-3]) - last(queue[-4]),
                    last(queue[-2]) - last(queue[-3]),
                    last(queue[-1]) - last(queue[-2]),
                )
                if seq not in ltrend:
                    ltrend[seq] = last(queue[-1])

        for k, v in ltrend.items():
            if k in gtrend:
                gtrend[k] += v
            else:
                gtrend[k] = v

    print(max([v for _, v in gtrend.items()]))


if __name__ == "__main__":
    main()
