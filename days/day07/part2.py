import sys


def check(score: int, t: int, x: list[int], idx: int) -> bool:
    if idx >= len(x):
        return score == t

    if t > score:
        return False

    next = x[idx]

    plus = check(score, t + next, x, idx + 1)
    mul = check(score, t * next, x, idx + 1)
    conc = check(score, int(f"{t}{next}"), x, idx + 1)

    return plus or mul or conc


def main() -> None:
    data = sys.stdin.read().strip()

    score = []
    nums = []
    for line in data.splitlines():
        a, b = line.split(": ")
        score.append(int(a))
        nums.append(list(map(int, b.split())))

    t = 0

    for i in range(len(score)):
        s = nums[i][0]
        if check(score[i], s, nums[i], 1):
            t += score[i]

    print(t)


if __name__ == "__main__":
    main()
