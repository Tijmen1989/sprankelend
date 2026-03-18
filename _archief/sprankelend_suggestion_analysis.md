# SPRANKELEND Suggestion System - Technical Analysis

## 1. SUGGESTION STORAGE & DATA STRUCTURE

### Main State (localStorage key: `l_suggesties`)
```javascript
{
  historie: [{id, datum, status: 'ja'|'nee'|'ander'|'nietnu'|'niksvoormij'|'rustig'|'lichter', cat}],
  huidig: {id, datum, cat, tekst, ...full suggestion object} or null,
  niveau: 1-3,        // escalation/deescalation level
  laatsteCategorie: null,
  laatsteActieType: null,
  stilteWeek: boolean,
  weekCounter: number,
  wachtOpErvaring: boolean,
  ervaringLog: [{datum, val: 'fijn'|'neutraal'|'teveel'|'reactie_viel_tegen'|...}],
  typeHistorie: [{type, status: 'ja'|'nee', datum}],
  permanentBlock: [id, id, ...],
  lisanneFavorieten: [id, id, ...],
  uitgesteld: {cat, terugOp: datum},
  lopend: {id, cat, tekst, startDatum, duurDagen}
}
```

### Suggestion Object Format
```javascript
{
  id: string,
  cat: 'micro'|'relationeel'|'opdracht'|'vastmaak'|'sessie'|'dynamiek',
  spoor: 'A'|'B'|'C',  // Often relates to theme/intensity
  zwaarte: 1-3,        // Weight/difficulty
  type: 'face_to_face'|'digitaal'|'op_afstand'|'etc',
  items: [],           // Physical items needed ['collar','polsboeien','blinddoek',...]
  subtiel: boolean,    // Can show when Milou (child) is present
  opbouw: boolean,
  minDagen: number,    // Minimum days active before this can show
  vibe: string,
  
  // CORE FIELDS
  tekst: string,       // Main suggestion text for Lisanne
  zegSubtiel: string,  // What to say when subtle (Milou present)
  zegPrive: string,    // What to say in private
  actieType: string,   // 'stem', 'relationeel', 'item', 'fysiek_item', etc.
  
  // LESSON-LINKING (KEY FOR PRACTICE FLOW)
  naLes: number,       // Lesson ID that unlocks this (e.g., naLes: 9)
  
  // SPOOR 4 (4-track system)
  spoor4: 1-4,         // Track intensity level
  
  // ADDITIONAL CONTEXT
  inzicht: string,     // Why this works (coaching)
  waarom: string,      // Alternative explanation
  watJeKuntMerken: string,  // What to observe in Tim
  naMoment: string,    // After-care instructions
  disclaimer: string,
  leerpad: number,     // Learning path indicator (0 = fase 0)
  stap: number,        // Step within learning path
  core: boolean,       // Essential in this learning path
  stretch: boolean,    // Optional challenge
  herhalingFraming: boolean,  // Framing for repeated suggestions
  samenFraming: boolean,      // Framing for together-time
  mechanisme: string,  // 'bevestiging', 'anticipatie', 'nieuwheid', etc.
  eigenInitiatief: boolean,   // Initiative marker for Tim's tracking
}
```

---

## 2. SUGGESTION SELECTION ALGORITHM

### Main Function: `kiesSuggestie(state)`
Location: Line 7767+

**Execution flow (pseudocode):**

```
FUNCTION kiesSuggestie(state):
  // ─── BAILOUT CHECKS ───
  IF all_recent_nee AND no_initiatief_lastMonth AND 2+_teveel → RETURN null
  IF stilteWeek AND no_lopend → RESET lopend; mark stilteWeek
  
  // ─── SOFT RESET CHECK ───
  IF daysGemist >= 3 → SET forceerZacht = true (soft reset)
  IF daysGemist >= 10 → RESET successReeks + zachteReeks (hard reset)
  
  // ─── FAILSAFE CHECKS ───
  IF lastExperience = 'teveel' AND daysAgo <= 2 → SET forceerZacht
  IF lastExperience = 'reactie_viel_tegen' AND daysAgo <= 1 → SET forceerZacht
  IF last_2_status = ['nee','nee'] → SET forceerZacht
  IF lastIntensity >= 2 → maxZwaarte = 1; ELSE maxZwaarte = niveau + 1
  IF timWarmte = 'koud' → maxZwaarte = 1; 60% chance forceerZacht
  
  // ─── FASE 0 CHECK (days 1-5) ───
  IF fase = 0 AND daysActive < 5:
    → Filter SUGGESTIE_POOL for leerpad = 0
    → Return random from pool
  
  IF fase = 0 AND daysActive >= 5 → UPDATE fase to 1
  
  // ─── DETERMINE DAY TYPE ───
  IF forceerZacht:
    dagtype ∈ ['gewoon_jullie','presence','bevestiging']
  ELSE IF Sunday:
    IF reflectiedag → 'reflectie'
    ELSE → ['gewoon_jullie','presence','rust']
  ELSE IF Friday (Milou home):
    → ['digitaal_bevestiging', 'digitaal_anticipatie', 'gewoon_jullie', 'presence']
  ELSE IF Saturday:
    → ['gewoon_jullie', 'presence', 'bevestiging', 'licht_focus']
  ELSE (Mon-Thu):
    Track weekly spoor 4 counts
    IF focusCount < 2 → ['focus', 'bevestiging', 'gewoon_jullie', 'presence']
    ELSE IF bevestigingCount < 1 → ['bevestiging', 'focus', 'gewoon_jullie', 'presence']
    ELSE → diverse mix with lighter content
  
  // ─── LISANNE SIGNAL BOOST ───
  IF was_fijn in last 2 days AND !forceerZacht → 50% dagtype = 'herhaling'
  IF wil_proberen in last 2 days AND !forceerZacht → 50% dagtype = 'nieuwheid'|'focus'
  
  // ─── PROTECTION RULE ───
  IF 2+ intense in last 3 days AND dagtype != 'gewoon_jullie'|'presence':
    → dagtype = 'gewoon_jullie'
  
  // ─── FILTER POOL BY DAGTYPE ───
  FILTER SUGGESTIE_POOL WHERE:
    - NOT in recent 15 (recenteIds)
    - zwaarte <= maxZwaarte
    - NOT blocked (isSuggestieGeblokkerd)
    - dagtype matches
    - [KEY] IF s.naLes: REQUIRE lesson in _lesVoortgang.gelezen
    - [KEY] IF items.length > 0: REQUIRE les 7 (tiksignalen)
    - [KEY] IF sensory items: REQUIRE les 8 (zintuigen)
  
  // ─── PICK & RETURN ───
  RETURN random from filtered pool OR null
```

### Key Safety Gates
1. **Lesson-linked suggestions**: `if(s.naLes && !_lesVoortgang.gelezen.includes(s.naLes)) return false`
2. **Physical items require Les 7** (tiksignalen + aftercare)
3. **Sensory items require Les 8** (blinddoek, etc.)
4. **Warm gate**: `if(_timWarmte === 'koud')` softens suggestions

---

## 3. SUGGESTION LOADING & DISPLAY FLOW

### When New Suggestion Loads
**Location:** Line 11114 in `renderApp()`

```javascript
// Load new suggestion only if:
// 1. state.huidig is null (user accepted/rejected previous)
// 2. User hasn't seen one today
IF !state.huidig AND !seenTodayAlready:
  suggestie = kiesSuggestie(state)
  IF suggestie:
    state.huidig = { ...suggestie, datum: today(), bron: 'systeem' }
    saveSuggestieState(state)
```

### Rendering: `renderVandaag(state)`
**Location:** Line 12251+

1. **Blocking checks first** (terugkom-check, evaluatie) → early return
2. **Status bar** (energy + agenda preview)
3. **Week-thema kaart** (learning path progress)
4. **MAIN CARD selector:**
   - IF `wachtOpErvaring` → show experience check (fijn/neutraal/teveel/etc)
   - ELSE IF `reflectieVraag today` → show reflection prompt
   - ELSE IF `state.huidig` → show suggestion card
   - ELSE → show "nothing" state or prompts
5. **Suggestion card contains:**
   - Framing context ("Idee voor vandaag:")
   - Suggestion text
   - "Zeg dit" example (subtiel or prive variant)
   - Support info (waarom, what to notice, etc.)
   - **Buttons: "Dit doe ik" | "Ander idee"**

---

## 4. "DIT DOE IK" / "ANDER IDEE" FLOW

### "Dit doe ik" (Accept)
**Function:** `verwerkKeuze('ja')` (Line 8671+)

```
1. Add to historie: {id, datum: today(), status: 'ja', cat}
2. IF lopend.duurDagen → state.lopend = {id, cat, tekst, startDatum, duurDagen}
3. Determine if experience check needed:
   - If zwaarte >= 2 OR first time this category OR random 33%
   - → state.wachtOpErvaring = true
4. Escalation: if last 3 = 'ja' AND niveau < 3 → niveau++
5. Track spoor 4 if eigenInitiatief
6. state.huidig = null
7. Check wens expiry
8. RENDER → shows experience check next
```

### "Ander idee" (Alternative)
**Function:** `verwerkKeuze('ander')` (Line 8750+)

```
1. Check if in "ruzie-modus" or "warmte-pauze":
   - IF YES → reject, show "Rustige periode"
   - RETURN

2. Count andrCount++
3. IF andrCount >= 3:
   - andrCount = 0
   - Build pool from different categories (not current cat)
   - Filter by: recent, blocked, zwaarte
   - state.huidig = NEW SUGGESTION from pool
   - RENDER → shows new suggestion immediately

4. ELSE:
   - state.huidig = null
   - RENDER → shows "Wat nu?" state
```

---

## 5. LESSON-PRACTICE INTEGRATION (naLes)

### Current Lesson-Linked Suggestions: `LESPRACTICE_SUGGESTIES`
**Location:** Line 3630+

Format example:
```javascript
{
  id: 'sr01',
  cat: 'micro',
  naLes: 9,  // "Unlock after les 9"
  spoor4: 3,
  tekst: "Pak Tim's hand en leg hem ergens neer...",
  // ... rest of suggestion
}
```

Lessons with practice suggestions:
- **Les 9**: Pace control, direction ("seks op jouw voorwaarden")
- **Les 15**: Impact (tikken, bijten)
- **Les 17**: Rules & flexibility
- **Les 21**: Psychological play
- **Les 7, 8**: Gate requirements (items, sensory)

### Safety Bridge Check
**Location:** Line 8102 in `_basisFilter()`

```javascript
if(s.naLes && !_lesVoortgang.gelezen.includes(s.naLes)) 
  return false;  // Hide suggestion until lesson read
```

---

## 6. HOW TO INJECT LESSON-PRACTICE ACTIONS (PRIORITY FLOW)

### Architecture for Priority Lesson-Linked Suggestions

To make lesson-practice suggestions take priority over regular pool:

#### Step 1: Extend `kiesSuggestie()` with Priority Check
**Insert after STAP 5 (dagtype determination), BEFORE STAP 7 (pool filtering):**

```javascript
// ═══════════════════════════════════════════════
// PRIORITY CHECK: Lesson-linked suggestions
// ═══════════════════════════════════════════════
const _lesVoortgang = getLesVoortgang();
const _recentlyReadLesId = _lesVoortgang.gelezen.length > 0 
  ? _lesVoortgang.gelezen[_lesVoortgang.gelezen.length - 1] 
  : null;

if(_recentlyReadLesId){
  const _lessonPracticeSuggestions = SUGGESTIE_POOL.filter(s => 
    s.naLes === _recentlyReadLesId &&
    !recenteIds.includes(s.id) &&
    s.zwaarte <= maxZwaarte &&
    !isSuggestieGeblokkeerd(state, s.id)
  );
  
  // IF lesson practice suggestions available: prioritize them
  if(_lessonPracticeSuggestions.length > 0){
    const chosen = pick(_lessonPracticeSuggestions);
    window._schedulerLog.dagtype = 'lesson_practice_' + _recentlyReadLesId;
    window._schedulerLog.gekozen = chosen.id + ' (lesson_practice)';
    return chosen;
  }
}
// ═══════════════════════════════════════════════
```

#### Step 2: Track "Recently Read Lesson" State
Add to `getSuggestieState()`:
```javascript
lessonPracticeLead: null,  // {lesId, startedAt, suggestionsShown: []}
```

#### Step 3: Mark Lesson as "in Practice Mode"
After `_lesMarkeerGelezen()` (line 4657+), add:
```javascript
const sugState = getSuggestieState();
sugState.lessonPracticeLead = {
  lesId: lesNr,
  startedAt: today(),
  suggestionsShown: []
};
saveSuggestieState(sugState);
```

#### Step 4: Prevent Lesson-Practice Spam
Modify priority check:
```javascript
const _practiceLead = state.lessonPracticeLead;
if(_practiceLead && daysSince(_practiceLead.startedAt) <= 7){
  // Only show max 3 suggestions from this lesson in 7 days
  if(_practiceLead.suggestionsShown.length >= 3){
    // Fall through to regular logic
  } else {
    // Show lesson practice suggestion
    const chosen = pick(_lessonPracticeSuggestions);
    _practiceLead.suggestionsShown.push(chosen.id);
    // ... return chosen
  }
}
```

---

## 7. STATE MANAGEMENT - KEY localStorage KEYS

| Key | Type | Purpose |
|-----|------|---------|
| `l_suggesties` | Object | Main suggestion state (histoire, huidig, niveau, etc.) |
| `l_lesVoortgang` | Object | Lesson reading progress: `{gelezen: [1,2,3], huidig: 4, gelezenOp: {1: '2026-03-17'}}` |
| `l_zachteReeks` | Number | Count of soft/easy days in sequence |
| `l_signalen_voor_tim` | Array | Lisanne's signals: `{type: 'was_fijn'|'wil_proberen', datum}` |
| `l_eersteKeerCat` | Object | Track first-time category frames: `{micro: true, vastmaak: true}` |
| `l_lastSuggestieDatum` | Date string | Last time suggestion was accepted |
| `l_initiatief_log` | Array | Tim's initiative tracking |

---

## 8. TIMING & SCHEDULER

### When Suggestions Appear
1. **On app load** (`renderApp()` line 11114): If `state.huidig === null`, call `kiesSuggestie()`
2. **After user choice**: Once user accepts/rejects, `state.huidig` is set to null, triggering next load on next render
3. **No hard refresh needed**: Suggestion scheduler is **reactive** to user interactions

### Duration & Expiry
- **Daily suggestion**: New one each day (same one can repeat if user keeps saying "ander")
- **Lopend (ongoing) suggestions**: Lasts `duurDagen` (usually 1-7 days)
- **Experience check**: Always shown after high-weight suggestions (zwaarte >= 2) or first new category
- **Automatic expiry**: Suggestion older than 1 day is replaced

---

## 9. CONCEPT: LESSON-LINKED SUGGESTIONS ALREADY EXISTS

**YES, partially implemented:**
- `LESPRACTICE_SUGGESTIES` array (3630+) contains 16 suggestions with `naLes` properties
- Safety gate in `_basisFilter()` (8102) prevents showing unless lesson read
- But **no priority system** — they compete with regular pool

**To make truly priority:**
1. Add check in `kiesSuggestie()` BEFORE general filtering
2. Return lesson-practice suggestion if available (don't fall through to dagtype)
3. Track "recently read lesson" in state to manage frequency
4. Add cap (max 3 per lesson over 7 days) to prevent spam

---

## 10. IMPLEMENTATION CHECKLIST

To add full lesson-practice priority system:

- [ ] Add `lessonPracticeLead` to suggestion state
- [ ] Insert priority check in `kiesSuggestie()` (after STAP 5)
- [ ] Update `_lesMarkeerGelezen()` to set `lessonPracticeLead`
- [ ] Add frequency cap (3 per lesson per 7 days)
- [ ] Add debug log entry in `window._schedulerLog`
- [ ] Test with multiple lessons (9, 15, 17, 21)
- [ ] Verify no conflict with "Ander idee" logic
- [ ] Ensure lesson practice suggestions still respect gates (items = les 7, sensory = les 8)

