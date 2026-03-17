# Diepe Analyse: Samenhang Sprankelend Systeem

## Drie leersystemen die naast elkaar leven

Het systeem heeft drie manieren waarop Lisanne leert — maar ze praten niet met elkaar.

### Systeem A: De 22 Grote Lessen (LESSEN_INHOUD)
Wat het doet: Lisanne opent een les, leest theorie, krijgt een oefening.
Gate: getLesGate() — fase + vorige les gelezen + 3 dagen wachttijd.
Progressie: Lineair (1→2→3→...→22), gekoppeld aan fase 0-4.

### Systeem B: De 18 Mini-Lesjes (MINI_LESJES)
Wat het doet: Korte inzichten ("Goed om te weten") die verschijnen bij suggesties.
Gate: kiesMiniLesje() — fase ≥ 1, energie ≠ laag, advanced gate voor les13-18.
Progressie: Lineair op volgorde, maar apart van de grote lessen.
Koppeling: Heeft `bijSuggestie` veld (welke categorieën passen erbij) — maar dit wordt alleen gebruikt als trigger, niet als filter in de suggestiemotor.

### Systeem C: De 41 Kern-Suggesties (KERN_LP1-LP6)
Wat het doet: Concrete oefeningen in 6 leerpaden met stap-progressie.
Gate: _bepaalActiefLeerpad() — 3 "ja" + 1 eigenInitiatief per pad.
Progressie: LP1→LP2→...→LP6, met stap 1-4 binnen elk pad. Gekoppeld aan fase 0-6.

---

## GAT 1: Twee aparte fase-systemen (KRITIEK)

**Het probleem:**
- LESSEN_INHOUD gebruikt fase 0-4 (via getEffectieveLesjesFase)
- KERN_LP leerpaden gebruiken fase 0-6 (via _bepaalActiefLeerpad → s4.fase)
- getEffectieveLesjesFase() leest s4.fase, dus de leerpaden STUREN de lessen
- Maar de lessen sturen NIET de leerpaden

**Wat dit betekent:**
Lisanne kan leerpad 3 bereiken (en suggesties krijgen over fysiek contact, items) zonder ooit Les 7 (vastzitten als rust) of Les 10 (nazorg) gelezen te hebben. De suggesties lopen vooruit op de theorie.

**Omgekeerd**: Lisanne kan Les 7 gelezen hebben maar nog op leerpad 1 zitten als ze weinig suggesties accepteert. De theorie loopt vooruit op de praktijk.

**Risico:** Lisanne krijgt een suggestie "Maak Tim's polsen vast" (KERN_LP4) zonder ooit geleerd te hebben over tiksignalen, nazorg, of veiligheid (Les 7/10).

---

## GAT 2: De 22 lessen en de suggesties kennen elkaar niet (KRITIEK)

**Het probleem:**
Geen enkele suggestie in SUGGESTIE_POOL heeft een veld dat verwijst naar een les.
Geen enkele les heeft een veld dat verwijst naar specifieke suggesties.

**Wat dit betekent:**

| Les | Leert | Suggesties die dit oefenen? |
|-----|-------|---------------------------|
| Les 1: Richting geven | Keuzes maken zonder overleg | ✅ KERN_LP1/LP2 hebben dit (maar weten niet dat ze bij les 1 horen) |
| Les 3: Aanraking | Bewuste aanraking: nek, schouder, nagels | ✅ KERN_LP3 doet dit (maar geen link) |
| Les 5: Stilte en wachten | Anticipatie opbouwen | ⚠️ ANTICIPATIE_POOL bestaat, maar is niet gekoppeld aan les 5 |
| Les 7: Vastzitten als rust | 4 stijlen vastmaken, tiksignalen, nazorg | ⚠️ vz01-vz16 pool bestaat, KERN_LP4 heeft ib02/ib05, maar geen verwijzing naar les 7 |
| Les 8: Zintuigen | Blinddoek + sensory play | ⚠️ KERN_LP5 np01/np03 doen dit, maar weten niet van les 8 |
| Les 9: Seks op jouw voorwaarden | Pace control, "niet nu", stoppen | ❌ Geen suggesties die dit expliciet oefenen |
| Les 10: Het moment erna | Nazorg: deken, stilte, water | ❌ naMoment velden bestaan op sommige suggesties, maar geen les-link |
| Les 12: Wat jij hieraan hebt | Lisanne's eigen plezier ontdekken | ❌ Geen suggesties die dit begeleiden |
| Les 13: Service | "Ik wil dat je X doet" vs "X moet gedaan worden" | ⚠️ SERVICE suggesties bestaan, maar geen progressie van les→suggestie |
| Les 14: Speelsheid | Plagen, humor, luchtig | ⚠️ HUMOR_POOL bestaat, maar geen link naar les 14 |
| Les 15: Impact | Tikken, kaarswas, bijten | ❌ Geen impact-suggesties in de pool |
| Les 17: Regels | Dagelijkse/wekelijkse regels instellen | ❌ Geen suggesties die helpen regels op te zetten |
| Les 19: Orgasmecontrole | Edging, onthouding, toestemmingsregel | ❌ Geen suggesties (bewust — maar er is ook geen brug) |
| Les 20: Sessie-opbouw | Opening→kern→afsluiting structuur | ⚠️ KERN_LP6 raakt hieraan, maar kent les 20 niet |
| Les 21: Psychologisch spel | Onzekerheid, wachten, stilte als macht | ❌ Geen suggesties |

**De ❌ lessen zijn "dode eilanden"** — Lisanne leest ze, maar het systeem helpt haar niet om ze te oefenen.

---

## GAT 3: De mini-lesjes zijn ontkoppeld van beide systemen (BELANGRIJK)

**Het probleem:**
Mini-lesjes (les01-les18) hebben een `bijSuggestie` veld dat categorieën noemt (micro, opdracht, sessie, etc.), maar kiesMiniLesje() kiest een mini-les op basis van volgorde, NIET op basis van welke suggestie vandaag wordt getoond.

**Voorbeeld:**
- Lisanne krijgt vandaag suggestie ks03 ("Wijs Tim een plek op de bank aan") → cat:'micro'
- Mini-lesje van vandaag is les08 (nazorg, bijSuggestie:['sessie','vastmaak','micro'])
- les08 gaat over nazorg na intense momenten
- De suggestie gaat over iemand een bankplek aanwijzen
- Het lesje past niet bij de suggestie

**Wat zou moeten:** Het mini-lesje zou moeten matchen met de categorie/het thema van de dagelijkse suggestie.

---

## GAT 4: Les-inhoud vs. Leerpad-inhoud: dubbel werk of gaten (BELANGRIJK)

De 22 grote lessen en de 6 leerpaden dekken deels dezelfde onderwerpen, maar met andere progressie:

| Leerpad | Dekking | Overlappende les(sen) | Gat |
|---------|---------|----------------------|-----|
| LP0: Gewoon Samen | Warmte, verbinding | — | Geen les nodig |
| LP1: Kleine Signalen | Toon zetten, micro-keuzes | Les 1, 2 | ✅ Goed aligned |
| LP2: Jij Kiest | Beslissingen nemen, programma plannen | Les 1, 2, 4 | ✅ Redelijk aligned |
| LP3: Dichterbij | Bewust aanraken, nabijheid | Les 3 | ✅ Aligned |
| LP4: Iets Beginnen | Collar, polsboeien, rituelen | Les 4, 7, 16 | ⚠️ Items VOOR veiligheidslessen |
| LP5: Iets Nieuws | Blinddoek, temperatuur, langere sessies | Les 8, 9 | ⚠️ Sensory VOOR seks-les |
| LP6: Jouw Avond | Volledige regie, choreografie | Les 20 | ⚠️ Geen link naar les 20 |

**Het gevaar bij LP4:** Lisanne bereikt LP4 (items introduceren) na ~35 dagen actief gebruik. Maar Les 7 (vastzitten als rust — inclusief tiksignalen en nazorg) wordt pas ontgrendeld bij fase 2, wat kan SAMENVALLEN met LP4 maar niet gegarandeerd eerder is. Ze zou polsboeien kunnen gebruiken zonder ooit over tiksignalen geleerd te hebben.

---

## GAT 5: Feedback van suggesties voedt de lessen niet (GEMIDDELD)

**Het probleem:**
Als Lisanne 5x "fijn" zegt bij aanrakingssuggesties (LP3), wordt dat geteld voor leerpad-progressie. Maar het systeem weet niet:
- Dat Les 3 (Aanraking) relevant zou zijn om aan te bieden
- Dat ze klaar is voor Les 8 (Zintuigen) omdat ze aanraking al goed vindt

De lessen worden aangeboden op basis van fase + volgorde + 3 dagen wachttijd.
De suggesties worden gekozen op basis van leerpad + energie + dagtype.
Er is geen brug.

---

## GAT 6: Lisanne→Tim signalen beïnvloeden de suggestiemotor niet (GEMIDDELD)

**Het probleem:**
Lisanne kan drie signalen sturen: vanavond_niet, was_fijn, wil_proberen.
- vanavond_niet zet vrijeDag_[datum] → blokkeert avondsuggesties ✅
- was_fijn → wordt opgeslagen maar NIET gelezen door kiesSuggestie()
- wil_proberen → wordt opgeslagen maar NIET gelezen door kiesSuggestie()

**Wat zou moeten:**
- "was_fijn" zou de herhaling-dagtype moeten boosten (herhaal wat werkte)
- "wil_proberen" zou de nieuwheid-dagtype moeten boosten (iets nieuws aanbieden)

---

## GAT 7: Tim's warmte/discipline niet in suggestiemotor (GEMIDDELD)

Tim logt dagelijks discipline, warmte-momenten, etc. De suggestiemotor (kiesSuggestie) leest dit NIET.

**Wat dit betekent:**
- Tim kan een slechte dag hebben (lage warmte) maar Lisanne krijgt een intense suggestie
- Tim kan juist heel ontvankelijk zijn maar Lisanne krijgt een "gewoon jullie" dagtype

De suggestiemotor kent maar één richting: Lisanne's input → suggestie. Tim's staat is onzichtbaar.

---

## GAT 8: Geen terugkoppeling van "eerste keer" ervaringen (LAAG)

Het systeem detecteert "eerste keer een categorie" en vraagt dan altijd om feedback. Maar die feedback wordt niet expliciet bewaard als "eerste keer succes/falen" per categorie.

**Voorbeeld:** Lisanne maakt Tim voor het eerst vast. Ze zegt "fijn." Dit wordt gelogd als generieke "fijn" ervaring. Er is geen markering "eerste vastmaak-ervaring was positief" die later invloed heeft op welke vastmaak-suggesties verschijnen.

---

## GAT 9: Lessen 15, 19, 21 hebben geen oefenpad (LAAG maar structureel)

Deze drie lessen zijn puur theorie zonder corresponderende suggesties:
- **Les 15 (Impact):** Geen impact-suggesties in enige pool. Lisanne leest over tikken/bijten maar krijgt nooit een concrete suggestie om het te proberen.
- **Les 19 (Orgasmecontrole):** Bewust geen suggesties (te intiem voor een app), maar er is ook geen "zacht eerste stap" suggestie.
- **Les 21 (Psychologisch spel):** Geen suggesties voor onzekerheid/wachten/inspectie.

---

## GAT 10: Mini-lesje thema's matchen niet met leerpad-progressie (LAAG)

Mini-lesjes hebben een `thema` veld (gekozen-worden, duidelijkheid, stilte, nazorg, etc.).
Leerpaden hebben een `naam` (Kleine Signalen, Jij Kiest, Dichterbij, etc.).

Er is geen mapping. Mini-les05 (thema:'wachten') zou perfect passen bij LP5 (Iets Nieuws), maar het systeem weet dat niet.

---

## Samenvattend: Wat werkt WEL goed

Voordat ik alleen gaten noem — dit werkt uitstekend:

1. **De 4-sporen scheduler** — intelligent, veilig, adaptief. Echt goed ontworpen.
2. **Beschermingslagen** — teveel/ruzie/warmte-pauze/energie. Meerdere vangnetten.
3. **LP progressie-logica** — 3 ja + 1 eigenInitiatief is een slim criterium.
4. **Dagtype-variatie** — geen twee dezelfde dagen. Goed ritme.
5. **De vz01-vz16 pool** — 4 stijlen vastmaken zonder spullen, mooi uitgewerkt.
6. **Les-inhoud kwaliteit** — de 22 lessen zijn inhoudelijk sterk en progressief.
7. **Anti-clustering** — voorkomt oververzadiging.

---

## Prioriteiten

### MOET GEFIXT (systeem-integriteit)

**#1 — Veiligheidsbrug les 7 ↔ LP4**
LP4 introduceert polsboeien/items. Les 7 leert tiksignalen en nazorg.
Fix: LP4 suggesties (ib01, ib02, ib05) mogen pas verschijnen als Les 7 is gelezen.

**#2 — Mini-lesje matchen op suggestie-categorie**
kiesMiniLesje() zou `sug.cat` moeten checken tegen `les.bijSuggestie[]` en bij een match voorrang geven aan dat lesje.

### ZOU MOETEN

**#3 — Lisanne-signalen in suggestiemotor**
"was_fijn" → boost herhaling. "wil_proberen" → boost nieuwheid/focus.

**#4 — Les-gelezen als gate voor gerelateerde suggesties**
Een `naLes` veld op suggesties die pas verschijnen nadat de bijbehorende les is gelezen.
Bijv: vastmaak-suggesties → naLes:7. Sensory suggesties → naLes:8.

**#5 — Practice-suggesties voor "dode eiland" lessen**
Minstens 2-3 oefensuggesties voor: Les 9 (seks-regie), Les 15 (impact), Les 17 (regels), Les 21 (psychologisch spel).

### KAN BETER

**#6 — Tim's warmte als soft-gate**
getWarmte() als extra input in kiesSuggestie: lage warmte → zachter, hoge warmte → meer ruimte.

**#7 — Eerste-keer tracking per categorie**
Bewaar expliciet: { cat:'vastmaak', eersteDatum:'...', eersteErvaring:'fijn' }. Gebruik dit voor "eerste keer" framing in UI.

**#8 — Mini-lesje thema ↔ leerpad mapping**
Maak een mapping zodat mini-lesjes met thema:'wachten' voorrang krijgen als het actieve leerpad LP5 is.
