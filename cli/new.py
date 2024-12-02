import click

from cli.config import DAYS_DIR
from cli.utils import get_day_dir

PY_TEMPLATE = """
import sys


def main() -> None:
    data = sys.stdin.read().strip()
    print("...")

if __name__ == "__main__":
    main()
    
""".strip()


@click.command()
@click.argument("day", type=click.IntRange(min=1, max=25))
def new(day: int) -> None:

    day_directory = get_day_dir(day)

    if day_directory.is_dir():
        raise ValueError(f"The day{day:02} already exists")

    day_directory.mkdir(parents=True)

    for file, content in [
        (day_directory / "debug.txt", ""),
        (day_directory / "input.txt", ""),
        (day_directory / "part1.py", PY_TEMPLATE),
        (day_directory / "part2.py", PY_TEMPLATE),
    ]:
        with file.open("w+", encoding="utf8") as f:
            f.write(content)

        print(f"Successfully create a file {file.relative_to(DAYS_DIR)}")
