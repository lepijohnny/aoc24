import re
import sys


def main() -> None:
    data = sys.stdin.read().strip()

    stones = list(data.split())

    for i in range(25):
        blk = []
        for j in range(len(stones)):
            s = stones[j]
            if int(s) == 0:
                blk.append(str(1))
                continue

            if len(s) % 2 == 0:
                blk.append(str(int(s[0 : len(s) // 2])))
                blk.append(str(int(s[len(s) // 2 :])))
                continue

            blk.append(str(int(s) * 2024))

        stones = blk

    print(len(stones))


if __name__ == "__main__":
    main()
