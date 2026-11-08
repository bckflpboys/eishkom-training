# -*- coding: utf-8 -*-
"""
build_poetry.py - Generates the 25 poetry items for Afrikaans HL P2 Nov 2025.
Questions 1 to 5:
- Question 1: "27 april 1994" (Vincent Oliphant) - Opstelvraag [10]
- Question 2: "Briefie aan Madiba" (Sandra O'Kelly) - Kontekstueel [10] (2.1, 2.2.1, 2.2.2, 2.3, 2.4, 2.5)
- Question 3: "'n Paternoster vir Suid-Afrika" (Lina Spies) - Kontekstueel [10] (3.1, 3.2, 3.3, 3.4, 3.5, 3.6)
- Question 4: "Suiwer wiskunde" (N.P. van Wyk Louw) - Kontekstueel [10] (4.1, 4.2, 4.3, 4.4, 4.5, 4.6)
- Question 5: "Ek is my ma se kind" (Danelle Jacobs) - Kontekstueel [10] (5.1, 5.2, 5.3, 5.4, 5.5, 5.6)
"""

import json

SOURCE_ID = "dbe-afrikaans_hl-g12-p2-2025-nov"
MEMO_ID = "dbe-afrikaans_hl-g12-p2-2025-nov-memo"

POETRY_RUBRIC = """### ASSESSERINGSRUBRIEK VIR OPSTELVRAAG – HUISTAAL: POËSIE [10 PUNTE]

| Kriteria | Uitsonderlik | Knap | Gemiddeld | Elementêr | Onvoldoende |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **INHOUD**<br>Interpretasie van onderwerp. Diepte van argument, verantwoordbaarheid en insig in teks.<br>**(6 PUNTE)** | **5–6**<br>- Diepgaande interpretasie van onderwerp<br>- Reeks treffende argumente wat behoorlik uit die gedig gerugsteun is<br>- Uitstekende begrip van die genre en gedig | **4**<br>- Toon begrip van die onderwerp en het die onderwerp goed geïnterpreteer<br>- Respons redelik gedetailleerd<br>- Begrip van genre en gedig duidelik | **3**<br>- Redelike interpretasie van die onderwerp<br>- Enkele deeglike argumente gegee, maar nie almal ewe goed gemotiveer nie<br>- Basiese begrip van genre en gedig | **2**<br>- Onbevredigende interpretasie van die onderwerp<br>- Enkele argumente word ondersteun, maar bewyse nie altyd oortuigend nie<br>- Onvoldoende begrip van genre en gedig | **0–1**<br>- Geen begrip van die onderwerp nie<br>- Byna geen punte wat die onderwerp ondersteun nie<br>- Leerder het nie die genre en gedig onder die knie nie |
| **STRUKTUUR EN TAAL**<br>Struktuur, logiese vloei en aanbieding. Taalgebruik, toon en styl gebruik in opstel.<br>**(4 PUNTE)** | **4**<br>- Samehangende struktuur<br>- Argumente goed gestruktureer en daar is duidelike ontwikkeling<br>- Taalgebruik, toon en styl is volwasse, dit beïndruk en is korrek<br>- Grammatika, spelling en punktuasie feitlik foutvry | **3**<br>- Duidelike struktuur en logiese vloei van argument<br>- Vloei van argumente kan gevolg word<br>- Taalgebruik grootliks korrek<br>- Toon en styl is grootliks korrek | **2**<br>- Enkele bewyse van struktuur<br>- 'n Goed gestruktureerde logiese vloei en samehang ontbreek in die opstel<br>- Geringe taalfoute<br>- Toon en styl meestal gepas | **1**<br>- Struktuur toon tekens van swak beplanning<br>- Argumente nie logies gerangskik nie<br>- Taalfoute beduidend<br>- Toon en styl nie geskik nie | **0–1**<br>- Struktuur swak<br>- Ernstige taalfoute<br>- Foutiewe styl |
"""

PASSAGE_POEM_1 = """### 27 april 1994 – Vincent Oliphant

```text
 1 uiteindelik vou ek die verlede toe
 2 knyp sy vlerke tussen duim en vinger vas
 3 tot hy veilig deur 'n gleuf in die geskiedenis glip
 4 en anderkant
 5 wonderbaarlik
 6 vry
 7 die duif van vrede sy blou vlerke sprei

 8 sodat my nuutgebore stem na woorde smag
 9 om 'n lied vir my land
10 soos 'n vlag aan die tong te laat sweef
11 bo die geruislose val van skanse van die vel

12 sodat ek vry uit die vervreemding tree
13 om in die oë van vergetenes en langverlorenes
14 uiteindelik myself te kan sien
15 soos iemand wat ek nooit geken het nie

16 om aan hulle die hand te gee
17 en te voel hoe vlees en vlees ontmoet

18 want een lyn van bloed loop deur die eeue
19 loop deur die ganse geskiedenis
20 loop deur elke uithoek van die land
21 loop deur my en loop deur jou
22 van Genesis tot nou
```
*[Bron: Die sagte vlees, Tafelberg, 1998]*"""

PASSAGE_POEM_2 = """### Briefie aan Madiba – Sandra O'Kelly

```text
 1 Liewe Madiba, ek skryf die vir jou.
 2 Ek weet jy kry briefies soos my een aan jou.
 3 Ons het nooit ontmoet nie, maar voordat jy groet.
 4 Wil ek jou iets vra, dit is iets wat ek moet.

 5 Gee my jou boeie, ek wil dit dra.
 6 Die merke op jou hande, jou vrese jou vrae
 7 Ek sal dit oppas, dit altyd bewaar.
 8 Eendag met liefde aan my kinders oordra.

 9 Liewe Madiba, jy sal van my hou.
10 Ek's lief vir my land en sy mense en sou 
11 so graag wil kom kuier en net met jou praat.
12 Oor ditjies en datjies en goed uit my hart.

13 Gee my jou drome, ek wil dit sien.
14 Die prys so betaal om ander te dien.
15 Ek sal dit koester die wêreld sal weet.
16 Jou voorbeeld en liefde sal ons nooit vergeet.

17 Gee my jou ambag, ek wil dit leer.
18 Hoe 'n leier en koning sy mense kan eer.
19 Ek sal dit beoefen, ek sal dit ken.
20 Dis teerheid en liefde wat ander kan wen.

21 Gee my jou drome, ek wil dit sien.
22 Die prys so betaal om ander te dien.
23 Ek sal dit koester, die wêreld sal weet.
24 Jou voorbeeld en liefde sal ons nooit vergeet.

25 Liewe Madiba, ek skryf die vir jou.
26 Ek weet daar's baie briefies soos my een aan jou.
27 Ons het nooit ontmoet nie, maar voordat jy groet.
28 Wil ek jou iets vra, dit is iets wat ek moet.
```
*[Bron: Sarah Theron se album Terug na jou, Select Musiek]*"""

PASSAGE_POEM_3 = """### 'n Paternoster vir Suid-Afrika – Lina Spies

```text
 1 Here, laat die name geheilig word
 2 van al die kinders van die land –

 3 van hulle
 4 wat modderkoekies gebak het uit sy aarde,
 5 dassies skrikgemaak het in sy klowe,
 6 wol getrap het in sy krale.

 7 Ek het asemloos toegekyk:
 8 swart bolywe geboë oor magtelose diere
 9 en skerp skêre wat my laat wag het,
10 bang vir die glip-slag, die bloed, die pyn.
11 Maar die swart versigtige hande
12 het selde dieper as die wit geknip
13 en ek kon die lootjies uitdeel
14 want die arbeider was sy loon waardig
15 volgens die aantal wat hy vrygemaak het
16 om ligvoets teen die somerheuwels uit te wei.

17 Maar die bale is lankal toegewerk en weggestuur,
18 die wololie van my voete afgewas,
19 my bene nie meer lam getrap nie.

20 Vergewe ons, die vergeetagtiges, die uitgerustes,
21 soos ons hulle vergewe, die luidrugtiges
22 wat nooit binne die kraal was nie,
23 wat nooit rietperd gery
24 en kaalvoet geloop het nie,

25 en Here, sien ons hande aan:
26 Kyk, om my wit pols is 'n armband van gras;
27 my donker speelmaat het dit kunstig gevleg
28 soos ek nooit kon nie ...

29 Aan U behoort die land
30 en die son
31   en die skape van sy weiding

32 Gee ons liefdevolle hande, Heer,
33 en sny U self versigtig aan die belemmerende kleed
34 dat daar nie onnodig bloed verspil nie

35 en deel U self die lootjies uit
```
*[Bron: Digby Vergenoeg, Human en Rousseau, 1971]*"""

PASSAGE_POEM_4 = """### Suiwer wiskunde – NP van Wyk Louw

```text
1 Die uurwerk kantel. En die ligbruin by
2 hang roerloos voor die blom wat nooit bevrug
3 word, nooit sal saadskiet, welk, en nooit verby
4 hierdie verstarde uur sal groei. Die lug

5 het stil soos ys gaan staan, so wit en blou.
6 Die brander wat wou oorbuig, val, en skuim,
7 bly in sy ligte sirkels vasgehou
8 en moet sy see 'n ewigheid versuim.
```
*[Bron: Nuwe Verse, Tafelberg, 1954]*"""

PASSAGE_POEM_5 = """### Ek is my ma se kind – Danelle Jacobs

```text
 1 Ek het my pa se oë,
 2 maar ek sien die wêreld soos my ma dit sien.
 3 Nege maande lank was haar baar my tuiste,
 4 en nou, al 18 jaar lank, is my hart hare.
 5 Ek sal volbors voor haar staan en haar beskerm teen enige seer,
 6 want sy het kleintyds my bebloede knieë met sagte hande versorg.
 7 Om te dink, daar was 'n tyd toe ek nie my ma kon verdra nie,
 8 maar die Here weet, ek verstaan dit nou:
 9 my ma was ook eens 'n dogtertjie,
10 en die wêreld het ook haar groen oë laat lek.
11 Sy was ook seergemaak
12 en sy wil net seker maak
13 dat ek nie dieselfde deurmaak nie.
14 Sy het vir my die vrede geskep wat sy nooit kon vind nie.
15 Ek het my pa se oë,
16 maar ek is my ma se kind.
```
*[Bron: POORT, 2024]*"""


def get_poetry_items():
    items = []

    # Question 1: Essay
    q1_memo = f"""VRAAG 1: LITERÊRE OPSTEL
"27 april 1994" – Vincent Oliphant

Hierdie vraag word aan die hand van die aangehegte ASSESSERINGSRUBRIEK VIR LITERÊRE OPSTEL – HUISTAAL: POËSIE nagesien.

LET WEL:
• Dis 'n breë raamwerk van feite.
• Al die feite hoef nie genoem te word nie.
• Nasienriglyn by Vraag 1:
  - Vir uitsonderlike inhoud sal die kandidaat minstens 1 van elk aanbied, m.a.w. minstens 1 voor- en alleenplasing, 1 voorbeeld van halfrym en 1 retoriese middel.
  - Die kandidaat kan die aspekte in enige volgorde aanbied.

ARGUMENTE WORD AANGEBIED EN ONDERSTEUN OF GEÏLLUSTREER DEUR NA DIE TEKS TE VERWYS:

**Inleiding:**
Die kandidaat bied 'n gepaste inleiding aan.

**1. VOOR- EN ALLEENPLASING:**
- *Voorplasing van "uiteindelik":* Die spreker se afwagting vir sy nuutgevonde vryheid word deur voorplasing uitgehef. Die woord "uiteindelik" word aan die begin van die eerste versreël geplaas om die spreker se emosionele verligting en vreugde oor die einde van apartheid te beklemtoon (Versreël 1: "uiteindelik vou ek die verlede toe"). Ook die afwagting van die spreker vir sy nuutgevonde vryheid word deur die voorplasing van "uiteindelik" in versreël 14 uitgelig, wat terselfdertyd die gebruik van "uiteindelik" in versreël 1 bevestig (Versreël 14: "uiteindelik myself te kan sien").
- *Voorplasing van "loop":* Die vooruitgang na vryheid word deur voorplasing van "loop" beklemtoon. Die woord "loop" aan die begin van versreëls 19–21 beklemtoon die vryheidsgedagte en die vooruitgang na en proses na vryheid, versoening en eenheid (Versreël 19: "loop deur die ganse geskiedenis..", Versreël 20: "loop deur elke uithoek", Versreël 21: "loop deur my en loop deur jou...").
- *Voorplasing van "sodat":* Die voorplasing van "sodat" beklemtoon die gevolge van die stemproses (Versreël 8: "sodat my nuutgebore stem na woorde smag...", Versreël 12: "sodat ek vry uit die vervreemding tree").
- *Alleenplasing van "wonderbaarlik":* Die spreker se ontsag vir hierdie nuwe vryheid word deur alleenplasing versterk. Die alleenstaande woord, "wonderbaarlik", beklemtoon die buitengewone en amper onwerklike aard van die nuutgevonde vryheid (Versreël 5: "wonderbaarlik").
- *Alleenplasing van "vry":* Die uiteindelike vervulling van die spreker se vryheidsbegeerte word deur alleenplasing beklemtoon. Die woord "vry" word alleen in 'n reël geplaas, wat die ervaring van vryheid na 'n hewige onderdrukking beklemtoon (Versreël 6: "vry").

**2. HALFRYM:**
- *Alliterasie van "v"-klanke:* Die spreker se emosionele reis na vryheid word klankmatig deur alliterasie versterk. Die herhaling van die "v"-klank beklemtoon hoe die spreker die verlede toevou en hoe die toekoms, wat deur vryheid gekenmerk word, intree (Versreël 1 en 2: "vou ek die verlede toe/knyp sy vlerke", Versreël 7: "Die duif van vrede sy blou vlerke sprei").
- *Alliterasie van "g"-klanke:* Die g-alliterasie skep 'n vloeiende en ritmiese effek wat 'n ligte/positiewe toon bewerkstellig en sodoende die vryheidstema ondersteun (Versreël 3: "tot hy veilig deur 'n gleuf in die geskiedenis glip").
- *Assonansie van "e"-klanke:* Die verbondenheid tussen mense en die geskiedenis word deur assonansie ondersteun. Die herhaling van die "e"-klank in woorde soos "vergetenes" en "langverlorenes" dra by tot 'n melancholiese toon, wat die emosionele diepte van die nuutgevonde vryheid in die gedig versterk (Versreël 13 en 14: "in die oë van vergetenes en langverlorenes/uiteindelik myself te kan sien").
- *Alliterasie van "s"-klanke:* Die bevryding van die stem en identiteit word deur halfrym geaktiveer. Die "s"-alliterasie boots die vloeiende beweging van 'n vlag of vlerke na, wat die idee van vryheid en oorwinning simboliseer (Versreëls 7 tot 11: "die duif van vrede sy blou vlerke sprei/sodat my nuutgebore stem na woorde smag/om 'n lied vir my land/soos 'n vlag aan die tong te laat sweef").

**3. RETORIESE MIDDELE:**
- *Herhaling van "vry":* Die herhaling van "vry" beklemtoon die vryheidsgedagte. Die woord "vry" word herhaal om die kernboodskap van die gedig te versterk – die spreker is uiteindelik vry en bewus van sy nuwe identiteit (Versreël 6 en 12: "vry"/"sodat ek vry uit die vervreemding tree").
- *Herhaling van "uiteindelik":* Die herhaling van "uiteindelik" in versreël 14 sluit aan by die afwagtinggedagte van versreël 1. Die woord "uiteindelik" word herhaal om aan te dui dat die spreker ná 'n lang stryd sy plek in die samelewing kan inneem en sy identiteit kan omhels (Versreël 1 en 14: "uiteindelik vou ek die verlede toe"/"uiteindelik myself te kan sien").
- *Herhaling van "loop deur":* Die vryheidsgedagte deur die mens se verbondenheid aan mekaar word beklemtoon deur middel van herhaling. Die herhaling van "loop deur" in die slotstrofe wys hoe die mens deur die geskiedenis onafskeidbaar aan mekaar verweef is. Dié herhaling beklemtoon dat vryheid ook in die erkenning van 'n gedeelde menslikheid en die besef dat mense vanaf een bloedlyn afkomstig is, lê (Versreëls 18 tot 21: "loop deur die eeue/loop deur die ganse geskiedenis/loop deur my en loop deur jou").

**Slot:**
Die kandidaat bied 'n gepaste slot aan.

[10]

{POETRY_RUBRIC}"""

    items.append({
        "item_id": f"{SOURCE_ID}-1",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "1",
        "marks": 10,
        "topic": 'Voorgeskrewe Poësie: "27 april 1994" (Vincent Oliphant) - Literêre Opstel',
        "passage": PASSAGE_POEM_1,
        "question": "Die vryheidsgedagte wat in die gedig uitgelig word, word effektief deur middel van voor- en alleenplasing, halfrym en retoriese middele oorgedra.\n\nBespreek hierdie stelling in 'n opstel van 250 tot 300 woorde. [10]",
        "memo": q1_memo,
        "final_answer": "Die vryheidsgedagte word versterk deur voorplasing ('uiteindelik', 'loop') en alleenplasing ('wonderbaarlik', 'vry'), halfrym (v- en g-alliterasie, e-assonansie) wat emosionele bevryding en ritme beklemtoon, en retoriese herhaling ('vry', 'uiteindelik', 'loop deur') wat die historiese oorgang na vryheid, versoening en gedeelde menslikheid uitlig.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # Question 2: Briefie aan Madiba
    # 2.1
    items.append({
        "item_id": f"{SOURCE_ID}-2.1",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "2.1",
        "marks": 3,
        "topic": 'Voorgeskrewe Poësie: "Briefie aan Madiba" (Sandra O\'Kelly)',
        "passage": PASSAGE_POEM_2,
        "question": "Benoem die strofebou EN die rymsoort wat deurgaans in die gedig gebruik word. Verduidelik in watter opsig die rymsoort effektief is. (3)",
        "memo": "* Kwatryn $\\checkmark$\n\nEN\n\n* Paarrym $\\checkmark$\n\nEN\n\n* Aangesien daar slegs TWEE persone/die spreker en Madiba in die gedig betrokke is, is die paarrym waar TWEE versreëls rym, baie effektief om na twee mense te verwys. $\\checkmark$",
        "final_answer": "Kwatryn; Paarrym; Die paarrym (twee rymende reëls) is effektief omdat daar slegs twee persone (die spreker en Madiba) by die gesprek betrokke is.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 2.2.1
    items.append({
        "item_id": f"{SOURCE_ID}-2.2.1",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "2.2.1",
        "marks": 1,
        "topic": 'Voorgeskrewe Poësie: "Briefie aan Madiba" (Sandra O\'Kelly)',
        "passage": PASSAGE_POEM_2,
        "question": "Die verkleinwoord in die titel impliseer 'n bepaalde stemming.\n\n2.2.1 Watter gesprekstyl word deur die titel van die gedig opgeroep? (1)",
        "memo": "Informeel/gemeensaam/kinderlik/vriendelik $\\checkmark$\n\n*(Die kandidaat bied 'n soortgelyke antwoord vir EEN punt aan.)*",
        "final_answer": "Informeel / gemeensaam / kinderlik / vriendelik",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 2.2.2
    items.append({
        "item_id": f"{SOURCE_ID}-2.2.2",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "2.2.2",
        "marks": 2,
        "topic": 'Voorgeskrewe Poësie: "Briefie aan Madiba" (Sandra O\'Kelly)',
        "passage": PASSAGE_POEM_2,
        "question": "Die verkleinwoord in die titel impliseer 'n bepaalde stemming.\n\n2.2.2 Bewys met TWEE ander aspekte uit die gedig dat hierdie spesifieke gesprekstyl deurgaans in die gedig volgehou word. (2)",
        "memo": "Enige TWEE van die volgende vir 1 punt elk:\n* Die aanspreekvorm: \"Liewe Madiba\"/\"Liewe\"/\"Madiba\" $\\checkmark$\n* Die gebruik van die informele (persoonlike voornaamwoord) \"jy\"/ (besitlike voornaamwoord) \"jou\" $\\checkmark$\n* Die gebruik van (verklein)woorde bv. \"ditjies en datjies\" $\\checkmark$\n\n*(Die kandidaat bied enige TWEE antwoorde vir EEN punt elk aan.)*",
        "final_answer": "Die informele aanspreekvorm 'Liewe Madiba' en die gebruik van die informele voornaamwoord 'jy'/'jou' (of verkleinwoorde soos 'ditjies en datjies').",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 2.3
    items.append({
        "item_id": f"{SOURCE_ID}-2.3",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "2.3",
        "marks": 2,
        "topic": 'Voorgeskrewe Poësie: "Briefie aan Madiba" (Sandra O\'Kelly)',
        "passage": PASSAGE_POEM_2,
        "question": "Die spreker vra drie vrae aan Madiba.\n\nWatter EEN vraag word in die gedig as die belangrikste vraag uitgehef? Motiveer jou antwoord. (2)",
        "memo": "\"Gee my jou drome, ek wil dit sien.\" $\\checkmark$\n\nEN\n\nDie herhaling van hierdie vraag/versoek (in twee afsonderlike strofes) lig hierdie versoek as die belangrikste uit. $\\checkmark$",
        "final_answer": "\"Gee my jou drome, ek wil dit sien.\" Dit word as die belangrikste versoek uitgehef omdat dit in twee afsonderlike strofes (strofe 4 en 6) herhaal word.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 2.4
    items.append({
        "item_id": f"{SOURCE_ID}-2.4",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "2.4",
        "marks": 1,
        "topic": 'Voorgeskrewe Poësie: "Briefie aan Madiba" (Sandra O\'Kelly)',
        "passage": PASSAGE_POEM_2,
        "question": "Benoem die stylfiguur in versreël 5. (1)",
        "memo": "Sinekdogee / metonimia $\\checkmark$",
        "final_answer": "Sinekdogee (of metonimia)",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 2.5
    items.append({
        "item_id": f"{SOURCE_ID}-2.5",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "2.5",
        "marks": 1,
        "topic": 'Voorgeskrewe Poësie: "Briefie aan Madiba" (Sandra O\'Kelly)',
        "passage": PASSAGE_POEM_2,
        "question": "Evalueer die effektiwiteit van versreëls 25 tot 28 as slot van die gedig. Motiveer jou antwoord. (1)",
        "memo": "Versreëls 25 tot 28 is effektief, want:\nDie herhaling van dieselfde woorde as dié in versreëls 1 tot 4 versterk die gedagte van 'n sikliese slot./dat hierdie woorde die hoogtepunt van die gedig vorm./versterk die gedagte van \"Briefie aan Madiba\"./die titel van die gedig. $\\checkmark$\n\n*(Die kandidaat bied 'n soortgelyke antwoord vir EEN punt aan.)*",
        "final_answer": "Dit is effektief omdat die herhaling van die aanvanklike strofe 'n sikliese slot skep en die gedagte van 'n persoonlike briefie aan Madiba beklemtoon.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # Question 3: 'n Paternoster vir Suid-Afrika
    # 3.1
    items.append({
        "item_id": f"{SOURCE_ID}-3.1",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "3.1",
        "marks": 1,
        "topic": "Voorgeskrewe Poësie: \"'n Paternoster vir Suid-Afrika\" (Lina Spies)",
        "passage": PASSAGE_POEM_3,
        "question": "Watter woord in strofe 1 maak die gedig inklusief? (1)",
        "memo": "al $\\checkmark$",
        "final_answer": "al",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 3.2
    items.append({
        "item_id": f"{SOURCE_ID}-3.2",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "3.2",
        "marks": 2,
        "topic": "Voorgeskrewe Poësie: \"'n Paternoster vir Suid-Afrika\" (Lina Spies)",
        "passage": PASSAGE_POEM_3,
        "question": "Verwys na versreëls 7 tot 16.\n\nWatter emosie by die spreker dra by tot die aanvanklike stemming in hierdie versreëls EN watter nuwe stemming word deur die woord \"Maar\" (versreël 11) ingelei? (2)",
        "memo": "Vrees/Magteloosheid/Bekommernis $\\checkmark$\n*(Die kandidaat bied 'n soortgelyke antwoord vir EEN punt aan.)*\n\nEN\n\nVerwondering/blydskap/geluk/verligting/gerusstelling $\\checkmark$\n*(Die kandidaat bied 'n soortgelyke antwoord vir EEN punt aan.)*",
        "final_answer": "Aanvanklike emosie: Vrees / bekommernis / angs; Nuwe stemming: Verligting / verwondering / gerusstelling.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 3.3
    items.append({
        "item_id": f"{SOURCE_ID}-3.3",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "3.3",
        "marks": 2,
        "topic": "Voorgeskrewe Poësie: \"'n Paternoster vir Suid-Afrika\" (Lina Spies)",
        "passage": PASSAGE_POEM_3,
        "question": "Die \"ek\" van versreël 7 het hom-/haarself nie as deel van die \"hulle\" (versreël 3) beskou nie.\n\nBewys aan die hand van versreëls 7 tot 19 EN versreëls 26 tot 28 dat dié stelling enersyds waar EN andersyds onwaar is. (2)",
        "memo": "* **Waar:** In versreël 7 is die \"ek\" net 'n toekyker / In versreël 13 is die \"ek\" die een wat die lootjies uitdeel (dus nie een van die werkers nie) / wololie afgewas en bene nie meer lam getrap nie. $\\checkmark$\n* **Onwaar:** In versreëls 26 tot 28 het die \"ek\" en die \"donker speelmaat\" saamgespeel (arband van gras wat saam gevleg is). $\\checkmark$\n\n*(Die kandidaat bied 'n soortgelyke antwoord vir EEN punt elk aan.)*",
        "final_answer": "Waar: Die spreker was 'n toeskouer wat lootjies uitgedeel het eerder as 'n arbeider. Onwaar: Die spreker het 'n donker speelmaat gehad en hulle het as kinders saam gespeel.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 3.4
    items.append({
        "item_id": f"{SOURCE_ID}-3.4",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "3.4",
        "marks": 1,
        "topic": "Voorgeskrewe Poësie: \"'n Paternoster vir Suid-Afrika\" (Lina Spies)",
        "passage": PASSAGE_POEM_3,
        "question": "Verwys na versreël 25 en versreël 32.\n\nDink jy hier is sprake van progressie in die verwysing na \"hande\" in hierdie versreëls? Motiveer jou antwoord. (1)",
        "memo": "Ja $\\checkmark$\nDaar is progressie van letterlike hande en wat ons daarmee doen na \"liefdevolle hande\", met ander woorde hoe ons teenoor mense optree/verhoudings moet herstel. $\\checkmark$\n\n*(Die kandidaat moet na beide kante van die progressie vir EEN punt verwys. Die kandidaat kan nie 'n NEE-antwoord aanbied nie. Die kandidaat bied 'n soortgelyke antwoord vir EEN punt aan.)*",
        "final_answer": "Ja, daar is progressie van letterlike hande wat dade verrig na figuurlike 'liefdevolle hande' wat dui op versoening, deernis en die herstel van menseverhoudings.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 3.5
    items.append({
        "item_id": f"{SOURCE_ID}-3.5",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "3.5",
        "marks": 1,
        "topic": "Voorgeskrewe Poësie: \"'n Paternoster vir Suid-Afrika\" (Lina Spies)",
        "passage": PASSAGE_POEM_3,
        "question": "Dink jy dat die slotreël van die gedig as gerusstellend of waarskuwend beskou kan word? Motiveer jou antwoord. (1)",
        "memo": "Gerusstellend, want God wat liefdevol is, sal self almal beloon, dus vanuit genade/liefde evalueer. $\\checkmark$\n\nOF\n\nWaarskuwend, God sal almal na verdienste beloon, dus op grond van hulle dade oordeel. $\\checkmark$\n\n*(Die kandidaat bied 'n soortgelyke antwoord vir EEN punt aan.)*",
        "final_answer": "Gerusstellend (God sal self vanuit genade en liefde beloon) OF Waarskuwend (God sal regverdig oordeel en elkeen volgens sy verdienste en dade beloon).",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 3.6
    items.append({
        "item_id": f"{SOURCE_ID}-3.6",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "3.6",
        "marks": 3,
        "topic": "Voorgeskrewe Poësie: \"'n Paternoster vir Suid-Afrika\" (Lina Spies)",
        "passage": PASSAGE_POEM_3,
        "question": "Die gedig se titel skep die indruk dat hierdie gedig 'n gebed vir Suid-Afrika is.\n\nMotiveer hierdie standpunt met verwysing na DRIE verskillende gebedsaspekte wat in die gedig na vore kom. (3)",
        "memo": "Enige DRIE van die volgende vir 1 punt elk:\n* \"laat die name geheilig word\" (aanbidding/heiliging) $\\checkmark$\n* \"vergewe ons, die vergeetagtiges\" (skuldbelydenis/vergifnis) $\\checkmark$\n* \"Aan U behoort die land\" (lofprysing/erkenning van God se soewereiniteit) $\\checkmark$\n* \"Gee ons liefdevolle hande, Heer,\" (voorbede/versoek) $\\checkmark$\n* Die Here word regstreeks aangespreek (\"Here\", \"U\", \"Heer\") $\\checkmark$\n\n*(Die kandidaat bied enige DRIE antwoorde vir EEN punt elk aan. Die kandidaat kan ook die soortgelyke gebedsaspekte omskryf.)*",
        "final_answer": "Drie gebedsaspekte: Heiliging van God se naam ('laat die name geheilig word'), skuldbelydenis en versoek om vergifnis ('Vergewe ons...'), en lofprysing/erkenning van God se heerskappy ('Aan U behoort die land').",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # Question 4: Suiwer wiskunde
    # 4.1
    items.append({
        "item_id": f"{SOURCE_ID}-4.1",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "4.1",
        "marks": 2,
        "topic": 'Voorgeskrewe Poësie: "Suiwer wiskunde" (N.P. van Wyk Louw)',
        "passage": PASSAGE_POEM_4,
        "question": "Die vraag wat in die gedig beantwoord word, is: Wat sou gebeur as tyd sou stilstaan?\n\nWatter woord in versreël 1 veroorsaak die totstilstandkoming van tyd EN watter TWEE opeenvolgende woorde in versreël 2 dien as inleiding tot die gevolge daarvan in strofe 1? (2)",
        "memo": "\"kantel\" $\\checkmark$\n\nEN\n\n\"hang roerloos\" / \"nooit bevrug\" $\\checkmark$",
        "final_answer": "Woord in versreël 1: 'kantel'; Twee opeenvolgende woorde in versreël 2: 'hang roerloos'.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 4.2
    items.append({
        "item_id": f"{SOURCE_ID}-4.2",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "4.2",
        "marks": 1,
        "topic": 'Voorgeskrewe Poësie: "Suiwer wiskunde" (N.P. van Wyk Louw)',
        "passage": PASSAGE_POEM_4,
        "question": "Evalueer die geslaagdheid van die kort eerste sin in versreël 1. Motiveer jou antwoord. (1)",
        "memo": "Die kort sin (met die punt aan die einde) is geslaagd, want dit bevestig/beklemtoon die finaliteit van die gedagte dat tyd tot stilstand kom. $\\checkmark$\n\n*(Die kandidaat kan nie aandui dat dit nie geslaagd is nie.)*",
        "final_answer": "Dit is geslaagd omdat die kort sin met die punt die skielikheid en absolute finaliteit van die stilstand van tyd beklemtoon.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 4.3
    items.append({
        "item_id": f"{SOURCE_ID}-4.3",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "4.3",
        "marks": 2,
        "topic": 'Voorgeskrewe Poësie: "Suiwer wiskunde" (N.P. van Wyk Louw)',
        "passage": PASSAGE_POEM_4,
        "question": "Verwys na versreël 2 en 3.\n\nWatter woorde sluit by die kringloop van lewe EN dood onderskeidelik aan? (2)",
        "memo": "Lewe: \"bevrug\" / \"(sal) saadskiet\" $\\checkmark$\n\nEN\n\nDood: \"welk\" $\\checkmark$",
        "final_answer": "Lewe: 'bevrug' / 'saadskiet'; Dood: 'welk'.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 4.4
    items.append({
        "item_id": f"{SOURCE_ID}-4.4",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "4.4",
        "marks": 3,
        "topic": 'Voorgeskrewe Poësie: "Suiwer wiskunde" (N.P. van Wyk Louw)',
        "passage": PASSAGE_POEM_4,
        "question": "Benoem die beeldspraak wat in versreël 5 voorkom EN verduidelik dan watter halfrym die tempo in hierdie beeldspraak bewerkstellig. Waarom, dink jy, is dié spesifieke halfrym gepas? (3)",
        "memo": "Beeldspraak: vergelyking (\"stil soos ys\") $\\checkmark$\n\nEN\n\nAssonansie (die lang aa-klanke in \"gaan staan\") / s-alliterasie (\"stil soos\") $\\checkmark$\n\nEN\n\nDie lang aa-klanke ondersteun die stollingsproses (alles gaan stadiger word as die tyd sou stilstaan en uiteindelik vries) / s-alliterasie versterk die gedagte van stilstand en stilte. $\\checkmark$",
        "final_answer": "Beeldspraak: Vergelyking; Halfrym: Assonansie van die lang aa-klanke (of s-alliterasie); Toepaslikheid: Die gerekte aa-klanke vertraag die leestempo en boots die bevriesing en stolling van tyd na.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 4.5
    items.append({
        "item_id": f"{SOURCE_ID}-4.5",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "4.5",
        "marks": 1,
        "topic": 'Voorgeskrewe Poësie: "Suiwer wiskunde" (N.P. van Wyk Louw)',
        "passage": PASSAGE_POEM_4,
        "question": "Watter ooreenkoms toon versreël 7 met die by se \"hang roerloos\" in versreël 2? (1)",
        "memo": "Die brander bly ook in die lug \"hang\" / vries in die lug / is met ander woorde \"roerloos\" / word in sy beweging vasgevries. $\\checkmark$\n\n*(Die kandidaat bied 'n soortgelyke antwoord vir EEN punt aan.)*",
        "final_answer": "Die brander word ook in die middel van sy beweging vasgevries en bly roerloos in die lug hang.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 4.6
    items.append({
        "item_id": f"{SOURCE_ID}-4.6",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "4.6",
        "marks": 1,
        "topic": 'Voorgeskrewe Poësie: "Suiwer wiskunde" (N.P. van Wyk Louw)',
        "passage": PASSAGE_POEM_4,
        "question": "Verwys na versreël 8.\n\nVerduidelik in watter opsig hier sprake van 'n sikliese slot in die gedig is. (1)",
        "memo": "\"ewigheid\" skakel met uurwerk/tyd-gedagte in versreël 1 / \"versuim\" skakel met wat gebeur wanneer die uurwerk kantel, dus tyd wat stilgestaan het en die ewigheid betree het. $\\checkmark$",
        "final_answer": "Die woord 'ewigheid' skakel terug na die begin van die gedig waar die 'uurwerk' gekantel het, wat die ewige stilstand van tyd volvoer.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # Question 5: Ek is my ma se kind (Ongesiene gedig)
    # 5.1
    items.append({
        "item_id": f"{SOURCE_ID}-5.1",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "5.1",
        "marks": 2,
        "topic": 'Ongesiene Poësie: "Ek is my ma se kind" (Danelle Jacobs)',
        "passage": PASSAGE_POEM_5,
        "question": "Skryf 'n woord uit versreël 2 neer wat deur herhaling beklemtoon word EN verduidelik die progressie vanaf letterlike tot figuurlike betekenis in versreël 1 en 2. (2)",
        "memo": "sien / \"sien\" / maar / \"maar\" $\\checkmark$\n\nEN\n\nDie woord \"sien\" deur middel van die pa se oë dui op 'n letterlike kyk na dinge / fisiese ooreenkoms met die pa se oë, maar in versreël 2 is sprake van 'n figuurlike \"sien\", met ander woorde wat die ma se beskouing van die wêreld/lewensuitkyk is. $\\checkmark$\n\n*(Die letterlike en die figuurlike \"sien\" moet deur die kandidaat vir EEN punt omskryf word.)*",
        "final_answer": "Woord: 'sien' (of 'maar'); Progressie: In versreël 1 dui 'oë' op die fisiese/letterlike oorerwing van die pa, terwyl 'sien' in versreël 2 figuurlik verwys na haar ma se lewensbeskouing en perspektief op die wêreld.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 5.2
    items.append({
        "item_id": f"{SOURCE_ID}-5.2",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "5.2",
        "marks": 3,
        "topic": 'Ongesiene Poësie: "Ek is my ma se kind" (Danelle Jacobs)',
        "passage": PASSAGE_POEM_5,
        "question": "Watter funksie verrig die beskrywende woorde in versreël 6? Haal 'n versreël aan wat die doel agter die ma se opvoeding uitspel EN dui aan in watter opsig die ma se grootwordjare van die spreker s'n verskil. (3)",
        "memo": "* Dit dui daarop/beklemtoon dat die ma die dogter sagkens/liefdevol versorg het (wanneer sy seergekry het) / versterk die kontras tussen die seerkry (\"bebloede knieë\") en die ma se liefdevolle versorging/vertroosting (\"sagte hande\"). $\\checkmark$\n\nEN\n\n* \"dat ek nie dieselfde deurmaak nie.\" / \"Sy het vir my die vrede geskep wat sy nooit kon vind nie.\" $\\checkmark$\n\nEN\n\n* Die dogter het in vrede/sonder seerkry/swaarkry grootgeword, maar haar ma kon nie vrede vind nie / het as dogtertjie seergekry / swaargekry. $\\checkmark$\n\n*(Die kandidaat moet na beide kante van die verskil vir EEN punt verwys.)*",
        "final_answer": "Funksie: Beklemtoon die ma se deernisvolle en liefdevolle versorging in kontras met pyn; Aanhaling: 'dat ek nie dieselfde deurmaak nie' (of 'Sy het vir my die vrede geskep wat sy nooit kon vind nie'); Verskil: Die spreker het in vrede en sekuriteit grootgeword, terwyl haar ma as kind swaargekry en pyn ervaar het.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 5.3
    items.append({
        "item_id": f"{SOURCE_ID}-5.3",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "5.3",
        "marks": 1,
        "topic": 'Ongesiene Poësie: "Ek is my ma se kind" (Danelle Jacobs)',
        "passage": PASSAGE_POEM_5,
        "question": "Watter aktuele kwessie ten opsigte van tieners word in versreël 7 aangeraak? (1)",
        "memo": "Rebelsheid van tieners / Opstandigheid van tieners / Onverdraagsaamheid teenoor ouers / Swak ouer-kind-verhoudings $\\checkmark$\n\n*(Die kandidaat bied 'n soortgelyke antwoord vir EEN punt aan.)*",
        "final_answer": "Tieners se opstandigheid, rebelsheid en onverdraagsaamheid teenoor hulle ouers.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 5.4
    items.append({
        "item_id": f"{SOURCE_ID}-5.4",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "5.4",
        "marks": 2,
        "topic": 'Ongesiene Poësie: "Ek is my ma se kind" (Danelle Jacobs)',
        "passage": PASSAGE_POEM_5,
        "question": "Benoem die beeldspraak in versreël 10. Dink jy hierdie beeld is effektief? Motiveer jou antwoord. (2)",
        "memo": "Personifikasie / Metafoor $\\checkmark$\n\nEN\n\nJa\nDit beklemtoon die ma se hartseer / Dit sluit by die volgende reël waarin hartseer genoem word aan / Dit versterk die onkeerbaarheid van haar trane (wat aansluit by baie seer / haar moeilike omstandighede). $\\checkmark$\n\n*(Die kandidaat kan nie 'n NEE-antwoord aanbied nie. Die twee vrae word onafhanklik van mekaar nagesien.)*",
        "final_answer": "Beeldspraak: Personifikasie (of metafoor); Effektiwiteit: Ja, dit beeld treffend uit hoe intens en aanhoudend die ma se trane en hartseer in die verlede gevloei het.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 5.5
    items.append({
        "item_id": f"{SOURCE_ID}-5.5",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "5.5",
        "marks": 1,
        "topic": 'Ongesiene Poësie: "Ek is my ma se kind" (Danelle Jacobs)',
        "passage": PASSAGE_POEM_5,
        "question": "Kies die korrekte antwoord en skryf net die vraagnommer en letter neer, bv. 5.5 E.\n\nDeur middel van watter retoriese middel word die woord \"maar\" in die gedig beklemtoon?\n\nA Herhaling\nB Voorplasing\nC Personifikasie\nD Vergelyking (1)",
        "memo": "A / Herhaling $\\checkmark$",
        "final_answer": "A",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 5.6
    items.append({
        "item_id": f"{SOURCE_ID}-5.6",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "5.6",
        "marks": 1,
        "topic": 'Ongesiene Poësie: "Ek is my ma se kind" (Danelle Jacobs)',
        "passage": PASSAGE_POEM_5,
        "question": "Watter afleiding oor die spreker se verhouding met haar pa kan volgens versreël 15 en 16 gemaak word? (1)",
        "memo": "Die pa en die dogter het nie 'n emosionele band nie / Daar is slegs 'n uiterlike/fisiese ooreenkoms, maar geen diep emosionele verbintenis soos met haar ma nie. $\\checkmark$\n\n*(Die kandidaat bied 'n soortgelyke antwoord vir EEN punt aan.)*",
        "final_answer": "Daar is 'n gebrek aan 'n hegte emosionele band tussen die spreker en haar pa (daar is slegs 'n fisiese ooreenkoms).",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    return items

if __name__ == "__main__":
    items = get_poetry_items()
    print(f"Generated {len(items)} poetry items.")
    print("Total marks:", sum(x["marks"] for x in items))
