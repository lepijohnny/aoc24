import sys
import re


class Keyboard:
    def __init__(self, type: str, layout: list[list[str]], key: str):
        self.type = type
        self.layout = layout
        self.position = key
        self.memory = key

        self.__key_map = {}
        w, h = len(self.layout), len(self.layout[0])
        for r in range(w):
            for c in range(h):
                self.__key_map[self.layout[r][c]] = (r, c)

    def push(self, key: str) -> tuple[str | None, str | None]:
        if self.position == key:
            return ("A", "A")

        x1, y1 = self.__key_map[self.position]
        x2, y2 = self.__key_map[key]

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


def sequence(pads: list[Keyboard], pad: int, keys: str | None, memory) -> int | None:
    if not keys:
        return None

    assert keys[-1] == "A"

    if pad >= len(pads):
        return len(keys)

    keyboard = pads[pad]

    if (pad, keys) in memory:
        return memory[(pad, keys)]

    seq = 0
    for key in keys:
        vals = keyboard.push(key)

        tmp = []
        for i in set([v for v in vals if v is not None]):
            tmp.append(sequence(pads, pad + 1, i, memory))
        seq += min([x for x in tmp if x is not None])

        keyboard.to_position(key)

    memory[(pad, keys)] = seq

    return seq


def main() -> None:
    data = sys.stdin.read().strip()

    numpad = Keyboard(
        "numpad",
        [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], [None, "0", "A"]],
        "A",
    )

    mine = Keyboard("mine", [[None, "^", "A"], ["<", "v", ">"]], "A")

    pads = [numpad]
    for i in range(24):
        pads.append(Keyboard("robot", [[None, "^", "A"], ["<", "v", ">"]], "A"))
    pads.append(mine)

    memory: dict[tuple[int, str], str] = {}
    t = 0
    for line in data.splitlines():
        t += sequence(pads, 0, line, memory) * int(re.findall(r"\d+", line)[0])
    print(t)


if __name__ == "__main__":
    main()
