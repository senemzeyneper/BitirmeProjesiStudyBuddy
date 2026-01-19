import json
import os
from pathlib import Path

DATA = Path("data")
DATA.mkdir(exist_ok=True)

FILES = [
    "users.json",
    "decks.json",
    "cards.json",
    "srs_state.json",
    "reviews.json",
    "counters.json"
]

for f in FILES:
    p = DATA / f
    if not p.exists():
        if f == "counters.json":
            p.write_text("{}", encoding="utf-8")
        else:
            p.write_text("[]", encoding="utf-8")


def load(name):
    path = DATA / name
    return json.loads(path.read_text(encoding="utf-8"))


def save(name, data):
    path = DATA / name
    tmp = path.with_suffix(".tmp")

    tmp.write_text(
        json.dumps(data, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )

    os.replace(tmp, path)


def next_id(key):
    counters = load("counters.json")

    counters[key] = counters.get(key, 0) + 1

    save("counters.json", counters)

    return counters[key]
