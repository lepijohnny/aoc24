import sys
import re


def main() -> None:
    data = sys.stdin.read().strip()

    pattern = "mul\((?P<a>\d{1,3}),(?P<b>\d{1,3})\)"

    print(data)
    matches = re.finditer(pattern, data)

    r = 0
    for match in matches:
        a = int(match["a"])
        b = int(match["b"])
        r += a * b

    print(r)


if __name__ == "__main__":
    main()
