# UX Analyse: Sprankelend Souffleur PWA — Lisanne's Experience on iPhone 15

**Date**: 2026-03-18
**Focus**: Complete user experience from home screen to daily interaction
**Device**: iPhone 15 (iOS 17+)
**User**: Lisanne (partner view)

---

## 1. FIRST IMPRESSION: What Lisanne Sees When Opening the App

### Launch Experience
- **PWA Splash Screen**: "Souffleur" appears as a native iOS app icon with dark theme
- **View Selection Screen**: Lands on a centered pin/role-selection screen (not persisted)
- **Design Quality**: Playfair Display serif title, soft midnight blue gradient (#1B1F27), clean two-button layout
- **Friction**: Every session requires choosing "Lisanne" vs "Tim" view — this is intentional to prevent accidental view exposure, but it's one extra tap

### Lisanne's "Vandaag" (Home Tab)
When Lisanne enters her view, the home screen shows:

1. **Status Bar** (Highest Priority - Always Visible)
   - Energy/mood status: "Goed / Normaal / Moe" with emoji (😊 / 🌿 / 😴)
   - Context: "Mooie dag", "Hou het klein", "Iets loopt", or "Klein moment gehad"
   - Tap to toggle energy level — hidden energy picker appears below
   - Agenda preview on right: "📅 Ochtend ▼" or "📅 Geen plannen ▼"
   - **Tap agenda button** → Smooth expand/collapse with safe transitions
   - **Design**: Compact, readable, high touch target (min 44px height)

2. **Week Thema Card** (Educational Anchor)
   - Shows current learning phase (e.g., "Verbinding")
   - Visual progress bar (7 segments) showing phase completion
   - Tap to toggle description — collapsible, doesn't waste space
   - Font: Source Serif 4 for sophistication
   - **Purpose**: Remind Lisanne this is part of a journey, not random suggestions

3. **Main Content Zone** — Priority Resolver
   The app chooses ONE dominant mode:

#### Mode A: Experience Check (After Accepting Suggestion)
- "Hoe voelde dit voor jullie?" with 3 emoji buttons
- "Leuk" (😊), "Oké" (😐), "Te veel" (😢)
- Additional options: "Reactie viel tegen", "Er ging iets mis"
- Heart toggle to favorite (❤️ vs 🧡)
- **Flow**: Suggests → Accept → Do → Return → Rate
- **Design**: Large emoji buttons (clear affordance), centered layout
- **Timing**: Appears 2-6 hours after she said "yes" to a suggestion
- **Psychology**: Frames as reflection, not judgment

#### Mode B: Reflection Question (Daily)
- Targeted follow-up question about a recent moment
- Textarea for optional written response (max 200 chars)
- "Bewaar" (Save) or "Overslaan" (Skip) buttons
- **Design**: Italic question in serif font, intimate tone
- **Trigger**: Random, once per day, if a moment happened
- **Benefit**: Teaches Lisanne to notice her own responses

#### Mode C: Suggestion (Primary Mode)
- **Context Label**: "Misschien leuk vandaag:", "Idee voor vanavond:", "Klein ideetje:" (randomized)
- **Frames** (conditional):
  - "Dit werkte eerder goed voor jullie" (if repeated suggestion)
  - "Vandaag is samen-zijn zelf het moment" (if it's just togetherness)
  - Aftercare hint if intense: "Kleine richting is al genoeg"
- **First-Time Framing**: "Dit is nieuw terrein. Rustig aan is prima."
- **Micro-intent Label**: "Dit is meer dan een klein moment — neem de tijd"
- **Suggestion Text**: Large, readable (1.05rem), in serif font
- **Speech Example**: `"Je mag ook zeggen: 'Zullen we vanavond...?'"`
  Styled as quoted speech with blue left border
- **"Meer info" Toggle**: Collapses at first, expands to show:
  - Disclaimer (safety/context)
  - "Waarom dit werkt" (insight block, blue background)
  - "Wat je kunt merken" (what to expect from Tim)
  - "Let eens op" (observation prompt)
  - Equipment/handleiding links
  - Duration estimate
  - Step-by-step instructions
  - "Na afloop" (aftercare)
  - Related learning phase
- **Mini-lesson Toggle**: "Goed om te weten" — educational snippet inline
- **Action Buttons**:
  - Primary: "✓ Dit doe ik" (blue, 44px height)
  - Secondary: "↻ Ander idee" (less prominent)
- **Rejection Menu** (Tap "Liever niet ▶️"):
  - "Niet nu" (come back later)
  - "Niks voor mij" (not a fit)
  - "Bewaar voor morgen" (try tomorrow)
  - "Wel een kleiner idee" (scale down)
  - "Dit klopt niet voor ons" (feedback)
  - "Vandaag even niet" (pause today)

#### Mode D: Pause/Rest View
- If in pause mode, full-screen motivational message:
  - "Neem de tijd. De app wacht op jullie."
  - "Rust is ook vooruitgang."
  - Can still dismiss to see a suggestion

#### Mode E: Autopilot (Rare)
- Quick suggestion Tim can relay: "Zeg dit tegen Lisanne..."
- For couples establishing rhythm
- Low frequency (not on first week)

#### Mode F: Active Exercise
- "Oefening" card with title, focus, instructions
- Terugblik (reflection) options at bottom
- Teaches both partners communication

---

## 2. GETTING TO A LESSON: Navigation Flow

### Lesson Access Points
1. **From Suggestions**: "Goed om te weten" toggle in suggestion card
2. **From Regelen Tab**: "Gids" section lists all lessons
3. **Deep Link**: If Lisanne taps a lesson preview

### The Lesson Experience: `toonScrollLes()`

#### Visual Design
- **Full-Screen Overlay**: Soft midnight blue radial gradient + backdrop blur (12px)
- **Typography**: Serif throughout (Source Serif 4), generous spacing
- **Safe Areas**: Respects notch and home indicator on iPhone
- **Close Button**: 48px touch target in top-right, circular with subtle background
- **Padding**: 28px top (+ safe-area), 20px sides, 48px bottom (+ safe-area)

#### Content Structure
1. **Header** (always visible)
   - Kicker label: "Jullie basis", "Aanraking & nabijheid", etc. (uppercase, 12px)
   - Large title: 30px serif, bold
   - Optional subtitle: 16px, italic, muted
   - Glow effect above (decorative radial gradient)

2. **Content Blocks** (fade-in animation, staggered)
   - **Scene**: Body text, 18px line-height 1.85 — plenty of breathing room
   - **Inzicht (Insight)**: Left-border accent (3px blue), larger font (20px), bold, quote-like styling
   - **Voorbeeld (Example)**: Subtle background, labeled "ZO KAN HET", may be carousel (swipeable)
   - **Probeer (Try This Week)**: Highlighted card, ends with button/gate
   - **Noot (Note)**: Softer text, contextual

3. **Gate Mechanism** (Prevents Skipping)
   - First section ends with "even lezen..." hint
   - User must scroll through ALL content before "Verder" button appears
   - **No skipping allowed** — teaches reading value
   - Once done: "Verder ▶️" button replaces gate

4. **Q&A Section** ("Verder verkennen")
   - Toggle: "Vragen die je misschien hebt ▼"
   - FAQ items with collapse/expand (↑ ↓ chevrons)
   - Can ask custom question via textarea
   - Tim notified when questions submitted

5. **Footer**
   - "Volgende ontdekking" link to next lesson
   - Only shows after lesson fully read

#### Fonts & Sizing on iPhone 15
- **Title**: 30px — large but not overwhelming
- **Body**: 18px — very readable in portrait
- **Label**: 12px (uppercase) — hierarchy clear
- **Secondary**: 16px — perfect for subtitles
- **Line height**: 1.85 — extremely generous
- **Letter spacing**: Subtle (0.005em) adds sophistication

#### Smooth Interactions
- Fade-in animations per block (0.3s stagger)
- Scroll-snap carousels (for multi-example sections)
- FAQ smooth expand (not instant)
- Transitions: 0.2s on borders, backgrounds
- Momentum scrolling enabled (`-webkit-overflow-scrolling: touch`)

#### Mobile-First Optimizations
- No horizontal overflow
- Touch targets always 44px+ minimum
- Buttons not cramped: `min-height:52px` for primary
- Carousel dots visible and tappable
- Safe-area insets respected (notch, home bar)

**Pain Point**: Lessons are beautiful but long. On a 6.1" screen, some require significant scrolling. **Quick win**: Add progress indicator or "Read time: 5 mins"

---

## 3. HOME TAB LAYOUT: Lisanne's Daily Dashboard

### Tab Navigation (Bottom)
```
✨ Vandaag (home)    📋 Plannen (regelen)    📖 Gids (gids)
```
- Tab height: 44px+ (good for thumbs)
- Icons above labels (no text-only tabs)
- Active tab: Accent blue color change
- Smooth transitions (0.2s)

### "Vandaag" Tab Content Order
1. Status bar + agenda (sticky at top when scrolling)
2. Week thema card (context)
3. Main card (suggestion, experience check, or exercise)
4. Below-fold items (if in specific modes)

### Scrolling Behavior
- Content area: `flex: 1; overflow-y: auto`
- Smooth scrolling enabled
- Scrollbar: Subtle, thin (4px), light blue tint
- Pull-to-refresh: Not implemented (no swipe gesture)
- **Note**: On iPhone 15, average "Vandaag" screen fits without scroll on first load

### "Plannen" (Regelen) Tab
- Manual schedule management
- Day planner with time blocks
- Can set rituals, dates
- Less about suggestions, more about structure
- **Visual**: Cards for each day-item, collapsible

### "Gids" (Guide) Tab
- Lesson index
- Searchable
- Progress indicators (✓ read, ○ not started)
- Grouped by domain (Verbinding, Fysiek, etc.)
- Can browse at own pace

---

## 4. OTHER FEATURES: Navigation & Capabilities

### Settings (Gear Icon, Top-Right Header)
- Opens modal (not full screen)
- Options:
  - Energy level preference
  - Ritual preferences
  - Frequency control
  - Notification settings
  - Trust level adjustment
  - Pause duration picker
  - Debug panel (3-tap on corner)

### Tim View Toggle (👤 Button, Top-Right Header)
- Returns to view selection screen
- Instant switch to Tim's dashboard
- **Design Intent**: Both partners have separate UIs, not cramped into tabs

### Main Content Transitions
- Crossfade between tabs: `app-fading` class
- Duration: 120ms out, render, fade back in
- Very smooth on iPhone 15's ProMotion display
- No janky loading states

### Search/Find
- Not visible in main UI
- Would require lesson database search
- Not a bottleneck for Lisanne (lessons are curated, not overwhelming)

---

## 5. VISUAL DESIGN & MOBILE OPTIMIZATION

### Color Palette
- **Primary Background**: #1B1F27 (soft midnight blue)
- **Surface**: rgba(255,255,255,.06) — very subtle
- **Text**: #F3F6FA (nearly white, not pure white = less strain)
- **Accent**: #7EA7FF (soft blue, not shocking)
- **Success**: #70C4A9 (calm teal)
- **Warm**: #7EA7FF (same as accent, for Tim's view)

### Fonts
1. **Playfair Display** (serif, elegant)
   - Used for: Page titles, section headers, major headings
   - Weights: 400 (regular), 600 (bold)

2. **DM Sans** (modern sans-serif)
   - Used for: Body text, buttons, UI labels
   - Weights: 400, 500, 600, 700

3. **Source Serif 4** (reading serif)
   - Used for: Lesson content, long-form text
   - Weights: 400, 500, 600 + italics
   - **Why**: Improves readability during lessons; signals "content mode"

### Spacing
- **Vertical rhythm**: 0.6rem, 1rem, 1.2rem, 1.5rem increments
- **Horizontal padding**: 1.2rem on sides (slightly inset from edges)
- **Card padding**: 1.3rem to 1.5rem (spacious, not cramped)
- **Gap between sections**: 0.9rem to 1rem (breathing room)

### Radius & Shadows
- Border radius: 18px (main), 14px (secondary)
- Shadows: 0 12px 30px rgba(0,0,0,.22) — subtle depth
- Borders: 1px solid rgba(255,255,255,.08) — barely-there dividers

### Touch Targets
- **Minimum**: 44px height on all buttons (iOS guideline)
- **Padding**: 0.75rem vertical on buttons = ~48px height
- **Gaps between buttons**: 0.6rem (tappable space maintained)
- **Tab bar height**: 44px + safe-area inset bottom = ~52px on iPhone with home bar
- **Lesson close button**: 48x48px (generous)

### Icon & Emoji Usage
- **Tab icons**: 1.3rem (readable, not tiny)
- **Experience buttons**: Large emojis (😊 😐 😢) inside buttons
- **Signal icons**: ✓ ↻ ○ ● for status
- **Section labels**: Uppercase text, no icon clutter

### Dark Mode
- **Enforced**: No light mode toggle; fully dark
- **Rationale**: Fits use case (intimate, evening-friendly, BDSM-context appropriate)
- **Anti-pattern avoided**: No white text on bright backgrounds

---

## 6. STATE MANAGEMENT: How the App Remembers Lisanne

### LocalStorage Keys (User-Visible Behavior)
1. **`l_onboarded`**: First-time flag (hides onboarding after completion)
2. **`l_standaard_energie`**: Energy preference (laag / normaal / goed)
3. **`l_ritueel_voorkeur`**: Ritual choice (samen / dagmoment / contact / geen)
4. **`l_lastseen_suggestie_state`**: Current suggestion state (JSON blob)
5. **`l_suggestie_state`**: Compressed state object
   - `huidig`: Current suggestion
   - `wachtOpErvaring`: Waiting for feedback
   - `historie`: Array of past decisions
   - `lisanneFavorieten`: Hearted suggestions
6. **`bewaard_suggestie`**: Saved for tomorrow (persists one suggestion)
7. **`l_eersteKeerCat`**: Categories Lisanne's seen (for "first-time framing")
8. **`l_reflectieVraag`**: Daily reflection prompt
9. **`l_reflectieBeantwoord_<date>`**: Flag for today's response

### What This Means
- **Progress is kept**: Lisanne's journey is persistent across sessions
- **Preferences stick**: Her energy level, ritual choice, trust level all saved
- **Suggestions personalize**: App learns what she likes (favorites influence next suggestions)
- **No account needed**: Entirely local (privacy by design)

### Onboarding Flow
1. **Screen 1-5**: Tim's message, expectations-setting, how to use app
2. **Preference Steps**:
   - Energy level (laag/normaal/goed)
   - Ritual preference (together / share / contact / spontaneous)
   - Trust level (gentle / full control)
3. **Completion**: `l_onboarded = true` → Home screen unlocked

**UX Note**: Onboarding text is warm, not sterile. Tim speaks directly ("Ik heb dit gemaakt omdat..."). This builds trust before any suggestion appears.

---

## 7. THE TIM'S VIEW (Partner Context)

While this analysis focuses on Lisanne, Tim's app mirrors her structure but with different content:

### Tim's Tabs
1. **Vandaag (Jouw taken)**: Discipline tasks, daily checklist
2. **Jullie (Samen)**: Shared moments, signals Lisanne sent, feedback requests
3. **Moment (Reflectie)**: Log moments, write reaction, see Lisanne's feedback
4. **Mijn inzet (Overzicht)**: Warmth metric, stats, streak tracker

### Key Interaction
- Tim can send Lisanne signals: "Vanavond even niet", "Dat was fijn", "Wil iets proberen"
- Lisanne sees Tim's messages immediately (not a notification, just visible on home)
- Creates shared awareness without forced communication

---

## 8. MISSING FEATURES / ONBOARDING GAPS

### What Would Make Lisanne Actually OPEN This Daily

**Current Strengths**:
- ✅ No spam (smart scheduler, respects refusals)
- ✅ Personalized (learns preferences, favorites)
- ✅ Educational (lessons are genuinely good)
- ✅ Intimate (Tim's voice, not clinical)

**Gaps That Could Drive Daily Use**:

1. **No Notifications**
   - Currently relies on manual app opening
   - **Quick win**: Add optional push notifications (once daily, "Lisanne, een idee voor jou")
   - **Concern**: Could feel nagging; must be highly tunable

2. **No Streak/Habit Gamification (Lisanne's Side)**
   - Tim has a "🔥 X days" streak tracker
   - Lisanne has no visible progress metric
   - **Quick win**: Add a subtle "7 days of moments" counter or "Consecutive days opening"
   - **Design principle**: Make progress visible without toxicity

3. **No "Just Chat" Mode**
   - All interactions are structured (suggestions, exercises)
   - Sometimes couples just want to share reactions
   - **Quick win**: Add a simple "Today's highlight" text exchange (Lisanne → Tim)

4. **No Calendar View**
   - Lisanne can't see past moments or trends
   - **Quick win**: Basic calendar heatmap (days with activity) in "Gids" or new tab

5. **No Favorite Quick Access**
   - Lisanne's ❤️ favorites are saved but not easy to re-access
   - Must scroll through main suggestion again
   - **Quick win**: Top-level "Favorieten" button in Regelen tab or floating action

6. **Settings Are Hidden**
   - Gear icon is small, top-right
   - Energy level picker exists but not obvious
   - **Quick win**: Make energy level toggle more prominent (currently secondary)

7. **Lessons Feel Separate**
   - Three tabs (Vandaag / Plannen / Gids) are siloed
   - No flow between daily suggestions and educational content
   - **Quick win**: "Learn more" button on suggestions pre-filled to relevant lesson
   - **Current state**: Mini-lessons are inline now (good!) but full lessons still separate

---

## 9. DEVICE-SPECIFIC OBSERVATIONS: iPhone 15 Portrait Mode

### Screen Real Estate (390 × 844 effective)
- **Status bar**: 44px (includes notch time + info)
- **App header**: 1rem padding = ~16px top, with h2 = ~48px total
- **Content area**: Available ~700px (after header + tab bar)
- **Tab bar**: ~52px (44px + safe-area-inset-bottom for home bar)

### Key Measurements
```
Device: iPhone 15 (6.1" diagonal)
Viewport: 390px wide × 844px tall
Safe areas:
  - Top: 44px (notch)
  - Bottom: 34px (home indicator)

App Layout:
  Header:     ~48px
  Content:    ~700px (flex-1)
  Tab bar:    ~52px (with safe-area)
```

### Font Rendering
- **Anti-aliasing**: Enabled (`-webkit-font-smoothing: antialiased`)
- **Font rendering**: Modern (CFF-based Google fonts)
- **Legibility**: Excellent at all stated sizes
- **No scaling issues**: Text never too small or cramped

### Gesture Support
- **Swipe navigation**: Not implemented (relies on button clicks)
- **Pull-to-refresh**: Not implemented
- **Long-press**: On favorites (toggles heart)
- **Tap-hold**: On lesson carousel (no action, just standard press)
- **Back button**: None (uses browser back or close buttons)

---

## 10. WHAT WORKS WELL ON iPhone 15

### 🟢 Strengths

1. **Fullscreen immersion**: Dark mode + gradient background feel premium
2. **Touch-friendly buttons**: All 44px+ minimum, never cramped
3. **Typography hierarchy**: Serif/sans mix is elegant and readable
4. **Breathing room**: Padding around content doesn't feel wasteful
5. **Smooth animations**: Fade transitions, expand/collapse feel native
6. **Accessibility of preferences**: Energy level, ritual choice easy to set upfront
7. **No cognitive load**: Suggestion view shows one thing; rejection requires explicit menu (not decision fatigue)
8. **PWA installation**: "Add to Home Screen" works; app icon is branded
9. **Safe area handling**: Notch and home indicator never obscured
10. **Lesson experience**: Serif fonts + generous spacing = reading experience, not "app experience"

---

## 11. WHAT'S FRUSTRATING OR CONFUSING

### 🔴 Friction Points

1. **View Selection Every Session**
   - Lisanne must tap "Lisanne" every time app opens
   - **Intent**: Privacy (good); **UX cost**: 1 extra tap every day
   - **Solution**: Option to remember view (with warning about security)

2. **Energy Level Buried**
   - Status bar shows energy, but changing it requires:
     - Tap status bar → Tap energy button → Pick emoji
   - **Better**: Make energy change a single-tap cycle (left arrow?) on the label
   - **Current**: Hidden in settings only (less discoverable)

3. **Lesson Back-and-Forth**
   - Reading a lesson in overlay, then returning to home = friction
   - Can't "save for later" a lesson to return to suggestions
   - **Solution**: "Continue reading later" bookmark button

4. **No Visual Progress on Suggestions**
   - Lisanne doesn't see how many suggestions she's tried
   - Tim has a "streak" metric; Lisanne has none
   - **Psychological impact**: May feel less investment in journey

5. **Favorite Suggestions Not Re-discoverable**
   - ❤️ favorites are liked, but no easy re-access
   - If she wants to try a favorite again, must wait for scheduler to offer it or dig in Regelen
   - **Solution**: "Favorieten" section in Regelen tab with recent hearts

6. **Agenda Panel Expand Animation**
   - Smooth, but if agenda has only 2 items, padding feels wasted
   - **Nitpick**: Minor UX efficiency loss

7. **"Liever Niet" Menu Is Hidden**
   - Secondary rejection options require opening menu
   - If Lisanne instinctively taps the button, it's hard to find "Wel een kleiner idee"
   - **Solution**: Show top 2-3 options as quick chips, rest in menu

8. **No Time-of-Day Context**
   - App suggests "vanavond" or "vandaag" but never shows current time
   - **Edge case**: If it's 10 PM and suggestion says "Vandaag", ambiguous if she should act now or tomorrow

9. **Lesson Gates Feel Aggressive**
   - "Even lezen..." → must read all → "Verder" button
   - Can't skip ahead to action items
   - **Rationale**: Ensures comprehension; **UX cost**: feels forced

10. **Settings Modal (Not Full-Screen)**
    - Takes up ~90% of screen but not immersive
    - Unclear if she can dismiss by tapping outside
    - **UX pattern**: Use full-screen sheet (slides up from bottom) for settings

---

## 12. QUICK WINS TO IMPROVE DAILY USAGE

### High-Impact, Low-Effort Changes

#### 1. **Add "Did You Know?" Lesson Previews**
   - On first load of home screen, show tiny lesson card ("Learn: Why anticipation matters")
   - Tappable to read full lesson
   - **Cost**: ~2 hours
   - **Impact**: Drives lesson discovery, adds educational angle to home screen

#### 2. **Make Energy Level a Single-Tap Toggle**
   - Instead of: Tap status → Tap picker → Choose emoji
   - Change to: Tap energy emoji directly → Cycle through (laag → normaal → goed → laag)
   - **Cost**: ~30 mins
   - **Impact**: Removes friction, makes preference visible every day

#### 3. **Add "Favorites" to Regelen Tab**
   - Quick section: "Recent favorites — Try these again"
   - Shows last 3-5 ❤️ suggestions
   - One-tap to "Ja, dit doe ik"
   - **Cost**: ~1.5 hours
   - **Impact**: Reminds Lisanne of things that worked; drives re-engagement

#### 4. **Notification Opt-In During Onboarding**
   - Step 3 preference: "Get a daily reminder?"
   - Time picker (9 AM, 7 PM, etc.)
   - "Or I'll find the app when I want"
   - **Cost**: ~1 hour (push setup already exists)
   - **Impact**: Biggest driver of daily opening without being pushy

#### 5. **Add Progress Indicator to Home**
   - Subtle: "Moments with Tim: 3 this week"
   - Below status bar, before suggestions
   - No gamification, just awareness
   - **Cost**: ~1 hour
   - **Impact**: Makes Lisanne feel her engagement is tracked (positive feedback loop)

#### 6. **Lesson "Continue Later" Bookmark**
   - Lesson overlay gets bookmark icon (top-right, near close)
   - Saved lessons accessible via Gids tab
   - **Cost**: ~2 hours
   - **Impact**: Removes "all or nothing" feeling of lessons

#### 7. **Energy Level Shows in Lesson Intro**
   - Lesson header adds line: "Tailored for your current energy (Goed)"
   - Mini-personalization; reminds Lisanne she was profiled
   - **Cost**: ~30 mins
   - **Impact**: Feels more bespoke

#### 8. **"Seen This Before?" Link in Suggestion**
   - If this suggestion was offered in past 30 days, show: "You saw this on March 10. Your feedback: 'Te veel'."
   - Prevents re-offering duds
   - **Cost**: ~1 hour
   - **Impact**: Builds app credibility ("It listens to me")

#### 9. **Ritual Reminder Nudge**
   - If ritual preference is set (e.g., "Samen op de bank"), and it's 9 PM:
   - Small, non-intrusive card: "Moment voor jullie ritueel?"
   - Can dismiss or tap to set timer
   - **Cost**: ~2 hours (scheduler work)
   - **Impact**: Drives daily structured togetherness

#### 10. **Lesson Search**
   - Gids tab gets search bar
   - "Find lessons about..." + list
   - **Cost**: ~1.5 hours
   - **Impact**: If Lisanne wants to revisit "How to read a signal from Tim", she can find it fast

---

## 13. ONBOARDING IMPROVEMENTS

### Current Onboarding is Good, But Could Add:

1. **Walkthrough of Tab Navigation**
   - After final onboarding screen, before home: "Here's where you'll spend time"
   - Hover/highlight each tab briefly

2. **Empty-State Guidance**
   - First time Lisanne reaches home with no suggestion: "Check back in a few hours" + clock animation

3. **Rejection Tutorial**
   - First time she taps "Liever niet", guide appears: "Here are your options"
   - Only once, then dismissed

4. **Lesson Intro Tour**
   - First lesson should highlight gates, FAQ, "Verder verkennen"
   - Teaches interaction patterns

---

## 14. WHAT MAKES LISANNE WANT TO OPEN THE APP DAILY

### Psychology of Re-engagement

**Current Design Does Well**:
- ✅ Suggestions are personal, not generic
- ✅ Tim's feedback loop (she sees his appreciation)
- ✅ Lessons feel like growth, not homework
- ✅ No judgment (all choices are valid)
- ✅ Low-pressure defaults ("Or not, that's fine too")

**Missing Ingredients** (Why She Might Forget):
- ❌ No "what happened since last time?" summary
- ❌ No social proof (can't see Tim's progress directly)
- ❌ Lessons don't integrate with daily suggestions (feels like separate feature)
- ❌ No streak/achievement (except Tim's side)
- ❌ No "surprise me" mode (all interaction is choice-heavy)

### To Increase Daily Opens:

1. **Home Screen Summary**
   - "This week: You tried 3 ideas. Tim loved 2 of them."
   - Makes progress visible immediately

2. **Tim's Warmth Meter on Lisanne's View**
   - One-way visibility: How is Tim feeling about your leadership?
   - Creates bidirectional feedback loop

3. **Weekly Recap**
   - Saturday or Sunday: "Week in review — 7 moments, 3 new ideas, Tim's favorite was..."
   - Celebratory tone, not report

4. **Random Lesson "Insight of the Day"**
   - Home screen shows random quote/insight from Lisanne's unread lessons
   - Tappable to read full lesson
   - Changes daily

5. **"Tim Has a Moment Idea"**
   - Occasionally show: "Tim is thinking about something for you. Look in Jullie tab to see it."
   - Drives cross-app engagement

---

## 15. COMPETITIVE COMPARISON: Why This Stands Out

### vs. Generic Relationship Apps
- **Not transactional**: No points, badges, levels
- **Not surveillance**: Tim's view is separate; mutual, not hierarchical
- **Intimate tone**: Educational without clinical
- **Branded identity**: Dark, sophisticated, uses serif fonts intentionally
- **Thoughtful friction**: View selection, lesson gates — friction that *serves* the user

### vs. Journaling Apps
- **Structured suggestions**: Not "write freely" (unclear what to do)
- **Partner integration**: Dual-user design, not solo
- **Behavioral**: Teaches through suggestion + reflection, not introspection

### vs. Meditation/Wellness Apps
- **Context-specific**: Not generic "be mindful"
- **Humor-light**: Doesn't take itself too seriously
- **Concrete**: Actual activities, not vague guidance

---

## 16. VERDICT: UX QUALITY ON iPhone 15

### Overall Score: **8.5 / 10**

**What Lisanne Gets**:
- Premium, dark, intimate interface
- Personalized suggestions that respect her choices
- Educational content that feels enriching
- Connection to Tim without surveillance
- Privacy-first (no accounts, local-only)

**Friction Points**:
- View selection every session (minor)
- Energy level buried (medium)
- Favorites not re-accessible (medium)
- No daily habit loop (engagement)
- No streak/progress visible (Lisanne's side)

**Why It Works**:
- Fits device (iPhone 15's screen size, safe areas)
- Typography & spacing are generous, not cramped
- Dark mode feels intimate, not dark
- Touch targets always adequate
- Animations smooth (ProMotion-friendly)
- Lessons are genuinely beautiful reading experiences

### What Would Push It to 9+:
1. Notifications (biggest driver of daily opens)
2. Visible progress / streak (psychological engagement)
3. Favorites quick access (removes friction)
4. Energy toggle single-tap (reduces steps)
5. Home summary card (context at a glance)

---

## 17. ACTIONABLE RECOMMENDATIONS FOR PRODUCT

### Phase 1 (1-2 weeks): Quick Wins
- [ ] Single-tap energy toggle on status bar
- [ ] Favorites section in Regelen tab
- [ ] Progress card on home screen ("3 moments this week")
- [ ] Lesson bookmarks (continue later)

### Phase 2 (2-4 weeks): Engagement
- [ ] Push notification opt-in during onboarding
- [ ] Daily lesson "insight of the day" on home
- [ ] Ritual reminders at scheduled times
- [ ] Lesson search in Gids tab

### Phase 3 (4+ weeks): Delight
- [ ] Weekly recap email/card
- [ ] Tim's warmth meter visibility (read-only)
- [ ] "Tim has a moment idea" cross-tab notification
- [ ] Random "Surprise me" suggestion mode

### Phase 4 (Polish): UX Debt
- [ ] Settings → full-screen sheet (not modal)
- [ ] Walkthrough tour of tabs (first-time)
- [ ] Time-of-day context ("It's 10 PM — tonight or tomorrow?")
- [ ] "Seen before" suggestion feedback

---

## 18. CONCLUSION

**Sprankelend Souffleur** achieves something rare: a mobile app that feels intentional, intimate, and premium without being precious or annoying.

The **design serves the purpose**: Dark mode + generous spacing + serif fonts create an environment where Lisanne feels safe exploring a sensitive topic. The two-view architecture (Lisanne vs. Tim) prevents accidental exposure and respects both partners' agency.

**The gap**: It's a beautiful *product*, but not yet a *habit*. Lisanne won't open it daily unless:
1. She gets reminded (notifications)
2. She sees her progress (streaks, summaries)
3. She can easily re-engage with favorites
4. The daily suggestion feels like a conversation, not a task

**The opportunity**: A few thoughtful additions (notifications, progress tracking, favorites quick access, home summary) would transform "that cool app Tim made" into "part of our daily rhythm."

**Overall**: For an intimate PWA serving a sensitive use case, the UX quality is excellent. The device fit is perfect. The experience respects the user. It's 8/10 today; 9.5/10 with the recommended quick wins.

---

**Analysis completed**: 2026-03-18
**Device**: iPhone 15 (6.1", iOS 17)
**Perspective**: Product design, user research, mobile UX specialist
