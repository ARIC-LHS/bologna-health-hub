from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "_data"

def load(name):
    with open(DATA / name, encoding="utf-8") as f:
        return yaml.safe_load(f) or []

def write(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")

for topic in load("topics.yml"):
    tid = topic["id"]

    write(
        ROOT / "topics" / f"{tid}.md",
        f"""---
layout: topic
topic_id: {tid}
permalink: /topics/{tid}/
---
"""
    )

for researcher in load("researchers.yml"):
    rid = researcher["id"]

    write(
        ROOT / "researchers" / f"{rid}.md",
        f"""---
layout: researcher
researcher_id: {rid}
permalink: /researchers/{rid}/
---
"""
    )

print("Wrapper pages generated")
