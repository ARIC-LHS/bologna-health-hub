from pathlib import Path
import yaml
import re

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "_data"

ID_RE = re.compile(r"^[a-z0-9]+(?:-+[a-z0-9]+)*$")

def load(name):
    with open(DATA / name, encoding="utf-8") as f:
        return yaml.safe_load(f) or []

def index(items, label):
    result = {}
    for item in items:
        item_id = item.get("id")
        assert item_id, f"{label}: missing id"
        assert ID_RE.match(item_id), f"{label}: invalid id {item_id}"
        assert item_id not in result, f"{label}: duplicate id {item_id}"
        result[item_id] = item
    return result

topics = index(load("topics.yml"), "topic")
researchers = index(load("researchers.yml"), "researcher")
contributions = index(load("contributions.yml"), "contribution")

for cid, c in contributions.items():

    assert c["researcher_id"] in researchers, \
        f"{cid}: unknown researcher"

    assert c["topic_id"] in topics, \
        f"{cid}: unknown topic"

    assert c.get("source_version"), \
        f"{cid}: missing source_version"

    assert c.get("source_date"), \
        f"{cid}: missing source_date"

    assert c.get("last_reviewed"), \
        f"{cid}: missing last_reviewed"

print("Validation passed.")
