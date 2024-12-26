import re
import sys


def main() -> None:
    data = sys.stdin.read().strip()

    blks = data.split("\n\n")

    operands = {}
    for line in blks[0].splitlines():
        n, v = line.split(": ")
        operands[n] = int(v)

    evl = []
    for line in blks[1].splitlines():
        m = re.search(r"(\w+)\s+(XOR|AND|OR)\s+(\w+)\s*->\s*(\w+)", line)
        if m:
            op1, op, op2, r = m.group(1), m.group(2), m.group(3), m.group(4)

            evl.append((op1, op2, r, f"{op1} {op.lower()} {op2}"))
            for i in [op1, op2, r]:
                if i not in operands:
                    operands[i] = None

    while len(evl) > 0:
        a, b, r, cmd = evl.pop()

        real_a = operands[a]
        real_b = operands[b]

        if real_a == None or real_b == None:
            evl.insert(0, (a, b, r, cmd))
            continue

        real_cmd = (
            cmd.replace(a, str(real_a)).replace(b, str(real_b)).replace("xor", "^")
        )
        real_r = eval(real_cmd)
        operands[r] = real_r

    zz_wrong = [(k, v) for k, v in operands.items() if "z" in k]
    zz = sorted([(k, v) for k, v in operands.items() if "z" in k], reverse=True)
    binary = "".join(str(v) for _, v in zz)
    print(int(binary, 2))

    print(zz_wrong)


if __name__ == "__main__":
    main()
