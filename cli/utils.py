import os

from pathlib import Path
from requests import Session
from dotenv import load_dotenv

from cli.config import DAYS_DIR


def get_req_session() -> Session:
    session = Session()
    session.headers.update({"User-Agent": "nikola.radin@gmail.com"})

    load_dotenv()
    session.cookies.set("session", os.environ["SESSION_COOKIE"])

    return session


def get_day_dir(day: int) -> Path:
    return Path(DAYS_DIR) / f"day{day:02}"
