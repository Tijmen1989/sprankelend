#!/usr/bin/env python3
"""
Cluster C: Progressie repareren
1. Speelsheid eerder: voeg speelse noot toe aan les 8 (Van dichtbij naar kwetsbaar)
2. Probeer-blokken verrijken met hoe/wanneer/context (les 8, 10, 12)
3. Imperfecte scène toevoegen aan les 12
4. Les 29 en 32 uitbreiden
"""

import re

FILE = '/sessions/peaceful-optimistic-ramanujan/mnt/Sprankelend/index.html'

with open(FILE, 'r', encoding='utf-8') as f:
    content = f.read()

changes = 0

# ============================================================
# 1. SPEELSHEID EERDER: noot toevoegen aan les 8 (id:8)
# Na de kernboodschap van les 8, voor de probeer
# ============================================================

old_les8_probeer = "{type:'probeer', tekst:'Dit hoeft niet deze week. En niet morgen.\\nMaar als je er klaar voor bent \\u2014 kies een avond dat jullie alleen zijn.\\nEn zeg het. Twee woorden.\\nHet maakt niet uit wat er daarna gebeurt. Het maakt niet uit als jullie lachen.\\nHet gaat erom dat je het deed.'}"

new_les8_probeer = """{type:'noot', tekst:'En dan nog dit: het mag ook leuk zijn.\\nAls je \\"kleed je uit\\" zegt en jullie schieten allebei in de lach \\u2014 dan is dat geen mislukking. Dat is jullie. De spanning en de humor kunnen naast elkaar bestaan.\\nMisschien zeg je iets en het klinkt raar. Misschien doet hij iets onhandigs. Misschien giechelen jullie allebei en duurt het moment maar dertig seconden.\\nDat telt ook. Speelsheid haalt de druk eraf. En soms leidt een lach naar een moment dat stiller en echter is dan je had verwacht.'},
    {type:'probeer', tekst:'Dit hoeft niet deze week. En niet morgen.\\nMaar als je er klaar voor bent \\u2014 kies een avond dat jullie alleen zijn. Milou slaapt of is er niet.\\nEn zeg het. Twee woorden.\\nAls jullie lachen: prima. Probeer het dan nog een keer. Iets stelliger.\\nHet gaat erom dat je het deed.'}"""

if old_les8_probeer in content:
    content = content.replace(old_les8_probeer, new_les8_probeer)
    changes += 1
    print("1. Speelsheid-noot + verbeterde probeer aan les 8 toegevoegd")
else:
    print("WARNING: Les 8 probeer niet gevonden")

# ============================================================
# 2. PROBEER-BLOK LES 10 (id:10) verrijken met context
# Huidige: "Geef een keer het teken..."
# ============================================================

old_les10_probeer = "{type:'probeer', tekst:'Geef een keer het teken.\\nDe halsband neerleggen. De politiehandboeien klikken. Of gewoon drie woorden.\\nHet maakt niet uit wat er daarna gebeurt.\\nHet gaat om het moment dat jij de avond verschuift.'}"

new_les10_probeer = "{type:'probeer', tekst:'Geef een keer het teken.\\nKies een avond dat jullie rustig zitten. Milou slaapt. Geen haast.\\nDe halsband neerleggen. Of gewoon drie woorden: \\u201ckom eens hier.\\u201d\\nJe hoeft niet te weten wat er daarna komt. Het gaat om het moment dat jij de avond verschuift.\\nEn als het raar voelt: dat is normaal. De tweede keer voelt het al minder raar.'}"

if old_les10_probeer in content:
    content = content.replace(old_les10_probeer, new_les10_probeer)
    changes += 1
    print("2. Les 10 probeer verrijkt met context")
else:
    print("WARNING: Les 10 probeer niet gevonden")

# ============================================================
# 3. PROBEER-BLOK LES 12 (id:12) verrijken
# Huidige: "Wacht op het moment. Zeg één zin. Kijk wat er gebeurt."
# ============================================================

old_les12_probeer = "{type:'probeer', tekst:'Wacht op het moment. Zeg \\u00e9\\u00e9n zin. Kijk wat er gebeurt.'}"

new_les12_probeer = "{type:'probeer', tekst:'Wacht op het moment \\u2014 het komt vanzelf. Hij pakt zijn telefoon als dat niet mag. Hij vergeet een afspraak.\\nZeg \\u00e9\\u00e9n zin. Rustig, kort, geen uitleg: \\u201cdat was niet de afspraak.\\u201d\\nEn dan door. Niet nabespreken, niet checken of hij het begrepen heeft. Jij gaat gewoon verder.\\nDe eerste keer voelt het misschien overdreven. Maar kijk naar zijn reactie \\u2014 hij voelt het. En de rest van de avond is anders.'}"

if old_les12_probeer in content:
    content = content.replace(old_les12_probeer, new_les12_probeer)
    changes += 1
    print("3. Les 12 probeer verrijkt")
else:
    print("WARNING: Les 12 probeer niet gevonden")

# ============================================================
# 4. IMPERFECTE SCÈNE toevoegen aan les 12
# Na de sub-frenzy noot, voor de inzicht "correctie is richting"
# ============================================================

old_les12_inzicht = "    {type:'inzicht', tekst:'Correctie is niet straf.\\nHet is <b>richting</b>.\\nDezelfde spier.'}"

new_les12_inzicht = """    {type:'voorbeeld', tekst:'<b>En zo gaat het soms:</b>\\nHij deed iets fout. Je wilde iets zeggen. Maar het moment was voorbij voordat je de woorden had.\\nOf je zei het \\u2014 maar het kwam er zachter uit dan je bedoelde. Meer als vraag dan als mededeling.\\nOf je zei het perfect, maar hij keek je aan alsof je een grap maakte. En toen twijfelde je.\\n\\nAllemaal normaal. De eerste correcties zijn onhandig. De toon klopt niet. De timing is net te laat. Je voelt je overdreven.\\nMaar het punt is: je deed het. En de volgende keer gaat het iets makkelijker. En de keer daarna voelt het bijna normaal.'},
    {type:'inzicht', tekst:'Correctie is niet straf.\\nHet is <b>richting</b>.\\nDezelfde spier.'}"""

if old_les12_inzicht in content:
    content = content.replace(old_les12_inzicht, new_les12_inzicht)
    changes += 1
    print("4. Imperfecte scène aan les 12 toegevoegd")
else:
    print("WARNING: Les 12 inzicht 'correctie is richting' niet gevonden")

# ============================================================
# 5. LES 29 (id:29, "Dit heeft gevolgen") uitbreiden
# Zoek de probeer van les 29 en voeg daarvoor een extra noot toe
# ============================================================

old_les29_probeer = "{type:'probeer', tekst:'Je hoeft dit niet te oefenen.\\nMaar lees de opties door. Ze staan klaar als je ze nodig hebt.'}"

# Check if this exists
if old_les29_probeer in content:
    new_les29_block = """{type:'noot', tekst:'En hier is misschien het belangrijkste: een consequentie heeft altijd een afsluiting.\\nNa de straf \\u2014 hoe klein of groot ook \\u2014 moet er een moment zijn dat zegt: het is klaar. Wij zijn weer goed.\\nDat kan een hand op zijn schouder zijn. Een kort \\u201chet is klaar.\\u201d Of gewoon: je gedraagt je weer normaal tegen hem. Dat is het sein.\\nZonder afsluiting blijft Tim hangen in het gevoel dat hij iets fout deed. En dat is niet het doel. Het doel is: correctie, afsluiting, door.\\n\\nEn nog iets: gebruik dit niet als je boos bent. Consequenties werken alleen als ze kalm en bewust zijn. Als je ge\\u00efrriteerd bent, wacht. Benoem het later, als je helder bent. Een consequentie vanuit boosheid voelt als straf. Een consequentie vanuit rust voelt als structuur.'},
    {type:'noot', tekst:'Hoe vaak? Bijna nooit.\\nDe meeste dingen los je op met \\u00e9\\u00e9n zin: \\u201cdat was niet de afspraak.\\u201d Dat is genoeg in 80% van de gevallen.\\nEen consequentie is voor de uitzonderingen. Herhaald gedrag. Iets dat je al drie keer hebt benoemd. Of iets dat je echt raakt.\\nAls je consequenties te vaak gebruikt, verliezen ze hun kracht. Dan worden het regels in plaats van momenten. Houd het zeldzaam. Dan voelt het als het er is.'},
    {type:'probeer', tekst:'Je hoeft dit niet te oefenen.\\nMaar lees de opties door. Ze staan klaar als je ze nodig hebt.\\nEn als het moment komt: kies iets dat past bij wat er mis ging. Klein als het klein was. Groter als het nodig is. En sluit altijd af.'}"""

    content = content.replace(old_les29_probeer, new_les29_block)
    changes += 1
    print("5. Les 29 uitgebreid met twee extra noten en verrijkte probeer")
else:
    print("WARNING: Les 29 probeer niet gevonden")

# ============================================================
# 6. LES 32 (id:32, "Vandaag niet") uitbreiden
# ============================================================

old_les32_probeer = "{type:'probeer', tekst:'Dit hoef je niet te oefenen.\\nWeet dat het er is.'}"

if old_les32_probeer in content:
    new_les32_block = """{type:'noot', tekst:'Het verschil tussen \\u201cvandaag niet\\u201d en gewoon een slechte dag is belangrijk.\\nOp een gewone dag zonder dynamiek merk je misschien niks. Het leven gaat door.\\nMaar \\u201cvandaag niet\\u201d na een fout \\u2014 dat voelt Tim. Omdat hij weet wat hij mist. Omdat de structuur er normaal w\\u00e9l is. Die afwezigheid is de consequentie.\\n\\nEn het herstel is net zo belangrijk als het wegnemen.\\nAls je de dynamiek teruggeeft, doe het bewust. Niet \\u201coh ja, we doen het weer.\\u201d Maar: \\u201ckom hier.\\u201d Of de halsband weer neerleggen. Dat moment \\u2014 het terugkrijgen \\u2014 is voor Tim misschien het krachtigste van alles.'},
    {type:'probeer', tekst:'Dit hoef je niet te oefenen. Het is een gereedschap voor het moment dat je het nodig hebt.\\nAls dat moment komt: wees duidelijk. \\u201cVandaag niet.\\u201d Geen uitleg, geen discussie.\\nEn als je het teruggeeft: maak het een moment. Dat is de cirkel.'}"""

    content = content.replace(old_les32_probeer, new_les32_block)
    changes += 1
    print("6. Les 32 uitgebreid met extra noot en verrijkte probeer")
else:
    print("WARNING: Les 32 probeer niet gevonden")

# ============================================================
# 7. PROBEER-BLOK LES 9 (check-in) verrijken met hoe/wanneer
# ============================================================

old_les9_probeer = "{type:'probeer', tekst:'Plan \\u00e9\\u00e9n check-in.\\nGeen groot gesprek. Gewoon op een rustig moment:\\n\\u201cHoe was voor jou?\\u201d\\nLuister. Deel. En ga dan weer verder met jullie dag.'}"

new_les9_probeer = "{type:'probeer', tekst:'Plan \\u00e9\\u00e9n check-in deze week.\\nKies een rustig moment: zondagochtend met koffie, een wandeling, of als Milou naar school is.\\nGeen groot gesprek \\u2014 \\u00e9\\u00e9n open vraag: \\u201cHoe was deze week voor jou?\\u201d\\nLuister zonder te reageren. Deel zelf ook iets.\\nEn dan weer verder met jullie dag. Dat is alles.'}"

if old_les9_probeer in content:
    content = content.replace(old_les9_probeer, new_les9_probeer)
    changes += 1
    print("7. Les 9 probeer verrijkt met timing/context")
else:
    print("WARNING: Les 9 probeer niet gevonden")

# ============================================================
# WRITE
# ============================================================

with open(FILE, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\nKlaar! {changes} wijzigingen doorgevoerd.")
