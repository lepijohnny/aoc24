import re
import sys
from functools import cache


@cache
def cost(game, xy: tuple[int, int], push, money: int) -> int:
    A, B = push
    if A > 100 or B > 100:
        return sys.maxsize

    btn_a, btn_b, prize = game
    x, y = xy
    px, py = prize
    if x > px or y > py:
        return sys.maxsize

    if x == px and y == py:
        print(f"Done={A}, {B}")
        return money

    ax, ay = btn_a
    ifa = cost(game, (x + ax, y + ay), (A + 1, B), money + 3)

    bx, by = btn_b
    ifb = cost(game, (x + bx, y + by), (A, B + 1), money + 1)

    return min(ifa, ifb)


def main() -> None:
    data = sys.stdin.read().strip()

    game = []
    for d in data.split("\n\n"):
        a, b, prize = d.splitlines()

        btn_ax, btn_ay = map(int, re.findall(r"\d+", a))
        btn_bx, btn_by = map(int, re.findall(r"\d+", b))
        prz_x, prz_y = map(int, re.findall(r"\d+", prize))

        game.append(((btn_ax, btn_ay), (btn_bx, btn_by), (prz_x, prz_y)))

    print(game)

    t = []

    for g in game:
        c = cost(g, (0, 0), (0, 0), 0)

        if c < sys.maxsize:
            t.append(c)

    print(sum(t))


if __name__ == "__main__":
    main()
