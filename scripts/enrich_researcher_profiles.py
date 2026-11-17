from pathlib import Path
import yaml

RESEARCHERS = Path("_data/researchers.yml")
ENRICHMENT = Path("scripts/researcher_profile_enrichment.yml")

researchers = yaml.safe_load(RESEARCHERS.read_text(encoding="utf-8"))
enrichment = yaml.safe_load(ENRICHMENT.read_text(encoding="utf-8"))

DATA = {
    "michele-protti": {
        "department": "Department of Pharmacy and Biotechnology",
        "public_email": "michele.protti2@unibo.it",
        "official_profile_url": "https://www.unibo.it/sitoweb/michele.protti2/en",
        "profile_url_type": "individual",
    },
    "milena-raffi": {
        "department": "Department of Biomedical and Neuromotor Sciences",
        "public_email": "milena.raffi@unibo.it",
        "official_profile_url": "https://www.unibo.it/sitoweb/milena.raffi/en",
        "profile_url_type": "individual",
    },
    "monica-baiula": {
        "department": "Department of Pharmacy and Biotechnology",
        "public_email": "monica.baiula@unibo.it",
        "official_profile_url": "https://www.unibo.it/sitoweb/monica.baiula/en",
        "profile_url_type": "individual",
    },
    "monica-forni": {
        "department": "Department of Medical and Surgical Sciences",
        "public_email": "monica.forni@unibo.it",
        "official_profile_url": "https://www.unibo.it/sitoweb/monica.forni/en",
        "profile_url_type": "individual",
    },
    "ohad-zivan": {
        "department": "Department of Medical and Surgical Sciences",
        "public_email": "ohad.zivan@unibo.it",
        "official_profile_url": "https://www.unibo.it/sitoweb/ohad.zivan/en",
        "profile_url_type": "individual",
    },
    "olivia-manfrini": {
        "department": "Department of Medical and Surgical Sciences",
        "public_email": "olivia.manfrini@unibo.it",
        "official_profile_url": "https://www.unibo.it/sitoweb/olivia.manfrini/en",
        "profile_url_type": "individual",
    },
    "rita-fioresi": {
        "department": "Department of Pharmacy and Biotechnology",
        "public_email": "rita.fioresi@unibo.it",
        "official_profile_url": "https://www.unibo.it/sitoweb/rita.fioresi/en",
        "profile_url_type": "individual",
    },
    "rita-stagni": {
        "department": 'Department of Electrical, Electronic, and Information Engineering "Guglielmo Marconi"',
        "public_email": "rita.stagni@unibo.it",
        "official_profile_url": "https://www.unibo.it/sitoweb/rita.stagni/en",
        "profile_url_type": "individual",
    },
    "roberta-spadoni": {
        "department": "Department of Agricultural and Food Sciences",
        "public_email": "roberta.spadoni@unibo.it",
        "official_profile_url": "https://www.unibo.it/sitoweb/roberta.spadoni/en",
        "profile_url_type": "individual",
    },
    "roberto-mandrioli": {
        "department": "Department of Pharmacy and Biotechnology",
        "public_email": "roberto.mandrioli@unibo.it",
        "official_profile_url": "https://www.unibo.it/sitoweb/roberto.mandrioli/en",
        "profile_url_type": "individual",
    },
    "sabrina-valente": {
        "department": "Department of Medical and Surgical Sciences",
        "public_email": "sabrina.valente2@unibo.it",
        "official_profile_url": "https://www.unibo.it/sitoweb/sabrina.valente2/en",
        "profile_url_type": "individual",
    },
    "sara-borgomaneri": {
        "department": "Department of Psychology",
        "public_email": "sara.borgomaneri@unibo.it",
        "official_profile_url": "https://www.unibo.it/sitoweb/sara.borgomaneri/en",
        "profile_url_type": "individual",
    },
    "stefano-mattioli": {
        "department": "Department of Medical and Surgical Sciences",
        "public_email": "s.mattioli@unibo.it",
        "official_profile_url": "https://www.unibo.it/sitoweb/s.mattioli/en",
        "profile_url_type": "individual",
    },
    "tullia-gallina-toschi": {
        "department": "Department of Agricultural and Food Sciences",
        "public_email": "tullia.gallinatoschi@unibo.it",
        "official_profile_url": "https://www.unibo.it/sitoweb/tullia.gallinatoschi/en",
        "profile_url_type": "individual",
    },
}

by_id = {x["id"]: x for x in enrichment}

for rid, values in DATA.items():
    if rid not in by_id:
        raise RuntimeError(f"Researcher non presente: {rid}")
    by_id[rid].update(values)

ENRICHMENT.write_text(
    yaml.safe_dump(enrichment, allow_unicode=True, sort_keys=False, width=1000),
    encoding="utf-8",
)

print("=== ENRICHMENT MAPPING ===")
print("Researchers:", len(enrichment))
print("Department:", sum(bool(x["department"]) for x in enrichment))
print("Email:", sum(bool(x["public_email"]) for x in enrichment))
print("Individual profile:", sum(x["profile_url_type"] == "individual" for x in enrichment))
print("Institution URL:", sum(x["profile_url_type"] == "institution" for x in enrichment))
print("Still without profile URL:", sum(not x["official_profile_url"] for x in enrichment))