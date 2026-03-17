# Sprankelend Souffleur — Systeemoverzicht (v5, definitief ontwerp)

---

## 1. Wat is de app?

Een PWA die Lisanne begeleidt in het opbouwen van een FLR/BDSM-dynamiek met Tim. De app neemt Tim's rol als "uitlegger/starter" over.

**Technisch:** Eén HTML-bestand, lokaal, localStorage, instant laden, volledig offline.

### Kernprincipes
1. **Fluistering, niet systeem.** Als Lisanne de complexiteit voelt, is het te veel.
2. **Lisanne hoeft het niet zelf te willen** — maar ruimte als ze het wél leuk vindt.
3. **Relatie-app met dynamiek als onderdeel.**
4. **Tim doet het werk.** Lisanne wordt alleen belast met wat per se van haar moet komen.
5. **Lisanne zoekt zelf niks op.** Info actief brengen op het juiste moment.
6. **"Normaal goed" is ook goed.** Niet alles hoeft bijzonder, spannend of leerzaam.
7. **De app mag erkennen en normaliseren, maar niet psychologisch verklaren.** Relatie-app, geen therapie-app.

---

## 2. Wie zijn Tim en Lisanne?

- Bijna 14 jaar samen, dochter Milou
- Appartement, 60m², geen boven/beneden
- Milou: ma-do school, vrijdag thuis, weekend thuis. Na ~19:00 naar bed
- Koken niet zelf (behalve ontbijt)
- Tim loopt na 19:00 in z'n blote kont rond
- Lisanne: niet assertief, responsief, zoent niet (nooit gedaan), raakt Tim aan (bank) maar niet seksueel/spontaan
- Tim mist bevestiging. BDSM overheerst gedachten omdat bevestiging/intimiteit ontbreekt
- Huishouden: Lisanne doet het meeste, Tim heeft duidelijke communicatie nodig
- Kernmechanisme: mededelen werkt, vragen niet

---

## 3. App-architectuur

### Lisanne's view — Drie tabs
- **Vandaag**: Spotlight (één ding), moment-blok
- **Plannen**: Hiërarchisch opgebouwd:
  - BOVENAAN: 2 grote acties ("Iets zeggen" / "Iets kiezen")
  - DAARONDER: Tim's dag, Afspraken, Terugkijken
- **Gids**: Gefilterd per thema. Info actief bij suggestie, Gids voor wie meer wil weten

### Tim's view — Per dag maximaal:
- 1 hoofdtaak
- 1 correctie/steun-signaal
- 1 optionele reflectie
- Onderhoudstaken (wens, registraties, markeren) gebatcht: wekelijks, niet dagelijks

### Geen dubbele acties
Vandaag = reageren. Plannen = actie. Gids = info.

---

## 4. Het Leerpad — drie sporen

Naast elkaar, niet na elkaar:

### Spoor A: "Samen leven"
Fundament. Loopt altijd door. Dates, humor, verrassingen, complimenten, speelse straffen (thema 2+). Tim doet ook dingen voor Lisanne — balans bewaken.

### Spoor B: "Bevestiging en intimiteit" (doorlopende laag)
Geen vast percentage. Concrete complimenten, bewust aanraken. Zoenen: pas na 3+ maanden, als zaadje. Bij consequent negeren: frequentie verlagen, niet pushen.

### Spoor C: "De dynamiek" (thema's 1-5)
Lisanne leert sturen. Niet omdat ze het wil, maar omdat Tim het fijn vindt. Ruimte als ze het wél leuk vindt.

---

## 5. De vijf dynamiek-thema's

### Thema 1: "Zeggen, niet vragen"
Verschil vragen/mededelen. Lost huishoudprobleem op. Variatie: berichtje (makkelijker) en face-to-face. Bewustwordingsvraag 1 op 3 keer. Succes terugspiegelen eerste 2 weken. Door na: meerdere acties, positief, min. 2 weken.

### Thema 2: "Ontdek wat het doet"
Effect van woorden/houding. Bewust zijn is genoeg. Door na: meerdere suggesties, positief, 1x eigen initiatief, min. 2-3 weken.

### Thema 3: "Dit doe ik voor Tim"
Items. Begin minst intimiderend (blinddoek, halsband). Handleiding actief erbij (niet "zoek op"). Door na: meerdere items, min. 2 verschillende, positief, min. 3 weken.

### Thema 4: "Een moment bouwen"
Samenhangende momenten. Stap-voor-stap. Aftercare specifiek. Kort eerst (10-15 min). Aftercare ook al bij thema 2-3 na spannende suggesties.

### Thema 5: "Jullie eigen stijl"
Concreet ander app-gedrag:
- Minder voorgeschreven suggesties
- Meer check-ins ("Hoe was dat?")
- Meer favorieten-rotatie
- Geen "waarom" meer
- Meer Plannen-initiatief gefaciliteerd
- App stuurt minder, bevestigt meer

### Progressie
Niet lineair. Terugval is normaal. 6 weken in thema 1 is oké. De app kan alleen helpen als er af en toe iets geprobeerd wordt — maar geen druk.

### Eerste maand
Meetbaar zachter dan het plan suggereert. Weinig Spoor C, veel bevestiging, veel succeservaring op communicatie, nauwelijks itemdruk.

---

## 6. BDSM-framing: gefaseerd

**Fase 1** (thema 1-2): "Dit kan fijn zijn voor Tim."
**Fase 2** (thema 3): "Tim vindt dit fijn."
**Fase 3** (thema 4): "Hoe was dit voor jou?" — deur openen
**Fase 4** (thema 5): "Dit is iets van jullie." — loslaten

---

## 7. Intensiteit en comfort

### Meegroeisysteem
"vond ik leuk" → meer. "spannend maar oké" → tempo. "te veel" → terug.

### Comfortzone per spoor
Per spoor tracken, niet één spiraal. Zachte uitstappen.

### Drie lagen van afwijzing
**UI voor Lisanne:** twee knoppen.
**Intern systeem:** drie betekenissen.

| Wat Lisanne kiest | Intern | Gedrag |
|---|---|---|
| "Niet nu" | Korte rem | Komt later terug |
| "Niks voor mij" | Lange rem | Verdwijnt 4-8 weken, komt alleen terug als context veranderd is, in zachtere vorm |
| Harde grens | Apart vastgelegd (via grenzen-check-in) | Komt nooit terug |

**"Niks voor mij" is geen permanente ban.** Als iets voor Tim belangrijk is: bewaren als gevoelig thema, later zachter herintroduceren. Nooit direct opnieuw pushen. Nooit Lisanne confronteren met "Tim vindt dit belangrijk" na afwijzing.

**Voor Tim:** "Dat Lisanne dit nu niet wil, betekent niet nooit. Laat dit rusten. De app zoekt later een zachtere ingang."

**Periodieke herwaardering:** na maanden, zacht: "Zijn er dingen die eerst niet bij je pasten, maar die nu misschien anders voelen?" Niet gekoppeld aan specifiek item.

### Leren van overslaan
3x negeren → minder aanbieden.

### Tim's wens-kanaal
Vrij tekst + 3 opties ("meer spanning" / "meer aanraking" / "meer leiding"). Gevoelsniveau, niet specifieke acties. Max 1 actief, nieuwe overschrijft oude. Verborgen achter extra tik. "Zelf gedaan" registratie: simpel, geen invloed op thema-sprongen, hooguit lichte comfort-boost. Als wens niet omgezet: "Je wens is meegenomen. Timing kwam niet uit."

---

## 8. Weekritme

### Suggesties per week
Fase 1-3: max 3. Fase 4: max 4. Fase 5+: max 5. Niet op vaste dagen.

### Dagdeel
Ma-do overdag (school): berichtje-acties. Ochtend: niks. Avond na 19:00: fysiek. Vrijdagavond: kans na bedtijd. Geen suggesties die geluid vereisen als Milou thuis is.

### Regels
- Nooit meer dan 1 ding per dag (suggestie OF reflectie)
- Max 2 lege dagen op rij
- Min. 1 dag buffer tussen humor en serieuze dynamiek

### Autopilot
Dagen zonder suggestie. Max 3/week, 1 rustdag ertussen. Groeit mee met thema's (stopt niet na thema 3).

### Rustdagen
Warme bevestiging + actieve terugblik (alleen positief) + Tim's dag + link naar Plannen.

---

## 9. Spotlight (Vandaag-tab)

| Situatie | Label |
|----------|-------|
| Ervaringscheck | "Even checken" |
| Suggestie avond | "Voor vanavond" |
| Suggestie overdag | "Later vandaag" |
| Herinnering | "Terugblik" |
| Autopilot | "Snel idee" |
| Rustdag | "Rustige dag" |
| Stille week | "Rustige week" |

Moment-blok: max 1 item (reflectie > dagafsluiting > weekreflectie > oefening > praise).

---

## 10. Tim's view — compleet

Tim maakt ook een reis: van "ik moet alles zelf regelen" naar "ik mag loslaten."

### Dagritme (evolueert per thema)
Thema 1: reageren op mededelingen. Thema 3: items voorbereiden. Thema 4: aftercare. Doorlopend: zachte taken voor Lisanne.

### Tim's emotionele reis (spaarzaam en concreet)
- **Eenzaamheid:** "Dit is ook voor jou niet makkelijk."
- **Schuldgevoel:** "Dit is geen manipulatie — het is een uitnodiging."
- **Angst stopt weer:** "Dit keer houdt de app het ritme vast."
- **Ongeduld:** "Thema 1 IS het echte werk."
- **Kwetsbaarheid:** optie om te zeggen "ik voel me onzeker"
- **Fantasie vs werkelijkheid:** "Het echte is anders. En kwetsbaarder."
- **Leren ontvangen:** "Ontvangen zonder sturen is ook een vaardigheid."
- **Overdrijven:** "Reageer warm maar rustig. Overdrijven voelt als druk."
- **Niet vergelijken:** "Wat voor jullie werkt is goed."

Toon: concreet, kort. "Dat je rustig bleef, helpt Lisanne." Niet: "Wat jij doet is zo moeilijk en waardevol."

### Anti-coaching
"Geniet ervan. Verwacht niet meer." / "Heb je hints gegeven?"

### Verwachtingsmanagement
Bij elke thema-overgang: "Er verandert iets. Blijf rustig."

### Teleurstelling
"Focus op dat ze het deed, niet op hoe."

### Tim ziet progressie (hints)
"Lisanne is deze week actief geweest." Zonder details.

### Tim checkt niet te veel
View update 1x per dag. Onderhoud wekelijks gebatcht.

### Bijzondere dag
"Vakantie" / "bijzondere dag" / "we hebben het moeilijk"

---

## 11. Lisanne beschermen

### Waardering
Rustige erkenning na eerste keer, na iets spannends, op rustdagen. "Je probeerde iets nieuws. Dat is al veel."

### Eigenwaarde
Nooit impliceren dat ze niet genoeg doet. "Je doet precies genoeg."

### Info actief brengen
Handleiding direct bij suggestie. Niet "zoek op in de Gids."

### "Mag altijd stoppen"
In onboarding + als vaste subtiele escape in suggestie-UI + bij eerste moeilijke momenten. Niet als losse tekst overal doorheen.

### Eerste mislukt moment
"Dat is normaal. Het wordt makkelijker." Eén zin.

### Meerdere negatieve signalen
3+ achter elkaar → zachte reset naar Spoor A.

### Grenzen vastleggen
Na eerste weken: open vraag. Wordt harde grens.

---

## 12. De relatie beschermen

### Ruzie-modus
"We hebben het moeilijk" → alleen Spoor A of pauze.

### Veiligheidsklep
Beide views negatief → automatisch 2 weken Spoor A. Relatie boven dynamiek.

### Balans
Regelmatig: Tim doet iets voor Lisanne.

### De app trekt zich terug
Thema 1-3: "Doe dit." Thema 4: "Probeer dit." Thema 5: check-ins. Post-leerpad: companion. "Dit is een hulpmiddel."

---

## 13. Bewustwording en reflecties

### Bewustwordingsvragen (1 op 3, direct)
"Heb je het gevraagd of medegedeeld?"

### Micro-feedback
Fijn / oké / ongemakkelijk. "Neutraal goed" is een erkende staat. Niet alles hoeft bijzonder.

### Uitgebreide reflecties
Alleen wekelijks of na bijzondere momenten.

### Undo
30 seconden na invullen.

---

## 14. Content-regels

- Max 2 zinnen per suggestie
- Max 1 "waarom" (verdwijnt over tijd)
- Complimenten concreet
- Pool groot genoeg per thema: variatie op zelfde concept
- Toon evolueert: uitleggend → meedenkend → incheckend
- Humor alleen in Spoor A of lichte Spoor B. Nooit naast kwetsbaarheid of serieuze dynamiek.
- Verboden woorden: fluister, zacht in zijn oor, laat spanning hangen, ondeugend, sensueel, indringend, verleid
- Verboden context: koffie (thee), bad, voeten. Tim raakt Lisanne niet aan bij borsten/voeten

---

## 15. Onboarding

Tim geeft de app: "Ik heb iets gemaakt dat ons misschien helpt."
Eerste opening: druk wegnemen, veilig, nieuwsgierig. Meer niet.
Eerste week: alleen zacht Spoor A en B.
Drop-off: "Welkom terug. Geen druk." Altijd licht na pauze.

---

## 16. Gids-tab

### Actief informeren
Essentiële info bij de suggestie zelf. Gids voor wie meer wil.

### Gefilterd
"Nu relevant" (thema + bezit). "Later" als teaser (niet als lijst): "Later misschien: 2 dingen" → pas na tik openen.

### Altijd zichtbaar
"Als iets niet goed voelt, stopt het."

---

## 17. Praktisch

- Items kopen/opbergen: Tim regelt. App herinnert: afgesloten doos/lade.
- Geluid: geen geluid-suggesties als Milou thuis.
- Notificaties: nooit inhoudelijk. Configureerbaar tijdstip. Niet tijdens ochtend-drukte.
- Export/import (P2): backup tegen verlies.

---

## 18. Designregels

1. **Fluistering, niet systeem.**
2. **Lisanne hoeft het niet te willen** — maar ruimte als ze het wél leuk vindt.
3. **Tim doet het werk.** Onderhoud wekelijks gebatcht.
4. **Lisanne zoekt niks op.** Info actief brengen.
5. **Max 2 zinnen.** Handleiding actief erbij.
6. **"Dit wil ik niet" = data, niet falen.** Drie interne lagen.
7. **Nooit meer dan 1 ding per dag.**
8. **"Kan dit als kritiek gelezen worden?"** Zo ja: herschrijven.
9. **Balans geven/ontvangen.**
10. **Tim ook waarderen, niet alleen corrigeren.**
11. **"Normaal goed" is ook goed.** Niet alles hoeft bijzonder.
12. **Humor nooit naast kwetsbaarheid.**
13. **Erkennen en normaliseren, niet verklaren.** Relatie-app, geen therapie.
14. **Thema 5 = concreet ander app-gedrag,** niet alleen concept.

---

## 19. Wat gebouwd moet worden

### P0 — Voorkomt falen
- [ ] "Niet nu" / "Niks voor mij" altijd zichtbaar (drie interne lagen)
- [ ] Lisanne-waardering
- [ ] Info actief bij suggestie brengen
- [ ] Rustdag-spotlight met terugblik
- [ ] Undo voor ervaringen

### P1 — Maakt slim
- [ ] Suggestie-pool taggen: spoor, thema, dagdeel, milou
- [ ] Nieuwe suggesties Spoor A + B
- [ ] Thema-tracking + progressie-logica (non-lineair)
- [ ] Comfortzone per spoor
- [ ] Scheduler met alle filters
- [ ] Micro-feedback (fijn/oké/ongemakkelijk) + bewustwordingsvragen 1 op 3
- [ ] Tim's wens-kanaal
- [ ] Tim's dagritme evoluerend + emotionele reis (spaarzaam)
- [ ] BDSM-framing gefaseerd
- [ ] Anti-coaching per thema-overgang
- [ ] Drop-off re-engagement
- [ ] Ruzie-modus + veiligheidsklep
- [ ] "Zelf gedaan" registratie (Tim's view, lichte impact)
- [ ] Overgeslagen suggesties tracken
- [ ] Normalisatie "was raar" + zachte reset bij 3x negatief
- [ ] Lisanne's grenzen vastleggen
- [ ] Autopilot meegroeien met thema's
- [ ] Stemming-indicator
- [ ] Periodieke herwaardering afgewezen suggesties

### P2 — Maakt mooi
- [ ] Onboarding
- [ ] Taalverschuiving + humor
- [ ] Gids gefilterd (teaser-stijl)
- [ ] Bijzondere dagen / vakantie
- [ ] Post-leerpad modus
- [ ] Export/import
- [ ] Cross-device sync
- [ ] Pincode/verbergen
