import sys
import re


def main() -> None:
    data = sys.stdin.read().strip()

    pattern = r"(?P<on>do\(\))|(?P<off>don't\(\))|(?P<mul>mul\((?P<a>\d{1,3}),(?P<b>\d{1,3})\))"

    matches = re.finditer(pattern, data)

    r = 0
    do = True
    for match in matches:
        if match["on"]:
            do = True
        if match["off"]:
            do = False
        if do and match["mul"]:
            a = int(match.group("a"))
            b = int(match.group("b"))
            r += a * b

    print(r)


if __name__ == "__main__":
    main()
