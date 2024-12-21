import sys
import re


class Keyboard:
    def __init__(self, layout: list[list[str]], key: str):
        self.layout = layout
        self.position = key

    def push(self, key: str) -> tuple[str | None, str | None]:
        if self.position == key:
            return ("A", "A")

        key_map = {}
        w, h = len(self.layout), len(self.layout[0])
        for r in range(w):
            for c in range(h):
                key_map[self.layout[r][c]] = (r, c)

        x1, y1 = key_map[self.position]
        x2, y2 = key_map[key]

        diffx, diffy = x1 - x2, y1 - y2
        lr = ("v" if diffx < 0 else "^") * abs(diffx)
        ud = (">" if diffy < 0 else "<") * abs(diffy)

        udlr = None
        if self.layout[x1][y2]:
            udlr = ud + lr + "A"

        lrud = None
        if self.layout[x2][y1]:
            lrud = lr + ud + "A"

        return (udlr, lrud)

    def to_position(self, key: str) -> None:
        self.position = key


def sequence(pads: list[Keyboard], pad: int, keys: str | None) -> str | None:
    if not keys:
        return None

    assert keys[-1] == "A"

    if pad >= len(pads):
        return keys

    keyboard = pads[pad]

    seq = ""
    for key in keys:
        tries = [*keyboard.push(key)]

        tmp = []
        for tt in [t for t in tries if t is not None]:
            tmp.append(sequence(pads, pad + 1, tt))
        seq += min(tmp, key=len)

        keyboard.to_position(key)

    return seq


def main() -> None:
    data = sys.stdin.read().strip()

    numpad = Keyboard(
        [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], [None, "0", "A"]], "A"
    )

    dirpad1 = Keyboard([[None, "^", "A"], ["<", "v", ">"]], "A")
    dirpad2 = Keyboard([[None, "^", "A"], ["<", "v", ">"]], "A")

    t = 0
    for line in data.splitlines():
        seq = sequence([numpad, dirpad1, dirpad2], 0, line)
        t += len(seq) * int(re.findall(r"\d+", line)[0])

    print(t)


if __name__ == "__main__":
    main()
