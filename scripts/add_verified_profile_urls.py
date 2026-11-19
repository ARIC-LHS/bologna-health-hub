from pathlib import Path
import yaml

PATH = Path("_data/researchers.yml")

URLS = {
    # UNIBO - personal profiles
    "andrea-bedini": "https://www.unibo.it/sitoweb/andrea.bedini/en",
    "angela-montanari": "https://www.unibo.it/sitoweb/angela.montanari/en",
    "antonello-lorenzini": "https://www.unibo.it/sitoweb/antonello.lorenzini/en",
    "arrigo-francesco-giuseppe-cicero": "https://www.unibo.it/sitoweb/arrigo.cicero/en",
    "barbara-monti": "https://www.unibo.it/sitoweb/b.monti/en",
    "barbara-zambelli": "https://www.unibo.it/sitoweb/barbara.zambelli/en",
    "claudia-zanna": "https://www.unibo.it/sitoweb/claudia.zanna/en",
    "giorgia-comai": "https://www.unibo.it/sitoweb/giorgia.comai2/en",
    "cristiana-caliceti": "https://www.unibo.it/sitoweb/cristiana.caliceti/en",
    "enrico-valli": "https://www.unibo.it/sitoweb/enrico.valli4/en",
    "federico-ravaioli": "https://www.unibo.it/sitoweb/f.ravaioli/en",
    "francesca-maffei": "https://www.unibo.it/sitoweb/francesca.maffei/en",
    "francesca-massenzio": "https://www.unibo.it/sitoweb/francesca.massenzio2/en",
    "francesco-decataldo": "https://www.unibo.it/sitoweb/francesco.decataldo2/en",
    "giulia-maesano": "https://www.unibo.it/sitoweb/giulia.maesano2/en",
    "igor-diemberger": "https://www.unibo.it/sitoweb/igor.diemberger/en",
    "laura-mercolini": "https://www.unibo.it/sitoweb/laura.mercolini/en",
    "luca-mazzei": "https://www.unibo.it/sitoweb/luca.mazzei2/en",
    "luca-mulazzani": "https://www.unibo.it/sitoweb/luca.mulazzani/en",
    "luca-palmerini": "https://www.unibo.it/sitoweb/luca.palmerini/en",
    "luciano-potena": "https://www.unibo.it/sitoweb/luciano.potena2/en",
    "maddalena-giannella": "https://www.unibo.it/sitoweb/maddalena.giannella/en",
    "marco-candela": "https://www.unibo.it/sitoweb/marco.candela/en",
    "marco-montevecchi": "https://www.unibo.it/sitoweb/m.montevecchi/en",
    "maria-chiara-pelleri": "https://www.unibo.it/sitoweb/mariachiara.pelleri2/en",
    "maria-cristina-bisi": "https://www.unibo.it/sitoweb/mariacristina.bisi/en",
    "maria-giulia-bacalini": "https://www.unibo.it/sitoweb/mariagiuli.bacalini2/en",
    "marina-tadolini": "https://www.unibo.it/sitoweb/marina.tadolini/en",
    "michele-protti": "https://www.unibo.it/sitoweb/michele.protti2/en",
    "milena-raffi": "https://www.unibo.it/sitoweb/milena.raffi/en",
    "monica-baiula": "https://www.unibo.it/sitoweb/monica.baiula/en",
    "monica-forni": "https://www.unibo.it/sitoweb/monica.forni/en",
    "ohad-zivan": "https://www.unibo.it/sitoweb/ohad.zivan/en",
    "olivia-manfrini": "https://www.unibo.it/sitoweb/olivia.manfrini/en",
    "rita-fioresi": "https://www.unibo.it/sitoweb/rita.fioresi/en",
    "rita-stagni": "https://www.unibo.it/sitoweb/rita.stagni/en",
    "roberta-spadoni": "https://www.unibo.it/sitoweb/roberta.spadoni/en",
    "roberto-mandrioli": "https://www.unibo.it/sitoweb/roberto.mandrioli/en",
    "sabrina-valente": "https://www.unibo.it/sitoweb/sabrina.valente2/en",
    "sara-borgomaneri": "https://www.unibo.it/sitoweb/sara.borgomaneri/en",
    "stefano-mattioli": "https://www.unibo.it/sitoweb/s.mattioli/en",
    "tullia-gallina-toschi": "https://www.unibo.it/sitoweb/tullia.gallinatoschi/en",
    "alessandra-tolomelli": "https://www.unibo.it/sitoweb/alessandra.tolomelli/en",
    "laura-anderlucci": "https://www.unibo.it/sitoweb/laura.anderlucci/en",
    "cristina-angeloni": "https://www.unibo.it/sitoweb/cristina.angeloni/en",
    "alessandra-bendini": "https://www.unibo.it/sitoweb/alessandra.bendini/en",
    "silvia-bordoni": "https://www.unibo.it/sitoweb/silvia.bordoni/en",
    "patrizia-brigidi": "https://www.unibo.it/sitoweb/patrizia.brigidi/en",
    "silvia-cetrullo": "https://www.unibo.it/sitoweb/silvia.cetrullo/en",
    "federica-d-amico": "https://www.unibo.it/sitoweb/federica.damico8/en",
    "carmela-fimognari": "https://www.unibo.it/sitoweb/carmela.fimognari/en",
    "francesca-fornari": "https://www.unibo.it/sitoweb/francesca.fornari2/en",
    "beatrice-fraboni": "https://www.unibo.it/sitoweb/beatrice.fraboni/en",
    "giuliano-galimberti": "https://www.unibo.it/sitoweb/giuliano.galimberti/en",
    "isacco-gualandi": "https://www.unibo.it/sitoweb/isacco.gualandi2/en",
    "elisabetta-lalumera": "https://www.unibo.it/sitoweb/elisabetta.lalumera/en",
    "marco-malaguti": "https://www.unibo.it/sitoweb/marco.malaguti/en",
    "anna-vittoria-mattioli": "https://www.unibo.it/sitoweb/annavittoria.mattioli/en",
    "simone-rampelli": "https://www.unibo.it/sitoweb/simone.rampelli/en",
    "saverio-ranciati": "https://www.unibo.it/sitoweb/saverio.ranciati2/en",
    "edoardo-redivo": "https://www.unibo.it/sitoweb/edoardo.redivo/en",
    "valeria-righi": "https://www.unibo.it/sitoweb/valeria.righi2/en",
    "tommaso-salzillo": "https://www.unibo.it/sitoweb/tommaso.salzillo/en",
    "erika-scavetta": "https://www.unibo.it/sitoweb/erika.scavetta2/en",
    "matilde-tura": "https://www.unibo.it/sitoweb/matilde.tura2/en",
    "eleonora-turrini": "https://www.unibo.it/sitoweb/eleonora.turrini/en",
    "silvia-turroni": "https://www.unibo.it/sitoweb/silvia.turroni/en",

    # AOUBO - verified individual pages
    "alessandra-stancari":
        "https://www.aosp.bo.it/il-policlinico/professionisti/alessandra-stancari",
    "maria-trapanese":
        "https://www.aosp.bo.it/il-policlinico/professionisti/maria-trapanese",
}

INSTITUTION_URLS = {
    "alessandra-bolotta": "https://www.aosp.bo.it/",
    "cecilia-garofalo": "https://www.isnb.it/",
    "francesco-nonino": "https://www.ausl.bologna.it/",
    "alessandro-perin": "https://www.isnb.it/",
    "gian-luca-pirazzoli": "https://www.ausl.bologna.it/",
    "luisa-sambati": "https://www.isnb.it/",
}

researchers = yaml.safe_load(PATH.read_text(encoding="utf-8"))
by_id = {r["id"]: r for r in researchers}

for rid, url in URLS.items():
    if rid not in by_id:
        continue
    by_id[rid]["official_profile_url"] = url
    by_id[rid]["profile_url_type"] = "individual"

for rid, url in INSTITUTION_URLS.items():
    if rid not in by_id:
        continue
    if not by_id[rid].get("official_profile_url"):
        by_id[rid]["official_profile_url"] = url
        by_id[rid]["profile_url_type"] = "institution"

PATH.write_text(
    yaml.safe_dump(
        researchers,
        allow_unicode=True,
        sort_keys=False,
        width=1000,
    ),
    encoding="utf-8",
)

with_url = [r for r in researchers if r.get("official_profile_url")]
missing = [r for r in researchers if not r.get("official_profile_url")]

print("=== VERIFIED PROFILE URL ENRICHMENT ===")
print("Researchers:", len(researchers))
print("With department:", sum(bool(r.get("department")) for r in researchers))
print("With official URL:", len(with_url))
print(
    "Individual profiles:",
    sum(r.get("profile_url_type") == "individual" for r in researchers)
)
print(
    "Institutional fallback:",
    sum(r.get("profile_url_type") == "institution" for r in researchers)
)
print("Still missing:", len(missing))

print("\nSTILL MISSING:")
for r in sorted(missing, key=lambda x: x["sort_name"].casefold()):
    print(f'{r["id"]:42} | {r["name"]}')