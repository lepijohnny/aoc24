import sys
import re


def combo(reg: tuple[int, int, int], operand: int):
    A, B, C = reg

    if operand == 4:
        return A

    if operand == 5:
        return B

    if operand == 6:
        return C

    if operand == 7:
        raise RuntimeError("Invalid combo operand")

    return operand


def adv(
    state: tuple[tuple[int, int, int], list[int], int], operand: int
) -> tuple[tuple[int, int, int], list[int], int]:
    (A, B, C), pout, next = state

    A = int(A / 2 ** combo((A, B, C), operand))

    return ((A, B, C), pout, next + 2)


def bxl(
    state: tuple[tuple[int, int, int], list[int], int], operand: int
) -> tuple[tuple[int, int, int], list[int], int]:
    (A, B, C), pout, next = state

    B = B ^ operand

    return ((A, B, C), pout, next + 2)


def bst(
    state: tuple[tuple[int, int, int], list[int], int], operand: int
) -> tuple[tuple[int, int, int], list[int], int]:
    (A, B, C), pout, next = state

    B = combo((A, B, C), operand) % 8

    return ((A, B, C), pout, next + 2)


def jnz(
    state: tuple[tuple[int, int, int], list[int], int], operand: int
) -> tuple[tuple[int, int, int], list[int], int]:
    (A, B, C), pout, next = state

    if A == 0:
        return ((A, B, C), pout, next + 2)

    return ((A, B, C), pout, operand)


def bxc(
    state: tuple[tuple[int, int, int], list[int], int], operand: int
) -> tuple[tuple[int, int, int], list[int], int]:
    (A, B, C), pout, next = state

    B = B ^ C

    return ((A, B, C), pout, next + 2)


def out(
    state: tuple[tuple[int, int, int], list[int], int], operand: int
) -> tuple[tuple[int, int, int], list[int], int]:
    (A, B, C), pout, next = state

    pout.append(combo((A, B, C), operand) % 8)

    return ((A, B, C), pout, next + 2)


def bdv(
    state: tuple[tuple[int, int, int], list[int], int], operand: int
) -> tuple[tuple[int, int, int], list[int], int]:
    (A, B, C), pout, next = state

    B = int(A / 2 ** combo((A, B, C), operand))

    return ((A, B, C), pout, next + 2)


def cdv(
    state: tuple[tuple[int, int, int], list[int], int], operand: int
) -> tuple[tuple[int, int, int], list[int], int]:
    (A, B, C), pout, next = state

    C = int(A / 2 ** combo((A, B, C), operand))

    return ((A, B, C), pout, next + 2)


def main() -> None:
    data = sys.stdin.read().strip()

    blkz = data.split("\n\n")

    A, B, C = blkz[0].splitlines()
    A = int(re.findall(r"\d+", A)[0])
    B = int(re.findall(r"\d+", B)[0])
    C = int(re.findall(r"\d+", C)[0])

    program = list(map(int, re.findall(r"\d+", blkz[1])))

    instr = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]

    state = ((A, B, C), [], 0)
    i = 0
    while i < len(program) - 1:
        opcode, operand = program[i], program[i + 1]
        state = instr[opcode](state, operand)
        ((A, B, C), pout, n) = state
        i = n

    print(f"State={state}, Program={program}")


if __name__ == "__main__":
    main()
