from pathlib import Path
import yaml

PATH = Path("_data/researchers.yml")

DEPARTMENT_BY_ID = {
    # DIBINEM
    "maria-giulia-bacalini": "Department of Biomedical and Neuromotor Sciences",
    "maria-chiara-pelleri": "Department of Biomedical and Neuromotor Sciences",
    "milena-raffi": "Department of Biomedical and Neuromotor Sciences",
    "claudia-zanna": "Department of Biomedical and Neuromotor Sciences",
    "silvia-cetrullo": "Department of Biomedical and Neuromotor Sciences",
    "antonello-lorenzini": "Department of Biomedical and Neuromotor Sciences",
    "cristiana-caliceti": "Department of Biomedical and Neuromotor Sciences",
    "marco-montevecchi": "Department of Biomedical and Neuromotor Sciences · University Dental Clinic, Periodontology Unit",

    # FABIT
    "laura-mercolini": "Department of Pharmacy and Biotechnology",
    "marco-candela": "Department of Pharmacy and Biotechnology",
    "simone-rampelli": "Department of Pharmacy and Biotechnology",
    "federica-d-amico": "Department of Pharmacy and Biotechnology",
    "patrizia-brigidi": "Department of Pharmacy and Biotechnology",
    "silvia-turroni": "Department of Pharmacy and Biotechnology",
    "andrea-bedini": "Department of Pharmacy and Biotechnology",
    "monica-baiula": "Department of Pharmacy and Biotechnology",
    "barbara-monti": "Department of Pharmacy and Biotechnology",
    "francesca-massenzio": "Department of Pharmacy and Biotechnology",
    "barbara-zambelli": "Department of Pharmacy and Biotechnology",
    "luca-mazzei": "Department of Pharmacy and Biotechnology",
    "roberto-mandrioli": "Department of Pharmacy and Biotechnology",
    "michele-protti": "Department of Pharmacy and Biotechnology",
    "rita-fioresi": "Department of Pharmacy and Biotechnology",

    # DIMEC
    "ohad-zivan": "Department of Medical and Surgical Sciences",
    "stefano-mattioli": "Department of Medical and Surgical Sciences",
    "sabrina-valente": "Department of Medical and Surgical Sciences",
    "monica-forni": "Department of Medical and Surgical Sciences",
    "arrigo-francesco-giuseppe-cicero": "Department of Medical and Surgical Sciences",
    "olivia-manfrini": "Department of Medical and Surgical Sciences",
    "federico-ravaioli": "Department of Medical and Surgical Sciences",
    "maddalena-giannella": "Department of Medical and Surgical Sciences",
    "marina-tadolini": "Department of Medical and Surgical Sciences",
    "luciano-potena": "Department of Medical and Surgical Sciences",
    "giorgia-comai": "Department of Medical and Surgical Sciences",
    "igor-diemberger": "Department of Medical and Surgical Sciences",

    # DISTAL
    "roberta-spadoni": "Department of Agricultural and Food Sciences",
    "giulia-maesano": "Department of Agricultural and Food Sciences",
    "luca-mulazzani": "Department of Agricultural and Food Sciences",
    "tullia-gallina-toschi": "Department of Agricultural and Food Sciences",
    "alessandra-bendini": "Department of Agricultural and Food Sciences",
    "enrico-valli": "Department of Agricultural and Food Sciences",
    "matilde-tura": "Department of Agricultural and Food Sciences",

    # QUVI
    "carmela-fimognari": "Department for Life Quality Studies",
    "cristina-angeloni": "Department for Life Quality Studies",
    "francesca-fornari": "Department for Life Quality Studies",
    "elisabetta-lalumera": "Department for Life Quality Studies",
    "francesca-maffei": "Department for Life Quality Studies",
    "marco-malaguti": "Department for Life Quality Studies",
    "anna-vittoria-mattioli": "Department for Life Quality Studies",
    "valeria-righi": "Department for Life Quality Studies",
    "eleonora-turrini": "Department for Life Quality Studies",

    # STAT
    "laura-anderlucci": 'Department of Statistical Sciences "Paolo Fortunati"',
    "angela-montanari": 'Department of Statistical Sciences "Paolo Fortunati"',
    "giuliano-galimberti": 'Department of Statistical Sciences "Paolo Fortunati"',
    "saverio-ranciati": 'Department of Statistical Sciences "Paolo Fortunati"',
    "edoardo-redivo": 'Department of Statistical Sciences "Paolo Fortunati"',

    # DEI
    "rita-stagni": 'Department of Electrical, Electronic and Information Engineering "Guglielmo Marconi"',
    "maria-cristina-bisi": 'Department of Electrical, Electronic and Information Engineering "Guglielmo Marconi"',
    "luca-palmerini": 'Department of Electrical, Electronic and Information Engineering "Guglielmo Marconi"',

    # CHIMIND
    "tommaso-salzillo": 'Department of Industrial Chemistry "Toso Montanari"',
    "silvia-bordoni": 'Department of Industrial Chemistry "Toso Montanari"',
    "isacco-gualandi": 'Department of Industrial Chemistry "Toso Montanari"',

    # DIFA
    "beatrice-fraboni": 'Department of Physics and Astronomy "Augusto Righi"',

    # Chemistry
    "alessandra-tolomelli": 'Department of Chemistry "Giacomo Ciamician"',

    # Psychology
    "sara-borgomaneri": 'Department of Psychology "Renzo Canestrari"',

    # T72: Scavetta and Decataldo
    "erika-scavetta": 'Department of Industrial Chemistry "Toso Montanari"',
    "francesco-decataldo": "Department of Medical and Surgical Sciences",

    # ISNB
    "luisa-sambati": "U.O.C. Neurology Clinic · Metropolitan Neurological Network (NEUROMET)",
    "gian-luca-pirazzoli": "IRCCS Istituto delle Scienze Neurologiche di Bologna",
    "francesco-nonino": "Epidemiology and Statistics Unit · IRCCS Istituto delle Scienze Neurologiche di Bologna",
    "cecilia-garofalo": "Bologna Neuroscience Biobank (BNB) · IRCCS Istituto delle Scienze Neurologiche di Bologna",
    "alessandro-perin": "Neurosurgery Unit · IRCCS Istituto delle Scienze Neurologiche di Bologna",

    # AOUBO
    "alessandra-bolotta": "IRCCS Azienda Ospedaliero-Universitaria di Bologna",
    "alessandra-stancari": "Clinical Pharmacy, Production and Research Unit · IRCCS Azienda Ospedaliero-Universitaria di Bologna",
    "maria-trapanese": "Clinical Pharmacy, Production and Research Unit · IRCCS Azienda Ospedaliero-Universitaria di Bologna",
}

researchers = yaml.safe_load(PATH.read_text(encoding="utf-8"))

ids = {r["id"] for r in researchers}
mapped = set(DEPARTMENT_BY_ID)

missing = sorted(ids - mapped)
extra = sorted(mapped - ids)

if missing or extra:
    raise RuntimeError(
        f"Department mapping mismatch. Missing={missing}; Extra={extra}"
    )

for r in researchers:
    r["department"] = DEPARTMENT_BY_ID[r["id"]]

PATH.write_text(
    yaml.safe_dump(
        researchers,
        allow_unicode=True,
        sort_keys=False,
        width=1000,
    ),
    encoding="utf-8",
)

print("Researchers:", len(researchers))
print("Departments:", sum(bool(r.get("department")) for r in researchers))
print("Missing departments:", sum(not r.get("department") for r in researchers))