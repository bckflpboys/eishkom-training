# -*- coding: utf-8 -*-
"""
build_dramas.py - Generates the 28 drama items for Afrikaans HL P2 Nov 2025.
Questions 14 to 17:
- Question 14: Krismis van Map Jacobs (Adam Small) - Opstelvraag [25]
- Question 15: Krismis van Map Jacobs (Adam Small) - Kontekstueel [25] (15.1, 15.2, 15.3.1, 15.3.2, 15.4, 15.5, 15.6.1, 15.6.2, 15.7, 15.8, 15.9, 15.10, 15.11, 15.12)
- Question 16: Mis (Reza de Wet) - Opstelvraag [25]
- Question 17: Mis (Reza de Wet) - Kontekstueel [25] (17.1, 17.2, 17.3.1, 17.3.2, 17.4, 17.5, 17.6, 17.7, 17.8, 17.9.1, 17.9.2, 17.10)
"""

import json

SOURCE_ID = "dbe-afrikaans_hl-g12-p2-2025-nov"
MEMO_ID = "dbe-afrikaans_hl-g12-p2-2025-nov-memo"

DRAMA_RUBRIC = """### AFDELING B EN C: ASSESSERINGSRUBRIEK VIR OPSTELVRAAG – HUISTAAL: ROMAN EN DRAMA [25 PUNTE]

| Kriteria | Uitsonderlik | Knap | Gemiddeld | Elementêr | Onvoldoende |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **INHOUD**<br>Interpretasie van onderwerp. Diepte van argument, verantwoordbaarheid en insig in teks.<br>**(15 PUNTE)** | **12–15**<br>- Diepgaande interpretasie van onderwerp<br>- Uitsonderlike respons: 14–15; Uitstekende respons: 12–13<br>- Reeks treffende argumente wat behoorlik uit die roman/drama gerugsteun is<br>- Uitstekende begrip van die genre en teks | **9–11**<br>- Toon begrip van die onderwerp en het die onderwerp goed geïnterpreteer<br>- Respons redelik gedetailleerd<br>- Enkele deeglike argumente gegee, maar nie almal ewe goed gemotiveer nie<br>- Begrip van genre en teks duidelik | **6–8**<br>- Redelike interpretasie van die onderwerp; nie alle aspekte in detail ondersoek nie<br>- Enkele goeie punte ter ondersteuning van die onderwerp<br>- Enkele argumente word ondersteun, maar bewyse nie altyd oortuigend nie<br>- Basiese begrip van genre en teks | **4–5**<br>- Onbevredigende interpretasie van die onderwerp: byna geen aspekte in detail ondersoek nie<br>- Min punte wat die onderwerp ondersteun<br>- Baie min relevante argumente<br>- Weinig begrip van genre en teks | **0–3**<br>- Geen begrip van die onderwerp nie<br>- Swak poging om die vraag te beantwoord<br>- Argumente oortuig nie<br>- Leerder het nie die genre en teks onder die knie nie |
| **STRUKTUUR EN TAAL**<br>Struktuur, logiese vloei en aanbieding. Taalgebruik, toon en styl gebruik in opstel.<br>**(10 PUNTE)** | **8–10**<br>- Samehangende struktuur<br>- Argumente goed gestruktureer en daar is duidelike ontwikkeling<br>- Uitstekende inleiding en slot<br>- Inleiding, slot en ander paragrawe samehangend georganiseer<br>- Taalgebruik, toon en styl is volwasse, dit beïndruk en is korrek | **6–7**<br>- Duidelike struktuur<br>- Logiese vloei van argument<br>- Inleiding, slot en ander paragrawe samehangend georganiseer<br>- Taalgebruik, toon en styl is grootliks korrek | **4–5**<br>- Enkele bewyse van struktuur<br>- Logika en samehang is duidelik, maar met foute<br>- Paragrafering meestal korrek<br>- Enkele taalfoute; toon en styl meestal gepas | **2–3**<br>- Struktuur toon tekens van swak beplanning<br>- Argumente nie logies gerangskik nie<br>- Paragrafering foutief<br>- Taalfoute beduidend; toon en styl nie geskik nie | **0–1**<br>- Gebrek aan beplande struktuur belemmer vloei van argumente<br>- Argumente nie logies gerangskik nie<br>- Taalfoute en foutiewe styl laat hierdie skryfstuk misluk<br>- Paragrafering foutief<br>- Styl en toon nie geskik nie |
| **PUNTEVERSPREIDING** | **20–25** | **15–19** | **10–14** | **5–9** | **0–4** |
"""

PASSAGE_KRISMIS_CONTEXT = """### KRISMIS VAN MAP JACOBS – Adam Small
[Konteks: Die drama speel af op die Kaapse Vlakte gedurende apartheid ná die gedwonge verskuiwings uit Distrik Ses. Johnnie ('Map') Jacobs word ná sewe jaar uit die tronk op parool vrygelaat waar hy opgesluit was vir die moord op Ivan Philander. Die gemeenskap worstel met armoede, bendegeweld en ontvlugting, terwyl Blanchie, sy jeugliefde, ook probeer ontsnap uit haar pynlike verlede.]"""

PASSAGE_TEKS_I = """### TEKS I – KRISMIS VAN MAP JACOBS (Adam Small)

```text
 1 CAVERNELIS: Dis hoekom ek en Maudie en Blanchie hierso wil weg! 
 2 
 3 LA GUMA:    Best of luck to you, mister Cavernelis. Jy maak geld om hierso yt te 
 4             briek. Best of luck. Maar 'is 'n sterk tronk dié. Kyk, die tralies! (Hy trek 
 5             regaf strepe in die lug, met albei hande, en wys na die geboue in die 
 6             omgewing.) 
 7 
 8 CAVERNELIS: Anyway, dis hoekom ons seker nie nou gaan worry met 'n shower in 
 9             die huis nie, mister La Guma. Dis 'n onnodige uitgawe, op 'n huurhuis. 
10 
11 LA GUMA:    (luister nie): 'n Sterk tronk, sê ek … 
12 
13 CAVERNELIS: (plaas die tou in La Guma se hande terug, maar dié let dit skaars op): 
14             Ja … 
15 
16 LA GUMA:    Nou is Map Jacobs ook terug … 
17             Cavernelis sê niks.  
18             Yt die tronk yt. Terug, hiérnatoe. Kan jy dit vir jou imagine? Hiérnatoe? 
19             Cavernelis sê niks.  
20 
21 LA GUMA:    Kamma yt die tronk yt. Na dit toe. (Hy wys, bars dan uit van die lag.) 
22             An' you know, what really gets me? Lat die mense almal actually nog 
23             bid! Nog in die Here in glo! Praise the Lord, en al daai jazz! 
24 
25 CAVERNELIS: Wel … 
26             Bo by die woonstelvenster verskyn Blanchie se gesig weer, om te sien 
27             wat haar pa ophou. Sy roep dan. 
28 
29 BLANCHIE:   Daddy! Daddy! 
30 
31 LA GUMA:    En ek hoor Map Jacobs is oek kamma gebekeer! 
32 
33 CAVERNELIS: Ek kom, Blanchie …! Okay, goodnight, mister La Guma … 
34 
35 LA GUMA:    (is nog nie klaar gepraat nie. Cavernelis huiwer weer): Weet jy hoekom 
36             hulle vir hom Map ge-call het? You know why?
```"""

PASSAGE_TEKS_J = """### TEKS J – KRISMIS VAN MAP JACOBS (Adam Small)

```text
 1 BLANCHIE: … (Dan skielik, hard.) Johnnie … Wat het … met ons gebeur … Wat … 
 2           Ek … is … so … sleg … 
 3 MAP:      (sit sy hand op haar mond): Nee! … Jy's … goed … 
 4 BLANCHIE: Jy lieg … Jy … lieg, Johnnie … lieg, lieg, lieg!!! 
 5 MAP:      (asof hy haar geskreeu nie hoor nie): Dis ek wat sleg is ... Dis … ek … 
 6           Blanchie … Wat het met ons gebeur … 
 7           (Hy hou haar vas, stýf; sy hom. Hy lig sy oë op.) Apostel George! Here! 
 8           Ma! … Blanchie … Blanchie … Wat het met ons … gebeur … 
 9 BLANCHIE: Ek is so vuil, Johnnie … 
10 MAP:      Jy is … mooi … 
11 BLANCHIE: (saggies): Johnnie … Wat het … van ons geword …  
12           'n Lang stilte. 
13 MAP:      Alles … en niks … Blanchie … 
14 BLANCHIE: (huil): Johnnie … 
15 MAP:      Alles … en niks … (Hy huil en lag. Dan sy ook – huil en lag.) Ek het vir jou 
16           … alles ge-vertel … Blanchie … voor Apostel George … voor die Here … 
17           en voor Ma … Daar is niks meer nie … 
18 BLANCHIE: Ek het vir jou … ook … ge-vertel … alles … Johnnie … 
19           Hulle hou mekaar styf vás. Soen mekaar hartstogtelik. Die wind van die 
20           Kaapse Vlakte wáái, en blý waai, maar dan word dit ook die geluid van 'n 
21           trein wat deur die townships reis. En skielik 'n huilende sirene en remme 
22           van die trein wat staal op staal laat sing. Blanchie en Map weerloos teen 
23           die wind en die huilende trein – teen die gebeurtenis.
```"""

PASSAGE_MIS_CONTEXT = """### MIS – Reza de Wet
[Konteks: Die drama speel af op die vooraand van 31 Augustus 1936 tydens die Groot Depressie in 'n armoedige huisie op 'n Suid-Afrikaanse plattelandse dorp. Miem en haar dogter Meisie leef in 'n ingehokte, neerdrukkende bestaan waar hulle mis in sakke verpak terwyl die pa, Gabriël, homself al sewe jaar op die solder afsonder. Jaarliks op dié nag verdwyn 'n jong meisie wanneer die sirkus op die dorp is.]"""

PASSAGE_TEKS_K = """### TEKS K – MIS (Reza de Wet)

```text
 1 MIEM:   (kyk op. Hard) O ja … Onthou tog die slopemmer! Dis al twee dae!  
 2         (Sag aan MEISIE) Weet jy, hy was die hele middag so onrustig. (Tel weer 
 3         haar voet op en laat dit op 'n stoel rus)  
 4 MEISIE: (knik) Ek het gehoor. 
 5         'n Sagte huilwind word gehoor. 
 6 MIEM:   (kyk op) Heen en weer. Heen en weer. Sonder ophou. 
 7 MEISIE: Ja. 
 8 MIEM:   Ek dink hy voel dit aan. Die onheil. As vannag tog net verby wil gaan. Al 
 9         die verstandiges het voorsorg getref. Slotte en grendels. Luike 
10         toegespyker. Maar jy hoef jou nie te kwel nie, my kind. Ek sal die hele 
11         nag by jou waak. 
12 MEISIE: Ja, Ma. 
13 MIEM:   Sit regop! Hoeveel keer moet ek dit nog sê? As jy 'n man wil hê, moet jy 
14         let op jou postuur. 
15         Hulle werk verder. 
16 MIEM:   (na 'n stilte) Dan is dit altesame tweehonderd. Ek het vanmiddag gaan 
17         tel. Die ander honderd-en-sewentig is heeltemal vol en toegewerk. (Byt 
18         garing met haar tande af) So ja. (Hou die sak uit na MEISIE) 
19         MEISIE neem die sak en sit dit op die hoop. Terwyl MIEM verder praat, 
20         trek sy 'n lengte goiing van die rol af en meet dit. 
21 MIEM:   Kom nou, Meisie, hou reguit. 
22         MEISIE trek die goiing styf terwyl MIEM sny. 
23 MIEM:   (sny) Die skêr is al weer stomp, Meisie, jy moet dit slyp. Meestal beesmis. 
24         So dertig perdemis en tien vark. Ja, ons doen goed die maand. 
25         Vroeglente wil almal die grond bewerk. (Baie vriendelik) Miskien koop ek 
26         vir jou 'n nuwe rok. (Neem die goiing, skuif die rol eenkant toe en gaan 
27         sit moeisaam)  
28         Die wind huil om die huis. 
29 MEISIE: (sit ook) Dankie, Ma. 
30         Kort stilte. Hulle werk. 
31 MIEM:   Wat was dit! 
32 MEISIE: Wat, Ma?
```"""

PASSAGE_TEKS_L = """### TEKS L – MIS (Reza de Wet)

```text
 1 MIEM:      (trots) Sy is mooi, nè? 
 2 KONSTABEL: Ja, Mevrou. 
 3            MEISIE staan op en beweeg stadig terug na haar stoel. Daar is 'n kort 
 4            stilte. MEISIE werk aan haar sak. MIEM en GERTIE kyk na die 
 5            KONSTABEL. Die KONSTABEL kyk voor hom uit. Die valdeur klap 
 6            hard oop. MEISIE kyk op. 'n Slopemmer sak stadig na onder. 
 7 MEISIE:    Kyk, Ma! Hier kom dit! 
 8 MIEM:      (hard. Kyk op) Wees versigtig! Dis al meer as twee dae! 
 9            MEISIE, MIEM en GERTIE hou die emmer dop. Dit sak baie stadig af 
10            tot op die vloer. Die emmer is vol slymerige bruin water. Aan die 
11            uitdrukking op almal se gesigte kan 'n mens aflei dat die inhoud baie 
12            sleg ruik. MEISIE gaan nader en met haar kop half weggedraai, begin 
13            sy die tou losmaak. GERTIE druk 'n sakdoek voor haar neus. MEISIE 
14            kry die knoop los. Die tou word vinnig opgetrek en die valdeur klap hard 
15            toe. 
16 MIEM:      Gaan maak dit tog leeg, my kind. En spoel dit goed uit. 
17 KONSTABEL: Laat ek help. 
18 MEISIE:    Dankie. As dit vol is, is dit baie swaar. As jy eenkant vat, dan vat ek die 
19            anderkant. 
20 KONSTABEL: Dis goed so. 
21 MEISIE:    (bly) En as ons baie gesels, dan hoef ons nie die musiek te hoor nie.
```"""


def get_drama_items():
    items = []

    # =========================================================================
    # VRAAG 14: KRISMIS VAN MAP JACOBS – OPSTELVRAAG [25]
    # =========================================================================
    q14_memo = f"""VRAAG 14: KRISMIS VAN MAP JACOBS – OPSTELVRAAG
Adam Small

Hierdie vraag word aan die hand van die aangehegte RUBRIEK VIR DIE NASIEN VAN DIE OPSTELVRAAG VIR DIE ROMAN EN DRAMA (bladsy 52) nagesien.

LET WEL:
• Dis 'n breë raamwerk van feite.
• Al die feite hoef nie genoem te word nie.

ARGUMENTE WORD AANGEBIED EN ONDERSTEUN OF GEÏLLUSTREER DEUR NA DIE TEKS TE VERWYS:

**Inleiding:**
Die kandidaat bied 'n gepaste inleiding aan.

**1. MAP HANTEER SY NEGATIEWE WERKLIKHEID:**
- *Werkloosheid en bendes:* Map hanteer die harde werklikheid van werkloosheid en werkreservering op die Kaapse Vlakte deur by bendes aan te sluit. Alhoewel hy matriek gehad het, was daar slegs werk as 'n 'messenger' beskikbaar weens sy velkleur (Bl. 24: "Toe's al die jobs vir wittes... Net messenger vir my! Messenger! Wit bastards!!").
- *Soeke na identiteit:* Map voel uitgesluit en soek 'n plek waar hy behoort. Die bende bied hom 'n identiteit, beskerming en mag, maar lei tot sy ondergang. Sy tatoeëermerke versinnebeeld sy desperate soeke na identiteit (Bl. 31, 51: "'it was 'n terrible gesoek seker, vir 'n identity... Daai's wat 'n man doen as jy desperate is, in 'n plek soes dié").
- *Misdaad en tronkstraf:* As leier van die bende gee hy opdragte vir misdade en roof. Hy vermoor uiteindelik sy vriend Ivan Philander en word tronk toe gestuur. Tronkstraf word 'n fisiese tronk binne die groter sosiale tronk van die Kaapse Vlakte (Bl. 15, 23).
- *Godsdiensbekering:* Map probeer ontvlug van sy skuldgevoelens en kriminele verlede deur hom tot godsdiens te wend onder leiding van Apostel George. Sy bekering en belydenis voor sy ma en Blanchie bring emosionele heling, al bly die gemeenskap agterdogtig (Bl. 48, 62–64).

**2. BLANCHIE HANTEER HAAR NEGATIEWE WERKLIKHEID:**
- *Ontvlugting uit armoede:* Blanchie wil desperaat ontsnap uit die haglike omstandighede van die Kaapse Vlakte en hul huurhuis sonder 'n stort (Bl. 9–10). Sy smag na 'n luukse lewe en 'n man wat haar kan wegneem.
- *Modelwerk en prostitusie:* Sy ontvlug deur as 'model' by Lonely Hearts Massage Parlour te gaan werk, wat in werklikheid prostitusie is vir ryk wit mans (Bl. 28, 42). Dit bring egter selfveragting en diepe skaamte mee (Bl. 58: "Ek is so vuil, Johnnie...").
- *Sosiale verwerping:* Haar poging om deur haar voorkoms en seksualiteit te ontvlug, lei tot verdere veroordeling deur die gemeenskap (Maud noem haar 'n 'jintoe', Cyril en Tommy verag haar) (Bl. 35, 45).
- *Heling by Johnnie:* Uiteindelik vind Blanchie vrede wanneer sy en Map mekaar in hul weerloosheid vind, hul geheime bely en ware liefde bo oppervlakkige ontvlugting kies (Bl. 68–70).

**Slot:**
Die kandidaat bied 'n gepaste slot aan.

[25]

{DRAMA_RUBRIC}"""

    items.append({
        "item_id": f"{SOURCE_ID}-14",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "14",
        "marks": 25,
        "topic": "Drama: Krismis van Map Jacobs (Adam Small) - Literêre Opstel",
        "passage": PASSAGE_KRISMIS_CONTEXT,
        "question": "Bespreek in 'n opstel van 400 tot 450 woorde hoe die aktuele tema van ontvlugting uit 'n negatiewe werklikheid in Map en Blanchie se lewens vanaf die eksposisie tot aan die einde van die drama na vore kom. [25]",
        "memo": q14_memo,
        "final_answer": "Map ontvlug werkloosheid en sosiale marginalisering deur by bendes aan te sluit en mag deur misdaad en tatoeëermerke te soek, en wend hom later tot godsdiensbekering om van sy skuldgevoelens verlos te word; Blanchie ontvlug die troostelose armoede van die Vlakte deur modelwerk en prostitusie by Lonely Hearts Massage Parlour, wat haar egter met selfveragting laat totdat sy en Map uiteindelik mekaar in emosionele belydenis en versoening vind.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # =========================================================================
    # VRAAG 15: KRISMIS VAN MAP JACOBS – KONTEKSTUELE VRAAG [25]
    # =========================================================================
    # 15.1
    items.append({
        "item_id": f"{SOURCE_ID}-15.1",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "15.1",
        "marks": 1,
        "topic": "Drama: Krismis van Map Jacobs (Adam Small) - Kontekstueel",
        "passage": PASSAGE_TEKS_I,
        "question": "\"Dis hoekom ek en Maudie en Blanchie hierso wil weg!\" (Reël 1)\n\nNa watter spesifieke ruimte verwys Cavernelis? (1)",
        "memo": "Die Kaapse Vlakte / die township / die huurwoonstelblokke op die Vlakte. $\\checkmark$",
        "final_answer": "Die Kaapse Vlakte (of die township / woonstelle).",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 15.2
    items.append({
        "item_id": f"{SOURCE_ID}-15.2",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "15.2",
        "marks": 1,
        "topic": "Drama: Krismis van Map Jacobs (Adam Small) - Kontekstueel",
        "passage": PASSAGE_TEKS_I,
        "question": "Watter wanpersepsie oor La Guma sou sy woorde aan Cavernelis: \"Best of luck.\" (reël 3) by die leser kon skep? (1)",
        "memo": "Dit kan die wanpersepsie skep dat La Guma werklik simpatiek is en opreg omgee vir Cavernelis se welsyn / hom die beste toewens, terwyl hy eintlik sinies, spottend en verbitterd is. $\\checkmark$",
        "final_answer": "Dat hy werklik simpatiek en opreg besorg is oor Cavernelis se gesin, terwyl hy eintlik sinies en spottend is.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 15.3.1
    items.append({
        "item_id": f"{SOURCE_ID}-15.3.1",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "15.3.1",
        "marks": 1,
        "topic": "Drama: Krismis van Map Jacobs (Adam Small) - Kontekstueel",
        "passage": PASSAGE_TEKS_I,
        "question": "\"Maar 'is 'n sterk tronk dié. Kyk, die tralies!\" (Reël 3)\n\n15.3.1 Wat word deur La Guma se woorde oor die ruimte waarbinne hulle hul bevind, geïmpliseer? (1)",
        "memo": "Dit impliseer dat die Kaapse Vlakte self 'n onontkombare tronk van armoede, wanhoop en maatskaplike verval is waaruit niemand werklik kan ontsnap nie / die omstandighede sal nooit verander nie. $\\checkmark$",
        "final_answer": "Dit impliseer dat die Kaapse Vlakte self 'n metaforiese tronk is waaruit inwoners nie kan ontsnap nie.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 15.3.2
    items.append({
        "item_id": f"{SOURCE_ID}-15.3.2",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "15.3.2",
        "marks": 2,
        "topic": "Drama: Krismis van Map Jacobs (Adam Small) - Kontekstueel",
        "passage": PASSAGE_TEKS_I,
        "question": "\"Maar 'is 'n sterk tronk dié. Kyk, die tralies!\" (Reël 3)\n\n15.3.2 Na watter gebeurtenis het Blanchie besluit om uit hierdie \"tronk\" te ontsnap EN watter gebeurtenis veroorsaak dat sy nie daarin slaag nie? (2)",
        "memo": "* **Besluit om te ontsnap:** Nadat Map vir Ivan Philander vermoor het en tronk toe gestuur is / toe sy besef die lewe op die Vlakte het vir haar geen toekoms nie. $\\checkmark$\n\nEN\n\n* **Mislukking van ontsnapping:** Haar modelwerk het in prostitusie ontaard en die wit mans het haar slegs uitgebuit / sy het swanger geraak en 'n aborsie gehad / sy is maatskaplik en emosioneel verwerp en moes terugkeer. $\\checkmark$",
        "final_answer": "Besluit: Ná Map se moord op Ivan en sy gevangenisstraf; Mislukking: Haar 'modelwerk' het in vernederende prostitusie ontaard en sy is deur haar minnaars in die steek gelaat.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 15.4
    items.append({
        "item_id": f"{SOURCE_ID}-15.4",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "15.4",
        "marks": 2,
        "topic": "Drama: Krismis van Map Jacobs (Adam Small) - Kontekstueel",
        "passage": PASSAGE_TEKS_I,
        "question": "Die neweteks in reël 12 lei tot die retoriese vrae in reël 13.\n\nMotiveer hierdie stelling deur na die dramatiese doel van die retoriese vrae te verwys EN dui aan op watter manier die toename in emosie in dié retoriese vrae aangedui word. (2)",
        "memo": "* **Dramatiese doel:** Die retoriese vrae beklemtoon La Guma se verbystering, ongeloof en sinisme dat Map enigiets positiefs op die Vlakte kan verwag / dit betrek Cavernelis en die gehoor om na te dink oor die sinloosheid van terugkeer. $\\checkmark$\n\nEN\n\n* **Toename in emosie:** Dit word aangedui deur die herhaling van en klem op die woord \"hiérnatoe\" (met die klemteken). $\\checkmark$",
        "final_answer": "Dramatiese doel: Beklemtoon La Guma se ongeloof en sinisme oor die sinloosheid van terugkeer na 'n plek van ellende; Toename in emosie: Word aangedui deur die beklemtoonde herhaling van 'hiérnatoe'.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 15.5
    items.append({
        "item_id": f"{SOURCE_ID}-15.5",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "15.5",
        "marks": 2,
        "topic": "Drama: Krismis van Map Jacobs (Adam Small) - Kontekstueel",
        "passage": PASSAGE_TEKS_I,
        "question": "Verwys na reël 11 en reël 22.\n\nIn watter opsig kan die nuus oor Map se vrylating uit die tronk as die motoriese moment van die drama beskou word? Kan jy jou met La Guma se agterdog oor Map se bekering identifiseer? Motiveer jou antwoord. (2)",
        "memo": "* **Motoriese moment:** Die oomblik wanneer die gemeenskap verneem dat Map vrygelaat word, neem die spanning skerp toe en word al die aksies, vrese en verhoudings in die drama aan die gang gesit. $\\checkmark$\n\nEN\n\n* **Agterdog gemotiveer:**\n  - **Ja:** Map was 'n gewelddadige bendeleier en moordenaar; sy bekering kan bloot 'n slenters wees om parool te verkry. $\\checkmark$\n  - **OF**\n  - **Nee:** Enige sondaar verdien vergifnis en ware bekering is altyd moontlik ongeag die verlede. $\\checkmark$",
        "final_answer": "Motoriese moment: Die nuus oor sy vrylating ontketen al die dramatiese spanning en aksie in die gemeenskap; Agterdog: Ja (sy gewelddadige verlede regverdig skeptisisme dat dit 'n paroolfoefie is) OF Nee (elke mens kan opreg tot inkeer kom).",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 15.6.1
    items.append({
        "item_id": f"{SOURCE_ID}-15.6.1",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "15.6.1",
        "marks": 2,
        "topic": "Drama: Krismis van Map Jacobs (Adam Small) - Kontekstueel",
        "passage": PASSAGE_TEKS_I,
        "question": "\"Weet jy hoekom hulle vir hom Map ge-call het? You know why?\" (Reël 24 en 25)\n\n15.6.1 Noem enige EEN van Map se tatoeëermerke. Dink jy sy tatoeëermerke hou met sy karakterontwikkeling verband? Motiveer jou antwoord. (2)",
        "memo": "* Enige EEN tatoeëermerk (1 punt): 'n kaal vrou / 'n kitaar / die vure van die hel / 'n mombakkies. $\\checkmark$\n\nEN\n\n* **Ja:** Map se tatoeëermerke vorm die 'kaart' (map) van sy lewe; dit weerspieël sy soeke na identiteit en sy verlede as bendeleier, terwyl sy besef van hul betekenis sy begeerte na 'n nuwe lewe as bekeerde onderstreep. $\\checkmark$\n*(Die kandidaat kan nie 'n NEE-antwoord aanbied nie.)*",
        "final_answer": "Tatoeëermerk: 'n Kaal vrou (of 'n kitaar / die vure van die hel / 'n mombakkies); Karakterontwikkeling: Ja, die merke vorm 'n fisiese kaart van sy sondige verlede waaruit hy nou probeer groei na 'n gereinigde mens.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 15.6.2
    items.append({
        "item_id": f"{SOURCE_ID}-15.6.2",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "15.6.2",
        "marks": 1,
        "topic": "Drama: Krismis van Map Jacobs (Adam Small) - Kontekstueel",
        "passage": PASSAGE_TEKS_I,
        "question": "\"Weet jy hoekom hulle vir hom Map ge-call het? You know why?\" (Reël 24 en 25)\n\n15.6.2 Evalueer die geslaagdheid van die feit dat Map twee name het. Verwys na beide name in die motivering van jou antwoord. (1)",
        "memo": "Die twee name is geslaagd omdat dit sy twee uiteenlopende identiteite versinnebeeld: \"Johnnie\" verwys na die onskuldige seun/skoolkind wat potensiaal getoon het en na wie hy aan die einde terugkeer, terwyl \"Map\" verwys na die gevreesde bendeleier en misdadiger. $\\checkmark$\n*(Die kandidaat verwys na beide name vir EEN punt.)*",
        "final_answer": "Dit is geslaagd: 'Johnnie' verteenwoordig die onskuldige seun en geliefde, terwyl 'Map' verwys na die geharde bendeleier met die getatoeëerde liggaam.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 15.7
    items.append({
        "item_id": f"{SOURCE_ID}-15.7",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "15.7",
        "marks": 2,
        "topic": "Drama: Krismis van Map Jacobs (Adam Small) - Kontekstueel",
        "passage": PASSAGE_TEKS_J,
        "question": "Verwys na Blanchie se woorde in reël 1 en 2: \"Ek … is … so … sleg …\"\n\nNoem enige EEN karakter in die drama wat hierdie woorde van Blanchie ondersteun. Dink jy hierdie karakter se houding teenoor Blanchie is geregverdig? Motiveer jou antwoord. (2)",
        "memo": "* Enige EEN karakter (1 punt): Cyril / La Guma / Richie / Tommy / Maud $\\checkmark$\n\nEN\n\n* **Regverdiging:**\n  - **Ja:** Blanchie het as prostituut by Lonely Hearts Massage Parlour gewerk en 'n aborsie gehad, wat die gemeenskap se morele afkeur ontlok het. $\\checkmark$\n  - **OF**\n  - **Nee:** Hulle veroordeel haar sonder om haar desperate armoede en magteloosheid te verstaan en steun bloot op skinderstories. $\\checkmark$",
        "final_answer": "Karakter: Maud (of Cyril / La Guma / Tommy); Regverdiging: Ja (sy het as prostituut gewerk) OF Nee (hulle veroordeel haar gevoelloos sonder begrip vir haar uitsiglose armoede).",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 15.8
    items.append({
        "item_id": f"{SOURCE_ID}-15.8",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "15.8",
        "marks": 1,
        "topic": "Drama: Krismis van Map Jacobs (Adam Small) - Kontekstueel",
        "passage": PASSAGE_TEKS_J,
        "question": "Verwys na die neweteks in reël 3.\n\nIn watter opsig ondersteun die neweteks Map se woorde aan Blanchie in reël 3? (1)",
        "memo": "Map sit fisies sy hand op haar mond om haar te keer om sleg van haarself te praat, wat sy opbeurende woorde dat sy goed en mooi is, tasbaar versterk. $\\checkmark$",
        "final_answer": "Deur sy hand op haar mond te sit, weier hy fisies dat sy haarself verkleineer en bevestig hy sy woorde dat sy 'goed' is.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 15.9
    items.append({
        "item_id": f"{SOURCE_ID}-15.9",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "15.9",
        "marks": 1,
        "topic": "Drama: Krismis van Map Jacobs (Adam Small) - Kontekstueel",
        "passage": PASSAGE_TEKS_J,
        "question": "Verwys na reël 11: \"Wat het … van ons geword …\"\n\nWatter belangrike verskil ten opsigte van hulle situasie word deur die woorde \"geword\" (reël 11) en \"gebeur\" (reël 1 en 6) beklemtoon? (1)",
        "memo": "\"Gebeur\" dui daarop dat hulle passiewe slagoffers van hul omstandighede was, terwyl \"geword\" erkenning gee dat hulle ook self aktief verander het en 'n aandeel aan hul eie verval en identiteitsverlies gehad het. $\\checkmark$",
        "final_answer": "'Gebeur' dui op dinge wat hulle as slagoffers oorgekom het, terwyl 'geword' dui op die aktiewe innerlike verandering en verval van hul eie wese.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 15.10
    items.append({
        "item_id": f"{SOURCE_ID}-15.10",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "15.10",
        "marks": 2,
        "topic": "Drama: Krismis van Map Jacobs (Adam Small) - Kontekstueel",
        "passage": PASSAGE_TEKS_J,
        "question": "Verwys na reëls 15 tot 17.\n\nNoem TWEE maniere hoe Apostel George vir Map help om van sy skuldgevoelens verlos te word. (2)",
        "memo": "TWEE maniere (1 punt elk):\n* Apostel George help Map om te glo dat die Here sy sondes vergewe en hom van sy misdaadverlede kan verlos $\\checkmark$\n* Apostel George moedig Map aan om voor sy ma en Blanchie sy dade openlik te bely, wat sy ma help om hom te vergewe en sy versoening te voltooi $\\checkmark$",
        "final_answer": "Hy leer Map dat God sy sondes vergewe, en hy lei Map om sy dade eerlik voor sy ma en Blanchie te bely.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 15.11
    items.append({
        "item_id": f"{SOURCE_ID}-15.11",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "15.11",
        "marks": 4,
        "topic": "Drama: Krismis van Map Jacobs (Adam Small) - Kontekstueel",
        "passage": PASSAGE_TEKS_J,
        "question": "In reëls 15 tot 18 sê Map en Blanchie dat hulle vir mekaar \"alles\" vertel het.\n\nNoem DRIE dinge wat Map vir Blanchie moes vertel EN EEN ding wat Blanchie vir Map moes vertel om van hulle skuldgevoelens verlos te word. (4)",
        "memo": "* DRIE dinge wat Map moes vertel (enige drie vir 1 punt elk):\n  - Map het opdrag gegee om vroue te beroof $\\checkmark$\n  - Map het toestemming gegee vir verkragting $\\checkmark$\n  - Map het sy vriend Ivan Philander vermoor $\\checkmark$\n  - Map het homself aan die polisie oorgegee $\\checkmark$\n  - Map het 'n lewensveranderende bekering in die tronk ervaar $\\checkmark$\n\nEN\n\n* EEN ding wat Blanchie moes vertel (1 punt):\n  - Blanchie moes erken dat sy as prostituut vir wit mans gewerk het / 'n aborsie gehad het $\\checkmark$",
        "final_answer": "Map se belydenis (drie feite): Hy het opdrag gegee vir rooftogte, verkragting goedgekeur, en sy vriend Ivan vermoor; Blanchie se belydenis (een feit): Sy het as prostituut vir wit mans gewerk (of het 'n aborsie gehad).",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 15.12
    items.append({
        "item_id": f"{SOURCE_ID}-15.12",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "15.12",
        "marks": 3,
        "topic": "Drama: Krismis van Map Jacobs (Adam Small) - Kontekstueel",
        "passage": PASSAGE_TEKS_I + "\n\n" + PASSAGE_TEKS_J,
        "question": "Herlees die volgende reëls:\n\nTEKS I (reël 9 en 10): \"(plaas die tou in La Guma se hande terug, maar dié let dit skaars op): Ja …\"\nTEKS J (reëls 19 tot 22): \"Die wind van die Kaapse Vlakte wáái, en blý waai, maar dan word dit ook die geluid van 'n trein wat deur die townships reis. En skielik 'n huilende sirene en remme van die trein wat staal op staal laat sing.\"\n\nWatter stemming word onderskeidelik deur die geluid van die \"wind\" en die geluid van die \"trein\" in TEKS J geskep? Watter rol speel die herhalende motief van die \"tou\" in TEKS I om 'n soortgelyke stemming in die drama te versterk? (3)",
        "memo": "* **Stemming van die wind:** Desperaad / nostalgies / moedeloos / ongenaakbaar / droefgeestig. $\\checkmark$\n* **Stemming van die trein:** Hartseer / emosioneel intens / stemming van verlies / rou / naderende noodlot. $\\checkmark$\n\nEN\n\n* **Rol van die tou:** Die tou simboliseer die harde, meedoënlose lewe en die ongenaakbare omstandighede waarin die karakters vasgevang is, wat 'n gevoel van magteloosheid en hulpeloosheid versterk. $\\checkmark$",
        "final_answer": "Stemming wind: Ongenaakbaar, troosteloos en moedeloos; Stemming trein: Dreigend, hartseer en pynlik; Rol van tou: Simboliseer die inwoners se vasgevangenheid in 'n meedoënlose bestaan sonder uitkoms.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # =========================================================================
    # VRAAG 16: MIS – OPSTELVRAAG [25]
    # =========================================================================
    q16_memo = f"""VRAAG 16: MIS – OPSTELVRAAG
Reza de Wet

Hierdie vraag word aan die hand van die aangehegte RUBRIEK VIR DIE NASIEN VAN DIE OPSTELVRAAG VIR DIE ROMAN EN DRAMA (bladsy 52) nagesien.

LET WEL:
• Dis 'n breë raamwerk van feite.
• Al die feite hoef nie genoem te word nie.

ARGUMENTE WORD AANGEBIED EN ONDERSTEUN OF GEÏLLUSTREER DEUR NA DIE TEKS TE VERWYS:

**Inleiding:**
Die kandidaat bied 'n gepaste inleiding aan.

**1. MIEM PROBEER UIT HAAR NEGATIEWE OMSTANDIGHEDE ONTVLUG:**
- *Ontvlugting in matriargale beheer:* Miem ontvlug die harde werklikheid van Gabriël se afwesigheid deur self die beheer oor die huishouding oor te neem. Sy ontken die absurditeit van sy sewejarige verblyf op die solder deur gereeld met hom te praat asof hy deel van die gesin is (Bl. 5: "Ek het vir jou 'n broodjie gebak... Onthou tog die slopemmer!").
- *Ontvlugting in moraliteit en vooroordeel:* Miem handhaaf 'n streng puriteinse Calvinistiese fasade. Sy veroordeel die buitewêreld, die sirkus en ander vroue (soos Gertie se vrese) om haarself bo sonde en verval te verhef (Bl. 7–9).
- *Ontvlugting in materiële drome vir Meisie:* Sy probeer haar armoede en mislike bestaan ontvlug deur te droom van 'n geskikte man en 'n nuwe rok vir Meisie, terwyl sy haar terselfdertyd streng beheer en emosioneel onderdruk (Bl. 6, 12).
- *Ontvlugting in vrees en grendels:* Sy dink sy kan die onheil van die buitewêreld uitsluit deur vensters toe te spykers en deure te sluit, maar sluit ironies die gevaar (die Konstabel) binne-in haar eie huis toe (Bl. 10, 18).

**2. MEISIE PROBEER UIT HAAR NEGATIEWE OMSTANDIGHEDE ONTVLUG:**
- *Verstikkende gevangenskap:* Meisie leef in 'n klaustrofobiese omgewing waar sy gedwing word om sakke mis te stik, die slopemmer uit te gooi en onder haar ma se konstante kritiek te buig. Haar eie identiteit word onderdruk – sy word bloot "Meisie" genoem (Bl. 5–6).
- *Ontvlugting deur sintuie en die sirkus:* Sy ontvlug haar omstandighede deur skelm na die sirkusliggies te kyk en na die betowerende sirkusmusiek te luister. Dit verteenwoordig 'n wêreld van skoonheid, vryheid en kleur (Bl. 8, 14).
- *Die Konstabel as katalisator:* Wanneer die blinde Konstabel opdaag, gebruik hy Meisie se regte naam (Margareta Johanna) en komplimenteer haar skoonheid. Dit gee haar vir die eerste keer 'n gevoel van eiewaarde en ontketen haar begeerte om te ontsnap (Bl. 25–28).
- *Fisiese ontvlugting aan die einde:* Aan die einde van die drama trek Meisie haar wit aannemingsrok aan, gooi die slopemmer en die goiingsakke agter haar neer, en dans saam met die Konstabel by die agterdeur uit die nag en die mis in – 'n volkome, radikale ontvlugting uit haar moederlike tronk (Bl. 38–40).

**Slot:**
Die kandidaat bied 'n gepaste slot aan.

[25]

{DRAMA_RUBRIC}"""

    items.append({
        "item_id": f"{SOURCE_ID}-16",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "16",
        "marks": 25,
        "topic": "Drama: Mis (Reza de Wet) - Literêre Opstel",
        "passage": PASSAGE_MIS_CONTEXT,
        "question": "Bespreek in 'n opstel van 400 tot 450 woorde hoe die aktuele tema van ontvlugting uit 'n negatiewe werklikheid in Miem en Meisie se lewens vanaf die eksposisie tot aan die einde van die drama na vore kom. [25]",
        "memo": q16_memo,
        "final_answer": "Miem ontvlug haar somber werklikheid en Gabriël se selfafsondering op die solder deur streng Calvinistiese beheer, kunsmatige vroomheid en materiële drome vir Meisie te kweek, terwyl Meisie haar verstikkende arbeid en identiteitsloosheid ontvlug deur na die sirkusliggies en -musiek te smag totdat sy uiteindelik saam met die Konstabel in die mis verdwyn.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # =========================================================================
    # VRAAG 17: MIS – KONTEKSTUELE VRAAG [25]
    # =========================================================================
    # 17.1
    items.append({
        "item_id": f"{SOURCE_ID}-17.1",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "17.1",
        "marks": 1,
        "topic": "Drama: Mis (Reza de Wet) - Kontekstueel",
        "passage": PASSAGE_TEKS_K,
        "question": "Verwys na reël 1.\n\nNa watter gesuggereerde ruimte kyk Miem op? (1)",
        "memo": "Die solder / die solderluik waar Gabriël al sewe jaar lank woon. $\\checkmark$",
        "final_answer": "Die solder (waar Gabriël hom afsonder).",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 17.2
    items.append({
        "item_id": f"{SOURCE_ID}-17.2",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "17.2",
        "marks": 1,
        "topic": "Drama: Mis (Reza de Wet) - Kontekstueel",
        "passage": PASSAGE_TEKS_K,
        "question": "Verwys na reëls 1 tot 5.\n\nDink jy die neweteks in reël 5 is geslaagd teen die agtergrond van Miem se woorde? Motiveer jou antwoord. (1)",
        "memo": "Ja $\\checkmark$\nDie neweteks van die huilende wind ondersteun Miem se waarneming van Gabriël se onrus en bou die onheilspellende, onrusbarende en somber stemming van die nag op. $\\checkmark$",
        "final_answer": "Ja, die geluid van die huilwind beklemtoon die dreigende gevaar en sluit aan by Gabriël se rusteloosheid op die solder.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 17.3.1
    items.append({
        "item_id": f"{SOURCE_ID}-17.3.1",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "17.3.1",
        "marks": 1,
        "topic": "Drama: Mis (Reza de Wet) - Kontekstueel",
        "passage": PASSAGE_TEKS_K,
        "question": "Verwys na reëls 8 tot 11.\n\n17.3.1 Op watter datum speel die drama af? (1)",
        "memo": "31 Augustus 1936 $\\checkmark$",
        "final_answer": "31 Augustus 1936",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 17.3.2
    items.append({
        "item_id": f"{SOURCE_ID}-17.3.2",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "17.3.2",
        "marks": 2,
        "topic": "Drama: Mis (Reza de Wet) - Kontekstueel",
        "passage": PASSAGE_TEKS_K,
        "question": "Verwys na reëls 8 tot 11.\n\n17.3.2 Watter wanpersepsie oor Miem word in hierdie spreekbeurt geskep? Op watter manier bewys Miem die teendeel in die motoriese moment van die drama? (2)",
        "memo": "* **Wanpersepsie:** Dat Miem 'n waaksame, beskermende moeder is wat Meisie ten alle koste teen gevaar sal bewaar en die hele nag by haar sal waak. $\\checkmark$\n\nEN\n\n* **Teendeel in motoriese moment:** Wanneer daar aan die deur geklop word (motoriese moment), laat Miem die vreemde Konstabel in die huis in en stuur sy Meisie selfs later alleen saam met hom buitetoe om die slopemmer leeg te maak. $\\checkmark$",
        "final_answer": "Wanpersepsie: Dat Miem 'n onwrikbare wagter is wat Meisie veilig sal hou; Teendeel: Sy nooi die vreemde Konstabel self in die huis in en stuur Meisie alleen saam met hom buitetoe.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 17.4
    items.append({
        "item_id": f"{SOURCE_ID}-17.4",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "17.4",
        "marks": 2,
        "topic": "Drama: Mis (Reza de Wet) - Kontekstueel",
        "passage": PASSAGE_TEKS_K,
        "question": "Evalueer die geslaagdheid van Meisie se naam EN motiveer jou antwoord. Dui aan hoe Konstabel juis haar naam gebruik om haar te manipuleer. (2)",
        "memo": "* **Geslaagdheid van naam:** Die naam \"Meisie\" is geslaagd omdat dit haar identiteitloosheid, onderdanigheid en onbelangrikheid binne die gesin beklemtoon (sy is slegs 'n kind sonder eie identiteit). $\\checkmark$\n\nEN\n\n* **Manipulasie deur Konstabel:** Konstabel vra vir haar haar volle name (Margareta Johanna), komplimenteer haar daaroor en erken haar as 'n volwaardige vrou, waardeur hy haar vertroue wen en haar manipuleer om saam met hom te vlug. $\\checkmark$",
        "final_answer": "Geslaagdheid: Beklemtoon haar identiteitloosheid en kinderlike ondergeskiktheid; Manipulasie: Konstabel vra haar ware naam (Margareta Johanna) en komplimenteer haar skoonheid om haar vertroue te wen.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 17.5
    items.append({
        "item_id": f"{SOURCE_ID}-17.5",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "17.5",
        "marks": 3,
        "topic": "Drama: Mis (Reza de Wet) - Kontekstueel",
        "passage": PASSAGE_TEKS_K,
        "question": "Dink jy dié teks as deel van die eksposisie/uiteensetting van die drama is geslaagd? Motiveer jou antwoord deur na DRIE funksies van hierdie teks as deel van die eksposisie te verwys. (3)",
        "memo": "Ja, dit is geslaagd. $\\checkmark$\nDRIE funksies (enige drie vir 1 punt elk):\n* Dit beskryf die armoedige agtergrond en milieu waarin Miem en Meisie leef $\\checkmark$\n* Dit stel die tyd (31 Augustus), ruimte en die dreigende onheil van die nag vas $\\checkmark$\n* Dit stel die hoofkarakters (Miem en Meisie) en hul dinamiek/verhouding aan die leser bekend $\\checkmark$\n* Dit lig die misterie van Gabriël se teenwoordigheid op die solder uit $\\checkmark$\n\n*(Die kandidaat kan nie 'n NEE-antwoord aanbied nie.)*",
        "final_answer": "Ja; Drie funksies: Stel die somber milieu en tydperk vas, onthul die hoofkarakters en hul onderdrukkende verhouding, en skep die spanning van dreigende onheil in die nag.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 17.6
    items.append({
        "item_id": f"{SOURCE_ID}-17.6",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "17.6",
        "marks": 1,
        "topic": "Drama: Mis (Reza de Wet) - Kontekstueel",
        "passage": PASSAGE_TEKS_L,
        "question": "Wat probeer Miem met haar opmerking aan Konstabel in reël 1 bereik? (1)",
        "memo": "Miem probeer om die Konstabel se aandag op Meisie te vestig en hom onder die indruk van Meisie se skoonheid te bring (aangesien hy blind is) met die hoop om 'n huwelikskandidaat vir Meisie te vind. $\\checkmark$",
        "final_answer": "Sy probeer Konstabel se belangstelling in Meisie wek en hom beïndruk met haar skoonheid sodat hy as potensiële huweliksmaat kan dien.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 17.7
    items.append({
        "item_id": f"{SOURCE_ID}-17.7",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "17.7",
        "marks": 4,
        "topic": "Drama: Mis (Reza de Wet) - Kontekstueel",
        "passage": PASSAGE_TEKS_L,
        "question": "Verwys na reël 4: \"MEISIE werk aan haar sak.\"\n\nHoe skakel Meisie se handeling enersyds met die titel van die drama EN andersyds met hulle lewensomstandighede? Noem nog TWEE ander opsigte hoe die titel van die drama met die gebeure in die drama skakel. (4)",
        "memo": "* **Skakeling met titel:** Die sakke word met dieremis gevul om verkoop te word (die letterlike betekenis van \"mis\"). $\\checkmark$\n* **Skakeling met lewensomstandighede:** Hulle leef in uiterste armoede en moet die vuil, stink mis verpak om 'n karige inkomste te verdien. $\\checkmark$\n\nEN\n\n* TWEE ander skakelings met die titel (enige twee vir 1 punt elk):\n  - Die mistigheid en mistige weer buite om die huis $\\checkmark$\n  - Die misleiding van die vroue deur Konstabel / hulle misverstaan sy motiewe $\\checkmark$\n  - Meisie wat aan die einde vermis raak en een van die vermiste meisies word $\\checkmark$\n  - Miem wat haar dogter Meisie ná haar verdwyning gaan mis $\\checkmark$",
        "final_answer": "Titel: Sy stik sakke vir mis; Lewensomstandighede: Weerspieël hul armoedige, mislike bestaan; Twee ander skakelings: Die misverstand/misleiding deur Konstabel en Meisie wat aan die einde vermis raak (of die mistige weer buite).",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 17.8
    items.append({
        "item_id": f"{SOURCE_ID}-17.8",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "17.8",
        "marks": 3,
        "topic": "Drama: Mis (Reza de Wet) - Kontekstueel",
        "passage": PASSAGE_TEKS_L,
        "question": "Verwys na reëls 5 tot 15.\n\nWat is die dramatiese doel van die sak van die slopemmer in hierdie teks? Watter TWEE gevolge hou dié handeling vir die verloop van die drama in? (3)",
        "memo": "* **Dramatiese doel:** Dit plaas weer die fokus op Meisie se afstootlike, walglike take en haar gevangenskap onder Gabriël se teenwoordigheid / dit beklemtoon die mislike bestaan waaruit sy moet ontsnap. $\\checkmark$\n\nEN\n\n* TWEE gevolge (1 punt elk):\n  - Omdat Konstabel aanbied om te help, is hy en Meisie vir die eerste keer alleen buite in die donker $\\checkmark$\n  - Konstabel kan met haar 'n geheime afspraak maak en haar vra om haar aannemingsrok aan te trek en kaalvoet na hom te kom $\\checkmark$",
        "final_answer": "Dramatiese doel: Beklemtoon Meisie se vernederende gevangenskap en diensbaarheid aan haar pa; Twee gevolge: Dit bring Meisie en Konstabel alleen saam buite, waar hy 'n afspraak met haar kan reël om te ontsnap.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 17.9.1
    items.append({
        "item_id": f"{SOURCE_ID}-17.9.1",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "17.9.1",
        "marks": 2,
        "topic": "Drama: Mis (Reza de Wet) - Kontekstueel",
        "passage": PASSAGE_TEKS_L,
        "question": "Verwys na reël 21.\n\n17.9.1 Waarom is Meisie se woorde in hierdie reël ironies? Wat probeer sy aan Miem bewys? (2)",
        "memo": "* **Ironie:** 'n Mens sou verwag dat Meisie, wat gedurig skelm na die sirkus loer en na die musiek smag, bly sou wees om dit te hoor, MAAR nou sê sy dat hulle baie moet gesels sodat sy nie die musiek hoef te hoor nie. $\\checkmark$\n*(Die kandidaat moet beide kante van die ironie aandui.)*\n\nEN\n\n* **Wat sy probeer bewys:** Sy probeer aan haar ma voorgee dat sy 'n gehoorsame, vrome dogter is wat haar ma se waarskuwings teen die bose sirkus ter harte neem. $\\checkmark$",
        "final_answer": "Ironie: Sy hunker eintlik na die sirkusmusiek maar sê nou sy wil dit uitdoof; Wat sy bewys: Sy probeer haar ma oortuig dat sy gehoorsaam is en nie deur die sirkus versoek word nie.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 17.9.2
    items.append({
        "item_id": f"{SOURCE_ID}-17.9.2",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "17.9.2",
        "marks": 2,
        "topic": "Drama: Mis (Reza de Wet) - Kontekstueel",
        "passage": PASSAGE_TEKS_L,
        "question": "Verwys na reël 21.\n\n17.9.2 Konstabel speel 'n drieledige rol as Meisie se bewonderaar, vertroueling en verleier in die drama. Kies enige EEN van die rolle wat hy vertolk EN motiveer jou antwoord deur na 'n handeling van Konstabel in die drama te verwys. (2)",
        "memo": "Kies enige EEN rol (1 punt) EN gee motivering (1 punt):\n* **Bewonderaar:** Konstabel komplimenteer haar oor haar skoonheid, haar hare en haar regte name (Margareta Johanna). $\\checkmark\\checkmark$\n* **Vertroueling:** Konstabel sê vir haar dat hy ook van die sirkus hou en belowe om nie haar geheime vir haar ma te vertel nie. $\\checkmark\\checkmark$\n* **Verleier:** Konstabel moedig haar aan om haar aannemingsrok aan te trek, buite in die donker te dans en haar ma se reëls te verbreek. $\\checkmark\\checkmark$",
        "final_answer": "Rol: Verleier (of bewonderaar / vertroueling); Motivering: Hy oorreed haar om haar aannemingsrok kaalvoet aan te trek en skelm saam met hom in die mis in te verdwyn.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 17.10
    items.append({
        "item_id": f"{SOURCE_ID}-17.10",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "17.10",
        "marks": 3,
        "topic": "Drama: Mis (Reza de Wet) - Kontekstueel",
        "passage": PASSAGE_TEKS_K + "\n\n" + PASSAGE_TEKS_L,
        "question": "Herlees die volgende reëls:\n\nTEKS K (reëls 25 tot 28): \"(Baie vriendelik) Miskien koop ek vir jou 'n nuwe rok.\"\nTEKS L (reël 16): \"Gaan maak dit tog leeg, my kind. En spoel dit goed uit.\"\n\nVerduidelik waarom Miem in TEKS K vriendelik met Meisie praat. Watter woord in TEKS L versag die bevel aan Meisie? Waarom is die versagting van hierdie bevel nie kenmerkend van Miem nie? (3)",
        "memo": "* **Vriendelikheid in TEKS K:** Miem besef dat hulle baie sakke mis verkoop het en 'n goeie inkomste verdien; sy wil Meisie vlei en tevrede hou sodat sy sal aanhou werk. $\\checkmark$\n* **Woord in TEKS L:** \"tog\" $\\checkmark$\n* **Nie kenmerkend nie:** Miem se gewone gesprekstoon teenoor Meisie is kortaf, dominerend, bevelend en krities (\"Sit regop!\"). $\\checkmark$",
        "final_answer": "Rede in Teks K: Miem is in 'n goeie bui oor goeie misverkope en vlei Meisie om haar hard aan die werk te hou; Woord in Teks L: 'tog'; Nie kenmerkend nie: Miem is gewoonlik kortaf, gebiedend en kras sonder enige hoflikheid.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    return items

if __name__ == "__main__":
    items = get_drama_items()
    print(f"Generated {len(items)} drama items.")
    print("Total marks:", sum(x["marks"] for x in items))
