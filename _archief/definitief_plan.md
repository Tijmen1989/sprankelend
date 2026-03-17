# Sprankelend Souffleur — Definitief Ontwerp v3

Dit document combineert het verbeterplan, ChatGPT's feedback, en alle diepere verbeterpunten tot één definitief plan.

---

## ARCHITECTUUR

### 7 lagen die elke week door elkaar lopen

| Laag | Wat | Minimaal per week |
|------|-----|-------------------|
| **Focus-pad** | Actieve leerpad-suggestie | 2x |
| **Doorloop** | Herhaling uit eerder pad | 1x |
| **Bevestiging** | Tim voelt zich gezien | 2x |
| **Gewoon jullie** | Warmte, humor, samen-zijn | 2x |
| **Anticipatie** | Spanning door hints/uitstel | 0-1x |
| **Nieuwheid** | Onverwacht, patroon breken | 0-1x |
| **Presence** | Er-zijn zonder actie | 0-1x |

Geen laag staat op zichzelf. Suggesties kunnen meerdere lagen raken (een combo-suggestie is focus + bevestiging + anticipatie tegelijk).

### 7 leerpaden (inclusief fase 0)

| Nr | Naam | Focus | Periode |
|----|------|-------|---------|
| 0 | Gewoon samen | Veiligheid + plezier. App voelt als leuke relatie-app. | Dag 1-5 |
| 1 | Kleine signalen | Initiatief nemen. Jij deed iets → het was oké. | Week 1-3 |
| 2 | Jij kiest | Beslissen. Jij koos → Tim volgde → dat voelde goed. | Week 3-5 |
| 3 | Dichterbij | Lichamelijk bewuster. Aanraken als statement. | Week 5-7 |
| 4 | Iets beginnen | Anticipatie. Opbouwen, hints, stoppen. | Week 7-9 |
| 5 | Iets nieuws proberen | Items: blinddoek, boeien. Hulpmiddelen, niet eng. | Week 9-11 |
| 6 | Jouw avond | Eigen moment creëren. Van begin tot eind. | Week 11-13 |

Paden stoppen nooit — ze verschuiven van focus naar achtergrond.

---

## DATASTRUCTUUR PER SUGGESTIE

### Bestaande velden (ongewijzigd)
```
id, cat, spoor, zwaarte, type, items, subtiel, opbouw, minDagen, vibe,
tekst, zegSubtiel, zegPrive, actieType, voorWie
```

### Nieuwe velden
```javascript
{
  leerpad: 0,              // 0-6, null = niet padgebonden (bevestiging, gewoon jullie)
  stap: 1,                 // stap binnen leerpad (progressie)
  mechanisme: null,        // null, 'anticipatie', 'bevestiging', 'nieuwheid', 'presence'
  inzicht: '...',          // korte zin vóór de actie (null = geen)
  inzichtUitleg: '...',    // langere uitleg achter toggle (null = geen)
  reflectieVraag: '...',   // verdiepende vraag ná de actie (null = standaard fijn/niks/teveel)
  eigenInitiatief: false,  // true = telt extra bij progressie als Lisanne het zelf bedenkt
  taalVariant: 'zacht'     // 'zacht' ("ik wil dat...") of 'direct' ("doe dit") — scheduler kiest op basis van fase
}
```

### Waarom deze velden

| Gevraagd | Oplossing | Reden |
|----------|-----------|-------|
| novelty, anticipatie, bevestiging | → `mechanisme` (1 veld) | Eén tag per suggestie is genoeg |
| relatieWarmte, dynamiekNiveau | → afleidbaar uit `cat` + `vibe` + `zwaarte` | Niet apart nodig |
| autonomieScore | → `eigenInitiatief` boolean | Simpeler |
| taalVariant (NIEUW) | 'zacht' vs 'direct' | Eerste 3 weken zachte taal, daarna mix |

---

## FASE 0: "GEWOON SAMEN" (dag 1-5)

### Doel
De app voelt als een leuke relatie-app. Geen dynamiek, geen opdrachten, geen opbouw. Alleen veiligheid en plezier. Lisanne leert de app vertrouwen voordat er iets gevraagd wordt.

### Dag-voor-dag

**Dag 1** — Warmte
"Vertel Tim iets dat je vandaag leuk vond. Over je dag, over hem, maakt niet uit."
Geen inzicht. Geen reflectie. Gewoon beginnen.

**Dag 2** — Nabijheid
"Ga 2 minuten tegen Tim aan zitten. Geen telefoon, geen tv. Gewoon even samen."
Mechanisme: presence.

**Dag 3** — Nieuwsgierigheid
"Vraag Tim iets wat je nog niet van hem weet. Of iets dat je lang niet gevraagd hebt."

**Dag 4** — Herinnering
"Herinner Tim aan een leuk moment samen. Kijken of hij het ook nog weet."

**Dag 5** — Licht eigen initiatief
"Doe vandaag iets kleins voor Tim. Een compliment, een aanraking, een berichtje. Jij kiest wat."
eigenInitiatief: true. Eerste keer dat Lisanne zelf kiest — maar nog zonder druk.

### Na dag 5
App vraagt niet "hoe ging het?" maar zegt: "Fijn dat je er bent. Volgende week gaan we een beetje verder."

---

## LEERPAD 1: "KLEINE SIGNALEN" (focus week 1-3)

### Kernles
Jij deed iets → Tim reageerde positief → het was oké.

### Stap 1: Digitaal initiatief
Drempel zo laag mogelijk. Telefoon, geen face-to-face.

| Var | Suggestie | Taal |
|-----|-----------|------|
| A | "Stuur Tim: 'Ik dacht net aan je.' Zonder context." | — |
| B | "Stuur Tim: 'Je ziet er goed uit vandaag.'" | — |
| C | "Stuur Tim: 'Ik vond het fijn gisteren.' Niet uitleggen." | — |
| **Open** | "Stuur Tim een berichtje. Maakt niet uit wat — iets liefs, iets grappigs, iets raars." | — |

### Stap 2: Terloops aanraken
Eerste fysieke initiatie. Kort, in het voorbijgaan.

| Var | Suggestie | Taal |
|-----|-----------|------|
| A | "Loop langs Tim en laat je hand even over zijn rug gaan. Doorlopen." | — |
| B | "Raak Tim aan op zijn buik als je langsloopt. Hand iets langer laten liggen." | — |
| C | "Leg je hand op Tim's arm als je naast hem zit. Kort. Terloops." | — |
| **Open** | "Raak Tim vandaag even terloops aan. Waar en hoe mag jij kiezen." | — |

### Stap 3: Bewust contact
Van toevallig naar met intentie.

| Var | Suggestie | Taal |
|-----|-----------|------|
| A | "Kijk Tim bewust aan. 5 seconden. Zeg niks." | — |
| B | "Zeg iets over Tim's lichaam. 'Je ziet er goed uit.' Of specifieker." | — |
| C | "Kijk Tim na als hij de kamer uitloopt. Laat merken dat je kijkt." | — |
| **Open** | "Laat Tim vandaag merken dat je naar hem kijkt. Op jouw manier." | — |

Inzicht bij deze stap: "Oogcontact is een van de sterkste signalen die je kunt geven."

### Stap 4: Stevig initiatief
Assertiever dan aaien. Stevigheid als variant.

| Var | Suggestie | Taal |
|-----|-----------|------|
| A | "Pak Tim's pols vast. Kort, stevig. Laat weer los." | — |
| B | "Druk je duim stevig in Tim's schouder. Niet als massage — als statement." | — |
| C | "Leg je hand plat op Tim's borst. Voel even zijn hartslag." | — |
| **Open** | "Raak Tim vandaag aan op een manier die steviger is dan normaal. Jij kiest hoe." | — |

Inzicht: "Stevig aanraken is niet hard. Het is duidelijk."

### Stap 5: Eigen keuze
Niet meer voorgeschreven. Brug naar LP2.

| Var | Suggestie |
|-----|-----------|
| A | "Loop langs Tim en raak hem aan — waar je wilt, hoe je wilt." |
| B | "Doe vandaag iets dat jij initieert. Aanraken, zeggen, sturen. Jij kiest." |
| C | "Bedenk één ding dat je voor Tim wilt doen. Doe het. Zeg er niks over." |

eigenInitiatief: true bij alle varianten.

---

## LEERPAD 2: "JIJ KIEST" (focus week 3-5)

### Kernles
Jij koos → Tim volgde → dat voelde goed voor allebei.

### Stap 1: Kleine keuzes
Dagelijks, laagdrempelig.

| Var | Suggestie | Taal |
|-----|-----------|------|
| A | "Kies wat jullie vanavond eten. Niet overleggen — jij kiest." | — |
| B | "Kies een serie voor vanavond. Zeg: 'We kijken dit.'" | — |
| C | "Bepaal waar jullie zitten. 'Kom op de bank.' Of: 'We zitten aan tafel.'" | — |
| **Open** | "Kies vanavond iets. Maakt niet uit wat. Het gaat om het kiezen." | — |

Inzicht: "Kiezen voelt misschien raar. Dat is normaal. Tim vindt het fijn als jij kiest."

### Stap 2: Zacht mededelen
Verschil voelen tussen vragen en zeggen. **Zachte taal eerst.**

| Var | Suggestie | Taalvariant |
|-----|-----------|-------------|
| A | "Zeg tegen Tim: 'Ik wil dat jij de keuken doet.' Niet vragen — zeggen." | zacht |
| B | "Zeg: 'Ik wil dat de was wordt opgehangen. Doe jij dat even.'" | zacht |
| C | "Zeg tegen Tim dat hij thee zet. Niet 'wil je?' maar 'zet even thee.'" | zacht |
| **Open** | "Zeg vandaag iets tegen Tim als mededeling in plaats van als vraag. Jij kiest wat." | — |

Reflectievraag: "Hoe voelde het om het te zeggen in plaats van te vragen?"

### Stap 3: Mededelen (direct)
Na minstens 2x "fijn" bij stap 2.

| Var | Suggestie | Taalvariant |
|-----|-----------|-------------|
| A | "Zeg: 'Keuken opruimen.' Kort. Duidelijk." | direct |
| B | "Zeg: 'Was ophangen. Als je klaar bent, kom je even hier.'" | direct |
| C | "Zeg: 'Douchen. Nu.' Niet meer dan dat." | direct |

### Stap 4: Combo (opdracht + spontaan moment)

| Var | Suggestie |
|-----|-----------|
| A | "Zeg dat Tim de keuken opruimt. Als hij bezig is: loop langs, knuffel van achteren." |
| B | "Laat Tim de was ophangen. Als hij klaar is: trek hem even naar je toe. Kort." |
| C | "Stuur Tim naar de supermarkt. Als hij terugkomt: pak het aan, kijk hem aan, zeg 'dankje.'" |
| **Open** | "Geef Tim een opdracht. En voeg er iets liefs aan toe — een aanraking, een blik, een woord." |

Inzicht: "Een opdracht hoeft niet streng te zijn. Het is een aanleiding voor een leuk moment."

### Stap 5: Grotere keuzes

| Var | Suggestie |
|-----|-----------|
| A | "Bepaal wanneer Tim naar bed gaat. Zeg het als mededeling." |
| B | "Bepaal de volgorde van de avond. Jij plant." |
| C | "Kies een serie. Zeg: 'We kijken dit. Haal thee.'" |

### Stap 6: Zelf bedenken

| Var | Suggestie |
|-----|-----------|
| A | "Bedenk zelf een opdracht voor Tim. Maakt niet uit wat." |
| B | "Bedenk drie dingen die Tim vandaag moet doen. Zeg ze achter elkaar." |
| **Open** | "Verzin vandaag iets voor Tim om te doen. Groot of klein — jij bepaalt." |

eigenInitiatief: true.

---

## LEERPAD 3: "DICHTERBIJ" (focus week 5-7)

### Kernles
Tim's lichaam is van jullie samen. Aanraken is normaal.

### Stap 1: Bewust kijken

| Var | Suggestie |
|-----|-----------|
| A | "Tim loopt naakt rond. Kijk bewust naar hem. Laat merken dat je kijkt." |
| B | "Bekijk Tim alsof je het voor het eerst ziet. Benoem wat je opvalt." |
| C | "Zeg: 'Blijf staan.' Bekijk hem. Van boven naar beneden. 'Goed. Je mag verder.'" |
| **Open** | "Kijk vandaag bewust naar Tim's lichaam. Op jouw manier." |

Inzicht: "Tim's lichaam is niet iets dat je 'mag' aanraken. Het is van jullie samen."

### Stap 2: Langzaam aanraken

| Var | Suggestie |
|-----|-----------|
| A | "Krab langzaam over Tim's rug. Van boven naar beneden. Neem de tijd." |
| B | "Laat je nagels zachtjes over zijn rug gaan. Kijk hoe zijn huid reageert." |
| C | "Ga met je vingertoppen over de binnenkant van Tim's onderarm. Heel licht." |
| **Open** | "Raak Tim vandaag langzaam aan. Waar en hoe lang mag jij kiezen." |

### Stap 3: Aanraken als statement

| Var | Suggestie |
|-----|-----------|
| A | "Pak Tim's kin vast en draai zijn gezicht naar je toe. Kijk hem aan. Laat los." |
| B | "Pak Tim's nek van achteren vast. Stevig, kort." |
| C | "Ga met je vinger over Tim's kaakrand. Van oor tot kin." |
| D | "Raak Tim's haar aan. Grijp het voorzichtig vast. Kort. Laat los." |

### Stap 4: Lichamelijke opdracht

| Var | Suggestie |
|-----|-----------|
| A | "Zeg: 'Kom hier. Shirt uit.' Bekijk hem. Dat is genoeg." |
| B | "Zeg: 'Draai je om.' Bekijk hem van achteren. Raak zijn schouderblad aan." |
| C | "Zeg: 'Ga zitten.' Ga achter hem staan. Handen op schouders. Zeg niks." |

### Stap 5: Grenzen verkennen

| Var | Suggestie |
|-----|-----------|
| A | "Raak Tim aan op borst en bovenbenen. Langzaam. Stop net voor het seksueel wordt." |
| B | "Trek Tim naar je toe aan zijn broekband. 'Dichter.' Meer hoeft niet." |
| C | "Bijt zachtjes in Tim's schouder als je langsloopt. Kort. Loop door." |
| **Open** | "Raak Tim vandaag aan op een plek die je normaal niet aanraakt. Jij kiest." |

eigenInitiatief: true bij open variant.

---

## LEERPAD 4: "IETS BEGINNEN" (focus week 7-9)

### Kernles
Anticipatie is krachtiger dan het moment zelf. Opbouwen en stoppen is een vaardigheid.

### Stap 1: Digitale spanning

| Var | Suggestie |
|-----|-----------|
| A | "Stuur Tim: 'Vanavond heb ik plannen.' Geen verdere uitleg." |
| B | "Stuur Tim een foto van het bed. Geen tekst." |
| C | "Stuur Tim: 'Als je thuiskomt wil ik dat je shirt uit is.'" |
| **Open** | "Stuur Tim vandaag een berichtje dat spanning creëert. Jij kiest wat." |

Inzicht: "Je hoeft niet te weten wat je gaat doen. De hint zelf doet al iets."

### Stap 2: Beginnen en stoppen

| Var | Suggestie |
|-----|-----------|
| A | "Raak Tim kort aan door zijn broek heen. Eén keer. Stop. Loop weg." |
| B | "Duw Tim achterover op de bank. 'Blijf zo.' Loop weg. Kom later terug." |
| C | "Raak de binnenkant van Tim's bovenbeen aan. Langzaam omhoog. Stop halverwege." |

Inzicht: "Anticipatie is krachtiger dan het moment zelf."

### Stap 3: Wachten als tool

| Var | Suggestie |
|-----|-----------|
| A | "Zeg: 'Ga naar de slaapkamer. Ik kom zo.' Laat hem 5 minuten wachten." |
| B | "Zeg: 'Niet bewegen.' Loop om Tim heen. Raak hem één keer aan." |
| C | "Ga dicht bij Tim staan. Adem langzaam in zijn nek. Raak hem niet aan. Loop weg." |

### Stap 4: Aankondigen

| Var | Suggestie |
|-----|-----------|
| A | "Zeg: 'Vanavond bepaal ik alles.' Vertel niet wat." |
| B | "Stuur drie losse berichten: 'Vanavond.' 'Na Milou slaapt.' 'Ik heb iets bedacht.'" |
| C | "Leg iets klaar op het bed — blinddoek, sjaal. Zeg er niks over. Wacht." |

### Stap 5: Eigen spanning-moment

| Var | Suggestie |
|-----|-----------|
| A | "Bouw vanavond spanning op. Hoe is aan jou. Het enige: maak het niet af." |
| B | "Creëer een moment van anticipatie. Tim verwacht iets maar weet niet wat." |

eigenInitiatief: true.

---

## LEERPAD 5: "IETS NIEUWS PROBEREN" (focus week 9-11)

### Kernles
Hulpmiddelen zijn gereedschap. Ze versterken wat je al kunt.

### Stap 1: Kennismaking (via Gids)
Geen actie-suggestie. Informatie over één item.

| Var | Item + uitleg |
|-----|---------------|
| A | Blinddoek — "Hiermee bepaal jij wat Tim voelt. Hij ziet niks." |
| B | Polsboeien — "Hiermee kan Tim niks doen. Jij hebt alle controle." |
| C | Halsband — "Een symbool. Tim voelt hem de hele tijd." |

Inzicht: "Een blinddoek is geen seks-ding. Het is een manier om aanraking intenser te maken."

### Stap 2: Eerste gebruik (kort)

| Var | Suggestie |
|-----|-----------|
| A | "Doe Tim de blinddoek om. 2 minuten. Eén aanraking. Blinddoek af." |
| B | "Doe Tim de polsboeien om. Laat hem 5 min zitten. Kijk hoe het voelt — voor jou." |
| C | "Doe Tim de halsband om als hij naakt rondloopt. Zeg er niks over." |

### Stap 3: Item + aanraking

| Var | Suggestie |
|-----|-----------|
| A | "Blinddoek. Raak Tim op drie plekken aan. Langzaam. Hij weet niet waar." |
| B | "Polsboeien. Raak Tim's borst en buik aan. Hij kan niks doen." |
| C | "Halsband. Pak de D-ring. Trek hem naar je toe." |

### Stap 4: Item + opdracht

| Var | Suggestie |
|-----|-----------|
| A | "Blinddoek. 'Je mag pas praten als ik het zeg.' Raak hem aan." |
| B | "Polsboeien. 'Niet bewegen. Ik bepaal wat er gebeurt.'" |
| C | "'Op je knieën.' Halsband om. Ga voor hem staan. Raak zijn hoofd aan." |

### Stap 5: Combinatie

| Var | Suggestie |
|-----|-----------|
| A | "Polsboeien + blinddoek. Totale controle. Aanraken wanneer en waar jij wilt." |
| B | "Halsband + polsboeien. Tim op bed. Verken zijn reacties." |
| **Open** | "Kies zelf een item. Jij bepaalt wat, hoe lang, en wat je ermee doet." |

### Stap 6: Eigen item-moment

| Var | Suggestie |
|-----|-----------|
| A | "Gebruik vanavond een item naar keuze. Combineer met wat je al kent. Jij regisseert." |

eigenInitiatief: true.
Inzicht: "Jij hoeft dit niet te 'willen' zoals Tim het wil. Jij mag het op jouw manier doen."

---

## LEERPAD 6: "JOUW AVOND" (focus week 11-13)

### Kernles
Jij kunt een moment creëren. Dat is wat je al doet, maar dan bewust.

### Stap 1: Kort moment met structuur

| Var | Suggestie |
|-----|-----------|
| A | "15 minuten. Begin met opdracht. Dan aanraken. Dan stoppen. Drie stappen." |
| B | "Plan kort moment: 1) Tim doet iets. 2) Jij raakt aan. 3) Jij zegt wanneer het klaar is." |

### Stap 2: Moment met item

| Var | Suggestie |
|-----|-----------|
| A | "Plan een moment met blinddoek. Begin: om. Midden: aanraken, pauzeren. Eind: af." |
| B | "Plan een moment met polsboeien. Tim kan niks. Jij doet wat je wilt." |

### Stap 3: Langer moment

| Var | Suggestie |
|-----|-----------|
| A | "Stuur Tim om 8 uur: 'Bereid je voor.' Om 9 uur begint het. Jij bepaalt wat." |
| B | "Tim: douchen, slaapkamer, klaarliggen. Laat hem wachten. Kom als jij klaar bent." |

### Stap 4: Volledig eigen moment

| Var | Suggestie |
|-----|-----------|
| A | "Vanavond is van jou. Geen suggestie. Jij bedenkt, plant, voert uit." |
| B | "Choreografeer een avond. Van eerste aanraking tot nazorg. Het mag simpel, het mag groots." |

eigenInitiatief: true.
Inzicht: "Wat je nu kunt, kon je 3 maanden geleden niet. Dat is niet niks."

---

## DOORLOPENDE LAGEN

### Bevestiging (structureel 2x per week, altijd)

| ID | Suggestie | Type |
|----|-----------|------|
| bv01 | "Stuur Tim: 'Ik dacht net aan je.' Zonder context." | digitaal |
| bv02 | "Kijk Tim bewust aan. 5 seconden. Zeg niks." | face_to_face |
| bv03 | "Zeg iets over Tim's lichaam. 'Je ziet er goed uit.'" | face_to_face |
| bv04 | "Stuur Tim: 'Je zag er net goed uit.' Gewoon dat." | digitaal |
| bv05 | "Geef Tim een compliment dat je normaal voor jezelf houdt." | face_to_face |
| bv06 | "Noem één ding dat je aan Tim waardeert. Hardop." | face_to_face |
| bv07 | "Kijk Tim na als hij wegloopt. Laat merken dat je kijkt." | face_to_face |
| bv08 | "Stuur Tim: 'Ik ben blij dat je er bent.'" | digitaal |

### Gewoon jullie (warmte + humor + presence)

**Warmte:**
| ID | Suggestie |
|----|-----------|
| gw01 | "Vertel Tim iets van je dag. Grappig of zwaar, maakt niet uit." |
| gw02 | "Ga tegen Tim aan zitten. Geen reden. Gewoon dichtbij." |
| gw03 | "Herinner Tim aan een leuk moment samen." |
| gw04 | "Pak Tim's hand even als jullie samen zijn." |
| gw05 | "Kook samen. Allebei een taak." |

**Humor:**
| ID | Suggestie |
|----|-----------|
| gw06 | "Zeg iets overdreven dramatisch tegen Tim. 'Je bent de knapste man van dit appartement.'" |
| gw07 | "Doe alsof Tim een VIP is. 'Meneer, uw thee. Kan ik verder nog iets voor u betekenen?'" |
| gw08 | "Geef Tim een compleet onlogisch compliment. 'Je hebt mooie ellebogen.'" |
| gw09 | "Daag Tim uit voor iets doms. Wie kan het langst op één been staan. Wie raadt het nummer." |
| gw10 | "Stuur Tim een meme of grappig filmpje dat je aan hem doet denken." |

**Presence:**
| ID | Suggestie |
|----|-----------|
| gw11 | "Kijk Tim 10 seconden aan zonder iets te zeggen. Gewoon kijken." |
| gw12 | "Blijf 2 minuten tegen Tim aan zitten. Geen telefoon, geen tv." |
| gw13 | "Leg je hand op Tim's arm en laat hem daar. Niks zeggen." |
| gw14 | "Zit samen 3 minuten zonder telefoon. Kijk uit het raam of naar elkaar." |
| gw15 | "Ga vanavond gewoon naast Tim zitten. Niks bijzonders. Samen zijn is ook goed." |

### Anticipatie (max 1x per week in fase 1-2, max 2x in fase 3+)

| ID | Suggestie | minDagen |
|----|-----------|----------|
| an01 | "Stuur Tim: 'Vanavond even jij en ik.' Meer niet." | 3 |
| an02 | "Loop langs Tim, raak hem kort aan, loop weer door." | 7 |
| an03 | "Zeg: 'Niet nu. Straks.' Loop weg." | 14 |
| an04 | "Stuur drie losse berichten: 'Vanavond.' 'Na Milou slaapt.' 'Ik heb iets bedacht.'" | 21 |
| an05 | "Leg iets klaar op het bed. Zeg er niks over." | 35 |
| an06 | "Zeg: 'Vanavond kom ik nog bij je terug.' Verder niks." | 7 |
| an07 | "Stuur Tim: 'Later wil ik iets van je.' Verder niks." | 14 |

### Nieuwheid (max 1x per 10 dagen fase 1, 1x per week fase 2+)

| ID | Suggestie | minDagen |
|----|-----------|----------|
| nw01 | "Doe vandaag iets met Tim dat je normaal niet doet. Maakt niet uit wat." | 7 |
| nw02 | "Verander vanavond één ding aan jullie routine. Iets kleins." | 14 |
| nw03 | "Trek Tim zonder waarschuwing naar je toe. Houd vast. Laat los." | 14 |
| nw04 | "Doe iets onverwachts. Geen plan nodig — het gaat om de afwijking." | 21 |

---

## SCHEDULER (PSEUDOCODE)

```
functie kiesDagSuggestie(state, historie, dagenActief):

  // ─── STAP 0: Energiecheck ───
  energie = state.energieVandaag  // 'laag', 'normaal', 'goed' (optioneel)
  als energie == 'laag':
    return kiesUit(PRESENCE + GEWOON_JULLIE_WARMTE)  // alleen zachte dingen
  als energie niet ingevuld:
    energie = 'normaal'  // default

  // ─── STAP 1: Soft reset check ───
  dagenGemist = aantalDagenZonderActiviteit(historie)
  als dagenGemist >= 3:
    toonBericht: "Geen probleem dat je even niks deed. Pak gewoon iets kleins op."
    forceer dagtype = 'gewoon_jullie' of 'presence'
    // Reset verwachting — geen schuld

  // ─── STAP 2: Bepaal actief leerpad ───
  actiefPad = bepaalActiefLeerpad(state, historie)
  huidigeStap = bepaalHuidigeStap(actiefPad, historie)

  // ─── STAP 3: Failsafe checks ───

  // Na "teveel"
  als laatsteReactie == 'teveel':
    volgende 2 dagen: alleen gewoon_jullie, bevestiging, of presence

  // Na "reactie viel tegen"
  als laatsteReactie == 'reactie_viel_tegen':
    toonBericht: "Dat zegt niks over wat jij deed.
                  Soms komt iets anders aan dan verwacht."
    volgendeDag: gewoon_jullie of bevestiging
    verlaagEscalatie: volgende focus mag niet zwaarder zijn

  // Na 2 zware suggesties
  als gisteren.zwaarte >= 2:
    vandaag: zwaarte <= 1 of gewoon_jullie

  // ─── STAP 4: Bepaal dagtype ───

  dagVanWeek = getDag()  // 0=zo ... 6=za

  als dagVanWeek == 0:  // zondag
    return RUST of REFLECTIE (als dag 14/28/42/56/70/84)

  als dagVanWeek == 5:  // vrijdag, Milou thuis
    dagtype = kiesUit([
      'digitaal_bevestiging',
      'digitaal_anticipatie',
      'gewoon_jullie'
    ], [40, 30, 30])

  als dagVanWeek == 6:  // zaterdag
    dagtype = kiesUit(['gewoon_jullie', 'presence', 'licht_focus'], [40, 30, 30])

  anders:  // ma-do
    dagtype = weekBalans()

  // ─── STAP 5: Weekbalans (ma-do) ───
  // Doel: 2x focus, 1x bevestiging, 1x mix

  weekTotNu = telDagtypenDezeWeek()

  als weekTotNu.focus < 2:
    dagtype = kiesUit(['focus', 'bevestiging', 'gewoon_jullie'], [50, 25, 25])
  als weekTotNu.bevestiging < 1:
    dagtype = kiesUit(['bevestiging', 'focus', 'gewoon_jullie'], [40, 35, 25])
  als weekTotNu.focus >= 2 EN weekTotNu.bevestiging >= 1:
    dagtype = kiesUit([
      'gewoon_jullie', 'doorloop', 'nieuwheid', 'anticipatie', 'presence'
    ], [30, 25, 15, 15, 15])

  // Extra: energie beïnvloedt gewichten
  als energie == 'goed' EN weekTotNu.focus < 3:
    verhoog kans op 'focus' met 15%

  // ─── STAP 6: Kies suggestie ───

  als dagtype == 'focus':
    pool = suggesties.filter(s =>
      s.leerpad == actiefPad
      && s.stap == huidigeStap
      && s.minDagen <= dagenActief
      && nietRecent(s, historie, 5)
    )
    // Taalvariant check
    als dagenActief < 21:
      prefereer suggesties met taalVariant == 'zacht'
    return kiesRandom(pool)

  als dagtype == 'bevestiging':
    pool = BEVESTIGING.filter(s => s.minDagen <= dagenActief && nietRecent(s, 5))
    return kiesRandom(pool)

  als dagtype == 'gewoon_jullie':
    pool = GEWOON_JULLIE.filter(s => nietRecent(s, 7))
    return kiesRandom(pool)

  als dagtype == 'presence':
    pool = PRESENCE.filter(s => nietRecent(s, 7))
    return kiesRandom(pool)

  als dagtype == 'doorloop':
    pool = suggesties.filter(s =>
      s.leerpad < actiefPad && s.minDagen <= dagenActief && nietRecent(s, 7)
    )
    return kiesRandom(pool)

  als dagtype == 'anticipatie':
    // Frequentie-check
    als dagenActief < 14 EN anticipatieInLaatste(5): return fallback('gewoon_jullie')
    als dagenActief < 28 EN anticipatieInLaatste(3): return fallback('gewoon_jullie')
    pool = ANTICIPATIE.filter(s => s.minDagen <= dagenActief && nietRecent(s, 7))
    return kiesRandom(pool)

  als dagtype == 'nieuwheid':
    als dagenActief < 14 EN nieuwheidInLaatste(10): return fallback('gewoon_jullie')
    pool = NIEUWHEID.filter(s => s.minDagen <= dagenActief && nietRecent(s, 14))
    return kiesRandom(pool)

  // ─── STAP 7: Progressie ───

  functie bepaalHuidigeStap(pad, historie):
    voor elke stap:
      fijn = tel(historie, pad, stap, 'fijn')
      teveel = tel(historie, pad, stap, 'teveel')
      pogingen = tel(historie, pad, stap)

      als fijn >= 2: volgende stap
      als pogingen >= 4: volgende stap (maar zachter aanbod)
      als teveel >= 2: vorige stap
      anders: huidige stap

  // ─── STAP 8: Padwissel ───

  functie bepaalActiefLeerpad(state, historie):
    voor elk pad (0-6):
      afgerond = afgerondeStappen(pad)
      eigen = eigenInitiatieven(pad)

      // Doorstroomeis
      als afgerond >= 3 EN eigen >= 1:
        volgend pad ontgrendeld

      // Grote stap checkpoint (LP3+)
      als pad >= 3:
        extra eis: minstens 3 positieve ervaringen uit vorig pad
        extra eis: geen recente "teveel" (laatste 7 dagen)

    return hoogsteOntgrendeldePad

  // ─── STAP 9: Success loop ───

  positieveReeks = aantalOpeenvolgendeFijn(historie)
  als positieveReeks >= 3 EN nietRecentGetoond('success_loop', 7):
    toonBericht: "Dit gaat goed de afgelopen dagen. Jullie bouwen iets op."
    // Kort, warm, geen score. Gewoon erkenning.

  // ─── STAP 10: Eigen initiatief ───

  als lisanneMeldt('eigenInitiatief'):
    toonBericht: "Mooi dat je dat zelf deed."
    verhoogProgressie: telt als 2x 'fijn'
    verhoogKans: meer vergelijkbare suggesties komende dagen
```

---

## TIM'S VIEW — CONCRETE DAGELIJKSE REMINDERS

Niet alleen "wees geduldig" maar specifiek per context:

### Gekoppeld aan Lisanne's actie van die dag

| Lisanne doet | Tim's reminder |
|--------------|----------------|
| Focus-suggestie | "Als Lisanne vanavond iets doet: reageer rustig. Niet groter maken dan het moment." |
| Bevestiging | "Lisanne oefent met kleine signalen. Geniet ervan. Vraag niet om meer." |
| Anticipatie | "Als Lisanne een hint geeft: laat het zo. Niet doorvragen." |
| Eigen initiatief | "Lisanne deed vandaag iets uit zichzelf. Benoem dat het je raakte, maar hou het klein." |
| Gewoon jullie | "Vandaag niks bijzonders. Gewoon samen zijn." |
| Reactie viel tegen | "Soms merkt Lisanne iets anders dan verwacht. Dat is normaal. Geef haar ruimte." |

### Algemene roterende Tim-inzichten

| Nr | Inzicht |
|----|---------|
| 1 | "Reageer positief op kleine dingen. Niet overdreven — gewoon laten merken dat het aankomt." |
| 2 | "Vandaag niks vragen. Laat Lisanne de toon zetten." |
| 3 | "Het moeilijkste: niks doen. Maar soms is dat precies wat nodig is." |
| 4 | "Lisanne maakt stappen die voor haar groot zijn, ook als ze klein lijken." |
| 5 | "Niet reageren is niet hetzelfde als niet willen." |
| 6 | "Hou het moment klein. Niet meteen meer verwachten." |
| 7 | "Lisanne heeft haar eigen tempo. Geduld is het grootste gebaar dat je kunt geven." |
| 8 | "Als Lisanne iets doet: geniet. Niet bijsturen, niet coachen. Gewoon ontvangen." |

---

## REFLECTIE-SYSTEEM

### Standaard (elke suggestie)
Drie opties: **fijn** / **niks** / **teveel**

Plus nieuwe optie: **reactie viel tegen** (triggert failsafe)

### Verdiepende vraag (bij 20-30% van suggesties)
Afwisselend, nooit dwingend. Voorbeelden:

| Context | Vraag |
|---------|-------|
| Na aanraking | "Merkte je iets aan Tim?" |
| Na opdracht | "Hoe voelde het om het te zeggen?" |
| Na anticipatie | "Was het spannend of makkelijk?" |
| Na eigen initiatief | "Wat koos je? Zou je het nog eens doen?" |
| Na nieuwheid | "Was dit anders dan verwacht?" |
| Algemeen | "Was dit leuk?" |

### Reflectiedagen (periodiek)

| Dag | Inhoud |
|-----|--------|
| 5 | Afsluiting fase 0. "Fijn dat je er bent. Volgende week een beetje verder." |
| 14 | Terugblik 2 weken. Overzicht + "Hoe voelt dat?" |
| 28 | Maandoverzicht. Wat ging goed? Counter: "X initiatieven, X aanrakingen, X keuzes." |
| 42 | Check tempo. "Voelt het goed zo?" |
| 56 | Grote mijlpaal. "Wat heb je geleerd?" + counter |
| 70 | Items-reflectie. "Hoe voelde dat?" |
| 84 | 3-maanden reflectie. "Wat kun je nu dat je toen niet kon?" + volledige counter |

### Langetermijn erkenning (bij reflectiedagen)
```
"Dit hebben jullie de afgelopen weken gedaan:
• 8 initiatieven
• 5 bewuste aanrakingen
• 3 keuzes gemaakt
• 2x zelf iets bedacht"
```
Geen score. Geen ranking. Alleen erkenning van groei.

---

## SOFT RESET BIJ VERGETEN

Als Lisanne 3+ dagen de app niet opent of niks doet:

**Geen schuld. Geen "je loopt achter."**

Tekst bij terugkomst:
"Hé, welkom terug. Geen probleem dat je even weg was. Pak gewoon iets kleins op."

Scheduler:
- Eerste dag terug: gewoon_jullie of presence
- Tweede dag: bevestiging (licht)
- Derde dag: terug naar focus (maar zachter dan waar ze was)

---

## APP-INTRODUCTIE (onboarding)

### Toon
Licht, nieuwsgierig, geen probleemframing.

### Lisanne ziet

**Scherm 1**: "Dit is een app voor jullie samen. Kleine suggesties om het leuk te houden."

**Scherm 2**: "Je krijgt elke dag iets. Soms iets om te doen, soms iets om te zeggen, soms gewoon even samen zijn."

**Scherm 3**: "Er is geen goed of fout. Doe wat goed voelt. Sla over wat niet past."

### Lisanne ziet NIET
- "Leerpad", "progressie", "fase"
- Scores, percentages, streaks
- Verwijzingen naar dynamiek/FLR/BDSM
- Enig gevoel van "je relatie heeft een probleem"

---

## SAMENVATTING: ALLES WAT VERANDERT

| Onderdeel | Was | Wordt |
|-----------|-----|-------|
| Start | Dag 1 = eerste suggestie | Fase 0: 5 dagen warmte eerst |
| Dagkeuze | Random pool + filters | Scheduler met dagtype, weekbalans, energiecheck |
| Leerpaden | Lineaire ladder | Golven: focus + doorloop + bijlijn, nooit stoppen |
| Mechanismes | Impliciet | 4 doorlopende lagen: bevestiging, anticipatie, nieuwheid, presence |
| Taal | Direct vanaf dag 1 | Eerst zacht ("ik wil dat..."), daarna direct |
| Suggesties | Allemaal specifiek | Mix specifiek + open varianten per stap |
| Reflectie | fijn/niks/teveel | + "reactie viel tegen" + verdiepende vraag 20-30% |
| Eigen initiatief | Niet gemeten | Erkend, telt 2x, beïnvloedt progressie |
| Failsafe | Niet aanwezig | Warme reactie + afkoeling + geen escalatie |
| Tim | Vaag ("wees geduldig") | Concrete dagelijkse reminders gekoppeld aan context |
| Vergeten | Niet afgehandeld | Soft reset: warm welkom terug, geen schuld |
| Humor | Weinig | 5+ humor-suggesties in Gewoon jullie |
| Presence | Niet apart | Eigen categorie: er-zijn zonder actie |
| Success loops | Alleen reflectiedagen | + tussentijdse "dit gaat goed" bij 3+ positieve reeks |
| Erkenning | Vaag | Concrete counter: X initiatieven, X aanrakingen |
| Onboarding | Niet ontworpen | 3 schermen: licht, speels, geen probleemframing |
| Energiecheck | Niet aanwezig | Optioneel: laag/normaal/goed beïnvloedt suggestiegewicht |
| Escalatie | 4 weken tot regie-avond | Checkpoints: 3 positieve ervaringen + eigen initiatief vereist |
| Opdrachttaal | Direct | Eerst "ik wil dat..." (week 1-3), dan mix, dan direct |
