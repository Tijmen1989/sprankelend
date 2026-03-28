#!/usr/bin/env python3
"""
Cluster A: Split les 3 into three new lessons and renumber everything.
The file contains literal JS escape sequences like \\u2550, \\u2014 etc.
Python reads these as two-char sequences (backslash + u + digits).
"""

import re
import sys

INPUT = '/sessions/peaceful-optimistic-ramanujan/mnt/Sprankelend/index.html'

with open(INPUT, 'r', encoding='utf-8') as f:
    content = f.read()

lines = content.split('\n')

# ============================================================
# STEP 1: Find les 3 and les 4 boundaries
# ============================================================

les3_comment_idx = None
les4_comment_idx = None
for i, line in enumerate(lines):
    if 'LES 3: DIT IS OOK VOOR JOU' in line:
        les3_comment_idx = i
    if 'LES 4: DE BRUG' in line:
        les4_comment_idx = i

assert les3_comment_idx is not None, "Could not find LES 3"
assert les4_comment_idx is not None, "Could not find LES 4"
print(f"Les 3 at line {les3_comment_idx + 1}, Les 4 at line {les4_comment_idx + 1}")

# ============================================================
# STEP 2: Build new les 3, 4, 5 content
# ============================================================

# Read the original les 3 to extract exact content (preserving escapes)
old_les3_lines = lines[les3_comment_idx:les4_comment_idx]
old_les3_text = '\n'.join(old_les3_lines)

# We'll build the new lessons by extracting scroll items from original les 3
# Original scroll order:
#   0: scene (kept in new 3)
#   1: inzicht "wat doet dit met jou" (kept in new 3)
#   2: voorbeeld "kriebel mijn rug" (kept in new 3)
#   3: inzicht "goed gevoel" (kept in new 3)
#   4: noot "drielagenmodel" (kept in new 3)
#   5: noot "voor Tim motivatie" (kept in new 3)
#   6: kernboodschap (kept in new 3)
#   7: noot "safeword + afspraken" → split: safeword part → new 4, afspraken part → new 5
#   8: noot "Tim verantwoordelijkheden" → new 5
#   9: probeer → split across new 3 and new 5

# Instead of complex extraction, write new files as template strings
# that mirror the original's escaping style

# Write new content using the file's own escape conventions
new_block = []

# === NEW LES 3: DIT IS OOK VOOR JOU ===
new_block.append("  // \\u2550\\u2550\\u2550 LES 3: DIT IS OOK VOOR JOU \\u2550\\u2550\\u2550")
new_block.append("  {id:3, titel:'Dit is ook voor jou', subtitel:'Jullie zijn nog steeds jullie.', domein:'verbinding', fase:0, type:'story',")
new_block.append("   scroll:[")

# Keep scene, inzicht, voorbeeld, inzicht, noot(drielagen), noot(Tim motivatie), kernboodschap from original
# Extract these from the original lines by finding the scroll items
# Let's find each {type: in the original
scroll_items = []
current_item_start = None
brace_depth = 0
in_scroll = False

for i, line in enumerate(old_les3_lines):
    if "scroll:[" in line:
        in_scroll = True
        continue
    if not in_scroll:
        continue

    # Track items by {type: markers
    if "{type:" in line and brace_depth == 0:
        if current_item_start is not None:
            scroll_items.append('\n'.join(old_les3_lines[current_item_start:i]))
        current_item_start = i

    # Track brace depth to find end of scroll array
    for ch in line:
        if ch == '{':
            brace_depth += 1
        elif ch == '}':
            brace_depth -= 1

    if '],\n' in line + '\n' and brace_depth <= 0 and in_scroll and current_item_start is not None:
        # End of scroll - capture last item
        # Check if this line ends the scroll
        pass

# Simpler approach: just use regex to find scroll items
scroll_match = re.search(r'scroll:\[\s*\n(.*?)\n\s*\],', old_les3_text, re.DOTALL)
if scroll_match:
    scroll_content = scroll_match.group(1)
    # Split on lines that start a new item
    items = re.split(r'\n\s*(?=\{type:)', scroll_content)
    items = [item.strip().rstrip(',') for item in items if item.strip()]
    print(f"Found {len(items)} scroll items in original les 3")
    for idx, item in enumerate(items):
        preview = item[:60].replace('\n', ' ')
        print(f"  Item {idx}: {preview}...")
else:
    print("ERROR: Could not extract scroll items")
    sys.exit(1)

# Items mapping:
# 0: scene → new 3
# 1: inzicht (wat doet dit met jou) → new 3
# 2: voorbeeld (kriebel mijn rug) → new 3
# 3: inzicht (goed gevoel) → new 3
# 4: noot (drielagenmodel) → new 3
# 5: noot (Tim motivatie) → new 3
# 6: kernboodschap → new 3
# 7: noot (safeword + afspraken - big block) → split: safeword stuff → new 4, afspraken → new 5
# 8: noot (Tim verantwoordelijkheden) → new 5
# 9: probeer → adapt for new 3

# NEW LES 3 scroll
les3_scroll = [items[0], items[1], items[2], items[3], items[4], items[5], items[6]]
# New probeer for les 3: focus on self-awareness
les3_probeer = "    {type:'probeer', tekst:'Let een keer niet op Tim.\\nLet op jezelf.\\nAls je iets zegt en hij doet het: hoe voelt dat?\\nNiet hoe het hoort te voelen. Hoe het \\u00e9cht voelt.\\nDat is de enige vraag die ertoe doet.'}"
les3_scroll.append(les3_probeer)

new_block.append(',\n'.join('    ' + item.strip() if not item.strip().startswith('{') else '    ' + item.strip() for item in les3_scroll))
new_block.append("  ],")

# verdieping and other sections for new les 3
new_block.append("  zichtbaar:{")
new_block.append("    intro:'', uitleg:'', voorbeeld:'',")
new_block.append("    oefening:'Let op jezelf. Hoe voelt het als hij gewoon doet wat je zegt?'")
new_block.append("  },")
new_block.append("  verdieping:[")
new_block.append("    {vraag:'Ik voel er eerlijk gezegd niet zoveel bij', antwoord:'Dat is prima. Niet iedereen voelt meteen iets. Het kan ook gewoon praktisch fijn zijn \\u2014 minder overleggen, minder herhalen. Dat is al genoeg reden om het te doen.'},")
new_block.append("    {vraag:'Ik voel me een beetje schuldig', antwoord:'Waarom? Jullie doen dit samen. En jij krijgt er ook iets voor terug. Dat is geen uitbuiting \\u2014 dat is samenwerking waar jullie allebei beter van worden.'},")
new_block.append("    {vraag:'Het voelde stiekem best goed', antwoord:'Mooi. Onthoud dat gevoel. Dat is jouw motivatie \\u2014 niet Tim\\u2019s behoefte, maar jouw eigen ervaring. Daar draait het uiteindelijk om.'},")
new_block.append("    {vraag:'Ik vergeet het soms een paar dagen', antwoord:'Dat kan gebeuren. Maar probeer het niet te lang te laten liggen \\u2014 regelmaat maakt het makkelijker, voor jou en voor Tim. Een klein ding per dag is al genoeg om het levend te houden.'}")
new_block.append("  ],")
new_block.append("  meerLezen:{")
new_block.append("    preview:'Volgende les: het vangnet dat onder alles zit.'")
new_block.append("  }},")

print("New les 3 built")

# === NEW LES 4: HET VANGNET ===
new_block.append("")
new_block.append("  // \\u2550\\u2550\\u2550 LES 4: HET VANGNET \\u2550\\u2550\\u2550")
new_block.append("  {id:4, titel:'Het vangnet', subtitel:'E\\u00e9n woord dat alles stopt.', domein:'verbinding', fase:0, type:'story',")
new_block.append("   scroll:[")
new_block.append("    {type:'scene', tekst:'Je hebt nu een paar dingen geprobeerd. Kleine opdrachten. Misschien iets persoonlijkers.\\nEn misschien dacht je ergens: maar wat als het te ver gaat? Wat als ik iets doe en hij wil stoppen? Of ik wil stoppen?\\nDat is precies waar deze les over gaat.'},")
new_block.append("    {type:'inzicht', tekst:'Er is \\u00e9\\u00e9n woord waarmee alles stopt. Meteen. Geen discussie, geen uitleg, geen \\u201cmaar we waren net...\\u201d Gewoon: stop.\\nJullie kiezen samen een woord \\u2014 iets dat je normaal niet zou zeggen. Dat woord is het vangnet onder alles wat hierna komt. Het maakt niet uit of je het ooit gebruikt. Het feit dat het er is, is genoeg.\\n\\nDit is niet alleen voor Tim. Dit is ook voor jou. Als jij midden in een moment denkt \\u201cik wil dit niet meer\\u201d \\u2014 dan zeg je het woord en het is voorbij. Geen uitleg nodig. Niet aan Tim, niet aan jezelf.'},")
new_block.append("    {type:'noot', tekst:'Waarom niet gewoon \\u201cstop\\u201d? Omdat \\u201cstop\\u201d soms iets anders betekent. Soms zeg je \\u201cstop\\u201d terwijl je eigenlijk bedoelt: even pauze, niet helemaal klaar. Een apart woord maakt het helder: als d\\u00edt woord valt, is het echt.\\n\\nKies iets dat makkelijk te onthouden is maar niet per ongeluk eruit floept. Veel mensen gebruiken een kleur (\\u201crood\\u201d), een voorwerp (\\u201cananas\\u201d), of iets absurds. Het maakt niet uit wat \\u2014 als jullie het allebei kennen.'},")
new_block.append("    {type:'inzicht', tekst:'En dan is er iets dat misschien nog belangrijker is dan het safeword zelf:\\n\\n<b>Doorlopend consent.</b>\\n\\nDat klinkt ingewikkeld, maar het is simpel: jullie checken af en toe in. Niet met een formulier of een gesprek \\u2014 gewoon door te letten op elkaar.\\nAls Tim stiller wordt dan normaal, als hij wegkijkt, als iets niet voelt zoals het hoort \\u2014 dan vraag je: \\u201cgaat het?\\u201d En als het antwoord nee is, stop je.\\nEn andersom: als jij je ongemakkelijk voelt, mag je altijd stoppen. Zonder reden. Zonder schuld.\\n\\nHet safeword is het noodrem. Doorlopend consent is de gordel die je altijd draagt.'},")
new_block.append("    {type:'noot', tekst:'E\\u00e9n formele regel die alles makkelijker maakt:\\n\\n<b>Tim neemt geen initiatief.</b>\\n\\nDat betekent: Tim start niks uit zichzelf. Geen \\u201czullen we vanavond...\\u201d, geen hints, geen druk. Alles begint bij jou. Als jij niks doet, gebeurt er niks. En dat is ok\\u00e9.\\n\\nDit is geen straf voor Tim \\u2014 dit is bescherming voor jou. Je hoeft nooit het gevoel te hebben dat je moet presteren, dat je achterloopt, of dat Tim zit te wachten. Hij wacht. Maar dat is zijn keuze, niet jouw probleem.\\n\\nDeze regel geldt altijd. Ook op goede dagen. Ook als Tim enthousiast is. Jij start het \\u2014 of het start niet.'},")
new_block.append("    {type:'kernboodschap', tekst:'Het vangnet zit er nu onder.\\nEen woord dat alles stopt. Doorlopend opletten. En Tim die niks start zonder jou.\\nDit maakt alles wat hierna komt veiliger.\\nNiet omdat het gevaarlijk is \\u2014 maar omdat het fijner is als je weet dat je altijd kunt stoppen.'},")
new_block.append("    {type:'probeer', tekst:'Kies samen het woord.\\nMaak er geen groot gesprek van \\u2014 gewoon: \\u201cwelk woord gebruiken we als we echt willen stoppen?\\u201d\\nKies iets. Klaar. Het ligt er nu.'}")
new_block.append("  ],")
new_block.append("  zichtbaar:{")
new_block.append("    intro:'', uitleg:'', voorbeeld:'',")
new_block.append("    oefening:'Kies samen het safeword. E\\u00e9n woord, klaar.'")
new_block.append("  },")
new_block.append("  verdieping:[")
new_block.append("    {vraag:'We hebben het nooit nodig gehad', antwoord:'Hopelijk niet. Maar het feit dat het er is maakt alles losser. Je durft meer als je weet dat je altijd kunt stoppen.'},")
new_block.append("    {vraag:'Tim vindt een safeword overdreven', antwoord:'Het is niet overdreven \\u2014 het is standaard. Iedereen die dit serieus doet heeft er een. Het is geen teken van angst, het is een teken van respect.'},")
new_block.append("    {vraag:'Ik vind het moeilijk om te stoppen midden in iets', antwoord:'Dat hoeft niet in \\u00e9\\u00e9n keer. Begin met kleine momenten onderbreken \\u2014 even pauze, even checken. Dat is al genoeg om te oefenen met stoppen.'},")
new_block.append("    {vraag:'Hoe weet ik of Tim echt ok\\u00e9 is?', antwoord:'Kijk naar zijn lichaam, niet naar zijn woorden. Ontspannen schouders, rustige ademhaling, oogcontact \\u2014 dat zijn goede tekens. Spanning, wegkijken, stilte die anders voelt \\u2014 dan even checken.'}")
new_block.append("  ],")
new_block.append("  meerLezen:{")
new_block.append("    preview:'Volgende les: de eerste echte afspraken samen.'")
new_block.append("  }},")

print("New les 4 built")

# === NEW LES 5: DE EERSTE AFSPRAKEN ===
new_block.append("")
new_block.append("  // \\u2550\\u2550\\u2550 LES 5: DE EERSTE AFSPRAKEN \\u2550\\u2550\\u2550")
new_block.append("  {id:5, titel:'De eerste afspraken', subtitel:'Klein, duidelijk, van jou.', domein:'verbinding', fase:0, type:'story',")
new_block.append("   scroll:[")
new_block.append("    {type:'scene', tekst:'Het vangnet ligt er. Het woord is gekozen. Tim weet dat hij niks start.\\nNu is het tijd voor iets concreets: de eerste afspraken. Niet veel. Twee of drie kleine dingen die er altijd zijn \\u2014 ook op de dagen dat je nergens aan denkt.'},")
new_block.append("    {type:'inzicht', tekst:'De basis is simpel:\\n\\n<b>Als jij iets zegt, doet Tim het. Zonder zucht, zonder tegenzin, zonder \\u201cmoet dat nu?\\u201d</b>\\n\\nDat is de basis. Dit is wat Tim je belooft. Als jij een opdracht geeft, voert hij die uit \\u2014 zonder enige vorm van ontevredenheid. Dat is wat hij je heeft beloofd door hieraan te beginnen.\\n\\nDaarnaast: \\u00e9\\u00e9n afspraak hebben jullie al. Geen telefoon aan tafel. Dat was er al voor deze app. Maar nu is het niet meer alleen een huisregel \\u2014 het is iets van jullie. Iets dat jij hebt bepaald.'},")
new_block.append("    {type:'voorbeeld', tekst:'Kies er nog \\u00e9\\u00e9n of twee bij. Hier zijn een paar suggesties:\\n\\u2022 Lisanne kiest de serie \\u2019s avonds.\\n\\u2022 Tim vraagt toestemming voor gamen.\\n\\u2022 Tim draagt altijd een onderbroek en zit niet aan zichzelf \\u2014 dat is van jou.\\n\\u2022 Bedtijd wordt bepaald door Lisanne.\\n\\nKies wat bij jullie past. Het maakt niet uit welke. Het gaat erom dat er iets is \\u2014 iets kleins, iets dagelijks \\u2014 dat Tim eraan herinnert: zij heeft dit besloten. Ook als je verder niks doet die dag.'},")
new_block.append("    {type:'noot', tekst:'En schrijf ze op. In een schriftje, op een briefje \\u2014 iets fysieks. Jouw handschrift. Leg het op het nachtkastje of plak het op de koelkast. Dat maakt het echt. Het is niet een schermpje dat je wegklikt \\u2014 het is iets dat er ligt. Dat Tim ziet als hij naar bed gaat. En elke keer dat hij het leest, weet hij: zij heeft dit besloten.'},")
new_block.append("    {type:'noot', tekst:'En als hij een afspraak breekt? Dan hoef je niks te doen. Je hoeft niet te straffen. Je hoeft alleen te zeggen: \\u201cdat was de afspraak.\\u201d Meer niet. Hij voelt de rest zelf.'},")
new_block.append("    {type:'noot', tekst:'En Tim? Die heeft ook zijn kant.\\nDit is niet alleen iets wat jij doet \\u2014 Tim heeft ook verantwoordelijkheden:\\n\\u2022 Hij houdt zich aan de afspraken zonder dat jij hem eraan hoeft te herinneren.\\n\\u2022 Hij zet jou niet onder druk om meer te doen, vaker te doen, of sneller te gaan.\\n\\u2022 Hij is eerlijk als jullie erover praten \\u2014 over wat werkt en wat niet.\\n\\u2022 Hij respecteert het als jij een dag, een week, niks doet.\\nDat is zijn kant van de afspraak. Jij hoeft dit niet alleen te dragen.'},")
new_block.append("    {type:'kernboodschap', tekst:'Twee of drie afspraken. Opgeschreven. Van jou.\\nTim houdt zich eraan. Jij hoeft hem niet te herinneren.\\nDit is de basis waar alles op staat \\u2014 laag 2 uit les 3, nu concreet gemaakt.'},")
new_block.append("    {type:'probeer', tekst:'Kies \\u00e9\\u00e9n extra afspraak erbij. Eentje die makkelijk is en elke dag terugkomt.\\nSchrijf alles op. Jouw handschrift. Leg het neer waar Tim het ziet.'}")
new_block.append("  ],")
new_block.append("  zichtbaar:{")
new_block.append("    intro:'', uitleg:'', voorbeeld:'',")
new_block.append("    oefening:'Kies \\u00e9\\u00e9n afspraak en schrijf hem op.'")
new_block.append("  },")
new_block.append("  verdieping:[")
new_block.append("    {vraag:'Tim wil het vaker dan ik', antwoord:'Jij bepaalt hoe vaak. Als hij meer wil, is dat een goed teken \\u2014 maar het ritme is aan jou.'},")
new_block.append("    {vraag:'Ik weet niet of dit voor mij is', antwoord:'Dat hoef je nu niet te weten. Probeer het een paar weken. Als het niks voor je doet, stop je. Maar geef het een eerlijke kans \\u2014 nieuwe dingen voelen altijd eerst een beetje vreemd.'},")
new_block.append("    {vraag:'Hij breekt steeds dezelfde afspraak', antwoord:'Dan is dat een gesprek. Niet boos, niet teleurgesteld \\u2014 gewoon: \\u201cdit is de afspraak. Waarom lukt het niet?\\u201d Misschien is de afspraak te moeilijk. Misschien moet je een andere kiezen. Dat is ok\\u00e9.'},")
new_block.append("    {vraag:'Hoeveel afspraken moeten we hebben?', antwoord:'Begin met twee of drie. Niet meer. Liever drie die altijd werken dan tien die je vergeet. Later kun je er altijd bij doen.'}")
new_block.append("  ],")
new_block.append("  meerLezen:{")
new_block.append("    preview:'Volgende les: van dagelijks naar persoonlijker.'")
new_block.append("  }},")

print("New les 5 built")

# Build new block text
new_block_text = '\n'.join(new_block)

# Replace old les 3 (from les3_comment to les4_comment) with new block
before = lines[:les3_comment_idx]
after = lines[les4_comment_idx:]

new_content = '\n'.join(before) + '\n' + new_block_text + '\n\n' + '\n'.join(after)

# ============================================================
# STEP 3: Renumber lesson IDs 4+ → +2 in LESSEN_INHOUD
# ============================================================

# Renumber comments: "LES N:" where N >= 6 (old 4 is now after our new 5)
# Wait - we need to renumber the OLD les 4-31, which come AFTER our new block.
# The old les 4 comment says "LES 4: DE BRUG" → should become "LES 6: DE BRUG"
# We must NOT renumber our new les 3, 4, 5.

# Strategy: find all "LES N:" patterns where N matches old numbering (4-31)
# and all {id:N, patterns.
# But our new block already has id:3, id:4, id:5 — we must not touch those.
# The old lessons start after our new block.

# Find position of old les 4 in new_content
old_les4_pos = new_content.find('LES 4: DE BRUG')
assert old_les4_pos is not None and old_les4_pos > 0, "Could not find old LES 4: DE BRUG"

# Split content: before old les 4 (includes our new 3,4,5) and from old les 4 onwards
part_before = new_content[:old_les4_pos - 50]  # a bit before the comment
# Actually, let's be more precise. Find the exact start of the old les 4 comment line.
# Search backwards from old_les4_pos to find start of line
line_start = new_content.rfind('\n', 0, old_les4_pos) + 1
part_before = new_content[:line_start]
part_after = new_content[line_start:]

# In part_after, renumber:
# - "LES N:" comments where N >= 4 → N+2
# - "{id:N," lesson definitions where N >= 4 → N+2

def renumber_after(text):
    # Renumber LES comment patterns (handles both \\u2550 decorated and simple)
    def replace_les_comment(m):
        num = int(m.group(1))
        if num >= 4:
            return m.group(0).replace(f'LES {num}:', f'LES {num + 2}:')
        return m.group(0)

    text = re.sub(r'LES (\d+):', replace_les_comment, text)

    # Renumber {id:N, in lesson definitions
    def replace_id(m):
        num = int(m.group(1))
        if num >= 4:
            return '{id:' + str(num + 2) + ','
        return m.group(0)

    text = re.sub(r'\{id:(\d+),', replace_id, text)

    return text

part_after = renumber_after(part_after)

new_content = part_before + part_after

# ============================================================
# STEP 4: Renumber LESOEFENINGEN
# ============================================================

# lesId:N where N >= 4 → N+2 (but NOT in our new les 3,4,5 exercises)
# And "// Les N:" comments where N >= 4 → N+2
# Our new exercises use lesId:3, 4, 5 — we must not touch those.
# The old exercises with lesId:4+ are the ones to renumber.

# Find LESOEFENINGEN section
leso_start = new_content.find('const LESOEFENINGEN = [')
assert leso_start > 0, "Could not find LESOEFENINGEN"
# Find end of array
leso_end = new_content.find('];', leso_start)
assert leso_end > 0

leso_section = new_content[leso_start:leso_end + 2]

# First, replace old les 3 exercises with new les 3,4,5 exercises
old_les3_ex_marker = "// Les 3: Kleine signalen, groot effect"
old_les4_ex_marker = "// Les 4:"  # This is already there

# Find old les 3 exercises block (from "// Les 3:" to just before "// Les 4:")
les3_ex_start = leso_section.find(old_les3_ex_marker)
les4_ex_start = leso_section.find(old_les4_ex_marker)

if les3_ex_start > 0 and les4_ex_start > 0:
    old_les3_exercises = leso_section[les3_ex_start:les4_ex_start]

    new_les345_exercises = """// Les 3: Dit is ook voor jou
  {lesId:3, volgorde:1, tekst:'Geef Tim vandaag \\u00e9\\u00e9n opdracht en let niet op hem \\u2014 let op jezelf. Hoe voelt het?', context:'middag', cat:'relationeel'},
  {lesId:3, volgorde:2, tekst:'Twee opdrachten vandaag. Bij allebei: merk op wat het met jou doet. Prettig? Onwennig? Schuldig? Alles is ok\\u00e9.', context:'middag', cat:'micro'},
  {lesId:3, volgorde:3, tekst:'Probeer vandaag drie keer iets te zeggen dat gewoon gebeurt. Geen overleg, geen herhaling. Let op het verschil.', context:'elk moment', cat:'opdracht'},

  // Les 4: Het vangnet
  {lesId:4, volgorde:1, tekst:'Kies vandaag samen het safeword. Maak er geen lang gesprek van \\u2014 gewoon kiezen en klaar.', context:'avond', cat:'relationeel'},
  {lesId:4, volgorde:2, tekst:'Check vandaag \\u00e9\\u00e9n keer bij Tim in tijdens een moment: \\u201cgaat het?\\u201d Kijk naar zijn reactie.', context:'avond', cat:'relationeel'},
  {lesId:4, volgorde:3, tekst:'Oefen vandaag met stoppen midden in iets. Gewoon: \\u201cwe zijn klaar.\\u201d Kijk hoe dat voelt.', context:'avond', cat:'relationeel'},

  // Les 5: De eerste afspraken
  {lesId:5, volgorde:1, tekst:'Schrijf vandaag jullie eerste twee afspraken op. Jouw handschrift, op papier.', context:'middag', cat:'opdracht'},
  {lesId:5, volgorde:2, tekst:'Kies vandaag \\u00e9\\u00e9n extra afspraak erbij. Iets kleins dat elke dag terugkomt.', context:'middag', cat:'opdracht'},
  {lesId:5, volgorde:3, tekst:'Check aan het eind van de dag: heeft Tim zich aan alle afspraken gehouden? Zo niet: \\u201cdat was de afspraak.\\u201d', context:'avond', cat:'opdracht'},

  """

    leso_section = leso_section[:les3_ex_start] + new_les345_exercises + leso_section[les4_ex_start:]
    print("Replaced les 3 exercises with new les 3,4,5 exercises")
else:
    print(f"WARNING: Could not find les 3 exercises (start={les3_ex_start}, end={les4_ex_start})")

# Now renumber old lesId:4+ to +2 in LESOEFENINGEN
# But we must NOT touch our new lesId:3,4,5 entries.
# Strategy: the new entries come before old lesId:4+ entries, so we can renumber
# from the old "// Les 4:" (which should now be "// Les 6:" after renumbering)
# Actually, the old "// Les 4:" markers need to change too.

# Renumber lesId:N where N >= 6 in LESOEFENINGEN
# Wait - we haven't renumbered the LESOEFENINGEN yet. The old entries still say lesId:4, 5, etc.
# But our new entries also say lesId:4, 5. We need to be careful.

# Find where the new les 5 exercises end (after "// Les 5: De eerste afspraken" block)
new_les5_end_marker = "// Les 5: De eerste afspraken"
new_les5_pos = leso_section.find(new_les5_end_marker)

# Find the next "// Les" comment after our new block
next_comment_pos = leso_section.find("\n  // Les ", new_les5_pos + len(new_les5_end_marker))

if next_comment_pos > 0:
    leso_before = leso_section[:next_comment_pos]
    leso_old = leso_section[next_comment_pos:]

    # Renumber in the old part: lesId:N → N+2, "// Les N:" → "// Les N+2:"
    def renumber_leso(text):
        def replace_lesid(m):
            num = int(m.group(1))
            if num >= 4:
                return f'lesId:{num + 2}'
            return m.group(0)
        text = re.sub(r'lesId:(\d+)', replace_lesid, text)

        def replace_comment(m):
            num = int(m.group(1))
            if num >= 4:
                return f'// Les {num + 2}:'
            return m.group(0)
        text = re.sub(r'// Les (\d+):', replace_comment, text)

        return text

    leso_old = renumber_leso(leso_old)
    leso_section = leso_before + leso_old
    print("Renumbered old LESOEFENINGEN entries")

# Put updated LESOEFENINGEN back
new_content = new_content[:leso_start] + leso_section + new_content[leso_end + 2:]

# ============================================================
# STEP 5: Update LES_SUGGESTIE_VOORKEUR
# ============================================================

lsv_start = new_content.find('const LES_SUGGESTIE_VOORKEUR = {')
assert lsv_start > 0, "Could not find LES_SUGGESTIE_VOORKEUR"

# Find matching closing };
brace_count = 0
lsv_end = lsv_start
for i in range(lsv_start, len(new_content)):
    if new_content[i] == '{':
        brace_count += 1
    elif new_content[i] == '}':
        brace_count -= 1
        if brace_count == 0:
            lsv_end = i + 2  # include };
            break

new_lsv = """const LES_SUGGESTIE_VOORKEUR = {
  1:  {cats:['micro','opdracht'], vibes:['controle'], actieTypes:['stem','opdracht']},
  2:  {cats:['micro','opdracht'], vibes:['controle'], actieTypes:['stem','opdracht']},
  3:  {cats:['micro','opdracht'], vibes:['controle','zacht'], actieTypes:['stem','opdracht']},
  4:  {cats:['relationeel'], vibes:['zacht','zorg'], actieTypes:['relationeel']},
  5:  {cats:['micro','opdracht'], vibes:['controle'], actieTypes:['stem','opdracht']},
  6:  {cats:['micro'], vibes:['spanning','stil'], actieTypes:['stem','positie']},
  7:  {cats:['micro'], vibes:['spanning','speels'], actieTypes:['stem']},
  8:  {cats:['micro'], vibes:['spanning','stil'], actieTypes:['stem','positie']},
  9:  {cats:['micro'], vibes:['spanning','speels'], actieTypes:['stem','op_afstand']},
  10: {cats:['relationeel'], vibes:['zacht','zorg'], actieTypes:['relationeel']},
  11: {cats:['micro','vastmaak'], vibes:['spanning'], actieTypes:['item']},
  12: {cats:['micro','controle'], vibes:['controle'], actieTypes:['correctie','stem']},
  13: {cats:['micro','relationeel'], vibes:['zacht','zorg'], actieTypes:['stem','relationeel']},
  14: {cats:['micro'], vibes:['controle','spanning'], actieTypes:['positie','stem']},
  15: {cats:['vastmaak'], vibes:['spanning','stil'], actieTypes:['item','fysiek_item']},
  16: {cats:['vastmaak','sessie'], vibes:['spanning'], actieTypes:['item','fysiek_item']},
  17: {cats:['micro','controle'], vibes:['spanning','controle'], actieTypes:['stem','beslissing']},
  18: {cats:['relationeel'], vibes:['zacht','zorg'], actieTypes:['relationeel']},
  19: {cats:['relationeel','micro'], vibes:['zacht'], actieTypes:['relationeel','stem']},
  20: {cats:['micro','relationeel'], vibes:['speels','zacht'], actieTypes:['stem']},
  21: {cats:['opdracht','dienstbaar','service'], vibes:['controle'], actieTypes:['opdracht','stem']},
  22: {cats:['micro'], vibes:['speels','spanning'], actieTypes:['stem','op_afstand']},
  23: {cats:['fysiek'], vibes:['spanning','controle'], actieTypes:['fysiek_item']},
  24: {cats:['vastmaak','sessie'], vibes:['spanning'], actieTypes:['item','fysiek_item']},
  25: {cats:['micro','opdracht'], vibes:['controle'], actieTypes:['stem','opdracht','beslissing']},
  26: {cats:['relationeel'], vibes:['zacht','zorg'], actieTypes:['relationeel']},
  27: {cats:['micro'], vibes:['speels','spanning'], actieTypes:['stem','beslissing','op_afstand']},
  28: {cats:['micro','controle'], vibes:['spanning'], actieTypes:['stem','beslissing']},
  29: {cats:['controle'], vibes:['controle','spanning'], actieTypes:['stem','correctie']},
  30: {cats:['sessie','vastmaak'], vibes:['spanning'], actieTypes:['item','fysiek_item','timing']},
  31: {cats:['micro','controle'], vibes:['spanning','stil'], actieTypes:['stem','timing']},
  32: {cats:['relationeel'], vibes:['zacht'], actieTypes:['relationeel']},
  33: {cats:['micro','relationeel','sessie'], vibes:['speels','spanning','zacht'], actieTypes:['stem']}
};"""

new_content = new_content[:lsv_start] + new_lsv + new_content[lsv_end:]
print("Updated LES_SUGGESTIE_VOORKEUR for 33 lessons")

# ============================================================
# STEP 6: Write output
# ============================================================

with open(INPUT, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("\nDone! Writing output...")

# Verification
lesson_ids = re.findall(r'\{id:(\d+),\s*titel:', new_content)
print(f"Lesson count: {len(lesson_ids)}")
print(f"Lesson IDs: {sorted(int(x) for x in lesson_ids)}")

ex_ids = sorted(set(int(x) for x in re.findall(r'lesId:(\d+)', new_content)))
print(f"LESOEFENINGEN lesIds: {ex_ids}")

lsv_ids = re.findall(r'^\s+(\d+):\s*\{cats:', new_content, re.MULTILINE)
print(f"LES_SUGGESTIE_VOORKEUR IDs: {sorted(int(x) for x in lsv_ids)}")

# Check for duplicate IDs
from collections import Counter
id_counts = Counter(int(x) for x in lesson_ids)
dupes = {k: v for k, v in id_counts.items() if v > 1}
if dupes:
    print(f"WARNING: Duplicate lesson IDs: {dupes}")
else:
    print("No duplicate lesson IDs - good!")
