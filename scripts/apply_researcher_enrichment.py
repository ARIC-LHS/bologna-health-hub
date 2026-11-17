from pathlib import Path
import yaml

RESEARCHERS = Path("_data/researchers.yml")
ENRICHMENT = Path("scripts/researcher_profile_enrichment.yml")

researchers = yaml.safe_load(RESEARCHERS.read_text(encoding="utf-8"))
enrichment = yaml.safe_load(ENRICHMENT.read_text(encoding="utf-8"))

enrichment_by_id = {x["id"]: x for x in enrichment}

if len(researchers) != 75:
    raise RuntimeError(f"Expected 75 researchers, found {len(researchers)}")

for researcher in researchers:
    data = enrichment_by_id.get(researcher["id"])

    if data is None:
        raise RuntimeError(f'Missing enrichment record: {researcher["id"]}')

    for field in (
        "public_email",
        "official_profile_url",
        "profile_url_type",
    ):
        value = data.get(field, "")
        if value:
            researcher[field] = value

RESEARCHERS.write_text(
    yaml.safe_dump(
        researchers,
        allow_unicode=True,
        sort_keys=False,
        width=1000,
    ),
    encoding="utf-8",
)

print("Researchers:", len(researchers))
print("Departments:", sum(bool(x.get("department")) for x in researchers))
print("Emails:", sum(bool(x.get("public_email")) for x in researchers))
print("Official URLs:", sum(bool(x.get("official_profile_url")) for x in researchers))
print("Individual URLs:", sum(x.get("profile_url_type") == "individual" for x in researchers))
print("Institution URLs:", sum(x.get("profile_url_type") == "institution" for x in researchers))