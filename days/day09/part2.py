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

    j = len(memory) - 1
    while j > 0:
        if memory[j] == ".":
            j -= 1
            continue

        blk = [memory[j]]
        while memory[j] != "." and memory[j] == memory[j - 1]:
            blk.append(memory[j])
            j -= 1

        if len(blk) > 0:
            idx = -1
            for i in range(len(memory) - len(blk)):
                if memory[i] == "." and len(set(memory[i : i + len(blk)])) == 1:
                    idx = i
                    break

            if idx != -1 and idx < j:
                for k in range(len(blk)):
                    memory[idx + k], memory[j + k] = blk[k], "."
        j -= 1

    t = 0
    for i in range(len(memory)):
        if memory[i] != ".":
            t += i * int(memory[i])
    print(t)


if __name__ == "__main__":
    main()
