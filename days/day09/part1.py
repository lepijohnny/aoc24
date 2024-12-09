import sys


def main() -> None:
    data = sys.stdin.read().strip()

    memory = []

    block = 0
    free = False
    for i in data:
        if free:
            for _ in range(int(i)):
                memory.append(".")
            free = False
        else:
            for _ in range(int(i)):
                memory.append(str(block))
            block += 1
            free = True

    i, j = 0, len(memory) - 1

    while i < j - 1:
        while memory[i] != ".":
            i += 1
            continue
        while memory[j] == ".":
            j -= 1
            continue
        memory[i], memory[j] = memory[j], memory[i]
        i += 1
        j -= 1

    t = 0
    for i in range(len(memory)):
        if memory[i] != ".":
            t += i * int(memory[i])
    print(t)


if __name__ == "__main__":
    main()
