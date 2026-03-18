# SPRANKELEND - Code Location Reference

## Critical Function Locations

### Suggestion Selection & Management
| Function | Line | Purpose |
|----------|------|---------|
| `kiesSuggestie(state)` | 7767 | Main suggestion selection algorithm (250+ lines) |
| `getSuggestieState()` | 6874 | Load suggestion state from localStorage |
| `saveSuggestieState(s)` | 6893 | Save suggestion state to localStorage |
| `verwerkKeuze(keuze)` | 8671 | Handle "Dit doe ik" / "Ander idee" / other responses |
| `renderVandaag(state)` | 12251 | Render main "Vandaag" tab with suggestions |
| `_basisFilter(s)` | 8093 | Filter function used in suggestion pool selection |

### Lesson Integration
| Function | Line | Purpose |
|----------|------|---------|
| `getLesVoortgang()` | 4029 | Load lesson progress from localStorage |
| `_lesMarkeerGelezen()` | 4656 | Mark lesson as read (client-side callback) |
| `_scrollLesMarkeerGelezen()` | 4416 | Mark scrollable lesson as read |
| `toonLes(lesNr)` | ~4500+ | Display lesson modal |
| `toonScrollLes(les, kleur)` | 4111 | Display scrollable lesson |

### Data Pools
| Pool | Line | Count | Purpose |
|------|------|-------|---------|
| `SUGGESTIE_POOL` | 1154 | 200+ | Main suggestion pool (aggregates all pools) |
| `LESPRACTICE_SUGGESTIES` | 3630 | 16 | Lesson-linked suggestions (naLes property) |
| `ONTDEKKING_SUGGESTIES` | 3302 | ~20 | Discovery suggestions (fase 3) |
| `GEWOON_JULLIE` | ~3382 | ~20 | Everyday intimacy suggestions |
| `LICHAMELIJKE_ACTIVITEITEN` | ~3610 | ~10 | Physical activity suggestions |
| `KERN_LP1-6` | 7350+ | 100+ | Learning path core suggestions (stap, leerpad) |

### Rendering & UI
| Function | Line | Purpose |
|----------|------|---------|
| `renderApp()` | 11100 | Main app render entry point |
| `renderVandaag()` | 12251 | Vandaag tab content |
| `renderLessenOverzicht()` | 4718 | Lessons list view |
| `renderGids()` | ~11300+ | Guide/help tab |
| `renderRegelen()` | ~11500+ | Planning/scheduling tab |

### Experience Tracking
| Function | Line | Purpose |
|----------|------|---------|
| `logErvaringMetUndo(val)` | ~12400+ | Log experience feedback (fijn/neutraal/teveel) |
| `skipExperienceCheck()` | ~12600+ | Skip experience feedback |
| `logTerugkomAntwoord(val)` | ~12700+ | Log comeback check |

---

## Key State Structures in localStorage

### Suggestion State (`l_suggesties`)
```javascript
// Location: Loaded via getSuggestieState() line 6874
{
  historie: Array<{id, datum, status, cat}>,
  huidig: Object|null,           // Current suggestion or null
  niveau: 1|2|3,                 // Escalation level
  wachtOpErvaring: boolean,      // Waiting for feedback
  ervaringLog: Array,
  typeHistorie: Array,
  permanentBlock: Array,         // IDs to never show again
  lisanneFavorieten: Array,      // User's favorites
  lopend: Object|null,           // Ongoing suggestion
  stilteWeek: boolean,           // Quiet week flag
  weekCounter: number,
  lessonPracticeLead: null|Object // [PROPOSED] Track after lesson read
}
```

### Lesson Progress (`l_lesVoortgang`)
```javascript
// Location: Loaded via getLesVoortgang() line 4029
{
  gelezen: Array<number>,        // Read lesson IDs [1, 2, 5, ...]
  huidig: number,                // Current lesson pointer
  meerLezenGeopend: Array,
  gelezenOp: Object,             // {lesId: "2026-03-17", ...}
  oefenTeller: Object            // {lesId: [{datum: "2026-03-17"}, ...]}
}
```

---

## Pool Composition & Filtering

### How SUGGESTIE_POOL is Built (Lines 1154-7633)
```
1. Start: SUGGESTIE_POOL = [] (line 1154)

2. Add core pools:
   - SPOOR_A_POOL (lines ~2000-2200) → push at line 2210
   - SPOOR_B_POOL (lines ~2000-2200) → push at line 2210

3. Add contextual pools:
   - OVERDAG_POOL (lines 2213-2299) → push at 2299
   - ONTDEKKING_SUGGESTIES (lines 3302-3376) → push at 3378
   - GEWOON_JULLIE (lines 3381-3557) → push at 3561
   - SAMEN_ERUIT (lines 3545-3557) → push at 3558
   - LICHAMELIJKE_ACTIVITEITEN (lines 3565-3624) → push at 3624
   - LESPRACTICE_SUGGESTIES (lines 3630-3690) → push at 3691  [KEY FOR LESSONS]

4. Add specialized pools:
   - BEVESTIGING_POOL (lines 7198-7202) → push at 7203
   - ANTICIPATIE_POOL (lines 7205-7235) → push at 7235
   - NIEUWHEID_POOL (lines 7237-7258) → push at 7258
   - HUMOR_POOL (lines 7260-7283) → push at 7283
   - PRESENCE_POOL (lines 7285-7309) → push at 7309
   - FASE0_POOL (lines 7312-7345) → push at 7345

5. Add learning path pools:
   - KERN_LP1-6 (lines 7350-7633) → all push at 7632-7633

Final pool has 200+ suggestions, searchable by naLes property
```

---

## Filtering & Safety Gates (Critical for Lesson-Practice)

### Main Filter Chain in `kiesSuggestie()`

**Stap 0-5:** Determine constraints
- Line 7788-7927: Calculate energy, soft reset, failsafe checks
- Line 7932-7948: Fase 0 check
- Line 7964-8034: Determine dagtype (day type)

**Stap 7:** Build filter
- Line 8093-8113: `_basisFilter()` defines what's eligible
  - **Line 8102**: LESSON GATE - `if(s.naLes && !_lesVoortgang.gelezen.includes(s.naLes)) return false`
  - **Line 8104**: ITEM GATE - all items require les 7
  - **Line 8108**: SENSORY GATE - blinddoek/oordopjes/etc require les 8

**Where to inject priority check:** Between line 8087 and line 8093 (before _basisFilter applies to dagtype pool)

---

## Key Variables & Helpers

### Time Tracking
| Variable | Line | Purpose |
|----------|------|---------|
| `today()` | Used throughout | Returns "YYYY-MM-DD" string |
| `debugNow()` | Used throughout | Returns Date object (respects debug override) |
| `daysSince(dateStr)` | Utility | Calculates days between date and now |

### State Accessors
| Function | Line | Purpose |
|----------|------|---------|
| `getSpoor4State()` | ~6900+ | Get 4-track intensity state |
| `saveSpoor4State()` | ~6900+ | Save 4-track intensity state |
| `getThemaState()` | ~6500+ | Get theme/domein progress |
| `getAgendaDag(date)` | ~11000+ | Get planned activities for day |

### Utility Helpers
| Function | Line | Purpose |
|----------|------|---------|
| `pick(array)` | Utility | Random selection from array |
| `weightedPick(options)` | Utility | Weighted random selection |
| `pickStabiel(arr, seed)` | Utility | Deterministic selection (same seed = same pick) |
| `isMilouAanwezig()` | ~7500+ | Is child present? |
| `isZachtModus()` | ~7500+ | Is soft/gentle mode active? |
| `isSuggestieGeblokkeerd(state, id)` | ~7500+ | Is suggestion blocked? |

---

## Debugging & Logs

### Window Debug Object
```javascript
window._schedulerLog = {
  totaal: number,           // Total in pool
  naEnergie: number,
  naRecent: number,
  naZwaarte: number,
  naGates: number,
  naRemmen: number,
  kandidaten: number,       // Filtered count
  dagtype: string,          // Selected day type
  forceerZacht: boolean,
  zachteReeks: number,
  gekozen: string,          // Selected ID + reason
  reden: string,
  filters: Array,
  warmteEffect: string,
  bescherming: string
}
```

**Access in browser console:**
```javascript
window._schedulerLog  // Latest scheduler run
getSuggestieState()   // Current state
getSpoor4State()      // 4-track intensity
SUGGESTIE_POOL.filter(s => s.naLes === 9)  // Find les 9 suggestions
```

---

## Integration Points for Lesson-Practice Priority

### Point 1: After Lesson Marked as Read
**File Location:** Line 4656+ (`_lesMarkeerGelezen()`)
**Action:** Mark lesson as "in practice mode" in suggestion state

### Point 2: In kiesSuggestie() Main Logic
**File Location:** Line 7767-8400 (kiesSuggestie function)
**Action:** Add priority check AFTER line 8087, BEFORE line 8088

### Point 3: During Pool Filtering
**File Location:** Line 8093-8113 (_basisFilter)
**Action:** No change needed; existing naLes gate works fine

### Point 4: When User Accepts Suggestion
**File Location:** Line 8671-8750 (verwerkKeuze)
**Action:** Track suggestion in lessonPracticeLead.suggestionsShown

### Point 5: Experience Feedback
**File Location:** Line 12382-12413 (experience check in renderVandaag)
**Action:** Standard flow unchanged

---

## Testing Checkpoints

To verify lesson-practice priority system works:

1. **Mark lesson 9 as read**
   - Call: `getLesVoortgang().gelezen.push(9); LS.set('l_lesVoortgang', ...)`
   - Verify: Next suggestion chosen should have `naLes: 9`

2. **Check that naLes gate blocks**
   - Get suggestion with naLes: 15 (unread)
   - Verify: _basisFilter returns false

3. **Verify Spoor 4 is tracked**
   - Accept suggestions with spoor4: 3, 4
   - Check: getSpoor4State().weekSpoorTelling

4. **Check "ander" doesn't bypass lesson-practice priority**
   - Accept lesson-practice suggestion
   - Click "ander" (if count < 3)
   - Verify: Shows different suggestion (not another lesson-practice)

5. **Verify safety gates still work**
   - Try showing suggestion with items but les 7 not read
   - Verify: Blocked by line 8104

---

## File Path Summary
**Single file:** `/sessions/determined-eager-mayer/mnt/Sprankelend/index.html` (~870KB)
- All HTML, CSS, and JavaScript in one file
- Modular by function naming (prefix: `render*`, `get*`, `save*`, `handle*`, `log*`)
- State persistence via localStorage only (no backend)
- Reactive rendering via `renderApp()` → called after every state change

