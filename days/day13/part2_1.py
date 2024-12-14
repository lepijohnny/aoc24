import re
import sys


def cost(game) -> int:
    # Cramer's Rule

    btn_a, btn_b, prize = game

    ax, ay = btn_a
    bx, by = btn_b
    px, py = prize

    det = ax * by - ay * bx
    det_a = px * by - py * bx
    det_b = ax * py - ay * px

    if det_a % det != 0 or det_b % det != 0:
        return 0

    n_a = det_a / det
    n_b = det_b / det

    return 3 * round(n_a) + round(n_b)


def main() -> None:
    data = sys.stdin.read().strip()

    game = []
    for d in data.split("\n\n"):
        a, b, prize = d.splitlines()

        btn_ax, btn_ay = map(int, re.findall(r"\d+", a))
        btn_bx, btn_by = map(int, re.findall(r"\d+", b))
        prz_x, prz_y = map(int, re.findall(r"\d+", prize))

        game.append(
            (
                (btn_ax, btn_ay),
                (btn_bx, btn_by),
                (prz_x + 10000000000000, prz_y + 10000000000000),
            )
        )

    t = []

    for i in range(len(game)):
        if True or i == 312:
            c = cost(game[i])
            if c != sys.maxsize:
                t.append(c)

    print(int(sum(t)))


if __name__ == "__main__":
    main()
