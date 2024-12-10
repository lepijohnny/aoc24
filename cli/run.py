import sys
import subprocess
import click

from cli.utils import get_day_dir


@click.command()
@click.argument("day", type=click.IntRange(min=1, max=25))
@click.argument("part")
@click.argument("debug", default="")
def run(day: int, part: str, debug: str) -> None:
    is_debug = debug.lower() in ["debug"]

    day_directory = get_day_dir(day)

    py = day_directory / f"part{part}.py"
    data = day_directory / "debug.txt" if is_debug else day_directory / "input.txt"

    for file in [py, data]:
        if not file.is_file():
            raise ValueError(f"(run) {file} doesn't exist")

    with data.open("r", encoding="utf-8") as file:
        proc = subprocess.run([sys.executable, str(py)], stdin=file)
        sys.exit(proc.returncode)
