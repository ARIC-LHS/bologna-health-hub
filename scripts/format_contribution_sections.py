import re
from pathlib import Path
import yaml

PATH = Path("_data/contributions.yml")

HEADING_PATTERNS = [
    r"projects?",
    r"relevant projects?",
    r"relevant research projects?",
    r"research projects?",
    r"running european projects?",
    r"funded projects?",
    r"selected projects?",
    r"selected projects / publications / patents",
    r"selected publications?",
    r"relevant publications?",
    r"relevant publications and projects?",
    r"selected relevant publications?",
    r"scientific publications?",
    r"publications?",
    r"peer-reviewed publications?",
    r"representative peer-reviewed publications relevant to the scope of the topic",
    r"three most relevant publications from the past 5 years",
    r"national and european research projects",
    r"relevant projects experience",
    r"relevant project experience",
    r"relevant project and methods",
    r"relevant projects and research activities",
    r"suggested consortium role and relevant projects",
    r"expertise",
r"expertise and experience",
r"expertise and scientific background",
r"research expertise and scientific background",
r"clinical expertise",
r"clinical expertise and research contribution",
r"experimental activities and methodology",
r"activities and methodologies",
r"potential contribution to the topics?",
r"potential role in the consortium",
r"relevant expertise and contribution",
r"research background",
r"available assets / feasibility",
r"trial-specific activities",
r"what we can provide",
r"proposed contribution to the topics?",
r"contribution to climate and exposome research",
]

heading_re = re.compile(
    r"^\s*(?:" + "|".join(HEADING_PATTERNS) + r")\s*:?\s*$",
    re.I,
)

contributions = yaml.safe_load(
    PATH.read_text(encoding="utf-8")
)

changed = 0
headings = 0

for contribution in contributions:

    text = contribution.get("contribution", "")

    if not text:
        continue

    output = []

    for line in text.splitlines():

        stripped = line.strip()

        if heading_re.fullmatch(stripped):

            label = stripped.rstrip(":").strip()

            output.append(
                f'<strong class="contribution-section-title">'
                f'{label}</strong>'
            )

            headings += 1

        else:
            output.append(line)

    new_text = "\n".join(output)

    if new_text != text:
        contribution["contribution"] = new_text
        changed += 1

PATH.write_text(
    yaml.safe_dump(
        contributions,
        allow_unicode=True,
        sort_keys=False,
        width=1000,
    ),
    encoding="utf-8",
)

print("Contributions changed:", changed)
print("Section headings formatted:", headings)