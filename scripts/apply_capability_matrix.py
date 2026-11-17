#!/usr/bin/env python3

import argparse
import json
import shutil
import subprocess
import sys
from collections import Counter
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
MATRIX_FILE = ROOT / "scripts" / "capability_matrix.yml"
MANIFEST_FILE = ROOT / "booklet_contributions_manifest.json"

CAPABILITIES_FILE = ROOT / "_data" / "capabilities.yml"
CONTRIBUTIONS_FILE = ROOT / "_data" / "contributions.yml"

BACKUP_DIR = ROOT / ".capability-backup"


def load_yaml(path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def save_yaml(path, data):
    path.write_text(
        yaml.safe_dump(
            data,
            allow_unicode=True,
            sort_keys=False,
            width=1000,
        ),
        encoding="utf-8",
    )


def topic_short(topic_id):
    values = [
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
    ]

    for value in values:
        if value in topic_id:
            return value

    raise RuntimeError(f"Topic non riconosciuto: {topic_id}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    matrix = load_yaml(MATRIX_FILE)

    manifest = json.loads(
        MANIFEST_FILE.read_text(encoding="utf-8")
    )

    contributions = load_yaml(CONTRIBUTIONS_FILE)

    capabilities = matrix["capabilities"]
    groups = matrix["groups"]

    # ---------------------------------------------------------
    # VALIDAZIONE MATRICE
    # ---------------------------------------------------------

    if len(capabilities) != 20:
        raise RuntimeError(
            f"Attese 20 capability, trovate {len(capabilities)}"
        )

    expected_tables = set(range(6, 75))
    actual_tables = set(groups)

    if actual_tables != expected_tables:
        missing = sorted(expected_tables - actual_tables)
        extra = sorted(actual_tables - expected_tables)

        raise RuntimeError(
            f"Matrice incompleta. Missing={missing}; Extra={extra}"
        )

    valid_capability_ids = set(capabilities)

    for table_number, rule in groups.items():

        requested = [
            rule["primary"],
            *(rule.get("secondary") or []),
        ]

        if not requested:
            raise RuntimeError(
                f"T{table_number}: nessuna capability"
            )

        if len(requested) > 3:
            raise RuntimeError(
                f"T{table_number}: più di 3 capability"
            )

        invalid = set(requested) - valid_capability_ids

        if invalid:
            raise RuntimeError(
                f"T{table_number}: capability non valide {invalid}"
            )

    # ---------------------------------------------------------
    #    # ---------------------------------------------------------
    # COSTRUZIONE TABLE -> CONTRIBUTIONS
    # ---------------------------------------------------------

    from build_booklet_dataset import TABLE_RESEARCHERS

    contribution_by_key = {
        (c["researcher_id"], c["topic_id"]): c
        for c in contributions
    }

    assignments = {}
    missing_contributions = []

    manifest_by_table = {
        item["table_number"]: item
        for item in manifest
    }

    for table_number in range(6, 75):

        item = manifest_by_table[table_number]
        topic_id = item["topic_id"]

        group_rule = groups[table_number]

        capability_ids = [
            group_rule["primary"],
            *(group_rule.get("secondary") or []),
        ]

        capability_ids = list(dict.fromkeys(capability_ids))

        researcher_ids = TABLE_RESEARCHERS[table_number]

        for researcher_id in researcher_ids:

            key = (researcher_id, topic_id)

            contribution = contribution_by_key.get(key)

            if contribution is None:
                missing_contributions.append(
                    f"T{table_number}: {researcher_id} -> {topic_id}"
                )
                continue

            contribution_id = contribution["id"]

            if contribution_id in assignments:
                raise RuntimeError(
                    f"{contribution_id} associata a più tabelle"
                )

            assignments[contribution_id] = capability_ids

    if missing_contributions:
        raise RuntimeError(
            "Contribution mancanti:\n"
            + "\n".join(missing_contributions)
        )

    # ---------------------------------------------------------
    # COPERTURA
    # ---------------------------------------------------------

    contribution_ids = {c["id"] for c in contributions}
    assigned_ids = set(assignments)

    unassigned = sorted(contribution_ids - assigned_ids)
    unknown = sorted(assigned_ids - contribution_ids)

    if unknown:
        raise RuntimeError(
            f"Assignment verso contribution inesistenti: {unknown}"
        )

    if unassigned:
        raise RuntimeError(
            f"Contribution senza capability: {unassigned}"
        )

    if len(contributions) != 113:
        raise RuntimeError(
            f"Attese 113 contribution, trovate {len(contributions)}"
        )

    # ---------------------------------------------------------
    # STATISTICHE DRY-RUN
    # ---------------------------------------------------------

    counts = Counter()

    for capability_ids in assignments.values():
        for capability_id in capability_ids:
            counts[capability_id] += 1

    print("=== CAPABILITY MATRIX AUDIT ===")
    print("Matrix version:", matrix["version"])
    print("Research Groups:", len(groups))
    print("Capabilities:", len(capabilities))
    print("Contributions:", len(contributions))
    print("Assigned contributions:", len(assignments))
    print("Unassigned contributions:", len(unassigned))
    print()

    print("=== DISTRIBUTION ===")

    for capability_id, metadata in capabilities.items():
        print(
            f"{capability_id:42} "
            f"{counts[capability_id]:3}  "
            f"{metadata['name']}"
        )

    print()

    if not args.apply:
        print("DRY-RUN PASS")
        print("Nessun file modificato.")
        return

    BACKUP_DIR.mkdir(exist_ok=True)

    shutil.copy2(
        CAPABILITIES_FILE,
        BACKUP_DIR / "capabilities.yml",
    )
    shutil.copy2(
        CONTRIBUTIONS_FILE,
        BACKUP_DIR / "contributions.yml",
    )

    new_capabilities = [
        {
            "id": capability_id,
            "name": metadata["name"],
        }
        for capability_id, metadata in capabilities.items()
    ]

    for contribution in contributions:
        contribution["capability_ids"] = assignments[
            contribution["id"]
        ]

    save_yaml(CAPABILITIES_FILE, new_capabilities)
    save_yaml(CONTRIBUTIONS_FILE, contributions)

    result = subprocess.run(
        [sys.executable, "scripts/generate_pages.py"],
        cwd=ROOT,
    )

    if result.returncode != 0:
        raise RuntimeError("generate_pages.py fallito")

    result = subprocess.run(
        [sys.executable, "scripts/validate_data.py"],
        cwd=ROOT,
    )

    if result.returncode != 0:
        shutil.copy2(
            BACKUP_DIR / "capabilities.yml",
            CAPABILITIES_FILE,
        )
        shutil.copy2(
            BACKUP_DIR / "contributions.yml",
            CONTRIBUTIONS_FILE,
        )
        raise RuntimeError(
            "Validazione fallita. Backup ripristinato."
        )

    print()
    print("CAPABILITY MATRIX APPLIED")
    print("Capabilities:", len(new_capabilities))
    print("Contributions:", len(contributions))
    print("Unclassified: 0")
    print("Validation: PASS")


if __name__ == "__main__":
    main()
