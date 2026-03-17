# Advies: Categorieën, Lessen & Implementatie

## Waar staan we nu?

We hebben 113 nieuwe suggesties in 19 thematische categorieën, plus 7 losse lessen. De bestaande app heeft ~580 suggesties in 6 cat-waarden (micro, opdracht, sessie, vastmaak, relationeel, dienstbaar) verdeeld over 3 sporen (A/B/C) met 5 thema's voor spoor C.

De vraag is: hoe past dit allemaal samen?

---

## Probleem 1: De V4-categorieën zijn geen app-categorieën

Mijn 19 thematische groepen (Zichtbare Macht, Inspectie, etc.) zijn *inhoudelijke* categorieën — ze beschrijven het *thema* van een suggestie. De app werkt met *vormcategorieën* — ze beschrijven het *type actie*:

| App-cat | Wat het is | Voorbeeld |
|---------|-----------|-----------|
| micro | Eén klein moment, snel | Berichtje sturen, hand in nek |
| opdracht | Tim moet iets doen | Klusje met deadline, regel voor de avond |
| vastmaak | Bondage als achtergrond | Polsboeien op de bank |
| sessie | Gestructureerd moment met begin/eind | Blinddoek + items + stappen |
| relationeel | Verbinding, warmte | Samen zitten, luisteren |
| dienstbaar | Bevestiging, zorgzaamheid | Compliment, aanraking |

**Elke V4-suggestie past al in één van deze zes.** We hoeven geen nieuwe cat-waarden te maken. Maar we moeten elke suggestie wél correct toewijzen. Voorbeelden:

- "Eet iets lekkers, water voor Tim" (#2) → **micro** (klein moment, geen items, face_to_face)
- "Tim masseert schouders, jij stuurt bij" (#102) → **opdracht** (Tim moet iets doen op jouw manier)
- "Enkelboeien terwijl Tim film kijkt" (#42) → **vastmaak** (bondage als achtergrond)
- "Kattennagels-sessie met blinddoek" (#72) → **sessie** (gestructureerd, items, stappen)
- "Na sessie: deken, thee, vasthouden" (#51) → **relationeel** (warmte, verbinding)
- "Tim zet thee, jij bepaalt alles" (#101) → **dienstbaar** (service)

De thematische groepering (Zichtbare Macht, Inspectie, etc.) is wél nuttig — maar als **tag/label**, niet als cat-waarde. Dit zou een nieuw veld kunnen zijn: `themaLabel`.

---

## Probleem 2: Drie soorten content die door elkaar lopen

In de 113 suggesties + 7 lessen zitten eigenlijk **drie fundamenteel verschillende dingen**:

### A. Suggesties (eenmalige acties)
"Doe dit vanavond." Één keer, klaar. Dit is wat de app nu al doet.
→ 90+ van de 113 zijn dit.

### B. Rituelen (terugkerende gewoontes)
"Doe dit elke avond / na elke sessie / elke ochtend."
→ #67 (halsband-ritueel), #68 (check-in), #69 (sleuteltje), #70 (na-moment), #71 (ochtend-thee)

Rituelen zijn géén suggesties. Een suggestie verschijnt één keer en is dan "gedaan". Een ritueel is een gewoonte die je opbouwt. De app moet rituelen anders behandelen:
- **Introductie**: één keer voorstellen als suggestie ("Probeer dit vanavond")
- **Herhaling**: daarna in een apart systeem ("Vaste gewoontes") met tracking
- **Groei**: na X keer succesvol → ritueel is "gevestigd", verdwijnt uit actieve suggesties

### C. Regels (doorlopende structuur)
"Dit geldt vanaf nu (tot het verandert)."
→ #108 (niet praten tenzij gevraagd), toestemming-structuur, tempo-controle

Regels zijn ook geen suggesties. Een regel is iets dat Lisanne *instelt* voor een avond, een week, of permanent. Voorbeelden:
- **Avondregel**: "Vanavond mag Tim niet op de bank" (eenmalig, vervalt na die avond)
- **Weekregel**: "Deze week vraagt Tim toestemming voor zijn telefoon" (vervalt na een week)
- **Vaste regel**: "Tim knielt als hij iets aangeeft" (permanent tot herzien)

De app heeft hier nu geen systeem voor. **Dit is een gap.** Mogelijke aanpak:
- Nieuw scherm: "Regels" naast de suggestiekaart
- Lisanne kan regels activeren/deactiveren
- Regels worden voorgesteld als suggestie ("Probeer deze week eens..."), bij succes kan Lisanne ze vastzetten

---

## Probleem 3: Lessen moeten suggesties ontsluiten

De 7 lessen die we hebben (Lichaamshouding als taal, Toestemming als structuur, etc.) zijn conceptueel. Maar eigenlijk heeft **elk thema** een les nodig. Niet alleen de 7 "pure les"-thema's, maar ook:

- Zichtbare Macht → Les: "Waarom ongelijkheid in comfort werkt"
- Inspectie → Les: "Bekijken als bezit — wat het voor Tim betekent"
- Contrast-momenten → Les: "De kracht van de overgang"
- Orgasmcontrole → Les: "Edging uitgelegd — waarom stoppen krachtiger is dan doorgaan"
- Aftercare → Les: "Waarom het moment erna net zo belangrijk is"
- ...etc.

**Voorstel: Elke themagroep krijgt één les die de bijbehorende suggesties ontsluit.**

Volgorde van lessen (= volgorde waarin thema's beschikbaar worden):

### Fase 1 — Basis (dag 0-7)
1. **Samen leven** (al bestaand in spoor A)
2. **Bevestiging** (al bestaand in spoor B)
3. **Zichtbare macht** — makkelijkste dynamiek-thema, geen items, geen protocol
4. **Lichaam als territorium** — aanraking als vanzelfsprekendheid

### Fase 2 — Controle (dag 7-21)
5. **Aandacht als machtsmiddel** — bewust kijken/negeren
6. **Service als devotie** — Tim doet iets, Lisanne stuurt
7. **Onthouding buiten seks** — kleine restricties
8. **Contrast-momenten** — zachtheid ↔ controle switches
9. **Onverwacht moment** — routine doorbreken
10. **Psychologisch spel** — spanning zonder spullen

### Fase 3 — Items & fysiek (dag 14-28)
11. **Bondage + normaal leven** — items als achtergrond
12. **Sensorisch** — temperatuur, textuur
13. **Inspectie** — bekijken als eigenaar
14. **Gekleed vs. bloot** — naaktheid als bewuste keuze
15. **Schrijven/markeren** — fysiek spoor achterlaten

### Fase 4 — Verdieping (dag 21-35+)
16. **Opbouw door de dag** — anticipatie over uren
17. **Intimiteit** — Lisanne leidt in bed
18. **Orgasmcontrole** — edging, denial
19. **Sessies** — gestructureerde scenes
20. **Aftercare** — het moment erna

### Dwarsliggers (geen fase, altijd beschikbaar zodra relevant)
- **Rituelen** — worden per stuk ontsloten wanneer het thema past
- **Regels** — worden voorgesteld als de bijbehorende les is gelezen

---

## Probleem 4: Lessen voor bestaande categorieën

De bestaande pool (~580 suggesties) heeft voor de meeste categorieën al een "Goed om te weten"-toggle met uitleg. Maar er zijn geen echte lessen die het *waarom* uitleggen. De nieuwe lessen zouden ook moeten gelden voor bestaande suggesties. Bijvoorbeeld:

De les "Aftercare" ontsluit niet alleen V4-suggesties #51-58, maar voegt ook automatisch aftercare-tips toe aan ALLE bestaande sessie/vastmaak-suggesties. Na elke sessie-suggestie zou een reminder kunnen verschijnen: "Denk aan het na-moment: deken, thee, even samen."

---

## Probleem 5: Wat nog ontbreekt

### A. Escalatiepaden
Binnen elk thema ontbreken niveaus. "Zichtbare Macht" heeft nu 12 suggesties die allemaal even zwaar zijn. Maar er is een natuurlijke opbouw:
- Niveau 1: Fris voor jou, water voor Tim (passief verschil)
- Niveau 2: "Op de grond" (actief commando)
- Niveau 3: Afstandsbediening afpakken (actieve inbreuk)

Elke themagroep zou 3 niveaus moeten hebben die mappen op zwaarte 1/2/3.

### B. "Wat als het niet werkt"
Voor elk thema: wat doet Lisanne als Tim negatief reageert? Of als zij zich er niet comfortabel bij voelt? De app mist deescalatie-paden per thema.

### C. Lisanne's comfort-mapping
Niet elk thema past bij Lisanne. Sommige zijn makkelijker (Zichtbare Macht — past bij haar karakter), sommige moeilijker (Inspectie — vereist bewuste dominantie). De app zou per thema een "past dit bij mij?"-check kunnen doen.

### D. Tim's werkpunten per thema
Tim heeft werkpunten (continu, niet roterend). Per thema zijn er specifieke signalen die Tim moet leren:
- Zichtbare Macht → Tim moet leren niet te onderhandelen
- Inspectie → Tim moet stil blijven staan
- Orgasmcontrole → Tim moet communiceren wanneer hij dichtbij is

### E. Combinatie-suggesties
De kracht zit vaak in combinaties van thema's. Inspectie + Gekleed vs. Bloot. Contrast-momenten + Bondage. Schrijven/markeren + De dag erna. De app zou thema's kunnen combineren in gevorderde suggesties.

---

## Implementatie-aanpak

### Stap 1: Review (nu)
Tim reviewt de 113 suggesties + 7 lessen in de review-tool. Resultaat: ja/nee/aanpassen per item.

### Stap 2: Conversie (na review)
Goedgekeurde suggesties omzetten naar app-format:
- `cat` toewijzen (micro/opdracht/sessie/vastmaak/relationeel/dienstbaar)
- `spoor` toewijzen (A/B/C)
- `thema` toewijzen (1-5 voor spoor C)
- `zwaarte` toewijzen (1-3)
- `vibe` toewijzen
- `actieType` toewijzen
- `items` toewijzen
- `minDagen` toewijzen
- Optioneel nieuw veld: `themaLabel` (bijv. "zichtbare_macht", "inspectie")

### Stap 3: Lessen schrijven
Per themagroep één les schrijven in het inzichten-format. Inclusief: wat het is, waarom het werkt, wat Tim eraan heeft, en een concreet eerste voorbeeld.

### Stap 4: Rituelen & regels — nieuw systeem
Klein nieuw feature bouwen:
- **Rituelen**: lijst van terugkerende gewoontes, met "vandaag gedaan?" toggle
- **Regels**: lijst van actieve regels, met aan/uit per avond/week/permanent
- Beide worden geïntroduceerd via het suggestiesysteem maar leven daarna apart

### Stap 5: Integratie
- Suggesties toevoegen aan SUGGESTIE_POOL
- Lessen toevoegen aan inzichtensysteem
- Aftercare-reminders koppelen aan bestaande sessie/vastmaak-suggesties
- Progressie-gates instellen: les gelezen → bijbehorende suggesties worden beschikbaar

### Stap 6: Testen
- Controleer dat progressie werkt (geen zware suggesties op dag 1)
- Controleer Milou-timing op alle suggesties
- Controleer Lisanne-filter op alle suggesties
- Check overlap met bestaande pool

---

## Samenvatting

| Wat | Aantal | Status |
|-----|--------|--------|
| Suggesties (eenmalige acties) | ~100 | In review-tool, wacht op Tim's review |
| Rituelen | 5-10 | Concept klaar, app-systeem moet gebouwd |
| Regels | 5-10 | Concept klaar, app-systeem moet gebouwd |
| Lessen (thema-specifiek) | ~20 | 7 geschreven, 13 nog te schrijven |
| Escalatiepaden per thema | 19 thema's × 3 niveaus | Nog niet uitgewerkt |
| Deescalatie/comfort-checks | 19 thema's | Nog niet uitgewerkt |
| Combinatie-suggesties | ~10-15 | Nog niet geschreven |
| Aftercare-reminders bij bestaande pool | ~40 sessie/vastmaak | Nog niet gekoppeld |

De kern: **suggesties zijn het makkelijkste stuk. Het echte werk zit in het systeem eromheen — lessen, rituelen, regels, progressie, en de verbinding daartussen.**
