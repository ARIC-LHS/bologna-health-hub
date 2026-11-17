from docx import Document
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
BOOKLET = ROOT / "BOOKLET_Cluster 1_2027.docx"
OUTPUT = ROOT / "booklet_contributions_manifest.json"

TOPIC_IDS = {
    "HORIZON-HLTH-2027-01-STAYHLTH-01": "horizon-hlth-2027-01-stayhlth-01",
    "HORIZON-HLTH-2027-01-ENVHLTH-02": "horizon-hlth-2027-01-envhlth-02",
    "HORIZON-HLTH-2027-02-DISEASE-01-TWO-STAGE": "horizon-hlth-2027-02-disease-01-two-stage",
    "HORIZON-HLTH-2027-01-DISEASE-05": "horizon-hlth-2027-01-disease-05",
    "HORIZON-HLTH-2027-01-DISEASE-06": "horizon-hlth-2027-01-disease-06",
    "HORIZON-HLTH-2027-01-DISEASE-07": "horizon-hlth-2027-01-disease-07",
    "HORIZON-HLTH-2027-01-DISEASE-08": "horizon-hlth-2027-01-disease-08",
    "HORIZON-HLTH-2027-01-DISEASE-10": "horizon-hlth-2027-01-disease-10",
    "HORIZON-HLTH-2027-02-DISEASE-14-TWO-STAGE": "horizon-hlth-2027-02-disease-14-two-stage",
    "HORIZON-HLTH-2027-01-CARE-02": "horizon-hlth-2027-01-care-02",
    "HORIZON-HLTH-2027-02-TOOL-01-TWO-STAGE": "horizon-hlth-2027-02-tool-01-two-stage",
    "HORIZON-HLTH-2027-01-IND-01": "horizon-hlth-2027-01-ind-01",
    "HORIZON-HLTH-2027-02-IND-02-TWO-STAGE": "horizon-hlth-2027-02-ind-02-two-stage",
}

TABLE_TOPIC = {}

for n in range(6, 11):
    TABLE_TOPIC[n] = "HORIZON-HLTH-2027-01-STAYHLTH-01"

for n in range(11, 28):
    TABLE_TOPIC[n] = "HORIZON-HLTH-2027-01-ENVHLTH-02"

for n in range(28, 32):
    TABLE_TOPIC[n] = "HORIZON-HLTH-2027-02-DISEASE-01-TWO-STAGE"

for n in range(32, 34):
    TABLE_TOPIC[n] = "HORIZON-HLTH-2027-01-DISEASE-05"

for n in range(34, 36):
    TABLE_TOPIC[n] = "HORIZON-HLTH-2027-01-DISEASE-06"

for n in range(36, 38):
    TABLE_TOPIC[n] = "HORIZON-HLTH-2027-01-DISEASE-07"

for n in range(38, 43):
    TABLE_TOPIC[n] = "HORIZON-HLTH-2027-01-DISEASE-08"

for n in range(43, 48):
    TABLE_TOPIC[n] = "HORIZON-HLTH-2027-01-DISEASE-10"

for n in range(48, 53):
    TABLE_TOPIC[n] = "HORIZON-HLTH-2027-02-DISEASE-14-TWO-STAGE"

for n in range(53, 59):
    TABLE_TOPIC[n] = "HORIZON-HLTH-2027-01-CARE-02"

for n in range(59, 70):
    TABLE_TOPIC[n] = "HORIZON-HLTH-2027-02-TOOL-01-TWO-STAGE"

for n in range(70, 72):
    TABLE_TOPIC[n] = "HORIZON-HLTH-2027-01-IND-01"

for n in range(72, 75):
    TABLE_TOPIC[n] = "HORIZON-HLTH-2027-02-IND-02-TWO-STAGE"


def clean(text):
    return re.sub(r"[ \t]+", " ", text.replace("\xa0", " ")).strip()


doc = Document(BOOKLET)

manifest = []

for table_number in range(6, 75):
    table = doc.tables[table_number - 1]

    label_1 = clean(table.cell(0, 0).text)
    label_2 = clean(table.cell(1, 0).text)

    if label_1 != "Research Group":
        raise RuntimeError(
            f"Table {table_number}: unexpected first label {label_1!r}"
        )

    if label_2 != "Expertise in relation to the topic":
        raise RuntimeError(
            f"Table {table_number}: unexpected second label {label_2!r}"
        )

    research_group = table.cell(0, 1).text.strip()
    expertise = table.cell(1, 1).text.strip()

    topic_code = TABLE_TOPIC[table_number]

    manifest.append(
        {
            "manifest_id": f"booklet-table-{table_number:02d}",
            "table_number": table_number,
            "topic_code": topic_code,
            "topic_id": TOPIC_IDS[topic_code],
            "research_group_raw": research_group,
            "expertise_raw": expertise,
            "source": "BOOKLET_Cluster 1_2027.docx",
            "graphics_included": False,
            "review_status": "raw-extracted",
        }
    )

if len(manifest) != 69:
    raise RuntimeError(
        f"Expected 69 Research Group tables, found {len(manifest)}"
    )

OUTPUT.write_text(
    json.dumps(
        manifest,
        ensure_ascii=False,
        indent=2,
    ),
    encoding="utf-8",
)

print("MANIFEST OK")
print("Research Group:", len(manifest))
print("Prima tabella:", manifest[0]["manifest_id"], manifest[0]["topic_id"])
print("Ultima tabella:", manifest[-1]["manifest_id"], manifest[-1]["topic_id"])
print("Asset grafici:", 0)
print("Output:", OUTPUT.name)