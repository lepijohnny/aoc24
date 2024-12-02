import sys
import traceback
import click

from cli.download import download
from cli.new import new
from cli.run import run


@click.group(
    context_settings={"help_option_names": ["--help", "-h"], "max_content_width": 120}
)
def cli() -> None:
    """Hello to the Advent of Code 2024."""
    pass


cli.add_command(download)
cli.add_command(new)
cli.add_command(run)


def main() -> None:
    try:
        cli()
    except ValueError as e:
        print(f"Error {e}")
        sys.exit(1)
    except Exception:
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
