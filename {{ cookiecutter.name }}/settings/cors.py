import os
from typing import NamedTuple, List


class CORSSettings(NamedTuple):
    ORIGINS: List[str]
    CREDENTIALS: bool
    METHODS: List[str]
    HEADERS: List[str]


def to_list(line: str) -> List[str]:
    if "," in line:
        raw = (a.strip() for a in line.split(",") if len(a.strip()) > 3)
        normalized = (a if a.startswith("https") else f"http://{a}" for a in raw)
    else:
        normalized = [line]
    return normalized


CORS = CORSSettings(to_list(os.getenv("ALLOWED_ORIGINS")), True, ["*"], ["*"])
