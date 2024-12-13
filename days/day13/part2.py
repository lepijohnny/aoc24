import re
import sys
from sympy import symbols, solve, Eq


def cost(game):

    btn_a, btn_b, prize = game

    ax, ay = btn_a
    bx, by = btn_b
    px, py = prize

    na, nb = symbols("na nb", integer=True)

    eq_a = Eq(ax * na + bx * nb, px)
    eq_b = Eq(ay * na + by * nb, py)

    solution = solve((eq_a, eq_b), (na, nb))

    if not solution:
        return 0

    return 3 * solution[na] + solution[nb]


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
        c = cost(game[i])
        if c != sys.maxsize:
            t.append(c)

    print(int(sum(t)))


if __name__ == "__main__":
    main()
