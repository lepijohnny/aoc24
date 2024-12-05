import sys


def main() -> None:
    data = sys.stdin.read().strip()

    brkz = data.split("\n\n")

    rlz = []
    for line in brkz[0].splitlines():
        rlz.append(tuple(list(map(int, line.split("|")))))

    t = 0
    for line in brkz[1].splitlines():
        upds = list(map(int, line.split(",")))
        c = True
        for r1, r2 in rlz:
            if r1 not in upds or r2 not in upds:
                continue

            i1 = upds.index(r1)
            i2 = upds.index(r2)
            if i1 > i2:
                c = False
                break

        if c:
            t += upds[len(upds) // 2]

    print(t)


if __name__ == "__main__":
    main()
