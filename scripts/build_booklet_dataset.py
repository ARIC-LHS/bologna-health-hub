#!/usr/bin/env python3

from __future__ import annotations

import argparse
import copy
import datetime as dt
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "_data"
RESEARCHERS_FILE = DATA_DIR / "researchers.yml"
CONTRIBUTIONS_FILE = DATA_DIR / "contributions.yml"
MANIFEST_FILE = ROOT / "booklet_contributions_manifest.json"
RESEARCHERS_DIR = ROOT / "researchers"
VALIDATOR = ROOT / "scripts" / "validate_data.py"

SOURCE_VERSION = "booklet-cluster1-2027-2026-11-17"
SOURCE_DATE = "2026-11-17"

VALID_INSTITUTIONS = {"unibo", "aoubo", "ior", "isnb"}


REMOVE_IDS = {
    "sabato-mellone",
    "francesca-ingravallo",
    "giulia-balboni",
    "marco-luppi",
    "marco-rinaldo-oggioni",
    "gaetano-la-manna",
    "paolo-boffetta",
    "katia-mattarozzi",
    "antonella-carbonaro",
    "caterina-garone",
    "emanuel-raschi",
    "mauro-comes-franchini",
    "elena-biagini",
    "lidia-strigari",
    "cristian-martignani",
    "giulia-fiorini",
    "valeria-corradetti",
}


ADD_RESEARCHERS = [
    ("luisa-sambati", "Luisa Sambati", "isnb"),
    ("gian-luca-pirazzoli", "Gian Luca Pirazzoli", "isnb"),
    ("silvia-cetrullo", "Silvia Cetrullo", "unibo"),
    ("simone-rampelli", "Simone Rampelli", "unibo"),
    ("federica-d-amico", "Federica D'Amico", "unibo"),
    ("tommaso-salzillo", "Tommaso Salzillo", "unibo"),
    ("beatrice-fraboni", "Beatrice Fraboni", "unibo"),
    ("francesco-nonino", "Francesco Nonino", "isnb"),
    ("patrizia-brigidi", "Patrizia Brigidi", "unibo"),
    ("silvia-turroni", "Silvia Turroni", "unibo"),
    ("alessandra-bendini", "Alessandra Bendini", "unibo"),
    ("matilde-tura", "Matilde Tura", "unibo"),
    ("carmela-fimognari", "Carmela Fimognari", "unibo"),
    ("cristina-angeloni", "Cristina Angeloni", "unibo"),
    ("francesca-fornari", "Francesca Fornari", "unibo"),
    ("elisabetta-lalumera", "Elisabetta Lalumera", "unibo"),
    ("marco-malaguti", "Marco Malaguti", "unibo"),
    ("anna-vittoria-mattioli", "Anna Vittoria Mattioli", "unibo"),
    ("valeria-righi", "Valeria Righi", "unibo"),
    ("eleonora-turrini", "Eleonora Turrini", "unibo"),
    ("barbara-monti", "Barbara Monti", "unibo"),
    ("francesca-massenzio", "Francesca Massenzio", "unibo"),
    ("laura-anderlucci", "Laura Anderlucci", "unibo"),
    ("giuliano-galimberti", "Giuliano Galimberti", "unibo"),
    ("saverio-ranciati", "Saverio Ranciati", "unibo"),
    ("edoardo-redivo", "Edoardo Redivo", "unibo"),
    ("silvia-bordoni", "Silvia Bordoni", "unibo"),
    ("cecilia-garofalo", "Cecilia Garofalo", "isnb"),
    ("alessandro-perin", "Alessandro Perin", "isnb"),
    ("isacco-gualandi", "Isacco Gualandi", "unibo"),
    ("erika-scavetta", "Erika Scavetta", "unibo"),
]


# Tabella del booklet -> researcher ID associati.
# Questa mappatura evita qualsiasi estrazione automatica ambigua dei nomi.
TABLE_RESEARCHERS = {
    6: ["maria-giulia-bacalini", "maria-chiara-pelleri"],
    7: ["luisa-sambati"],
    8: ["laura-mercolini"],
    9: ["milena-raffi"],
    10: ["gian-luca-pirazzoli"],

    11: ["claudia-zanna", "silvia-cetrullo"],
    12: ["marco-candela", "simone-rampelli", "federica-d-amico"],
    13: ["roberta-spadoni", "giulia-maesano"],
    14: ["ohad-zivan"],
    15: ["antonello-lorenzini"],
    16: ["cristiana-caliceti"],
    17: ["luca-mulazzani"],
    18: ["stefano-mattioli", "tommaso-salzillo", "beatrice-fraboni"],
    19: ["sabrina-valente"],
    20: ["francesco-nonino"],
    21: ["monica-forni", "patrizia-brigidi", "silvia-turroni"],
    22: ["milena-raffi"],
    23: [
        "tullia-gallina-toschi",
        "alessandra-bendini",
        "enrico-valli",
        "matilde-tura",
    ],
    24: [
        "carmela-fimognari",
        "cristina-angeloni",
        "francesca-fornari",
        "elisabetta-lalumera",
        "francesca-maffei",
        "marco-malaguti",
        "anna-vittoria-mattioli",
        "valeria-righi",
        "eleonora-turrini",
    ],
    25: ["andrea-bedini", "monica-baiula"],
    26: ["barbara-monti", "francesca-massenzio"],
    27: [
        "laura-anderlucci",
        "angela-montanari",
        "giuliano-galimberti",
        "saverio-ranciati",
        "edoardo-redivo",
    ],

    28: ["arrigo-francesco-giuseppe-cicero"],
    29: ["roberto-mandrioli"],
    30: ["olivia-manfrini"],
    31: ["federico-ravaioli"],

    32: ["barbara-monti", "francesca-massenzio"],
    33: ["barbara-zambelli", "luca-mazzei"],

    34: ["barbara-monti", "francesca-massenzio"],
    35: ["barbara-zambelli", "luca-mazzei"],

    36: ["barbara-monti", "francesca-massenzio"],
    37: ["barbara-zambelli", "luca-mazzei"],

    38: ["alessandra-bolotta"],
    39: ["barbara-monti", "francesca-massenzio"],
    40: ["barbara-zambelli", "luca-mazzei"],
    41: ["silvia-bordoni"],
    42: ["maddalena-giannella"],

    43: ["milena-raffi"],
    44: ["rita-stagni", "maria-cristina-bisi"],
    45: ["cristiana-caliceti", "antonello-lorenzini"],
    46: ["roberto-mandrioli"],
    47: ["arrigo-francesco-giuseppe-cicero"],

    48: ["cecilia-garofalo"],
    49: ["sara-borgomaneri"],
    50: ["rita-stagni", "maria-cristina-bisi"],
    51: ["luisa-sambati"],
    52: ["luca-palmerini"],

    53: ["marina-tadolini"],
    54: ["michele-protti"],
    55: ["barbara-monti", "francesca-massenzio"],
    56: ["alessandra-stancari", "maria-trapanese"],
    57: ["luciano-potena"],
    58: ["giorgia-comai"],

    59: ["marco-montevecchi"],
    60: ["cecilia-garofalo"],
    61: ["federico-ravaioli"],
    62: ["cristiana-caliceti", "antonello-lorenzini"],
    63: ["michele-protti"],
    64: ["rita-stagni", "maria-cristina-bisi"],
    65: ["sabrina-valente"],
    66: ["rita-fioresi"],
    67: ["igor-diemberger"],
    68: ["alessandro-perin"],
    69: ["luca-palmerini"],

    70: ["alessandra-tolomelli"],
    71: ["sabrina-valente"],

    72: [
        "isacco-gualandi",
        "erika-scavetta",
        "francesco-decataldo",
        "beatrice-fraboni",
    ],
    73: ["sabrina-valente"],
    74: ["laura-mercolini"],
}


def load_yaml(path: Path) -> list[dict]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))

    if not isinstance(data, list):
        raise RuntimeError(f"{path} non contiene una lista YAML.")

    return data


def load_manifest() -> list[dict]:
    data = json.loads(MANIFEST_FILE.read_text(encoding="utf-8"))

    if not isinstance(data, list):
        raise RuntimeError("Il manifest JSON non contiene una lista.")

    return data


def ensure_unique(records: list[dict], label: str) -> None:
    ids = [record.get("id") for record in records]

    if any(not value for value in ids):
        raise RuntimeError(f"{label}: uno o più record sono privi di id.")

    duplicates = sorted(
        identifier
        for identifier in set(ids)
        if ids.count(identifier) > 1
    )

    if duplicates:
        raise RuntimeError(f"{label}: ID duplicati: {duplicates}")


def atomic_write_yaml(path: Path, records: list[dict]) -> None:
    with tempfile.NamedTemporaryFile(
        mode="w",
        encoding="utf-8",
        dir=path.parent,
        prefix=f".{path.name}.",
        suffix=".tmp",
        delete=False,
    ) as handle:
        yaml.safe_dump(
            records,
            handle,
            allow_unicode=True,
            sort_keys=False,
            width=1000,
        )
        temporary = Path(handle.name)

    temporary.replace(path)


def new_researcher(
    researcher_id: str,
    name: str,
    institution_id: str,
) -> dict:
    if institution_id not in VALID_INSTITUTIONS:
        raise RuntimeError(
            f"Institution non valida per {name}: {institution_id}"
        )

    return {
        "id": researcher_id,
        "name": name,
        "institution_id": institution_id,
        "capability_ids": [],
        "infrastructure_ids": [],
        "network_ids": [],
        "tags": [],
        "contact_model": "aric-first",
        "public_email": "",
        "status": "expression-of-interest",
    }


def topic_short(topic_id: str) -> str:
    for value in (
        "stayhlth-01",
        "envhlth-02",
        "disease-01",
        "disease-05",
        "disease-06",
        "disease-07",
        "disease-08",
        "disease-10",
        "disease-14",
        "care-02",
        "tool-01",
        "ind-01",
        "ind-02",
    ):
        if value in topic_id:
            return value

    raise RuntimeError(f"Topic non riconosciuto: {topic_id}")


def clean_scientific_text(text: str) -> str:
    lines = []

    for raw_line in text.splitlines():
        line = re.sub(r"[ \t]+", " ", raw_line.replace("\xa0", " ")).strip()

        if not line:
            continue

        # Esclusione di eventuali didascalie grafiche.
        if re.match(
            r"^(figure|fig\.|figura|image|immagine)\s*\d*",
            line,
            flags=re.IGNORECASE,
        ):
            continue

        if line.startswith("image_"):
            continue

        lines.append(line)

    return "\n".join(lines).strip()


def contribution_title(
    researcher_name: str,
    topic_id: str,
    table_number: int,
) -> str:
    short = topic_short(topic_id).upper()
    return f"{researcher_name}: expertise for {short}"


def wrapper_text(researcher_id: str) -> str:
    return (
        "---\n"
        "layout: researcher\n"
        f"researcher_id: {researcher_id}\n"
        f"permalink: /researchers/{researcher_id}\n"
        "---\n"
    )


def run_validator() -> None:
    result = subprocess.run(
        [sys.executable, str(VALIDATOR)],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )

    if result.stdout:
        print(result.stdout.rstrip())

    if result.stderr:
        print(result.stderr.rstrip(), file=sys.stderr)

    if result.returncode != 0:
        raise RuntimeError(
            f"validate_data.py fallito con codice {result.returncode}"
        )


def build_dataset():
    current_researchers = load_yaml(RESEARCHERS_FILE)
    manifest = load_manifest()

    ensure_unique(current_researchers, "researchers.yml")

    if len(current_researchers) != 61:
        raise RuntimeError(
            f"Attesi 61 researcher iniziali, trovati "
            f"{len(current_researchers)}."
        )

    if len(manifest) != 69:
        raise RuntimeError(
            f"Attese 69 tabelle nel manifest, trovate {len(manifest)}."
        )

    expected_tables = set(range(6, 75))
    mapped_tables = set(TABLE_RESEARCHERS)

    if mapped_tables != expected_tables:
        missing = sorted(expected_tables - mapped_tables)
        extra = sorted(mapped_tables - expected_tables)

        raise RuntimeError(
            f"Mappatura tabelle incompleta. Mancanti={missing}; extra={extra}"
        )

    current_by_id = {
        record["id"]: copy.deepcopy(record)
        for record in current_researchers
    }

    missing_removals = sorted(REMOVE_IDS - set(current_by_id))

    if missing_removals:
        raise RuntimeError(
            f"Researcher da rimuovere non trovati: {missing_removals}"
        )

    final_by_id = {
        researcher_id: record
        for researcher_id, record in current_by_id.items()
        if researcher_id not in REMOVE_IDS
    }

    for researcher_id, name, institution_id in ADD_RESEARCHERS:
        if researcher_id in final_by_id:
            raise RuntimeError(
                f"ADD già presente nel dataset: {researcher_id}"
            )

        final_by_id[researcher_id] = new_researcher(
            researcher_id,
            name,
            institution_id,
        )

    final_researchers = list(final_by_id.values())

    if len(final_researchers) != 75:
        raise RuntimeError(
            f"Attesi 75 researcher finali, trovati {len(final_researchers)}."
        )

    ensure_unique(final_researchers, "nuovo researchers.yml")

    manifest_by_table = {
        record["table_number"]: record
        for record in manifest
    }

    if set(manifest_by_table) != expected_tables:
        raise RuntimeError(
            "Le tabelle del manifest non corrispondono a 6-74."
        )

    final_contributions = []

    for table_number in range(6, 75):
        manifest_record = manifest_by_table[table_number]
        researcher_ids = TABLE_RESEARCHERS[table_number]
        topic_id = manifest_record["topic_id"]

        scientific_text = clean_scientific_text(
            manifest_record["expertise_raw"]
        )

        if not scientific_text:
            raise RuntimeError(
                f"Testo scientifico vuoto nella tabella {table_number}."
            )

        for researcher_id in researcher_ids:
            if researcher_id not in final_by_id:
                raise RuntimeError(
                    f"Tabella {table_number}: researcher inesistente "
                    f"{researcher_id}"
                )

            researcher_name = final_by_id[researcher_id]["name"]
            short_topic = topic_short(topic_id)

            final_contributions.append(
                {
                    "id": f"{researcher_id}--{short_topic}",
                    "researcher_id": researcher_id,
                    "topic_id": topic_id,
                    "title": contribution_title(
                        researcher_name,
                        topic_id,
                        table_number,
                    ),
                    "contribution": scientific_text,
                    "assets": [],
                    "possible_contribution": scientific_text,
                    "contribution_types": [],
                    "capability_ids": [],
                    "infrastructure_ids": [],
                    "network_ids": [],
                    "evidence_basis": "direct-source",
                    "availability_status": "to-be-confirmed",
                    "source_version": SOURCE_VERSION,
                    "source_date": SOURCE_DATE,
                    "last_reviewed": SOURCE_DATE,
                }
            )

    # Una persona deve avere al massimo una contribution per topic.
    # Se lo stesso ID compare due volte, blocchiamo senza scegliere arbitrariamente.
    ensure_unique(final_contributions, "nuovo contributions.yml")

    final_ids = {record["id"] for record in final_researchers}

    orphans = sorted(
        record["id"]
        for record in final_contributions
        if record["researcher_id"] not in final_ids
    )

    if orphans:
        raise RuntimeError(f"Contribution orfane: {orphans}")

    topic_ids = {
        record["id"]
        for record in load_yaml(DATA_DIR / "topics.yml")
    }

    invalid_topics = sorted(
        {
            record["topic_id"]
            for record in final_contributions
            if record["topic_id"] not in topic_ids
        }
    )

    if invalid_topics:
        raise RuntimeError(f"Topic ID non validi: {invalid_topics}")

    return final_researchers, final_contributions


def create_backup() -> Path:
    timestamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    backup_dir = ROOT / ".migration-backups" / timestamp
    backup_dir.mkdir(parents=True, exist_ok=False)

    shutil.copy2(RESEARCHERS_FILE, backup_dir / "researchers.yml")
    shutil.copy2(CONTRIBUTIONS_FILE, backup_dir / "contributions.yml")

    wrappers_backup = backup_dir / "researchers"
    wrappers_backup.mkdir()

    for path in RESEARCHERS_DIR.glob("*.md"):
        shutil.copy2(path, wrappers_backup / path.name)

    return backup_dir


def restore_backup(backup_dir: Path) -> None:
    shutil.copy2(backup_dir / "researchers.yml", RESEARCHERS_FILE)
    shutil.copy2(backup_dir / "contributions.yml", CONTRIBUTIONS_FILE)

    for path in RESEARCHERS_DIR.glob("*.md"):
        path.unlink()

    for path in (backup_dir / "researchers").glob("*.md"):
        shutil.copy2(path, RESEARCHERS_DIR / path.name)


def apply_dataset(
    researchers: list[dict],
    contributions: list[dict],
) -> None:
    backup_dir = create_backup()

    print(f"Backup: {backup_dir.relative_to(ROOT)}")

    try:
        atomic_write_yaml(RESEARCHERS_FILE, researchers)
        atomic_write_yaml(CONTRIBUTIONS_FILE, contributions)

        final_ids = {record["id"] for record in researchers}

        RESEARCHERS_DIR.mkdir(parents=True, exist_ok=True)

        # Elimina solo wrapper che non appartengono più al dataset finale.
        for path in RESEARCHERS_DIR.glob("*.md"):
            if path.stem not in final_ids:
                path.unlink()

        # Crea o riallinea tutti i 75 wrapper.
        for researcher_id in sorted(final_ids):
            path = RESEARCHERS_DIR / f"{researcher_id}.md"
            path.write_text(
                wrapper_text(researcher_id),
                encoding="utf-8",
            )

        run_validator()

        written_researchers = load_yaml(RESEARCHERS_FILE)
        written_contributions = load_yaml(CONTRIBUTIONS_FILE)

        if len(written_researchers) != len(researchers):
            raise RuntimeError(
                "Il numero dei researcher scritti non coincide."
            )

        if len(written_contributions) != len(contributions):
            raise RuntimeError(
                "Il numero delle contribution scritte non coincide."
            )

    except Exception:
        print(
            "Errore durante l'applicazione. Ripristino automatico...",
            file=sys.stderr,
        )
        restore_backup(backup_dir)
        print("Backup ripristinato.", file=sys.stderr)
        raise


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Costruzione dataset Bologna Health Hub dal booklet 2027."
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Applica realmente il dataset. Senza questa opzione: dry-run.",
    )
    args = parser.parse_args()

    researchers, contributions = build_dataset()

    multiperson_tables = sum(
        len(TABLE_RESEARCHERS[number]) > 1
        for number in TABLE_RESEARCHERS
    )

    relations = sum(
        len(TABLE_RESEARCHERS[number])
        for number in TABLE_RESEARCHERS
    )

    print("=== BOOKLET DATASET DRY-RUN ===")
    print(f"Research Group:               {len(TABLE_RESEARCHERS)}")
    print(f"Tabelle multipersona reali:   {multiperson_tables}")
    print(f"Relazioni persona-topic:      {relations}")
    print(f"Researcher finali:            {len(researchers)}")
    print(f"Contribution finali:          {len(contributions)}")
    print("Asset grafici:                0")
    print("Testo scientifico:            integrale dal booklet")
    print("Immagini/didascalie:           escluse")

    if not args.apply:
        print()
        print("DRY-RUN completato. Nessun file modificato.")
        return 0

    apply_dataset(researchers, contributions)

    print()
    print("DATASET APPLICATO CORRETTAMENTE")
    print(f"Researcher:    {len(researchers)}")
    print(f"Contribution:  {len(contributions)}")
    print("Validator:     superato")
    print("Asset grafici: 0")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as error:
        print(f"ERRORE: {error}", file=sys.stderr)
        raise SystemExit(1)