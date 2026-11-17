import yaml
from pathlib import Path

PATH = Path("_data/researchers.yml")

SURNAME_BY_ID = {
    "milena-raffi": "Raffi",
    "laura-mercolini": "Mercolini",
    "maria-giulia-bacalini": "Bacalini",
    "maria-chiara-pelleri": "Pelleri",
    "angela-montanari": "Montanari",
    "monica-baiula": "Baiula",
    "andrea-bedini": "Bedini",
    "sabrina-valente": "Valente",
    "claudia-zanna": "Zanna",
    "marco-candela": "Candela",
    "francesca-maffei": "Maffei",
    "monica-forni": "Forni",
    "stefano-mattioli": "Mattioli",
    "tullia-gallina-toschi": "Gallina Toschi",
    "roberta-spadoni": "Spadoni",
    "cristiana-caliceti": "Caliceti",
    "antonello-lorenzini": "Lorenzini",
    "enrico-valli": "Valli",
    "luca-mulazzani": "Mulazzani",
    "francesco-decataldo": "Decataldo",
    "giulia-maesano": "Maesano",
    "ohad-zivan": "Zivan",
    "barbara-zambelli": "Zambelli",
    "luca-mazzei": "Mazzei",
    "maddalena-giannella": "Giannella",
    "arrigo-francesco-giuseppe-cicero": "Cicero",
    "roberto-mandrioli": "Mandrioli",
    "rita-stagni": "Stagni",
    "maria-cristina-bisi": "Bisi",
    "igor-diemberger": "Diemberger",
    "olivia-manfrini": "Manfrini",
    "federico-ravaioli": "Ravaioli",
    "sara-borgomaneri": "Borgomaneri",
    "luca-palmerini": "Palmerini",
    "luciano-potena": "Potena",
    "giorgia-comai": "Comai",
    "marina-tadolini": "Tadolini",
    "michele-protti": "Protti",
    "rita-fioresi": "Fioresi",
    "alessandra-tolomelli": "Tolomelli",
    "alessandra-bolotta": "Bolotta",
    "alessandra-stancari": "Stancari",
    "maria-trapanese": "Trapanese",
    "marco-montevecchi": "Montevecchi",
    "luisa-sambati": "Sambati",
    "gian-luca-pirazzoli": "Pirazzoli",
    "silvia-cetrullo": "Cetrullo",
    "simone-rampelli": "Rampelli",
    "federica-d-amico": "D'Amico",
    "tommaso-salzillo": "Salzillo",
    "beatrice-fraboni": "Fraboni",
    "francesco-nonino": "Nonino",
    "patrizia-brigidi": "Brigidi",
    "silvia-turroni": "Turroni",
    "alessandra-bendini": "Bendini",
    "matilde-tura": "Tura",
    "carmela-fimognari": "Fimognari",
    "cristina-angeloni": "Angeloni",
    "francesca-fornari": "Fornari",
    "elisabetta-lalumera": "Lalumera",
    "marco-malaguti": "Malaguti",
    "anna-vittoria-mattioli": "Mattioli",
    "valeria-righi": "Righi",
    "eleonora-turrini": "Turrini",
    "barbara-monti": "Monti",
    "francesca-massenzio": "Massenzio",
    "laura-anderlucci": "Anderlucci",
    "giuliano-galimberti": "Galimberti",
    "saverio-ranciati": "Ranciati",
    "edoardo-redivo": "Redivo",
    "silvia-bordoni": "Bordoni",
    "cecilia-garofalo": "Garofalo",
    "alessandro-perin": "Perin",
    "isacco-gualandi": "Gualandi",
    "erika-scavetta": "Scavetta",
}

researchers = yaml.safe_load(PATH.read_text(encoding="utf-8"))

ids = {r["id"] for r in researchers}

missing = sorted(ids - set(SURNAME_BY_ID))
extra = sorted(set(SURNAME_BY_ID) - ids)

if missing or extra:
    raise RuntimeError(
        f"Mapping mismatch. Missing={missing}; Extra={extra}"
    )

for r in researchers:
    surname = SURNAME_BY_ID[r["id"]]
    r["surname"] = surname
    r["sort_name"] = f"{surname}, {r['name']}"

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
print("Surname fields:", sum(bool(r.get("surname")) for r in researchers))
print("Sort names:", sum(bool(r.get("sort_name")) for r in researchers))

print("\nFirst 15 by surname:")
for r in sorted(researchers, key=lambda x: x["sort_name"].casefold())[:15]:
    print(f'{r["sort_name"]} -> {r["name"]}')