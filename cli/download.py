import click

from cli.utils import get_day_dir, get_req_session


@click.command()
@click.argument("day", type=click.IntRange(min=1, max=25))
def download(day: int) -> None:
    day_directory = get_day_dir(day)

    input_file = day_directory / "input.txt"

    if not input_file.is_file():
        raise ValueError(f"{input_file} doesn't exist")

    if input_file.stat().st_size != 0:
        raise ValueError(f"{input_file} is not empty")

    resp = get_req_session().get(f"https://adventofcode.com/2024/day/{day}/input")
    resp.raise_for_status()

    input_file.write_text(resp.text.strip(), encoding="utf-8")
