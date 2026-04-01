# Sprankelend Souffleur — Herzien Plan

## Uitgangspunt

Lisanne heeft ja gezegd. Ze wil het proberen, inclusief de app. Maar ze heeft heel duidelijk nodig:
- **Concreet**: wat moet ik doen, waarom op die manier, hoe ervaart Tim het
- **Intentie**: niet afvinken, maar begrijpen waarom je iets doet
- **Bevestiging**: dat proberen genoeg is, dat het niet perfect hoeft
- **Eigen tempo**: geen weekschema, geen druk, geen schuldgevoel

De kern van de uitdaging is niet het fysieke (bondage/doe-dingen zijn relatief makkelijk) maar het psychologische: dingen doen met INTENTIE, vanuit jezelf, omdat je weet wat het betekent.

---

## Wat de app al heeft (en wat we hergebruiken)

### Data & Pools (blijven intact, worden verrijkt)
| Systeem | Locatie | Status |
|---------|---------|--------|
| SUGGESTIE_POOL (~130+ suggesties) | lijn 1154 | ✅ Hergebruiken — al gecategoriseerd per spoor/vibe/zwaarte |
| SPULLEN_DB (items + beschrijvingen) | lijn 734 | ✅ Hergebruiken |
| BONDAGE_MATRIX (setup-recepten) | lijn 1056 | ✅ Hergebruiken |
| RITUEEL_POOL (8 rituelen) | lijn 1997 | ✅ Hergebruiken |
| REGEL_POOL (7 regels) | lijn 2041 | ✅ Hergebruiken |
| SPOOR_MAP (A/B/C tracks) | lijn 2083 | ✅ Hergebruiken |
| INZICHT_POOL (inzichten per thema/niveau) | lijn 2305 | ✅ Hergebruiken |
| TIM_WERKPUNTEN + SABOTEURS | lijn 2456 | ✅ Hergebruiken (Tim-view) |
| TIM_HOUDING_POOL + GEBAAR_POOL | lijn 2519 | ✅ Hergebruiken (Tim-view) |
| GEWOON_JULLIE (22+ suggesties) | lijn 3886 | ✅ Hergebruiken — belangrijk als basis |
| ONTDEKKING_SUGGESTIES (22 suggesties) | lijn 3804 | ✅ Hergebruiken |
| LICHAMELIJKE_ACTIVITEITEN | lijn 4069 | ✅ Hergebruiken |
| REFLECTIE_VRAGEN | lijn 3748 | ✅ Hergebruiken |
| ONTDEKKING_VRAGEN | lijn 3776 | ✅ Hergebruiken |

### Bestaande systemen (blijven intact, worden verfijnd)
| Systeem | Wat het doet | Aanpassing nodig? |
|---------|-------------|-------------------|
| getTimErvaartTekst() | "Wat Tim ervaart" per suggestie | ✅ Uitbreiden — meer per-suggestie teksten (Tim schrijft deze) |
| getEffectieveLesjesFase() | Fase-detectie met fallbacks | ✅ Hergebruiken ongewijzigd |
| kiesMiniLesje() | Dagelijks mini-lesje selectie | ✅ Hergebruiken — past al bij suggestie + leerpad |
| Opdrachttaal per fase | Toon verschuift per fase (0-4) | ✅ Hergebruiken — precies wat we willen |
| MINI_LESJES (35 lesjes) | Korte uitleg bij suggesties | ✅ Hergebruiken + eventueel uitbreiden |
| Milou-detectie (isMilouAanwezig) | Context-aware suggesties | ✅ Hergebruiken ongewijzigd |
| Suggestie-guards | Recency, blokkade, thema-gate | ✅ Hergebruiken ongewijzigd |
| Ervaring-logging | fijn/neutraal/teveel tracking | ✅ Hergebruiken — basis voor check-in |
| Lisanne's "Geef me een idee" | Sfeer-gebaseerde suggestie | ✅ Hergebruiken — eigenaarschap |
| Pauze-modus | Rustige dag zonder schuldgevoel | ✅ Hergebruiken — cruciaal |
| Agenda (Lisanne + Tim view) | Week-planning met dagdelen | ✅ Hergebruiken — planning-tool |
| Notificaties | Ochtend-check, override alerts | ✅ Hergebruiken |
| Onboarding (7 stappen + prefs) | Energie, ritueel, vertrouwensniveau | 🔧 Verfijnen — meer nadruk op "dit is geen test" |
| Sync-code systeem | Cross-device sync | ✅ Hergebruiken ongewijzigd |
| View-selectie (pin) | Lisanne vs Tim view | ✅ Hergebruiken ongewijzigd |

### Bestaande lessen (31 stuks — HERSCHRIJVEN)
| Systeem | Status |
|---------|--------|
| LESSEN_INHOUD (31 scroll-lessen) | 🔧 Herschrijven in nieuwe toon |
| Block types (scene/inzicht/noot/voorbeeld/kernboodschap/keuze/probeer) | ✅ Hergebruiken |
| LESOEFENINGEN (93 oefeningen, 3 per les) | 🔧 Herschrijven — concreter, meer "wat Tim ervaart" |

---

## Feedback-aanpassingen (01-04-2026)

Na review zijn deze 5 punten toegevoegd:

1. **Niet alleen Tim-centrisch**: Naast `watJeKuntMerken` (Tim's ervaring) ook een `watJijMerkt` veld — wat Lisanne zelf kan voelen. "Dit mag onwennig zijn", "je hoeft hier niks bij te voelen", "misschien merk je dat het even gek voelt". Voorkomt dat het een performance voor Tim wordt.
2. **`waaromZo` max 2 zinnen**: Geen mini-essays. Concreet, kort.
3. **Reflectie = emoji-tap eerst**: Na een ervaring eerst 😊/😐/😬 tap, dan optioneel tekstveld "Wil je iets kwijt?". Lichter dan meteen een tekstveld.
4. **"Dit is genoeg voor vandaag"**: Na elke uitgevoerde actie een korte bevestiging tonen.
5. **Anti-perfectionisme overal**: Niet alleen in onboarding maar ook in suggestie-kaarten, lessen, en terugkeer-berichten. Kleine zinnen als "dit hoeft niet goed", "proberen is genoeg", "dit mag onwennig zijn".

---

## Wat er NIEUW moet komen

### 1. "Wat Tim ervaart" — Prominenter en persoonlijker

**Probleem**: getTimErvaartTekst() bestaat, maar veel suggesties hebben geen `watJeKuntMerken` en vallen terug op generieke categorie-teksten.

**Oplossing**:
- Tim schrijft per suggestie (of per cluster van vergelijkbare suggesties) een persoonlijke tekst
- Formaat: 2-3 zinnen, eerste persoon, concreet
- Voorbeeld: *"Als je zegt 'nu' zonder het te vragen, stopt alles in mijn hoofd. Niet omdat ik moet gehoorzamen — maar omdat jij kiest. Dat is het mooiste gevoel dat ik ken."*
- Deze teksten worden ALTIJD getoond bij een suggestie (niet optioneel, niet achter een toggle)
- Implementatie: vul `watJeKuntMerken` aan op bestaande suggesties

**Plus: `watJijMerkt`** — wat Lisanne zelf kan voelen/merken. Niet wat ze MOET voelen, maar wat ze KAN merken. Voorkomt dat het een performance voor Tim wordt en maakt het ook haar ontdekking.
- Voorbeeld: *"Dit kan even gek voelen. Dat is normaal. Je hoeft er niks bij te voelen — kijk gewoon wat er gebeurt."*

**Bestaand systeem**: TIM_ERVAART object met categorieën → uitbreiden met meer categorieën en specifiekere teksten.

### 2. "Waarom op die manier" — Intentie-laag per suggestie

**Probleem**: Suggesties zeggen WAT je moet doen, maar niet WAAROM het op die manier moet.

**Oplossing**:
- Nieuw veld per suggestie: `waaromZo` (string)
- Wordt getoond onder de suggestie-tekst, visueel onderscheiden (bijv. italic, andere kleur)
- Voorbeeld bij "Zeg tegen Tim: keuken opruimen. Nu.":
  *"Niet vragen, maar zeggen. Het verschil is alles. Als je het vraagt, geef je Tim de keuze. Als je het zegt, neem jij de beslissing. En dat is precies wat hij nodig heeft — niet de taak, maar dat jij beslist."*
- Dit is de INTENTIE-laag: niet wat, maar waarom zo

**Implementatie**: nieuw veld `waaromZo` op suggestie-objecten.

### 3. Check-in momenten (reflectie na ervaring)

**Probleem**: De app logt ervaringen (fijn/neutraal/teveel) maar Lisanne schrijft nooit hoe het voelde.

**Oplossing**:
- Na het loggen van een ervaring: eerst emoji-tap (😊 fijn / 😐 oké / 😬 ongemakkelijk)
- Daarna optioneel: "Wil je iets kwijt?" tekstveld
- Na afronding: "Dit is al genoeg voor vandaag." bevestiging
- Bestaande REFLECTIE_VRAGEN gebruiken als starters/prompts
- Lisanne's reflecties worden opgeslagen en kunnen later teruggelezen worden
- Tim kan deze NIET zien (privacy) — tenzij Lisanne ze deelt

**Bestaand systeem**: logErvaring() + REFLECTIE_VRAGEN → uitbreiden met optioneel tekstveld en opslag.

### 4. Win-momenten / Vieringen

**Probleem**: De app registreert vooruitgang maar viert het niet.

**Oplossing**:
- Milestone-detectie: eerste suggestie gedaan, 5 suggesties, eerste "fijn", eerste keer zelf een idee gekozen, 7 dagen actief, etc.
- Viering: korte, warme boodschap + eventueel confetti-animatie
- Toon: "Hé, je hebt net je eerste week gehad. Weet je dat Tim gisteren als een blij kind rondliep? Dat heb jij gedaan."
- Geen score, geen punten, geen ranking — alleen erkenning

**Bestaand systeem**: eersteKeerCat tracking bestaat al → uitbreiden met milestone-berichten.

### 5. Toon-revisie: Supportive friend, niet teacher

**Probleem**: Huidige lessen zijn soms te "lesachtig" — alsof Lisanne examen moet doen.

**Oplossing**:
- Lessen herschrijven in de toon van een vriendin die het zelf ook doet
- Niet: "In een FLR is het belangrijk dat..." → Wel: "Weet je wat ik ontdekte? Als je gewoon zegt wat je wilt in plaats van te vragen..."
- Kernregel: elke les moet voelen als een gesprek, niet als een college
- Bestaande block types (scene/inzicht/noot/voorbeeld) blijven — de inhoud verandert

**Scope**: Dit is de grootste klus. 31 lessen × herziening. Doen we stap voor stap.

### 6. "Dit is geen test" — Schuld-vrije framing

**Probleem**: Lisanne kan het gevoel krijgen dat ze faalt als ze een dag overslaat.

**Oplossing**:
- Pauze-modus bestaat al → prominenter maken
- Na 3 dagen inactiviteit: zachte boodschap "Hé, geen stress. De app wacht op jou."
- Geen streak-counter, geen "je bent X dagen actief"
- Bij terugkeer na pauze: "Fijn dat je er weer bent" — niet "Je was X dagen weg"
- Energie-check bij openen: "Hoe voel je je vandaag?" → bij "laag" automatisch zachtere suggesties

**Bestaand systeem**: isPauzeModus(), energieVandaag, rustigeDag → combineren tot graceful re-entry.

### 7. Onboarding verfijning

**Probleem**: Huidige onboarding is goed maar kan meer nadruk leggen op veiligheid.

**Oplossing**:
- Scherm toevoegen: "Dit is geen to-do list. Er is geen goed of fout. Het enige wat telt is dat je het probeert."
- Tim's brief (onboarding stap 5) updaten met de positieve toon van het gesprek
- Preference-stappen (energie/ritueel/vertrouwen) blijven

**Bestaand systeem**: ONBOARDING_LISANNE array → teksten aanpassen.

---

## Wat we NIET doen

- ❌ Weekschema's of verplichte frequentie
- ❌ Emma & Lucas verhaallijnen (waar komen die vandaan?)
- ❌ Scores, punten, rankings
- ❌ Skill-based progressie ("je bent nu level 3")
- ❌ Verplichte reflecties
- ❌ "Je hebt X dagen niet geopend" guilt-trips
- ❌ Vergelijking met anderen
- ❌ getLesGate() aanpassen (laat voorlopig zo)

---

## Prioriteit en volgorde

### Fase 1: Quick wins (kunnen nu)
1. **`waaromZo` veld toevoegen** aan de 20 meest-gebruikte suggesties
2. **`watJeKuntMerken` uitbreiden** — Tim schrijft persoonlijke teksten
3. **Win-momenten** toevoegen (milestone-berichten bij bestaande tracking)
4. **Schuld-vrije terugkeer-berichten** na inactiviteit
5. **Onboarding teksten** verfijnen

### Fase 2: Check-in systeem
6. **Reflectie-tekstveld** na ervaring-logging
7. **Reflectie-opslag** en terugkijk-functie voor Lisanne

### Fase 3: Lessen herschrijven
8. **Les 1-5 herschrijven** in nieuwe toon (test met Lisanne)
9. **Les 6-15 herschrijven**
10. **Les 16-31 herschrijven**

### Fase 4: Verfijning
11. **Oefeningen herschrijven** (concreter, meer "wat Tim ervaart")
12. **MINI_LESJES uitbreiden** met intentie-focus
13. **PWA-optimalisatie** voor server deployment

---

## Technische aanpak

Alles blijft in het bestaande `index.html` single-file formaat. Geen agents, handmatig met Edit tool.

Per wijziging:
1. Edit de data (suggesties, lessen, teksten)
2. Edit de render-functies waar nodig
3. Syntax check: `sed -n '/<script>/,/<\/script>/p' index.html | sed '1d;$d' > /tmp/check.js && node --check /tmp/check.js`
4. Commit

De app wordt uiteindelijk een PWA op een server (Tim regelt hosting). De bestaande PWA manifest (lijn 15, base64) en service worker setup zijn al aanwezig.

---

## Samenvatting in één zin

De app heeft al 80% van wat nodig is. De revisie draait om drie dingen: **intentie toevoegen aan elke suggestie** (waaromZo), **Tim's persoonlijke ervaring prominenter maken** (watJeKuntMerken), en **de toon verschuiven van leraar naar vriendin** (lessen herschrijven).
