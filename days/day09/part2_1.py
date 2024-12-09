import sys


def main() -> None:
    data = sys.stdin.read().strip()

    free = []
    blks = []
    file_id = 0
    curr = 0
    for i, size in enumerate(data):
        if i % 2:
            free.append((-1, int(size), curr))
        else:
            blks.append((file_id, int(size), curr))
            file_id += 1
        curr += int(size)

    for i in range(len(blks) - 1, -1, -1):
        for j in range(len(free)):
            id_blk, size, idx_blk = blks[i]
            _, avl, idx = free[j]

            if idx_blk < idx:
                continue

            if avl == size:
                blks[i] = (id_blk, size, idx)
                free[j] = (-1, avl, idx_blk)
                break

            if avl > size:
                blks[i] = (id_blk, size, idx)
                free[j] = (-1, avl - size, idx + size)
                break

    t = 0
    for i, blk in enumerate(blks):
        id, size, idx = blk
        for j in range(idx, idx + size):
            t += j * id
    for i, blk in enumerate(free):
        id, size, idx = blk
        if id != -1:
            for j in range(idx, idx + size):
                t += j * id
    print(t)


if __name__ == "__main__":
    main()
