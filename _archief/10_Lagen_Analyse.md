# Sprankelend Souffleur — 10-Lagen Analyse

---

## 1. Conceptuele Architectuur

**Twee fase-systemen die niet syncen:**
- LESSEN gebruiken fase 0-4 (via `getEffectieveLesjesFase`)
- KERN_LP gebruikt fase 0-6 (via `_bepaalActiefLeerpad` → `s4.fase`)
- **Probleem**: Lisanne kan in kern-fase 5 zitten terwijl lessen maar tot fase 4 gaan. Lessen 19-22 worden dan gateless — ze kan kritieke lessen overslaan.
- **Fix**: Cap `s4.fase` op 4, óf maak lessen voor fase 5-6.

**Les 7 is de enige fysieke veiligheidsgate:**
- Eén "gelezen" klik opent ALLE fysieke item-suggesties
- Geen begripscheck, geen herleesmechanisme
- Lisanne kan Les 7 in 30 seconden doorskimmen en krijgt dan direct bondage-suggesties

---

## 2. Dynamiek-Logica

**Wat goed werkt:**
- naLes-velden koppelen items aan Les 7, sensory aan Les 8, en practice-suggesties aan Les 9/15/17/21
- minDagen voorkomt te snelle escalatie
- De sensory-brug blokkeert blinddoek/kaarsen tot Les 8 gelezen is

**Wat beter kan:**
- Veel suggesties (vooral micro/relationeel) hebben GEEN naLes — ze kunnen theoretisch verschijnen zonder dat Lisanne de context begrijpt
- Fase 0→1 gaat na 5 dagen — dat is kort voor de basisprincipes (richting geven, grenzen voelen)
- De sprong van fase 2 naar 3 is groot: van "zachte sturing" naar "items en impact"

---

## 3. UX & Gebruiksflow

**Overbelasting-risico:**
- Op één dag kan Lisanne zien: suggestie + mini-lesje + energiecheck + handleiding-toggle + waarom-toggle = 4-5 tekstlagen
- Er is geen "skip dit lesje" knop
- 30+ dagen = 30+ micro-beslissingen (energie kiezen, ja/nee/ander)

**Wat goed werkt:**
- Graceful fallbacks voorkomen lege pools
- "Niet nu" (7d), "Niks voor mij" (4-8w), "Dit klopt niet" (permanent) geven uitwegen
- Energie "laag" verzacht automatisch
- **Mist**: een "pauzeer app voor 3 dagen" knop of "sla deze hele categorie over"

**Waar het te schools voelt:**
- Les 7 als verplichte poort vóór speelgoed — voelt als huiswerk
- Mini-lesjes die verschijnen als je gewoon wilt spelen

---

## 4. Psychologische Consistentie

**Lisanne als kiezer — meestal goed:**
- Gescheiden views (Lisanne ziet Tim's warmte-systeem niet)
- Les 12 herframed als "wat jij hieraan hebt"
- Geen "Tim wil dit" berichten in haar feed

**Subtiel Tim-centrisch:**
- "Tim reageert sterk op kleine signalen" → metric is Tim's reactie
- "De hint zelf doet al iets" → impliciet: Tim's anticipatie
- Vastmaak: "controle" als doel, Tim als object
- **Beter**: herframe naar "Jij voelt de macht" in plaats van "Tim reageert"

---

## 5. Scheduler-Gedrag

**Boost-stacking probleem:**
- Elke boost is onafhankelijk (flatMap). Als een suggestie matcht op thema + comfort + wens + novelty:
  1×3×3×2 = 18× dezelfde suggestie in de pool
- **Fix**: Cap totale boost op 4× per suggestie

**gewoon_jullie loop-risico:**
- Na soft reset → forceerZacht=true → altijd gewoon_jullie
- Kan 7+ dagen herhalen zonder breaker
- **Fix**: Auto-break na 5+ gewoon_jullie achter elkaar

**Beschermende regel (2 intense in 3 dagen):**
- Conservatief maar blokkeert escalatie midden in een success-reeks
- Beter: gate op successReeks in plaats van alleen count

---

## 6. Suggestie-Kwaliteit

**watJeKuntMerken dekking:**
- Slechts 36 van 665+ suggesties (5%) hebben een `watJeKuntMerken` veld
- 95% van suggesties mist concrete feedback op of de actie werkte
- **Fix**: Prioriteer watJeKuntMerken voor de 50 meest-getoonde suggesties

**Kind-aanwezig:**
- Slechts 4 expliciete Milou-vermeldingen in suggesties
- Milou-boost op regel 7788 verdrievoudigt op_afstand suggesties maar filtert niet op geschiktheid
- **Fix**: Voeg `milouVeilig:false` veld toe aan suggesties die écht niet met kind in huis kunnen

**Vibe-concentratie:**
- 107 spanning-suggesties (16%), 95 speels (14%), 82 controle (12%)
- Veel spanning zonder genoeg zachte alternatieven
- 52 vastmaak-suggesties zijn variaties op hetzelfde thema

---

## 7. Ontwerpfouten / Logicafouten

**Dead path — reflectie dagtype:**
- Als dagtype='reflectie' geselecteerd wordt, returned de functie `null`
- Als renderVandaag dit niet correct afvangt → leeg scherm

**Pool-modifier conflicten:**
- Milou-boost (3×) + Humor-boost (3×) = 9× voor humor bij Milou aanwezig
- Geen max-cap op replicatie

**Novelty modifier + successReeks:**
- Na 4× fijn + novelty: nieuwe suggesties krijgen 2× EN stretch-boost 3× = overrepresentatie van onbekend + intens

**Soft reset na 2+ weken:**
- Geen hard reset van weekCounter, successReeks, zachteReeks
- Na 14 dagen pauze heeft successReeks=4 van vóór de pauze nog steeds effect
- **Fix**: Hard reset successReeks na 10+ dagen gemist

---

## 8. Content-Architectuur

**Practice-suggesties bestaan nu (net toegevoegd):**
- Les 9 → sr01-03 (seks-regie)
- Les 15 → im01-02 (impact)
- Les 17 → rf01-02 (regels/flexibiliteit)
- Les 21 → ps01-03 (psychologisch spel)

**Lessen die te veel uitleggen:**
- Les 21 (Psychologisch Spel) is 9000+ woorden met zero walkthrough
- Les 15 (Impact) geeft fysiologische details maar geen stappenplan
- **Fix**: Korter, concreter, meer "doe dit vanavond"

**Content gap:**
- Geen UI voor het instellen/tracken van eigen regels (Les 17 leert dit maar systeem ondersteunt het niet)
- Geen mechanisme om Tim's mentale staat te tracken (Les 21 noemt dit maar app kan het niet)

---

## 9. Groeicurve

**Fase 0 te kort (5 dagen):**
- Onboarding duurt 5 dagen, daarna direct fase 1
- Basisprincipes (richting geven, grenzen voelen) hebben meer tijd nodig
- **Fix**: Verhoog naar 7-10 dagen

**Progressie-gates realistisch?**
- Eis: 3 afgeronde suggesties + 1 eigen initiatief per leerpad
- Er zijn maar 4 suggesties met `eigenInitiatief:true` — progressie hangt vooral af van "ja" zeggen
- eigenInitiatief-flag zit alleen op nieuwheid-mechanisme suggesties
- **Fix**: Meer suggesties markeren als eigenInitiatief-telbaar, of gate verlagen naar alleen 3× ja

**Vastlopen in fase:**
- Mogelijk maar niet slecht — voorkomt geforceerde escalatie
- **Probleem**: Lisanne heeft geen inzicht in WAAROM suggesties "zacht" blijven
- **Fix**: Subtiele hint "Je hebt nog geen [categorie] gedaan — dat opent nieuwe mogelijkheden"

**successReeks overshoot:**
- Na 4× fijn: alle escalatie-boosts tegelijk actief (zwaarte 2 + opbouw + stretch)
- Geen demper — positieve feedback-spiraal kan overshooten vóór "teveel" triggered
- **Fix**: Maximaal 2 boost-lagen tegelijk

---

## 10. Edge Cases

**2 weken pauze:**
- Soft reset na 3 dagen (goed), maar geen hard reset van counters na 10+ dagen
- successReeks=4 van vóór de pauze blijft actief → te snelle escalatie bij terugkeer

**Alles "ja" voor 3 weken:**
- successReeks raakt maximum, alle boosts actief
- Systeem biedt alleen advanced content → lichtgewicht suggesties verdwijnen
- Geen decay-mechanisme op successReeks

**Alles "nee" voor 2 weken:**
- Na de bailout-conditie (alleNee + geen initiatief + teveel "teveel") → returned NULL
- **Leeg scherm** in plaats van recovery-suggesties
- **Fix**: Nooit null returnen, altijd minstens een zachte relationeel-suggestie

**Energie altijd "moe":**
- Hele week locked op spoor 1 (relationeel, zwaarte ≤1)
- Correct gedrag, maar GEEN indicatie naar gebruiker dat energie progressie blokkeert
- **Fix**: Na 7 dagen "laag" → hint "misschien energie aanpassen?"

**Tim's warmte altijd "koud":**
- Soft-gate beperkt maxZwaarte tot 1 en 60% kans op forceerZacht
- Correct maar Lisanne weet niet waarom alles zacht is
- **Fix**: Subtiele feedback "De app houdt rekening met jullie ritme"

**Milou altijd aanwezig:**
- Pool beperkt tot subtiele suggesties — correct
- Maar na 30 dagen alleen subtiel → Lisanne denkt dat app kapot is
- **Fix**: Na 14 dagen alleen subtiel → hint "Plan een avondje zonder Milou?"

**Geen lessen gelezen:**
- Items/sensory geblokkeerd → pool beperkt tot micro/opdracht/relationeel
- App werkt, maar gebruiker ziet geen hint dat lessen content unlocken

---

## Prioriteiten Samenvatting

### Kritiek (moet gefixt)
1. Bailout → NULL bij veel afwijzing (leeg scherm)
2. successReeks reset na lange pauze
3. Boost-cap (max 4× per suggestie)

### Belangrijk (zou moeten)
4. Fase 0 verlengen naar 7-10 dagen
5. gewoon_jullie loop-breaker
6. Meer watJeKuntMerken toevoegen (top-50 suggesties)
7. Herframe Tim-centrische teksten naar Lisanne-centrisch

### Kan beter
8. Progressie-hints ("dit opent nieuwe mogelijkheden")
9. "Pauzeer app" knop
10. Milou-veilig flag op suggesties
11. Les 21 inkorten
12. Eigen-regels UI
