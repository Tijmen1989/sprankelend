# Sprankelend Souffleur — Verbeterplan + 3 Mechanismes

## WAAR IK AFWIJK VAN DE OPDRACHT (en waarom)

### Tag-explosie → bewust beperkt houden
De opdracht vraagt 9+ nieuwe velden per suggestie (inzichtNr, novelty, anticipatie, bevestiging, autonomieScore, relatieWarmte, dynamiekNiveau, vibeType, leerpad). Dit is over-engineering voor een single-file PWA. Elke suggestie krijgt nu al 12+ velden. Meer velden = meer onderhoud, meer bugs, minder overzicht.

**Mijn aanpak**: 4 nieuwe velden die 90% van de waarde dekken:
- `mechanisme` — welk van de 3 mechanismes dit raakt (anticipatie/bevestiging/nieuwheid/null)
- `inzicht` — korte zin die context geeft vóór de actie
- `reflectieVraag` — optionele verdiepende vraag na de actie (niet altijd)
- `eigenInitiatief` — boolean: telt als eigen initiatief als Lisanne dit zelf doet buiten de app om

De rest (warmte, dynamiekniveau, etc.) is al af te leiden uit bestaande velden (cat, spoor, zwaarte, vibe).

### "noveltyPulse" als mechanic → verwerkt als tag, niet als apart systeem
Een los novelty-systeem is te complex. Nieuwheid zit al in de variatie-per-stap aanpak. Wat wél werkt: bepaalde suggesties taggen als `mechanisme:'nieuwheid'` zodat de scheduler ze kan spreiden.

### Leerpaden hernoemen → ja, maar niet te ver
"Ik mag iets doen" is inderdaad iets te therapeutisch. Maar namen als "Een beetje meer van jou" zijn te vaag — Lisanne moet snappen wat het pad inhoudt. Mijn voorstel:

| Oud | Nieuw | Waarom |
|-----|-------|--------|
| Ik mag iets doen | Kleine signalen | Lichter, speelser, minder "toestemming" |
| Ik bepaal iets | Jij kiest | Korter, actiever |
| Ik mag het lijf | Dichterbij | Minder klinisch, warmer |
| Ik mag spanning maken | Iets beginnen | Speelser, minder geladen |
| Ik mag items gebruiken | Iets nieuws proberen | Normaler, minder BDSM-frame |
| Ik maak een moment | Jouw avond | Simpel, krachtig |

---

## 1. VERBETERD 30-DAGENSYSTEEM

### Kernverandering: van ladder naar golven

Het oude systeem: stap 1 → 2 → 3 → 4 → 5 (ladder omhoog).
Het nieuwe systeem: golven die terugkomen, elke keer iets verder.

Elke week heeft een **mix van 5 lagen**:

| Laag | % in week 1-2 | % in week 3-4 | Altijd minimaal |
|------|---------------|---------------|-----------------|
| Focus-pad | 40% | 40% | 2x per week |
| Doorloop eerder pad | 10% | 20% | 1x per week |
| Bevestiging/gezien | 20% | 15% | 2x per week |
| Gewoon jullie (warmte) | 20% | 15% | 2x per week |
| Nieuwheid/anticipatie | 10% | 10% | 0-1x per week |

### Week 1-2: Focus "Kleine signalen"

**Dag 1 (ma) — Bevestiging**
"Stuur Tim: 'Ik dacht net aan je.' Zonder context."
Mechanisme: bevestiging. Tim voelt: ik word gezien.
Inzicht: "Tim reageert sterk op kleine signalen van jouw kant."

**Dag 2 (di) — Focus: Kleine signalen, stap 1**
"Loop langs Tim en laat je hand even over zijn rug gaan. Doorlopen."
Mechanisme: —. Pure oefening in initiatief.
Inzicht: "Het hoeft niet groot te zijn. Klein is genoeg."

**Dag 3 (wo) — Gewoon jullie**
"Vertel Tim iets grappigs van vandaag. Of iets dat je dwars zit. Maakt niet uit — het gaat om het delen."
Mechanisme: —. Warmte. Geen les.

**Dag 4 (do) — Focus: Kleine signalen, stap 1 (variant)**
"Raak Tim aan op zijn buik als je langsloopt. Hand iets langer laten liggen."
Mechanisme: —. Herhaling met variatie.
Reflectievraag (30% kans): "Was dit makkelijker dan de vorige keer?"

**Dag 5 (vr) — Anticipatie (licht)**
"Stuur Tim: 'Vanavond even jij en ik.' Meer niet."
Mechanisme: anticipatie. Eerste hint-suggestie. Digitaal = veilig (Milou thuis).
Inzicht: "Je hoeft niet te weten wat je gaat doen. De hint zelf doet al iets."

**Dag 6 (za) — Gewoon jullie**
"Ga expres even tegen Tim aan zitten. Geen reden. Gewoon dichtbij."

**Dag 7 (zo) — Rust**
Geen suggestie. "Vandaag even niks. Jullie zijn goed bezig."

---

**Dag 8 (ma) — Bevestiging**
"Kijk Tim bewust aan. 5 seconden. Zeg niks."
Mechanisme: bevestiging. Gezien worden via oogcontact.
Inzicht: "Oogcontact is een van de sterkste signalen die je kunt geven."

**Dag 9 (di) — Focus: Kleine signalen, stap 2**
"Zeg iets over Tim's lichaam. 'Je ziet er goed uit.' Of specifieker."
Mechanisme: bevestiging. Van aanraken naar woorden.

**Dag 10 (wo) — Nieuwheid**
"Doe vandaag iets dat je normaal niet doet met Tim. Maakt niet uit wat. Een ander soort aanraking, een onverwacht compliment, iets kleins."
Mechanisme: nieuwheid. Eerste novelty-moment. Heel vrij.
Reflectievraag: "Wat koos je? Was het spannend of makkelijk?"

**Dag 11 (do) — Focus: Kleine signalen, stap 2 (stevig)**
"Pak Tim's pols vast. Kort, stevig. Laat weer los."
Mechanisme: —. Stevigheid als nieuwe variant.
Inzicht: "Stevig aanraken is niet hard. Het is duidelijk."

**Dag 12 (vr) — Anticipatie**
"Stuur Tim overdag: 'Vanavond heb ik plannen.' Geen verdere uitleg."
Mechanisme: anticipatie. Digitaal, veilig.

**Dag 13 (za) — Doorloop Kleine signalen + eigen keuze**
"Raak Tim aan — waar je wilt, hoe je wilt. Jij kiest."
Mechanisme: —. Eerste eigen-keuze-moment.
Reflectievraag: "Wat koos je? Zou je het nog eens doen?"

**Dag 14 (zo) — Reflectie**
Geen suggestie. Overzicht van 2 weken. "Dit deed je. Hoe voelt dat?"

---

### Week 3-4: Focus "Jij kiest" + doorloop "Kleine signalen"

**Dag 15 (ma) — Focus: Jij kiest, stap 1**
"Kies vanavond wat jullie eten. Niet overleggen — jij kiest."
Mechanisme: —. Laagdrempeligste beslissing.
Inzicht: "Kiezen voelt misschien raar. Dat is normaal. Tim vindt het fijn."

**Dag 16 (di) — Bevestiging + doorloop**
"Geef Tim een compliment dat je normaal voor jezelf houdt."
Mechanisme: bevestiging. Doorloop van "Kleine signalen".

**Dag 17 (wo) — Gewoon jullie**
"Kies samen een film. Geen telefoon erbij. Gewoon kijken."

**Dag 18 (do) — Focus: Jij kiest, stap 2**
"Zeg tegen Tim: 'Jij ruimt de keuken op.' Niet vragen. Mededelen."
Mechanisme: —. Verschil voelen tussen vragen en zeggen.
Reflectievraag: "Hoe voelde het om het te zeggen in plaats van te vragen?"

**Dag 19 (vr) — Anticipatie + Jij kiest**
"Stuur Tim: 'Later wil ik iets van je.' Verder niks."
Mechanisme: anticipatie + jij kiest (ze bepaalt dat er iets komt).

**Dag 20 (za) — Gewoon jullie**
"Herinner Tim aan iets leuks dat jullie samen deden. Gewoon zeggen."

**Dag 21 (zo) — Rust**
Geen suggestie.

---

**Dag 22 (ma) — Doorloop Kleine signalen (stevig)**
"Leg je hand plat op Tim's borst. Voel even zijn hartslag."
Mechanisme: bevestiging. LP1 stopt niet.

**Dag 23 (di) — Focus: Jij kiest, stap 3 (combo)**
"Zeg tegen Tim dat hij de keuken opruimt. Als hij bezig is: loop langs, knuffel van achteren."
Mechanisme: —. Combo: opdracht + spontaan moment.
Inzicht: "Een opdracht hoeft niet streng te zijn. Het is een aanleiding voor een leuk moment."

**Dag 24 (wo) — Nieuwheid**
"Kies vanavond iets zonder overleg. Maakt niet uit wat — eten, serie, muziek, bedtijd. Het gaat om het kiezen."
Mechanisme: nieuwheid.

**Dag 25 (do) — Focus: Jij kiest, stap 3 (herhaling)**
"Laat Tim thee zetten. Als hij het brengt: trek hem even naar je toe. Kort."
Mechanisme: —. Combo herhaling.

**Dag 26 (vr) — Bevestiging**
"Stuur Tim: 'Je zag er net goed uit.' Gewoon dat."
Mechanisme: bevestiging. Digitaal (Milou thuis).

**Dag 27 (za) — Focus: Jij kiest, stap 4 (eigen)**
"Bedenk zelf een opdracht voor Tim. Maakt niet uit wat. Het gaat erom dat jij het bedenkt."
Mechanisme: —. Eerste keer zelf bedenken.
Reflectievraag: "Wat koos je? Hoe reageerde Tim?"

**Dag 28 (zo) — Reflectie**
Maandoverzicht. Wat deed ze? Wat was het makkelijkst? Waar wil ze meer van?

---

### Wat anders is dan het oude plan

| Aspect | Oud plan | Nieuw plan |
|--------|----------|------------|
| Structuur | Ladder: stap 1→2→3→4→5 | Golven: mix per week |
| Bevestiging | Af en toe een compliment | Structureel 2x per week, als doorlopende laag |
| Anticipatie | Niet apart benoemd | Bewust 1x per week, licht in begin |
| Nieuwheid | Niet aanwezig | 1x per 1-2 weken, heel vrij |
| Escalatie | Week 4 = "jij bepaalt de hele avond" | Week 4 = "bedenk zelf een opdracht" (veel zachter) |
| Vrije dagen | Restcategorie | Structureel 2x per week, even belangrijk als focus |
| Reflectie | fijn/niks/teveel | + verdiepende vraag bij 20-30% (afwisselend) |
| Eigen initiatief | Niet gemeten | Actief erkend + zwaarder meegeteld |

---

## 2. KERNINZICHTEN (10 stuks)

Inzichten verschijnen op de suggestiekaart vóór de actie. Kort, warm, geen uitleg tenzij Lisanne erop tikt.

### Fase 1: Kleine signalen (week 1-4)

**Inzicht 1**: "Tim reageert sterk op kleine signalen van jouw kant. Het hoeft niet groot te zijn."
Uitleg (achter toggle): "Uit alles wat Tim vertelt blijkt: het zijn niet de grote gebaren die hem raken, maar de kleine. Een aanraking in het voorbijgaan, een berichtje zonder aanleiding. Die dingen zijn voor hem bewijs dat je aan hem denkt."

**Inzicht 2**: "Stevig aanraken is niet hard. Het is duidelijk."
Uitleg: "Als je Tim's pols vastpakt of je duim in zijn schouder drukt, voelt hij geen pijn — hij voelt dat jij er bent. Stevigheid is een andere taal dan zachtheid, en Tim verstaat die taal goed."

**Inzicht 3**: "Je hoeft niet te weten wat je gaat doen. De hint zelf doet al iets."
Uitleg: "Als je Tim een berichtje stuurt met 'vanavond heb ik plannen', maakt het niet uit of je die plannen al hebt. Het berichtje zelf creëert iets — bij Tim, maar ook bij jou. Het is een deur die je openzet."

**Inzicht 4**: "Kiezen voelt misschien raar. Dat is normaal. Tim vindt het fijn als jij kiest."
Uitleg: "In veel relaties is 'wat wil jij?' de standaard. Maar Tim reageert beter op duidelijkheid. Niet omdat hij niet kan kiezen, maar omdat jouw keuze hem rust geeft."

### Fase 2: Dichterbij (week 5-8)

**Inzicht 5**: "Tim's lichaam is niet iets dat je 'mag' aanraken. Het is van jullie samen."
Uitleg: "Je hoeft geen toestemming te voelen om Tim aan te raken. Zijn lichaam reageert op jouw aanraking — niet als gunst, maar als verbinding. Dat is normaal in een relatie."

**Inzicht 6**: "Anticipatie is krachtiger dan het moment zelf."
Uitleg: "Het wachten, het niet-weten, het 'straks' — dat zijn de momenten waarin spanning groeit. Je hoeft niet alles af te maken. Juist het opbouwen en dan stoppen is ontzettend krachtig."

**Inzicht 7**: "Als iets niet landt, heb jij niks fout gedaan."
Uitleg: "Soms doe je iets en reageert Tim minder dan je verwacht. Dat zegt niks over jou. Het kan zijn moment niet zijn, hij kan in zijn hoofd zitten, of het effect komt later. Jij deed goed door het te proberen."

### Fase 3: Items en momenten (week 9-12)

**Inzicht 8**: "Een blinddoek is geen seks-ding. Het is een manier om aanraking intenser te maken."
Uitleg: "Als Tim niks ziet, wordt elke aanraking sterker. Niet omdat het 'kinky' is, maar omdat zijn andere zintuigen het overnemen. Jij bepaalt wat hij voelt."

**Inzicht 9**: "Jij hoeft dit niet te 'willen' zoals Tim het wil. Jij mag het op jouw manier doen."
Uitleg: "Tim geniet van de dynamiek op zijn manier. Jij hoeft dat niet te kopiëren. Als jij het doet omdat je ziet dat het hem iets geeft — dan is dat reden genoeg. Je hoeft er niet dezelfde kick van te krijgen."

**Inzicht 10**: "Wat je nu kunt, kon je 3 maanden geleden niet. Dat is niet niks."
Uitleg: "Terugkijkend: je stuurt berichtjes, je raakt aan, je kiest, je bouwt spanning op, je gebruikt items, je maakt momenten. Dat is niet 'de app volgen' — dat is iets nieuws leren en het eigen maken."

---

## 3. NIEUWE DATASTRUCTUUR SUGGESTIES

### Huidige velden (behouden)
```
id, cat, spoor, zwaarte, type, items, subtiel, opbouw, minDagen, vibe, tekst,
zegSubtiel, zegPrive, actieType, voorWie
```

### Nieuwe velden (toevoegen)
```javascript
{
  // BESTAAND (ongewijzigd)
  id: 'ks01',
  cat: 'relationeel',        // relationeel, micro, opdracht, vastmaak, sessie
  spoor: 'A',                // A=licht, B=dieper, C=dynamiek
  zwaarte: 1,                // 1-3
  type: 'face_to_face',      // face_to_face, digitaal, op_afstand
  items: [],
  subtiel: true,
  opbouw: false,
  minDagen: 0,
  vibe: 'warm',              // warm, speels, controle
  tekst: '...',
  zegSubtiel: null,
  zegPrive: null,
  actieType: 'aanraking',    // aanraking, stem, digitaal, relationeel
  voorWie: null,             // null=lisanne, 'tim'=tim

  // NIEUW
  leerpad: 1,                // 1-6, welk leerpad deze suggestie hoort
  stap: 2,                   // stap binnen het leerpad (voor progressie)
  mechanisme: 'bevestiging', // null, 'anticipatie', 'bevestiging', 'nieuwheid'
  inzicht: 'Tim reageert sterk op kleine signalen van jouw kant.',
  inzichtUitleg: 'Uit alles wat Tim vertelt blijkt: ...',  // achter toggle
  reflectieVraag: 'Was dit makkelijker dan de vorige keer?', // null = geen vraag
  eigenInitiatief: false     // true = telt als eigen initiatief als Lisanne dit zelf bedenkt
}
```

### Waarom deze 6 velden en niet 9+

| Gevraagd veld | Beslissing | Reden |
|---------------|------------|-------|
| novelty | → mechanisme:'nieuwheid' | Eén veld voor alle 3 mechanismes |
| anticipatie | → mechanisme:'anticipatie' | Idem |
| bevestiging | → mechanisme:'bevestiging' | Idem |
| vibeType | → bestaand veld `vibe` | Bestaat al |
| relatieWarmte | → afleidbaar uit cat + vibe | Niet apart nodig |
| dynamiekNiveau | → afleidbaar uit zwaarte + spoor | Niet apart nodig |
| autonomieScore | → `eigenInitiatief` boolean | Simpeler, zelfde functie |
| inzichtNr | → `inzicht` direct als tekst | Geen lookup-tabel nodig |
| leerpad + stap | → `leerpad` + `stap` | Ja, deze zijn nodig |

---

## 4. SCHEDULER-REGELS (PSEUDOCODE)

```
functie kiesDagSuggestie(lisanneState, historie, dagenActief):

  // ─── STAP 0: Bepaal actief leerpad ───
  actiefPad = bepaalActiefLeerpad(lisanneState)
  huidigeStap = bepaalHuidigeStap(actiefPad, historie)
  dagVanWeek = getDagVanWeek()  // 0=zo, 1=ma, ...

  // ─── STAP 1: Bepaal dagtype ───
  als dagVanWeek == 0:
    return RUST  // zondag altijd rust

  als dagVanWeek == 6:
    dagtype = kiesUit(['gewoon_jullie', 'licht_focus'], [60, 40])

  als dagVanWeek == 5:
    dagtype = kiesUit(['digitaal_bevestiging', 'digitaal_anticipatie', 'gewoon_jullie'], [40, 30, 30])

  anders:  // ma-do
    dagtype = kiesDagtypeOpBasis(weekSchema)

  // ─── STAP 2: Weekschema (ma-do) ───
  // Doel: 2x focus, 1x bevestiging, 1x mix (gewoon_jullie/doorloop/nieuwheid)
  weekSchema:
    als week_heeft_nog_geen_focus:
      dagtype = 'focus'
    als week_heeft_1x_focus_maar_geen_bevestiging:
      dagtype = kiesUit(['focus', 'bevestiging'], [50, 50])
    als week_heeft_2x_focus:
      dagtype = kiesUit(['bevestiging', 'gewoon_jullie', 'doorloop', 'nieuwheid'],
                         [30, 30, 25, 15])
    als week_heeft_focus_en_bevestiging:
      dagtype = kiesUit(['focus', 'gewoon_jullie', 'doorloop', 'nieuwheid'],
                         [35, 30, 25, 10])

  // ─── STAP 3: Kies suggestie op basis van dagtype ───

  als dagtype == 'focus':
    pool = suggesties.filter(s =>
      s.leerpad == actiefPad
      && s.stap == huidigeStap
      && s.minDagen <= dagenActief
      && nietRecentGebruikt(s, historie, 7)  // niet in afgelopen 7 dagen
    )
    return kiesRandom(pool)

  als dagtype == 'bevestiging':
    pool = suggesties.filter(s =>
      s.mechanisme == 'bevestiging'
      && s.minDagen <= dagenActief
      && nietRecentGebruikt(s, historie, 5)
    )
    return kiesRandom(pool)

  als dagtype == 'doorloop':
    vorigePaden = allePaden.filter(p => p < actiefPad)
    pool = suggesties.filter(s =>
      vorigePaden.includes(s.leerpad)
      && s.minDagen <= dagenActief
      && nietRecentGebruikt(s, historie, 7)
    )
    return kiesRandom(pool)

  als dagtype == 'gewoon_jullie':
    pool = GEWOON_JULLIE.filter(s => nietRecentGebruikt(s, historie, 10))
    return kiesRandom(pool)

  als dagtype == 'nieuwheid':
    pool = suggesties.filter(s =>
      s.mechanisme == 'nieuwheid'
      && s.minDagen <= dagenActief
      && nietRecentGebruikt(s, historie, 14)  // nieuwheid minder vaak
    )
    als pool.leeg: return kiesDagtypeOpBasis('gewoon_jullie')  // fallback
    return kiesRandom(pool)

  als dagtype == 'digitaal_anticipatie':
    pool = suggesties.filter(s =>
      s.mechanisme == 'anticipatie'
      && s.type == 'digitaal'
      && s.minDagen <= dagenActief
    )
    return kiesRandom(pool)

  // ─── STAP 4: Veiligheidsregels ───

  REGEL: Geen 2 zware suggesties achter elkaar
    als gisteren.zwaarte >= 2:
      vandaag moet zwaarte <= 1 OF dagtype == 'gewoon_jullie'

  REGEL: Na 'teveel' reactie → afkoelen
    als laatsteReactie == 'teveel':
      volgende 2 dagen: alleen gewoon_jullie of bevestiging

  REGEL: Anticipatie max frequentie
    als dagenActief < 14: max 1x per 5 dagen
    als dagenActief 14-28: max 1x per 3 dagen
    als dagenActief > 28: max 2x per week

  REGEL: Nieuwheid max frequentie
    als dagenActief < 14: max 1x per 10 dagen
    als dagenActief 14-28: max 1x per week
    als dagenActief > 28: max 2x per week

  REGEL: Bevestiging minimum
    elke week minstens 2 suggesties met mechanisme:'bevestiging'
    (ook als een ander dagtype gekozen is, bevestiging mag altijd bijgemixed)

  // ─── STAP 5: Progressie ───

  functie bepaalHuidigeStap(pad, historie):
    voor elke stap in pad:
      aantalFijn = historie.filter(h =>
        h.leerpad == pad && h.stap == stap && h.ervaring == 'fijn'
      ).length
      aantalTeveel = historie.filter(h =>
        h.leerpad == pad && h.stap == stap && h.ervaring == 'teveel'
      ).length
      aantalPogingen = historie.filter(h =>
        h.leerpad == pad && h.stap == stap
      ).length

      als aantalFijn >= 2: ga door naar volgende stap
      als aantalPogingen >= 4: ga door (maar met zachter aanbod)
      als aantalTeveel >= 2: ga terug naar vorige stap
      anders: blijf bij deze stap

    return huidigeStap

  // ─── STAP 6: Doorstroom naar volgend leerpad ───

  functie bepaalActiefLeerpad(state):
    voor elk leerpad (1-6):
      stappen = aantalStappen(leerpad)
      afgerond = aantalAfgerondeStappen(leerpad, historie)
      eigenInitiatieven = historie.filter(h =>
        h.leerpad == leerpad && h.eigenInitiatief == true
      ).length

      als afgerond >= 3 EN eigenInitiatieven >= 1:
        // klaar voor volgend pad als focus
        ga door

    return hoogsteOntgrendeldePad

  // ─── STAP 7: Failsafe bij neutrale/tegenvallende reactie ───

  als lisanneReactie == 'reactie_viel_tegen':
    // NIET: suggereren dat zij iets fout deed
    // WEL: warme bevestiging
    toonBericht: "Dat zegt niks over wat jij deed. Soms komt iets anders aan
                  dan verwacht. Kleine dingen hebben soms later pas effect."
    volgendeDag: forceer dagtype = 'gewoon_jullie' of 'bevestiging'
    verlaagEscalatie: volgende focus-suggestie mag niet zwaarder zijn

  // ─── STAP 8: Eigen initiatief belonen ───

  als lisanneMeldt('eigenInitiatief'):
    toonBericht: "Mooi dat je dat zelf deed."  // warm, kort, geen overdrijving
    verhoogProgressie: telt als 2x 'fijn' voor de huidige stap
    verhoogKans: meer vergelijkbare suggesties in komende dagen
    // NIET: confetti, badges, scores. Gewoon erkenning.
```

---

## 5. TWINTIG VOORBEELDSUGGESTIES

### 1. Bevestiging — gezien worden (week 1+)
```javascript
{id:'bv01', cat:'relationeel', spoor:'A', zwaarte:1, type:'digitaal',
 items:[], subtiel:true, opbouw:false, minDagen:0, vibe:'warm',
 leerpad:1, stap:1, mechanisme:'bevestiging',
 inzicht:'Tim reageert sterk op kleine signalen van jouw kant.',
 reflectieVraag:null,
 eigenInitiatief:false,
 tekst:'Stuur Tim een berichtje: \'Ik dacht net aan je.\' Zonder context — laat hem invullen.',
 zegSubtiel:null, zegPrive:null, actieType:'digitaal'}
```
**Waarom veilig**: Digitaal, geen face-to-face druk, geen verwachting.
**Mechanisme**: Bevestiging — Tim voelt: ze denkt aan me.

### 2. Bevestiging — lichamelijk (week 1+)
```javascript
{id:'bv02', cat:'relationeel', spoor:'A', zwaarte:1, type:'face_to_face',
 items:[], subtiel:true, opbouw:false, minDagen:3, vibe:'warm',
 leerpad:1, stap:3, mechanisme:'bevestiging',
 inzicht:'Oogcontact is een van de sterkste signalen die je kunt geven.',
 reflectieVraag:'Merkte je iets aan Tim toen je hem aankeek?',
 eigenInitiatief:false,
 tekst:'Kijk Tim bewust aan. Houd zijn blik 5 seconden vast. Zeg niks.',
 zegSubtiel:null, zegPrive:null, actieType:'relationeel'}
```
**Waarom veilig**: Geen aanraking nodig, geen woorden.
**Mechanisme**: Bevestiging — bewust gezien worden.

### 3. Bevestiging — woorden (week 1+)
```javascript
{id:'bv03', cat:'relationeel', spoor:'A', zwaarte:1, type:'face_to_face',
 items:[], subtiel:true, opbouw:false, minDagen:3, vibe:'warm',
 leerpad:1, stap:3, mechanisme:'bevestiging',
 inzicht:null,
 reflectieVraag:null,
 eigenInitiatief:false,
 tekst:'Zeg iets over Tim\'s lichaam. \'Je ziet er goed uit.\' Of specifieker: zijn armen, zijn rug.',
 zegSubtiel:null, zegPrive:null, actieType:'stem'}
```
**Waarom veilig**: Compliment, geen actie verwacht.
**Mechanisme**: Bevestiging — Tim voelt zich aantrekkelijk.

### 4. Bevestiging — onverwacht (week 2+)
```javascript
{id:'bv04', cat:'relationeel', spoor:'A', zwaarte:1, type:'digitaal',
 items:[], subtiel:true, opbouw:false, minDagen:7, vibe:'warm',
 leerpad:null, stap:null, mechanisme:'bevestiging',
 inzicht:null,
 reflectieVraag:null,
 eigenInitiatief:false,
 tekst:'Stuur Tim: \'Je zag er net goed uit.\' Gewoon dat. Geen vervolg.',
 zegSubtiel:null, zegPrive:null, actieType:'digitaal'}
```
**Waarom veilig**: Digitaal, kort, geen verwachting.
**Mechanisme**: Bevestiging — doorlopend, niet gekoppeld aan leerpad.

### 5. Anticipatie — eerste hint (week 1+)
```javascript
{id:'an01', cat:'relationeel', spoor:'A', zwaarte:1, type:'digitaal',
 items:[], subtiel:true, opbouw:false, minDagen:3, vibe:'speels',
 leerpad:null, stap:null, mechanisme:'anticipatie',
 inzicht:'Je hoeft niet te weten wat je gaat doen. De hint zelf doet al iets.',
 reflectieVraag:null,
 eigenInitiatief:false,
 tekst:'Stuur Tim: \'Vanavond even jij en ik.\' Meer niet.',
 zegSubtiel:null, zegPrive:null, actieType:'digitaal'}
```
**Waarom veilig**: Geen belofte, geen verwachting. Het berichtje IS het moment.
**Mechanisme**: Anticipatie — spanning door onbekendheid.

### 6. Anticipatie — stoppen (week 2+)
```javascript
{id:'an02', cat:'micro', spoor:'B', zwaarte:1, type:'face_to_face',
 items:[], subtiel:true, opbouw:false, minDagen:7, vibe:'speels',
 leerpad:4, stap:2, mechanisme:'anticipatie',
 inzicht:'Anticipatie is krachtiger dan het moment zelf.',
 reflectieVraag:'Merkte je iets aan Tim toen je wegliep?',
 eigenInitiatief:false,
 tekst:'Loop langs Tim, raak hem kort aan, en loop weer door. Niet stoppen.',
 zegSubtiel:null, zegPrive:null, actieType:'aanraking'}
```
**Waarom veilig**: Kort, terloops, zij bepaalt het tempo.
**Mechanisme**: Anticipatie — iets beginnen en niet afmaken.

### 7. Anticipatie — later (week 2+)
```javascript
{id:'an03', cat:'micro', spoor:'A', zwaarte:1, type:'face_to_face',
 items:[], subtiel:true, opbouw:false, minDagen:10, vibe:'speels',
 leerpad:4, stap:3, mechanisme:'anticipatie',
 inzicht:null,
 reflectieVraag:null,
 eigenInitiatief:false,
 tekst:'Zeg tegen Tim: \'Niet nu. Straks.\' Verder niks. Loop weg.',
 zegSubtiel:null, zegPrive:'Niet nu. Straks.', actieType:'stem'}
```
**Waarom veilig**: Twee woorden. Geen belofte over wat "straks" is.
**Mechanisme**: Anticipatie — uitstel als spanning.

### 8. Anticipatie — digitaal sterk (week 3+)
```javascript
{id:'an04', cat:'micro', spoor:'B', zwaarte:1, type:'digitaal',
 items:[], subtiel:true, opbouw:false, minDagen:14, vibe:'controle',
 leerpad:4, stap:4, mechanisme:'anticipatie',
 inzicht:null,
 reflectieVraag:null,
 eigenInitiatief:false,
 tekst:'Stuur Tim overdag drie losse berichten. \'Vanavond.\' \'Na Milou slaapt.\' \'Ik heb iets bedacht.\' Meer niet.',
 zegSubtiel:null, zegPrive:null, actieType:'digitaal'}
```
**Waarom veilig**: Digitaal, ze hoeft niks bedacht te hebben.
**Mechanisme**: Anticipatie — opbouw via fragmenten.

### 9. Nieuwheid — vrij (week 2+)
```javascript
{id:'nw01', cat:'relationeel', spoor:'A', zwaarte:1, type:'face_to_face',
 items:[], subtiel:true, opbouw:false, minDagen:7, vibe:'speels',
 leerpad:null, stap:null, mechanisme:'nieuwheid',
 inzicht:null,
 reflectieVraag:'Wat koos je? Was het spannend of makkelijk?',
 eigenInitiatief:true,
 tekst:'Doe vandaag iets met Tim dat je normaal niet doet. Maakt niet uit wat — een ander soort aanraking, een onverwacht compliment, iets kleins.',
 zegSubtiel:null, zegPrive:null, actieType:'relationeel'}
```
**Waarom veilig**: Totaal vrij. Geen verwachting. Zij kiest.
**Mechanisme**: Nieuwheid — de afwijking zelf is het doel.

### 10. Nieuwheid — routine breken (week 3+)
```javascript
{id:'nw02', cat:'relationeel', spoor:'A', zwaarte:1, type:'face_to_face',
 items:[], subtiel:true, opbouw:false, minDagen:14, vibe:'speels',
 leerpad:null, stap:null, mechanisme:'nieuwheid',
 inzicht:null,
 reflectieVraag:'Hoe reageerde Tim?',
 eigenInitiatief:true,
 tekst:'Verander vanavond één ding aan jullie routine. Waar jullie zitten, wat jullie doen, wanneer jullie naar bed gaan. Iets kleins.',
 zegSubtiel:null, zegPrive:null, actieType:'relationeel'}
```
**Waarom veilig**: Geen specifieke actie. Zij kiest de verandering.
**Mechanisme**: Nieuwheid — kleine afwijking van patroon.

### 11. Nieuwheid — onverwacht contact (week 3+)
```javascript
{id:'nw03', cat:'micro', spoor:'B', zwaarte:1, type:'face_to_face',
 items:[], subtiel:false, opbouw:false, minDagen:14, vibe:'speels',
 leerpad:null, stap:null, mechanisme:'nieuwheid',
 inzicht:null,
 reflectieVraag:null,
 eigenInitiatief:false,
 tekst:'Trek Tim zonder waarschuwing naar je toe als hij langsloopt. Houd hem even vast. Laat weer los.',
 zegSubtiel:null, zegPrive:null, actieType:'aanraking'}
```
**Waarom veilig**: Kort moment, geen vervolg verwacht.
**Mechanisme**: Nieuwheid — de verrassing is het effect.

### 12. Gewoon jullie — lachen (altijd)
```javascript
{id:'gw01', cat:'relationeel', spoor:'A', zwaarte:1, type:'face_to_face',
 items:[], subtiel:true, opbouw:false, minDagen:0, vibe:'warm',
 leerpad:null, stap:null, mechanisme:null,
 inzicht:null,
 reflectieVraag:null,
 eigenInitiatief:false,
 tekst:'Vertel Tim iets grappigs van vandaag. Of iets dat je dwars zit. Het gaat om het delen.',
 zegSubtiel:null, zegPrive:null, actieType:'relationeel'}
```
**Waarom veilig**: Nul druk. Gewoon praten.
**Mechanisme**: Geen — dit is het fundament.

### 13. Gewoon jullie — nabijheid (altijd)
```javascript
{id:'gw02', cat:'relationeel', spoor:'A', zwaarte:1, type:'face_to_face',
 items:[], subtiel:true, opbouw:false, minDagen:0, vibe:'warm',
 leerpad:null, stap:null, mechanisme:null,
 inzicht:null,
 reflectieVraag:null,
 eigenInitiatief:false,
 tekst:'Ga expres even tegen Tim aan zitten. Geen reden. Gewoon dichtbij.',
 zegSubtiel:null, zegPrive:null, actieType:'relationeel'}
```
**Waarom veilig**: Geen actie, geen prestatie. Gewoon zijn.
**Mechanisme**: Geen — warmte.

### 14. Gewoon jullie — herinnering (altijd)
```javascript
{id:'gw03', cat:'relationeel', spoor:'A', zwaarte:1, type:'face_to_face',
 items:[], subtiel:true, opbouw:false, minDagen:0, vibe:'warm',
 leerpad:null, stap:null, mechanisme:null,
 inzicht:null,
 reflectieVraag:null,
 eigenInitiatief:false,
 tekst:'Herinner Tim aan iets leuks dat jullie samen deden. Gewoon zeggen. Kijken of hij het ook nog weet.',
 zegSubtiel:null, zegPrive:null, actieType:'relationeel'}
```
**Waarom veilig**: Positieve emotie, geen verwachting.
**Mechanisme**: Geen — verbinding via gedeelde geschiedenis.

### 15. Gewoon jullie — waardering (altijd)
```javascript
{id:'gw04', cat:'relationeel', spoor:'A', zwaarte:1, type:'face_to_face',
 items:[], subtiel:true, opbouw:false, minDagen:0, vibe:'warm',
 leerpad:null, stap:null, mechanisme:null,
 inzicht:null,
 reflectieVraag:null,
 eigenInitiatief:false,
 tekst:'Noem één ding dat je aan Tim waardeert. Gewoon hardop zeggen.',
 zegSubtiel:null, zegPrive:null, actieType:'stem'}
```
**Waarom veilig**: Positief, kort, geen druk.
**Mechanisme**: Geen — maar raakt bevestiging (Tim voelt zich gezien).

### 16. Focus LP1 — terloops aanraken (week 1+)
```javascript
{id:'ks01', cat:'micro', spoor:'A', zwaarte:1, type:'face_to_face',
 items:[], subtiel:true, opbouw:false, minDagen:0, vibe:'warm',
 leerpad:1, stap:2, mechanisme:null,
 inzicht:'Het hoeft niet groot te zijn. Klein is genoeg.',
 reflectieVraag:null,
 eigenInitiatief:false,
 tekst:'Loop langs Tim en laat je hand even over zijn rug gaan. Niet stoppen, doorlopen.',
 zegSubtiel:null, zegPrive:null, actieType:'aanraking'}
```
**Waarom veilig**: Terloops, kort, geen oogcontact nodig.
**Mechanisme**: Geen — pure oefening in initiatief.

### 17. Focus LP2 — mededelen (week 3+)
```javascript
{id:'ks02', cat:'opdracht', spoor:'A', zwaarte:1, type:'face_to_face',
 items:[], subtiel:true, opbouw:false, minDagen:14, vibe:'controle',
 leerpad:2, stap:2, mechanisme:null,
 inzicht:'Kiezen voelt misschien raar. Dat is normaal. Tim vindt het fijn.',
 reflectieVraag:'Hoe voelde het om het te zeggen in plaats van te vragen?',
 eigenInitiatief:false,
 tekst:'Zeg tegen Tim: \'Jij ruimt de keuken op.\' Niet vragen. Mededelen.',
 zegSubtiel:null, zegPrive:'Keuken opruimen.', actieType:'stem'}
```
**Waarom veilig**: Huishoudelijk, klein, concreet.
**Mechanisme**: Geen — leren beslissen.

### 18. Focus LP2 — combo (week 3+)
```javascript
{id:'ks03', cat:'opdracht', spoor:'A', zwaarte:1, type:'face_to_face',
 items:[], subtiel:true, opbouw:false, minDagen:14, vibe:'warm',
 leerpad:2, stap:3, mechanisme:null,
 inzicht:'Een opdracht hoeft niet streng te zijn. Het is een aanleiding voor een leuk moment.',
 reflectieVraag:null,
 eigenInitiatief:false,
 tekst:'Zeg tegen Tim dat hij de keuken opruimt. Als hij bezig is: loop langs en geef hem een knuffel van achteren.',
 zegSubtiel:null, zegPrive:'Keuken opruimen. Nu.', actieType:'relationeel'}
```
**Waarom veilig**: De opdracht is normaal, de knuffel is spontaan.
**Mechanisme**: Geen — maar raakt bevestiging (Tim voelt zich gewild).

### 19. Eigen initiatief — erkenning
```javascript
{id:'ei01', cat:'relationeel', spoor:'A', zwaarte:1, type:'face_to_face',
 items:[], subtiel:true, opbouw:false, minDagen:7, vibe:'warm',
 leerpad:null, stap:null, mechanisme:null,
 inzicht:null,
 reflectieVraag:'Wat deed je? Hoe voelde het?',
 eigenInitiatief:true,
 tekst:'Doe vandaag iets voor Tim dat niet in de app staat. Iets dat van jou komt. Maakt niet uit wat.',
 zegSubtiel:null, zegPrive:null, actieType:'relationeel'}
```
**Waarom veilig**: Totaal vrij. Nul druk. Zij kiest.
**Mechanisme**: Geen — maar bouwt autonomie.

### 20. Failsafe — warmte na tegenvaller
```javascript
{id:'fs01', cat:'relationeel', spoor:'A', zwaarte:1, type:'face_to_face',
 items:[], subtiel:true, opbouw:false, minDagen:0, vibe:'warm',
 leerpad:null, stap:null, mechanisme:null,
 inzicht:'Als iets niet landt, heb jij niks fout gedaan.',
 reflectieVraag:null,
 eigenInitiatief:false,
 tekst:'Ga vanavond gewoon lekker naast Tim zitten. Niks bijzonders. Gewoon samen zijn is ook goed.',
 zegSubtiel:null, zegPrive:null, actieType:'relationeel'}
```
**Waarom veilig**: Geen prestatie. Geen verwachting. Alleen warmte.
**Mechanisme**: Geen — herstel na tegenvaller.

---

## SAMENVATTING: WAT ER VERANDERT

| Onderdeel | Oud | Nieuw |
|-----------|-----|-------|
| Dagkeuze | Random uit pool met filters | Scheduler met dagtype + weekbalans |
| Leerpaden | Lineaire ladder | Golven: focus + doorloop + bijlijn |
| Mechanismes | Impliciet | Expliciet: anticipatie, bevestiging, nieuwheid |
| Inzichten | Alleen in Gids | Op suggestiekaart (vóór actie) + reflectie (na actie) |
| Reflectie | fijn/niks/teveel | + verdiepende vraag bij 20-30% |
| Eigen initiatief | Niet gemeten | Erkend, telt 2x, beïnvloedt progressie |
| Failsafe | Niet aanwezig | Warme reactie + afkoeling in scheduler |
| "Gewoon jullie" | Restcategorie | Volwaardig spoor: humor, warmte, samen-zijn |
| Escalatie | Week 4 = "regie-avond" | Week 4 = "bedenk zelf een opdracht" |
| Padnamen | "Ik mag iets doen" | "Kleine signalen" (lichter, speelser) |
| Bevestiging | Af en toe | Structureel 2x per week, doorlopend |
| Datastructuur | 12 velden | +6 velden (leerpad, stap, mechanisme, inzicht, reflectieVraag, eigenInitiatief) |
