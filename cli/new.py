import click

from cli.config import DAYS_DIR
from cli.utils import get_day_dir

PY_TEMPLATE = """
import re
import sys


def main() -> None:
    data = sys.stdin.read().strip()
    print("...")

if __name__ == "__main__":
    main()

""".strip()


@click.command()
@click.argument("day", type=click.IntRange(min=1, max=25))
@click.option("--part", multiple=True)
def new(day: int, part: list[str]) -> None:
    day_directory = get_day_dir(day)

    if not day_directory.is_dir():
        day_directory.mkdir(parents=True)

    files = []
    files.append((day_directory / "debug.txt", ""))
    files.append((day_directory / "input.txt", ""))
    for p in set(list(part) + ["1", "2"]):
        files.append((day_directory / f"part{p}.py", PY_TEMPLATE))

    for file, content in files:
        if file.is_file():
            print(f"(new) File {file.relative_to(DAYS_DIR)} already exist...")
            continue

        with file.open("w+", encoding="utf8") as f:
            f.write(content)

        print(f"(new) Successfully create a file {file.relative_to(DAYS_DIR)}")
