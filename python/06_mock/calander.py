import datetime
from typing import Any
import requests


def is_weekday():
    # Python's datetime library treats Monday as 0 and Sunday as 6
    today = datetime.datetime.today()
    return 0 <= today.weekday() < 5


def get_holidays() -> dict[str, Any] | None:
    req = requests.get("http://localhost:8081/api/holidays")
    if req.status_code == 200:
        return req.json()
