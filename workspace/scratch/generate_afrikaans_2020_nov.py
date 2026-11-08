# -*- coding: utf-8 -*-
"""
Script to generate the standardized JSONL items for:
- Source ID: dbe-afrikaans_fal-g12-p1-2020-nov
- Paired Memo ID: dbe-afrikaans_fal-g12-p1-2020-nov-memo
- Subject: afrikaans_fal
- Grade: 12
- Marks: 80
"""

import json
import os
import re

SOURCE_ID = "dbe-afrikaans_fal-g12-p1-2020-nov"
MEMO_ID = "dbe-afrikaans_fal-g12-p1-2020-nov-memo"
SUBJECT = "afrikaans_fal"
GRADE = 12
LANGUAGE = "af"
TRACK = "languages_fal"

# Passages
PASSAGE_TEKS_A = """**TEKS A: TYDSKRIFARTIKEL**

### KYLIAN MBAPPÉ
**Die sokkerspeler met die goue voet én 'n goue hart!**

1. Kylian Mbappé is nie net die duurste tienersokkerspeler ter wêreld nie; hy is ook by FIFA se 2018 Wêreldbeker-sokkertoernooi in Rusland as die Jong Speler van die Toernooi aangewys.

2. Kylian het in 'n sportmal gesin in Bondy, 'n voorstad van Parys, Frankryk, grootgeword. Sy pa was 'n sokkerafrigter by AS Bondy waar Kylian se sokkerloopbaan begin het. Sy ma was 'n handbalspeler.

3. Sokker was van kleintyd af Kylian Mbappé se passie. Hy onthou dat hy as kind miniatuurdoelhokke in die huis opgestel het. Hy het ook sy kop kaal laat skeer, soos die speler, Zinedine Zinedane, s'n. Sy kamermure was vol foto's van sy held, Cristiano Ronaldo, en hy het daarvan gehou om FIFA se videospeletjie te speel.

4. Die sokkerwêreld het voor 2018 al van Kylian se bestaan geweet. Dit was voor sy sewentiende verjaardag in 2015 toe hy sy debuut in Monaco se eerste span gemaak het. Nadat hy sy eerste doel aangeteken het, het hy Thierry Henry se plek as die klub se jongste doelskieter ingeneem. In die twee seisoene daarna het hy nog 40 doele aangeteken. Dit het Paris Saint-Germaine (PSG) se aandag getrek en hulle wou Kylian hê.

5. Dié skatryk Franse klub het vir Monaco groot geld vir die doelskopper, wat toe 18 was, aangebied. Die hele proses om Kylian van Monaco na PSG oorgeplaas te kry, het amper R2,8 miljard gekos. Dit maak Kylian die duurste tienersokkerspeler ter wêreld. Dit het ook beteken dat Kylian weer na sy geboorteland kon teruggaan.

6. In 2018 het Kylian as 'n jong speler na die Wêreldbeker-sokkertoernooi in Rusland gegaan. Hy was opgewonde om teen die bestes in die sokkerwêreld te speel. Baie mense het gesê dat die bloedjong Kylian Mbappé 'n speler was om dop te hou en hulle was in die kol! Hy het vier doele in die toernooi aangeteken: een teen Peru, twee teen Argentinië en die laaste doel in die finale wedstryd. Dit is hoekom FIFA hom as die Jong Speler van die Toernooi aangewys het.

7. Toe Kylian die bal tydens die eindstryd verby die Kroasiese doelwagter tot agter in die net skop, het hy maar die tweede tiener in sokkergeskiedenis geword wat 'n doel in 'n Wêreldbekereindstryd aanteken. Só het hy Frankryk gehelp om Kroasië met 4–2 te wen en het hy Rusland as 'n súperster verlaat!

8. "Welkom in die klub," het Brasilië se Pelé ná Frankryk se oorwinning getwiet. Pelé was ook maar net 18 toe hy twee keer in 1958 se Wêreldbekereindstryd 'n doel aangeteken het. "Dis lekker om geselskap te hê. As Kylian so aanhou om my rekords te ewenaar, sal ek my stewels moet afstof …," het Pelé verder getwiet.

9. Dié jong Franse speler word nou die tiener-met-die-wêreld-aan-sy-voete genoem. Hy word reeds met die legende van Argentinië, Lionel Messi (31), en die Portugese ster, Cristiano Ronaldo (33), vergelyk. 'n Mens kan amper nie dink dat 'n 19-jarige dit kon regkry nie.

10. Om op só 'n jong ouderdom reeds soveel sukses te behaal, hou nie nét voordele in nie. Byvoorbeeld, Kylian is nog aan die begin van sy loopbaan, maar hy het reeds die top bereik. Hy kan ook nêrens meer gaan nie, of die mense hardloop na hom toe. Derdens was Kylian ook nog so besig om 'n wêreldsuperster te word, dat hy nie eens tyd gehad het om 'n rybewys te kry nie. Sy familie moet hom steeds vat waar hy wil wees.

11. Vir die wêreld is hy die volgende Lionel, Cristiano, Thierry of selfs Zinedine. Vir die kinders van Bondy is hy iets veel meer. Die buurt was bekend vir sy geweld en dwelmmisbruik, maar Kylian het gehelp om hierdie beeld te verander. Vir die kinders van Bondy is Kylian die lewende bewys dat enige iets moontlik is as jy hard genoeg oefen.

12. Kylian sal nie net vir sy sokkerprestasies onthou word nie, maar ook vir sy vrygewige hart. Hy het al die geld wat hy tydens die Wêreldbekertoernooi gekry het (baie meer as R4 miljoen), vir 'n organisasie wat siek en gestremde kinders gratis afrig, gegee.

13. Kylian Mbappé verdien dit om die tiener met die goue voet én 'n goue hart genoem te word.

[Bron: World Soccer Images; Verwerk uit Huisgenoot, 26 Julie 2018]

[DIAGRAM: 'n Swart-en-wit foto van Kylian Mbappé wat glimlaggend 'n trofeevormige beker (die FIFA Wêreldbeker 'Jong Speler van die Toernooi'-toekenning) vashou. Hy dra die amptelike Franse nasionale sokkertrui met die FFF-haanwapen.]"""

PASSAGE_TEKS_B = """**TEKS B: SPOTPRENT**

[DIAGRAM: 'n Spotprent wat afspeel in die registrasiekantoor van 'n universiteit.
* **Agtergrond & Bordjies:** 'n Bord bo teen die muur lui "UNIVERSITEIT". Links bo by die ingangdeur is 'n bordjie: "HOOFGEBOU - Doen hier aansoek om te registreer!".
* **Links (die tou studente):** 'n Lang, diggepakte ry jong studente staan en wag by die ingangsportaal. Hulle lyk sigbaar uitgeput en verveeld: sommige leun moeg teen die muur, party se oë is toe, ander dra oorfone of kyk moedeloos met lêers en dokumente onder die arm.
* **Middel (jongman by tafel):** 'n Jong man met 'n pet agterstevoor en 'n rugsak sit voor die administratiewe toonbank met aansoekvorms in die hand. Hy sê in 'n spraakborrel: "Sjoe, ek het nog nooit in so 'n lang tou gewag nie ..."
* **Regs (amptenare agter die tafel):**
  - 'n Ouer beampte/man met 'n bril en geruite hemp sit agter 'n lessenaar vol papierwerk en liasseerders. Hy kyk na die jongman en sê in 'n spraakborrel: "Boet, wag vir die dag dat jy vir werk aansoek doen."
  - Agter hom is twee vroulike kantoorwerkers besig met administrasie: een staan en liasseer dokumente in 'n liasseerkabinet, terwyl die ander een oor die lessenaar buk en na dokumente kyk. Albei is stil en fokus net op hul papierwerk.]

[Verwerk uit Die Burger, 10 Januarie 2018]"""

PASSAGE_TEKS_C = """**TEKS C: PRAATJIE / ARTIKEL**

### HALLO, THOBELA, SAWUBONA

Dit is goed om meer as een taal te kan praat, maar daar is dinge waaraan jy moet dink as jy 'n nuwe taal wil aanleer.

'n Nuwe taal kan op enige ouderdom aangeleer word. Kinders leer wel tale maklik aan, maar dit beteken nie dat jý te oud is om dit ook te kan doen nie.

Wil jy net iemand in sy eie taal kan groet of wil jy ernstig met jou buurvrou kan gesels? Voor jy enige taalkursus kies, moet jy besluit wat jy met die taal wil doen.

As jy die nuwe taal wil aanleer, moet jy dit eers leer praat voordat jy dit probeer skryf of lees. Onthou jy nie dis hoe jy kleintyd jou moedertaal leer praat het nie?

Wonder jy of jy slim genoeg is? Die aanleer van 'n taal het niks met slimwees te make nie. As jy genoeg tyd aan die nuwe taal bestee, sal jy dit bemeester. Verder is dit ook belangrik om, terwyl jy die taal aanleer, elke kans te gebruik om die taal te praat. Dit sal jou help om met selfvertroue te praat.

Luister na liedjies in die taal wat jy aanleer en probeer saamsing en die woorde onthou. Dit maak nie saak dat jy vals sing of die wysie verloor nie. Dis die woorde wat tel!

Nadat jy jou kursus voltooi het, moet jy aanhou om die nuwe taal te praat. As jy dit nie doen nie, gaan jy die nuwe taal gou weer vergeet.

[Verwerk uit SARIE, Oktober 2018]"""

PASSAGE_TEKS_D = """**TEKS D: ADVERTENSIE**

Die advertensie is in 'n netjiese advertensieraam met verskeie teksblokke en beelde uiteengesit:

* **Boonste teksblok (in 'n eie omlynde boks):**
  **Kom na Thandeka vir**
  **(3.1) (tradisioneel) drag ...**

* **Subopskrif:**
  **(3.2) G-r-o-o-t winskope eerskomende Saterdag!**

* **Beelde (bo en middel):**
  - 'n Foto van 'n glimlaggende vrou wat tradisionele patroonstowwe en klere vashou.
  - Twee portretfoto's: links 'n modieuse dame in 'n patroonbaadjie, en regs 'n glimlaggende man in 'n stylvolle baadjie.
  - Teks langsaan: **Mans en dames is welkom!**

* **Dienswaarborge (in 'n omlynde blok links):**
  **Thandeka waarborg stergehalte diens:**
  * Sy maak presies wat jy wil hê!
  * Die klere is netjies en (3.3) (goedkoop).
  * (3.4) Daar is 'n verskeidenheid material.
  * Daar is baie patrone (3.5) (uit wat/waaruit) jy kan kies.
  * Jy kan kies en keur tussen al die bykomstighede vir oud en jonk.
  * Die winkel is skoon en netjies.
  * (3.6) (Besigheid+ure): 07:30–20:00

* **Staalmonsters en bykomstighede (regs van die waarborge):**
  - Voorbeelde van verskillende lapstowwe en patrone (kolletjies, blompatrone, sirkels).
  - 'n Foto van tradisionele kralewerk/kralestel op 'n swart paspop.

* **Onderste slagspreuke:**
  **(3.8) Thandeka is wyd en syd bekend.**
  **(3.9) Jy kom maak 'n draai by haar.**

[Eie teks]"""

PASSAGE_TEKS_E = """**TEKS E: STROKIESPRENT**

'n Strokiesprent in vier opeenvolgende raampies met Neelsie en sy onderwyser (Meneer):

* **RAAMPIE 1:**
  - **Visueel:** Meneer (met bles kop, grys syhare, welige snor, bril en 'n das) praat streng en geïrriteerd met Neelsie. Neelsie (met stekelrige blonde hare) sit met 'n ongeërgde, verveelde gesigsuitdrukking.
  - **Meneer:** "(4.1) Neelsie, jy kom áltyd laat vir my rekenaarklas."
  - **Neelsie:** "(4.2) Sorry, Meneer."

* **RAAMPIE 2:**
  - **Visueel:** Meneer frons kwaai met plooie op sy voorkop, sy oë rek groot, en hy wys 'n beskuldigende vinger na Neelsie. Neelsie kyk steeds heeltemal ongeërg en verveeld na Meneer.
  - **Meneer:** "Jy speel áltyd (4.3) games in plaas daarvan om jou werk te doen!"
  - **Neelsie:** "Sorry, Meneer."

* **RAAMPIE 3:**
  - **Visueel:** Meneer hou aan om met 'n ernstige, kwaai gesig na Neelsie te wys. Neelsie se gesigsuitdrukking bly presies dieselfde (verveeld en onaangeraak).
  - **Meneer:** "(4.5) Jy kopieer áltyd die ander leerders se werk!"
  - **Neelsie:** "Sorry, Meneer."

* **RAAMPIE 4:**
  - **Visueel:** Meneer kyk moedeloos en streng. Neelsie rus sy ken gemaklik op sy hand en kyk nonchalant na Meneer.
  - **Meneer:** "En al wat jy doen, is om te sê: ''Sorry''!"
  - **Neelsie:** "Sorry, Meneer."

[Verwerk uit Meester.yolasite.com]"""

PASSAGE_TEKS_F = """**TEKS F: ARTIKEL**

### MANDELA-KOEK HELP KANKERLYERS

Altesaam 1 200 eiers en 625 (5.1.1) (kilogram) droë bestanddele is gebruik om die wêreld se grootste Nelson Mandela-koek te skep.

Dié koek het meer (5.1.2) (dan/as) 750 kilogram geweeg. Ses bakkers het vyf dae gewerk om die koek vir Cupcakes of Hope te (5.1.3) (bak). Die (5.1.4) (voltooi) koek is in die Sandton City-winkelsentrum uitgestal.

(5.1.5) Cupcakes of Hope doen elke jaar iets vir kinders met kanker. Hierdie koek is gebak om Mandela se geboortedag 'n (5.1.6) (honderd jaar) gelede te vier.

Sandy sê sulke (5.1.7) (geleentheid) is spesiaal. Mandela se kleinkinders was ook daar. Dit het die dag nog meer spesiaal gemaak. Mandela het gesê dat dit in mense se hande is om 'n verskil in (5.1.8) (…) eie gemeenskap te maak.

Die mense van Cupcakes of Hope doen die (5.1.9) (goed) wat hulle kan om 'n verskil in die gemeenskap te maak. Hulle wil 'n (5.1.10) (inspireer) vir meer mense wees om Cupcake-engele te word. Dit maak 'n mens baie (5.1.11) (ongelukkig).

'n Kankerlyertjie se ma was daar (5.1.12) (die organisasie vir hulle werk bedank).

(5.1.13) Cupcakes of Hope het gelede jaar 'n wêreldrekord vir die hoogste kolwyntjietoring opgestel. Dit was nie 'n klein (5.1.14) (toring) nie. Dit het 10,7 m hoog gestaan.

[Verwerk uit Beeld, 28 Julie 2018]"""

PASSAGE_TEKS_G = """**TEKS G: PRENT**

[DIAGRAM: 'n Prent met verskeie spotprentagtige figure en simbole, elk met 'n etiket wat na 'n vraag verwys:
* **5.2.1:** 'n Man in 'n hemp en das wat tussen twee oop deure staan gereed om te sluit (die winkelbestuurder wat wag vir klante om uit te gaan).
* **5.2.2:** 'n Aardbol / wêreldbol op 'n staander (waarmee 'n mens kyk waar lande in die wêreld lê). Langsaan is 'n man met 'n koptelefoon/oorfone en das.
* **5.2.3:** 'n Kok/sjef met 'n wit sjefshoed, voorskoot en wit koksuniform wat met oop hande glimlag. Bokant hom is 'n gedagteborrel.
* **Middel:** 'n Stapel muntstukke met 'n klawer/blommetjie, en 'n swart gradeplegtigheidshoed (mortarboard) met 'n opgerolde graadsertifikaat.
* **5.2.4:** 'n Verpleegster in 'n mediese uniform en verpleegsterskappie wat 'n leë bordjie/klembord vashou.
* **5.2.5:** 'n Vroulike figuur wat 'n toegedraaide geskenk met 'n strik aanbied ("Meneer, hier is u geskenk.").
* **Regs:** 'n Breed glimlaggende man in 'n formele hemp en das.]

[Bron: Google images]"""

items = [
    # ----------------------------------------------------
    # AFDELING A: LEESBEGRIP (30 punte)
    # TEKS A: TYDSKRIFARTIKEL (24 punte)
    # ----------------------------------------------------
    {
        "item_id": f"{SOURCE_ID}-1.1",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "language": LANGUAGE,
        "track": TRACK,
        "kind": "passage_questions",
        "question_ref": "1.1",
        "marks": 1,
        "topic": "Leesbegrip: Feitlike inligting",
        "passage": PASSAGE_TEKS_A,
        "question": "Waar is die 2018 Wêreldbeker-sokkertoernooi gehou?",
        "memo": "* $\\checkmark$ (In) Rusland",
        "final_answer": "(In) Rusland",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{SOURCE_ID}-1.2",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "language": LANGUAGE,
        "track": TRACK,
        "kind": "passage_questions",
        "question_ref": "1.2",
        "marks": 2,
        "topic": "Leesbegrip: Feite herroep",
        "passage": PASSAGE_TEKS_A,
        "question": "Waarom word Kylian se gesin \"sportmal\" genoem? Gee TWEE feite uit die leesstuk.",
        "memo": "* $\\checkmark$ Sy pa was (AS Bondy) se sokkerafrigter.\n* $\\checkmark$ Sy ma het handbal gespeel.\n**OF**\n* $\\checkmark$ Die hele gesin beoefen een of ander sportsoort.",
        "final_answer": "Sy pa was 'n sokkerafrigter (by AS Bondy) en sy ma was 'n handbalspeler.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{SOURCE_ID}-1.3",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "language": LANGUAGE,
        "track": TRACK,
        "kind": "passage_questions",
        "question_ref": "1.3",
        "marks": 2,
        "topic": "Leesbegrip: Feite herroep",
        "passage": PASSAGE_TEKS_A,
        "question": "Wie was Kylian se TWEE groot sokkerhelde uit sy kinderdae?",
        "memo": "* $\\checkmark$ Zinedine Zinedane / Zinedine / Zinedane\n* $\\checkmark$ Cristiano Ronaldo / Cristiano / Ronaldo",
        "final_answer": "Zinedine Zinedane en Cristiano Ronaldo.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{SOURCE_ID}-1.4",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "language": LANGUAGE,
        "track": TRACK,
        "kind": "passage_questions",
        "question_ref": "1.4",
        "marks": 1,
        "topic": "Leesbegrip: Oorsaak en gevolg",
        "passage": PASSAGE_TEKS_A,
        "question": "Waarom onthou mense Kylian se debuut in Monaco se eerste span?",
        "memo": "* $\\checkmark$ Hy was die jongste doelskieter. / Hy was maar net 16/nog nie 17 nie, toe hy Thierry Henry se plek as jongste doelskieter ingeneem het. *(Enige EEN of soortgelyk; jonk en prestasie moet gekombineer word)*",
        "final_answer": "Hy het Thierry Henry se plek as die klub se jongste doelskieter ingeneem toe hy nog nie 17 was nie.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{SOURCE_ID}-1.5",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "language": LANGUAGE,
        "track": TRACK,
        "kind": "passage_questions",
        "question_ref": "1.5",
        "marks": 1,
        "topic": "Leesbegrip: Afleiding uit teks",
        "passage": PASSAGE_TEKS_A,
        "question": "Hoe weet ons dat Monaco Kylian nie maklik laat gaan het nie?",
        "memo": "* $\\checkmark$ PSG moes Monaco (baie / R2,8 miljard) betaal (om hom te laat gaan). / Monaco/Hulle het baie geld gevra om Kylian te laat gaan. *(Enige EEN of soortgelyk aan bogenoemde)*",
        "final_answer": "Die proses om hom na PSG oorgeplaas te kry het amper R2,8 miljard gekos (Monaco het groot geld vir hom gevra).",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{SOURCE_ID}-1.6.1",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "language": LANGUAGE,
        "track": TRACK,
        "kind": "passage_questions",
        "question_ref": "1.6.1",
        "marks": 1,
        "topic": "Leesbegrip: Aanhaling uit teks",
        "passage": PASSAGE_TEKS_A,
        "question": "\"In 2018 het Kylian as 'n jong speler na die Wêreldbeker-sokkertoernooi in Rusland gegaan.\" (Paragraaf 6)\n\nBaie mense het gedink dat Kylian goed sou speel. Skryf DRIE OPEENVOLGENDE woorde uit die teks neer wat vir ons sê dat hierdie mense nie verkeerd was om so te dink nie.",
        "memo": "* $\\checkmark$ \"... in die kol!\" / in die kol *(Kandidaat word nie gepenaliseer as die woorde nie tussen aanhalingstekens is nie.)*",
        "final_answer": "\"in die kol!\"",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{SOURCE_ID}-1.6.2",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "language": LANGUAGE,
        "track": TRACK,
        "kind": "passage_questions",
        "question_ref": "1.6.2",
        "marks": 1,
        "topic": "Leesbegrip: Feitlike inligting",
        "passage": PASSAGE_TEKS_A,
        "question": "Hoeveel doele het Kylian in 2018 in Rusland aangeteken?",
        "memo": "* $\\checkmark$ 4 (doele) / Vier/vier (doele)",
        "final_answer": "4 (vier) doele",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{SOURCE_ID}-1.7.1",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "language": LANGUAGE,
        "track": TRACK,
        "kind": "passage_questions",
        "question_ref": "1.7.1",
        "marks": 1,
        "topic": "Leesbegrip: Feitlike inligting",
        "passage": PASSAGE_TEKS_A,
        "question": "Kylian word reeds met Argentinië se Lionel Messi en Portugal se Cristiano Ronaldo vergelyk. (Paragraaf 9)\n\nVir watter land het Kylian in FIFA se 2018 Wêreldbeker-sokkertoernooi gespeel?",
        "memo": "* $\\checkmark$ (Vir) Frankryk",
        "final_answer": "Frankryk",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{SOURCE_ID}-1.7.2",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "language": LANGUAGE,
        "track": TRACK,
        "kind": "passage_questions",
        "question_ref": "1.7.2",
        "marks": 1,
        "topic": "Leesbegrip: Vergelyking en konteks",
        "passage": PASSAGE_TEKS_A,
        "question": "Waarom is dit moeilik om te glo dat hy met Messi en Ronaldo vergelyk word?",
        "memo": "* $\\checkmark$ Kylian is nog baie jonk/net 19 jaar oud/nog aan die begin van sy loopbaan. / Kylian is baie jonger as Messi en Ronaldo. / Messi en Ronaldo is baie ouer as hy/het meer ervaring. / Messi en Ronaldo was sy helde uit sy kinderdae; nou word hy met hulle vergelyk. *(Enige EEN of soortgelyk aan bogenoemde)*",
        "final_answer": "Kylian is nog baie jonk (net 19 jaar oud en aan die begin van sy loopbaan), terwyl Messi en Ronaldo baie ouer ervare sokkerlegendes is.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{SOURCE_ID}-1.7.3",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "language": LANGUAGE,
        "track": TRACK,
        "kind": "passage_questions",
        "question_ref": "1.7.3",
        "marks": 1,
        "topic": "Leesbegrip: Prestasies vergelyk",
        "passage": PASSAGE_TEKS_A,
        "question": "Watter prestasie het Kylian behaal wat Messi en Ronaldo nie kon regkry nie?",
        "memo": "* $\\checkmark$ Kylian het as tiener 'n doel in 'n Wêreldbekereindstryd aangeteken. / Messi en Ronaldo het nie as tieners enige doele in 'n Wêreldbekereindstryd aangeteken nie. *(Enige EEN of soortgelyk aan bogenoemde)*",
        "final_answer": "Kylian het as tiener 'n doel in 'n Wêreldbekereindstryd aangeteken.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{SOURCE_ID}-1.8",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "language": LANGUAGE,
        "track": TRACK,
        "kind": "multiple_choice",
        "question_ref": "1.8",
        "marks": 1,
        "topic": "Leesbegrip: Figuurlike betekenis",
        "passage": PASSAGE_TEKS_A,
        "question": "Lees weer paragraaf 8.\n\nKies die KORREKTE antwoord uit dié tussen hakies:\n\nAs Pelé sê: \"Welkom in die klub\" (erken hy Kylian se prestasies/probeer hy Kylian na 'n ander sokkerklub lok).",
        "memo": "* $\\checkmark$ erken hy Kylian se prestasies",
        "final_answer": "erken hy Kylian se prestasies",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{SOURCE_ID}-1.9",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "language": LANGUAGE,
        "track": TRACK,
        "kind": "passage_questions",
        "question_ref": "1.9",
        "marks": 1,
        "topic": "Leesbegrip: Motivering van onwaarheid",
        "passage": PASSAGE_TEKS_A,
        "question": "Dit is moontlik dat Pelé in die toekoms saam met Kylian in 'n Wêreldbekertoernooi sal kan speel.\n\nMotiveer waarom hierdie stelling ONWAAR is.",
        "memo": "* $\\checkmark$ Pelé is (al) te oud om weer sokker te speel / hy het opgehou om sokker te speel. *(Of soortgelyk aan bogenoemde)*",
        "final_answer": "Pelé het al in 1958 gespeel en is reeds te oud om weer sokker te speel / hy het lankal opgehou speel.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{SOURCE_ID}-1.10",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "language": LANGUAGE,
        "track": TRACK,
        "kind": "passage_questions",
        "question_ref": "1.10",
        "marks": 2,
        "topic": "Leesbegrip: Identifisering van nadele",
        "passage": PASSAGE_TEKS_A,
        "question": "Kylian is reeds as 'n tiener 'n superster. Noem TWEE nadele wat dit vir hom inhou.",
        "memo": "* $\\checkmark$ Hy het nie meer privaatheid gehad nie. / Oral het mense op hom afgestorm.\n* $\\checkmark$ Hy het min oorgehad om na te strewe. / Hy het vroeg reeds die toppunt in sy sportloopbaan bereik. / Hy het min vrye tyd gehad / daar was nie tyd om sy bestuurslisensie te kry nie / sy ouers/familie moes hom nog rondry.\n*(Enige TWEE of soortgelyk aan bogenoemde)*",
        "final_answer": "1. Hy het geen privaatheid nie omdat mense oral na hom toe hardloop.\n2. Hy het nie eens tyd gehad om 'n rybewys te kry nie en sy familie moet hom steeds rondry.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{SOURCE_ID}-1.11",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "language": LANGUAGE,
        "track": TRACK,
        "kind": "passage_questions",
        "question_ref": "1.11",
        "marks": 1,
        "topic": "Leesbegrip: Feit teenoor mening",
        "passage": PASSAGE_TEKS_A,
        "question": "\"Vir die wêreld is hy die volgende Lionel, Cristiano, Thierry of selfs Zinedine.\" (Paragraaf 11)\n\nWaarom is dit 'n MENING en nie 'n feit nie?",
        "memo": "* $\\checkmark$ Kylian moet dit wat oor hom gesê word, nog eers bewys. / Daar kan nog baie dinge gebeur wat kan verhoed dat hy dieselfde as die genoemde spelers gereken kan word. / Op hierdie stadium is hy nog net die Jong Speler van die 2018 toernooi. / Dis net wat die skrywer/publiek voorspel/dink/voel. / Dit is nie op feite/bewyse gebaseer nie. *(Enige EEN of soortgelyk aan bogenoemde)*",
        "final_answer": "Dit is 'n mening omdat dit slegs is wat mense voorspel of dink; sy toekomstige sukses is nog nie 'n bewese feit nie.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{SOURCE_ID}-1.12",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "language": LANGUAGE,
        "track": TRACK,
        "kind": "passage_questions",
        "question_ref": "1.12",
        "marks": 1,
        "topic": "Leesbegrip: Sosiale kwessies",
        "passage": PASSAGE_TEKS_A,
        "question": "Noem EEN sosiale probleem wat die kinders van Bondy in Frankryk beleef.",
        "memo": "* $\\checkmark$ geweld / dwelmmisbruik / dwelms *(Enige EEN)*",
        "final_answer": "Geweld (of dwelmmisbruik).",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{SOURCE_ID}-1.13",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "language": LANGUAGE,
        "track": TRACK,
        "kind": "passage_questions",
        "question_ref": "1.13",
        "marks": 1,
        "topic": "Leesbegrip: Lewensles",
        "passage": PASSAGE_TEKS_A,
        "question": "Wat kan die kinders van Bondy uit Kylian se sukses leer?",
        "memo": "* $\\checkmark$ Jy moet hard werk/oefen om bo uit te kom / enige iets is moontlik as jy hard genoeg oefen. / Geweld en dwelms is nie die enigste uitweg nie. / Jy kan jonk al suksesvol wees. / Sportdeelname is beter as om dwelms te neem. *(Enige EEN of soortgelyk aan bogenoemde)*",
        "final_answer": "Enige iets is moontlik as jy hard genoeg oefen.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{SOURCE_ID}-1.14",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "language": LANGUAGE,
        "track": TRACK,
        "kind": "passage_questions",
        "question_ref": "1.14",
        "marks": 1,
        "topic": "Leesbegrip: Karaktereienskappe en beeldspraak",
        "passage": PASSAGE_TEKS_A,
        "question": "Waarom is dit gepas dat mense sê dat Kylian 'n ''goue hart'' het?",
        "memo": "* $\\checkmark$ Hy het al sy prysgeld (van die toernooi / baie meer as R4 miljoen) weggegee/vir liefdadigheid geskenk / vir 'n organisasie gegee wat siek en gestremde kinders gratis afrig. / Hy het bewys dat hy vir ander mense omgee / hy is baie vrygewig. *(Enige EEN of soortgelyk aan bogenoemde)*",
        "final_answer": "Hy het al sy prysgeld uit die Wêreldbekertoernooi (meer as R4 miljoen) vir 'n organisasie geskenk wat siek en gestremde kinders gratis afrig.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{SOURCE_ID}-1.15",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "language": LANGUAGE,
        "track": TRACK,
        "kind": "passage_questions",
        "question_ref": "1.15",
        "marks": 1,
        "topic": "Leesbegrip: Funksie van visuele teks",
        "passage": PASSAGE_TEKS_A,
        "question": "Waarom is daar 'n foto by die artikel?",
        "memo": "* $\\checkmark$ Iemand wat nie van Kylian Mbappé weet nie/nie weet hoe hy lyk nie, kan nou op die foto sien hoe hy lyk. / Die foto pas by die inhoud wat oor Kylian handel. / Die foto bevestig/ondersteun/bewys dit wat ons in die teks lees. / Die foto pas by die hoofopskrif. / Dit maak die mense nuuskierig om die artikel te lees. *(Enige EEN of soortgelyk aan bogenoemde)*",
        "final_answer": "Om vir die leser te wys hoe Kylian Mbappé lyk (en sy trofee uit te beeld).",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{SOURCE_ID}-1.16",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "language": LANGUAGE,
        "track": TRACK,
        "kind": "passage_questions",
        "question_ref": "1.16",
        "marks": 2,
        "topic": "Leesbegrip: Samevatting van prestasies",
        "passage": PASSAGE_TEKS_A,
        "question": "Gee TWEE redes waarom Kylian ná die 2018 Wêreldbekertoernooi onthou sal word.",
        "memo": "* $\\checkmark$ Hy is tydens die 2018 Wêreldbekertoernooi as die Jong Speler van die Toernooi aangewys / hy het vier doele in die toernooi aangeteken / hy het die tweede tiener geword om 'n doel in 'n eindstryd aan te teken.\n* $\\checkmark$ Hy het al sy toernooigeld weggegee / 'n verskil in sommige mense se lewens gemaak / hy was die jongman met die goue voet én die goue hart.\n*(Enige TWEE of soortgelyk aan bogenoemde)*",
        "final_answer": "1. Hy is aangewys as die Jong Speler van die Toernooi nadat hy vier doele aangeteken het (insluitend in die eindstryd).\n2. Hy het al sy toernooigeld aan liefdadigheid geskenk vir siek en gestremde kinders.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{SOURCE_ID}-1.17",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "language": LANGUAGE,
        "track": TRACK,
        "kind": "passage_questions",
        "question_ref": "1.17",
        "marks": 1,
        "topic": "Leesbegrip: Eie evaluering en mening",
        "passage": PASSAGE_TEKS_A,
        "question": "Na jy hierdie artikel gelees het, hoe voel jy oor sokkerspelers?",
        "memo": "* $\\checkmark$ Ek voel positief: Ek het iets goeds omtrent sokkerspelers geleer / dit het my laat besef dat sokkerspelers ook goeie dinge vir ander mense/gemeenskappe doen.\n**OF**\n* $\\checkmark$ Ek voel negatief: Daar word so baie geld aan sokker bestee terwyl daar mense is wat honger ly.\n**OF**\n* $\\checkmark$ Dit maak geen verskil nie, want ek hou nie van sokker nie/stel nie daarin belang nie.\n*(Enige EEN gemotiveerde antwoord of soortgelyk aan bogenoemde)*",
        "final_answer": "Positief, omdat die artikel wys dat sokkerspelers ook vrygewig kan wees en hul geld kan gebruik om ander mense te help.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },

    # ----------------------------------------------------
    # TEKS B: SPOTPRENT (6 punte)
    # ----------------------------------------------------
    {
        "item_id": f"{SOURCE_ID}-1.18",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "language": LANGUAGE,
        "track": TRACK,
        "kind": "passage_questions",
        "question_ref": "1.18",
        "marks": 1,
        "topic": "Spotprent: Begrip van situasie",
        "passage": PASSAGE_TEKS_B,
        "question": "Waarvoor staan die mense in die tou en wag?",
        "memo": "* $\\checkmark$ Hulle wil aansoek doen om te registreer/inskryf (by die universiteit). *(Enige EEN of soortgelyk aan bogenoemde)*",
        "final_answer": "Hulle staan in die tou om by die universiteit aansoek te doen om te registreer.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{SOURCE_ID}-1.19",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "language": LANGUAGE,
        "track": TRACK,
        "kind": "passage_questions",
        "question_ref": "1.19",
        "marks": 1,
        "topic": "Spotprent: Visuele analise",
        "passage": PASSAGE_TEKS_B,
        "question": "Hoe beeld die spotprenttekenaar visueel uit dat die studente al baie lank in die tou staan?",
        "memo": "* $\\checkmark$ Die studente lyk moeg / hulle oë is toe / die studente lyk verveeld / die studente lê/leun teen die muur / die spotprenttekenaar maak van verskillende moë gesigsuitdrukkings en liggaamshoudings gebruik / die tou is baie lank. *(Enige EEN of soortgelyk aan bogenoemde)*",
        "final_answer": "Die studente leun moeg teen die muur, party se oë is toe en hulle lyk baie verveeld en uitgeput.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{SOURCE_ID}-1.20",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "language": LANGUAGE,
        "track": TRACK,
        "kind": "multiple_choice",
        "question_ref": "1.20",
        "marks": 1,
        "topic": "Spotprent: Aanspreekvorme en taalkonvensies",
        "passage": PASSAGE_TEKS_B,
        "question": "Kies die KORREKTE antwoord. Skryf net die vraagnommer (1.20) en die antwoord (A–D) neer.\n\nDie man agter die tafel gebruik die aanspreekvorm \"Boet\", want ...\n\nA hy is familie van die jongman wat voor hom sit.\nB hy ken die jongman wat voor hom sit, persoonlik.\nC só spreek Afrikaanse mense 'n jongman dikwels aan.\nD die jongman het nie sy aansoekvorms volledig ingevul nie.",
        "memo": "* $\\checkmark$ C / só spreek Afrikaanse mense 'n jongman dikwels aan.",
        "final_answer": "C só spreek Afrikaanse mense 'n jongman dikwels aan.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{SOURCE_ID}-1.21.1",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "language": LANGUAGE,
        "track": TRACK,
        "kind": "multiple_choice",
        "question_ref": "1.21.1",
        "marks": 1,
        "topic": "Spotprent: Toon en boodskap",
        "passage": PASSAGE_TEKS_B,
        "question": "\"Boet, wag vir die dag dat jy vir werk aansoek doen.\"\n\nKies die KORREKTE woord uit dié tussen hakies. Skryf net die vraagnommer (1.21.1) en die antwoord neer.\n\nDie boodskap wat die man aan die jongman oordra, is (positief/negatief).",
        "memo": "* $\\checkmark$ negatief",
        "final_answer": "negatief",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{SOURCE_ID}-1.21.2",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "language": LANGUAGE,
        "track": TRACK,
        "kind": "passage_questions",
        "question_ref": "1.21.2",
        "marks": 1,
        "topic": "Spotprent: Motivering van afleiding",
        "passage": PASSAGE_TEKS_B,
        "question": "Motiveer jou antwoord op VRAAG 1.21.1.",
        "memo": "* $\\checkmark$ Die man sê dat die jongman in nog langer rye sal moet gaan staan wanneer hy vir werk aansoek doen. / Met hierdie woorde impliseer die man dat werk skaars is. / Baie mense doen vir dieselfde werk aansoek, want daar is nie baie werk nie. / Die man skets 'n donker prentjie van die jongman se werksvooruitsig. / Dis moeiliker om vir werk aansoek te doen as om by die universiteit te registreer. *(Enige EEN of soortgelyk aan bogenoemde; 1.21.1 moet korrek wees om 'n punt by 1.21.2 te verdien)*",
        "final_answer": "Die man impliseer dat werk baie skaars is en dat die toue om vir werk aansoek te doen selfs nog langer en moeiliker gaan wees.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{SOURCE_ID}-1.22",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "language": LANGUAGE,
        "track": TRACK,
        "kind": "passage_questions",
        "question_ref": "1.22",
        "marks": 1,
        "topic": "Spotprent: Afleiding uit agtergrondfigure",
        "passage": PASSAGE_TEKS_B,
        "question": "Waarom, dink jy, praat die twee dames wat in die kantoor werk, glad nie?",
        "memo": "* $\\checkmark$ Hulle konsentreer net op wat hulle (moet) doen. / Daar is baie werk om te doen / hulle is besig / hulle werk hard. / Hulle is al gewoond aan die werk wat hulle doen en doen dit sonder emosie. / Hulle raak nie by die mense betrokke nie. / Vir hulle is dit net maar nog 'n dag. / Hulle werk meganies omdat die ry studente eindeloos lank is. / Dis nie goeie maniere om te praat as iemand anders praat nie. / Hulle is bang vir hulle werkgewer. *(Enige EEN of soortgelyk aan bogenoemde)*",
        "final_answer": "Hulle is baie besig en konsentreer slegs op hul werk (papierwerk en liassering) omdat daar so baie studente is.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },

    # ----------------------------------------------------
    # AFDELING B: OPSOMMING (10 punte)
    # VRAAG 2
    # ----------------------------------------------------
    {
        "item_id": f"{SOURCE_ID}-2",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "language": LANGUAGE,
        "track": TRACK,
        "kind": "passage_questions",
        "question_ref": "2",
        "marks": 10,
        "topic": "Opsomming: Belangrike feite om te onthou as jy 'n nuwe taal wil aanleer",
        "passage": PASSAGE_TEKS_C,
        "question": """Jy wil graag 'n nuwe taal aanleer. Jy luister na 'n praatjie oor die radio daaroor. Jy maak aantekeninge oor die sewe belangrike feite om te onthou as jy 'n nuwe taal wil aanleer.

#### INSTRUKSIES
1. Skryf die SEWE belangrike feite om te onthou as jy 'n nuwe taal wil aanleer, puntsgewys neer.
2. Nommer die feite van 1 tot 7.
3. Jou opsomming mag nie langer as 70 woorde wees nie.
4. Skryf sover moontlik in jou EIE VOLSINNE.
5. Dui die korrekte getal woorde aan die einde van die opsomming aan.""",
        "memo": """**Puntetoekenning:**
* 7 punte vir 7 feite (1 punt per feit)
* 3 punte vir taal
* **Totaal punte: 10**

**Toekenning van taalpunte as leerders nie woordeliks aangehaal het nie:**
* 1–3 korrekte feite: 1 punt
* 4–5 korrekte feite: 2 punte
* 6–7 korrekte feite: 3 punte

**Toekenning van taalpunte as leerders woordeliks aangehaal het:**
* 6–7 korrekte aanhalings: geen punte word vir taal toegeken nie
* 1–5 korrekte aanhalings: 1 punt word vir taal toegeken

**Feite (Enige SEWE van die volgende agt feite in volsinne):**
1. * $\\checkmark$ Jy kan 'n taal op enige ouderdom aanleer.
2. * $\\checkmark$ Besluit waarom jy die taal wil aanleer / hoe gevorderd jou taalkursus moet wees.
3. * $\\checkmark$ Leer eers 'n taal praat voordat jy dit lees en/of skryf.
4. * $\\checkmark$ Jy hoef nie slim te wees om 'n nuwe taal aan te leer nie.
5. * $\\checkmark$ Bestee genoeg tyd aan die aanleer/oefen van die nuwe taal.
6. * $\\checkmark$ Gebruik elke geleentheid/kans om die nuwe taal te praat.
7. * $\\checkmark$ Luister na liedjies in die nuwe taal en sing saam.
8. * $\\checkmark$ Hou ná die kursus aan om die nuwe taal te praat.""",
        "final_answer": """1. Jy kan op enige ouderdom 'n nuwe taal aanleer.
2. Besluit vooraf wat jy met die nuwe taal wil doen.
3. Leer eers die taal praat voor jy dit lees of skryf.
4. Jy hoef glad nie slim te wees om 'n taal aan te leer nie.
5. Bestee genoeg tyd daaraan om die taal te bemeester.
6. Praat die taal by elke moontlike geleentheid.
7. Luister na liedjies in die taal en sing saam.

(67 woorde)""",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },

    # ----------------------------------------------------
    # AFDELING C: TAAL (40 punte)
    # VRAAG 3: ADVERTENSIE (10 punte)
    # ----------------------------------------------------
    {
        "item_id": f"{SOURCE_ID}-3.1",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "language": LANGUAGE,
        "track": TRACK,
        "kind": "question",
        "question_ref": "3.1",
        "marks": 1,
        "topic": "Taalstrukture: Verbuiging van die adjektief",
        "passage": PASSAGE_TEKS_D,
        "question": "Gee die KORREKTE vorm van die woord tussen hakies:\n\nKom na Thandeka vir (tradisioneel) drag …",
        "memo": "* $\\checkmark$ tradisionele",
        "final_answer": "tradisionele",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{SOURCE_ID}-3.2",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "language": LANGUAGE,
        "track": TRACK,
        "kind": "multiple_choice",
        "question_ref": "3.2",
        "marks": 1,
        "topic": "Advertensietegnieke: Tipografie en beklemtoning",
        "passage": PASSAGE_TEKS_D,
        "question": "Kies die KORREKTE antwoord om die sin mee te voltooi. Skryf net die vraagnommer (3.2) en die letter (A–D) neer.\n\nMet die ongewone skryfwyse van G-r-o-o-t wil die adverteerder beklemtoon dat …\n\nA die winkel groter as baie ander winkels is.\nB alles in die winkel vir grootgeboude mense bedoel is.\nC klante baie groot bedrae geld by die winkel gaan bestee.\nD die klere tydens hierdie uitverkoping baie goedkoop gaan wees.",
        "memo": "* $\\checkmark$ D / die klere tydens hierdie uitverkoping baie goedkoop gaan wees.",
        "final_answer": "D die klere tydens hierdie uitverkoping baie goedkoop gaan wees.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{SOURCE_ID}-3.3",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "language": LANGUAGE,
        "track": TRACK,
        "kind": "question",
        "question_ref": "3.3",
        "marks": 1,
        "topic": "Taalstrukture: Intensiewe vorme",
        "passage": PASSAGE_TEKS_D,
        "question": "Gee die INTENSIEWE VORM van die woord tussen hakies:\n\nDie klere is netjies en (goedkoop).",
        "memo": "* $\\checkmark$ spotgoedkoop",
        "final_answer": "spotgoedkoop",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{SOURCE_ID}-3.4",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "language": LANGUAGE,
        "track": TRACK,
        "kind": "question",
        "question_ref": "3.4",
        "marks": 1,
        "topic": "Taalstrukture: Spelling",
        "passage": PASSAGE_TEKS_D,
        "question": "Verbeter die SPELFOUT in die sin:\n\nDaar is 'n verskeidenheid material.",
        "memo": "* $\\checkmark$ materiaal / materiale",
        "final_answer": "materiaal",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{SOURCE_ID}-3.5",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "language": LANGUAGE,
        "track": TRACK,
        "kind": "multiple_choice",
        "question_ref": "3.5",
        "marks": 1,
        "topic": "Taalstrukture: Betreklike voornaamwoord met voorsetsel",
        "passage": PASSAGE_TEKS_D,
        "question": "Kies die korrekte VOORNAAMWOORD tussen hakies:\n\nDaar is baie patrone (uit wat/waaruit) jy kan kies.",
        "memo": "* $\\checkmark$ waaruit",
        "final_answer": "waaruit",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{SOURCE_ID}-3.6",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "language": LANGUAGE,
        "track": TRACK,
        "kind": "question",
        "question_ref": "3.6",
        "marks": 1,
        "topic": "Taalstrukture: Samestellings en verbindingsklanke",
        "passage": PASSAGE_TEKS_D,
        "question": "Vorm 'n SAMESTELLING met die woorde tussen hakies:\n\n(Besigheid+ure)",
        "memo": "* $\\checkmark$ Besigheidsure / besigheidsure",
        "final_answer": "Besigheidsure",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{SOURCE_ID}-3.7",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "language": LANGUAGE,
        "track": TRACK,
        "kind": "question",
        "question_ref": "3.7",
        "marks": 1,
        "topic": "Advertensie: Aanhaling uit teks",
        "passage": PASSAGE_TEKS_D,
        "question": "Mense van enige ouderdom kan by Thandeka kry wat hulle wil hê.\n\nSkryf VIER opeenvolgende woorde uit die advertensie neer wat dit vir ons sê.",
        "memo": "* $\\checkmark$ \"vir oud en jonk\" / vir oud en jonk",
        "final_answer": "\"vir oud en jonk\"",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{SOURCE_ID}-3.8",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "language": LANGUAGE,
        "track": TRACK,
        "kind": "multiple_choice",
        "question_ref": "3.8",
        "marks": 1,
        "topic": "Taalstrukture: Idiomatiese taal",
        "passage": PASSAGE_TEKS_D,
        "question": "Kies die KORREKTE antwoord uit dié tussen hakies:\n\n\"Thandeka is wyd en syd bekend\" beteken dat (al die mense in die dorp/mense van oral oor) weet wie Thandeka is.",
        "memo": "* $\\checkmark$ mense van oral oor",
        "final_answer": "mense van oral oor",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{SOURCE_ID}-3.9",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "language": LANGUAGE,
        "track": TRACK,
        "kind": "question",
        "question_ref": "3.9",
        "marks": 1,
        "topic": "Taalstrukture: Sinstipes (Bevelsin)",
        "passage": PASSAGE_TEKS_D,
        "question": "Skryf die sin hieronder as 'n BEVELSIN oor:\n\nJy kom maak 'n draai by haar.",
        "memo": "* $\\checkmark$ Kom maak 'n draai by haar.(!) / Jy moet 'n draai by haar kom maak.(!) / Kom maak by haar 'n draai.(!) / Jy moet by haar 'n draai kom maak.(!)",
        "final_answer": "Kom maak 'n draai by haar! (of: Jy moet 'n draai by haar kom maak!)",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{SOURCE_ID}-3.10",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "language": LANGUAGE,
        "track": TRACK,
        "kind": "question",
        "question_ref": "3.10",
        "marks": 1,
        "topic": "Advertensie: Teksverwysing en simbole",
        "passage": PASSAGE_TEKS_D,
        "question": "Waarvoor sou 'n mens vir Thandeka 'n ⭐ wou gee? Skryf TWEE opeenvolgende woorde uit die teks neer.",
        "memo": "* $\\checkmark$ \"stergehalte diens\" / \"verskeidenheid material(e)\" / \"baie patrone\" / \"tradisionele (tradisioneel) drag\" / \"groot winskope\" / \"die bykomstighede\" *(Kandidaat word nie gepenaliseer as die woorde nie tussen aanhalingstekens is nie.)*",
        "final_answer": "\"stergehalte diens\"",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },

    # ----------------------------------------------------
    # VRAAG 4: STROKIESPRENT (10 punte)
    # ----------------------------------------------------
    {
        "item_id": f"{SOURCE_ID}-4.1",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "language": LANGUAGE,
        "track": TRACK,
        "kind": "question",
        "question_ref": "4.1",
        "marks": 1,
        "topic": "Taalstrukture: Indirekte rede",
        "passage": PASSAGE_TEKS_E,
        "question": """Skryf die sin in RAAMPIE 1 in die INDIREKTE REDE.

Meneer sê vir Neelsie: "Jy kom áltyd laat vir my rekenaarklas."

Begin só: Meneer sê vir Neelsie dat …""",
        "memo": "* $\\checkmark$ Meneer sê vir Neelsie dat hy áltyd laat vir sy rekenaarklas kom. / Meneer sê vir Neelsie dat hy áltyd laat kom vir sy rekenaarklas. / Meneer sê vir Neelsie dat hy áltyd vir sy rekenaarklas laat kom. *(Enige EEN of soortgelyk aan bogenoemde)*",
        "final_answer": "Meneer sê vir Neelsie dat hy áltyd laat vir sy rekenaarklas kom.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{SOURCE_ID}-4.2",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "language": LANGUAGE,
        "track": TRACK,
        "kind": "question",
        "question_ref": "4.2",
        "marks": 1,
        "topic": "Taalstrukture: Suiwere Afrikaans en leenwoorde",
        "passage": PASSAGE_TEKS_E,
        "question": "Gee die AFRIKAANS vir \"Sorry\".",
        "memo": "* $\\checkmark$ Jammer / jammer / Ek is jammer. / Dit spyt my. / Verskoon my. / Ekskuus / askies / 'skuus *(Enige EEN of soortgelyk aan bogenoemde)*",
        "final_answer": "Jammer (of: Ek is jammer / Ekskuus)",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{SOURCE_ID}-4.3",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "language": LANGUAGE,
        "track": TRACK,
        "kind": "question",
        "question_ref": "4.3",
        "marks": 1,
        "topic": "Taalstrukture: Taalkonteks en rekenaarterme",
        "passage": PASSAGE_TEKS_E,
        "question": "Hoekom is dit aanvaarbaar dat Meneer van \"games\" praat?",
        "memo": "* $\\checkmark$ Rekenaartaal is gewoonlik in Engels. / Die kinders praat so (tienertaal). *(Enige EEN of soortgelyk aan bogenoemde)*",
        "final_answer": "Rekenaartaal/videospeletjies is gewoonlik in Engels (of: dit is hoe tieners praat).",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{SOURCE_ID}-4.4",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "language": LANGUAGE,
        "track": TRACK,
        "kind": "passage_questions",
        "question_ref": "4.4",
        "marks": 1,
        "topic": "Strokiesprent: Visuele elemente en lyftaal",
        "passage": PASSAGE_TEKS_E,
        "question": "Noem EEN visuele teken in RAAMPIE 2 wat vir ons sê dat Meneer geïrriteerd is met al die goed wat hy van Neelsie weet.",
        "memo": "* $\\checkmark$ Meneer/Hy frons / het plooie op sy voorkop. / Meneer/Hy wys vir Neelsie sy vinger. / Meneer se/Sy oë is groot. / Meneer/Hy glimlag nie. / Meneer se gesig/liggaamshouding. *(Enige EEN of soortgelyk aan bogenoemde)*",
        "final_answer": "Meneer wys beskuldigend met sy vinger na Neelsie (of: hy frons met plooie op sy voorkop / sy oë is groot).",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{SOURCE_ID}-4.5",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "language": LANGUAGE,
        "track": TRACK,
        "kind": "question",
        "question_ref": "4.5",
        "marks": 1,
        "topic": "Taalstrukture: Ontkennende vorm (Negatief)",
        "passage": PASSAGE_TEKS_E,
        "question": "Skryf die sin hieronder in die ONTKENNENDE VORM:\n\nNeelsie doen áltyd sy eie werk.",
        "memo": "* $\\checkmark$ Neelsie doen nooit sy eie werk nie. / Neelsie doen nie áltyd sy eie werk nie. *(Enige EEN)*",
        "final_answer": "Neelsie doen nooit sy eie werk nie. (of: Neelsie doen nie áltyd sy eie werk nie.)",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{SOURCE_ID}-4.6",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "language": LANGUAGE,
        "track": TRACK,
        "kind": "question",
        "question_ref": "4.6",
        "marks": 1,
        "topic": "Taalstrukture: Voegwoorde en woordorde",
        "passage": PASSAGE_TEKS_E,
        "question": "Verbind die sinne met die VOEGWOORD tussen hakies:\n\nMeneer is kwaad vir Neelsie. Hy doen nie sy werk nie. (omdat)",
        "memo": "* $\\checkmark$ Meneer is kwaad vir Neelsie omdat hy nie sy werk doen nie. / Omdat Neelsie/hy nie sy werk doen nie, is Meneer kwaad vir hom/Neelsie. *(Enige EEN)*",
        "final_answer": "Meneer is kwaad vir Neelsie omdat hy nie sy werk doen nie.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{SOURCE_ID}-4.7",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "language": LANGUAGE,
        "track": TRACK,
        "kind": "question",
        "question_ref": "4.7",
        "marks": 1,
        "topic": "Strokiesprent: Woordkeuse en aksenttekens",
        "passage": PASSAGE_TEKS_E,
        "question": "Met watter woord beklemtoon Meneer dat Neelsie gereeld dinge doen wat verkeerd is?",
        "memo": "* $\\checkmark$ áltyd / altyd",
        "final_answer": "áltyd",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{SOURCE_ID}-4.8.1",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "language": LANGUAGE,
        "track": TRACK,
        "kind": "multiple_choice",
        "question_ref": "4.8.1",
        "marks": 1,
        "topic": "Strokiesprent: Gesigsuitdrukking en liggaamstaal",
        "passage": PASSAGE_TEKS_E,
        "question": "Kies die KORREKTE woord uit dié tussen hakies. Skryf net die vraagnommer (4.8.1) en die antwoord neer:\n\nIn RAAMPIE 1 lyk Neelsie (jammer/verveeld).",
        "memo": "* $\\checkmark$ verveeld",
        "final_answer": "verveeld",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{SOURCE_ID}-4.8.2",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "language": LANGUAGE,
        "track": TRACK,
        "kind": "multiple_choice",
        "question_ref": "4.8.2",
        "marks": 1,
        "topic": "Strokiesprent: Vergelyking van raampies",
        "passage": PASSAGE_TEKS_E,
        "question": "Kies die KORREKTE woord uit dié tussen hakies. Skryf net die vraagnommer (4.8.2) en die antwoord neer:\n\nIn RAAMPIE 3 lyk Neelsie (anders/dieselfde) as in RAAMPIE 1.",
        "memo": "* $\\checkmark$ dieselfde",
        "final_answer": "dieselfde",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{SOURCE_ID}-4.9",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "language": LANGUAGE,
        "track": TRACK,
        "kind": "multiple_choice",
        "question_ref": "4.9",
        "marks": 1,
        "topic": "Taalstrukture: Idiome en figuurlike taal",
        "passage": PASSAGE_TEKS_E,
        "question": """Kies die KORREKTE antwoord. Skryf net die vraagnommer (4.9) en die letter (A–D) neer.

Watter IDIOOM pas die beste by Neelsie se reaksie op die dinge wat Meneer vir hom sê?

A Agteros kom ook in die kraal.
B Dit is water op 'n eend se rug.
C Van lekker lag, kom lekker huil.
D Hy pluk die vrugte van sy harde werk.""",
        "memo": "* $\\checkmark$ B / Dit is water op 'n eend se rug.",
        "final_answer": "B Dit is water op 'n eend se rug.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },

    # ----------------------------------------------------
    # VRAAG 5: ARTIKEL EN PRENT (20 punte)
    # TEKS F: ARTIKEL (14 punte)
    # ----------------------------------------------------
    {
        "item_id": f"{SOURCE_ID}-5.1.1",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "language": LANGUAGE,
        "track": TRACK,
        "kind": "question",
        "question_ref": "5.1.1",
        "marks": 1,
        "topic": "Taalstrukture: Afkortings",
        "passage": PASSAGE_TEKS_F,
        "question": "Skryf die AFKORTING vir die woord tussen hakies:\n\nAltesaam 625 (kilogram) meel is gebruik om die koek te bak.",
        "memo": "* $\\checkmark$ kg *(Daar mag nie 'n punt/hoofletter wees nie.)*",
        "final_answer": "kg",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{SOURCE_ID}-5.1.2",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "language": LANGUAGE,
        "track": TRACK,
        "kind": "multiple_choice",
        "question_ref": "5.1.2",
        "marks": 1,
        "topic": "Taalstrukture: Woordkeuse by vergelykings (dan / as)",
        "passage": PASSAGE_TEKS_F,
        "question": "Kies die korrekte WOORD tussen hakies:\n\nDie koek het meer (dan/as) 3 m hoog gestaan.",
        "memo": "* $\\checkmark$ as",
        "final_answer": "as",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{SOURCE_ID}-5.1.3",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "language": LANGUAGE,
        "track": TRACK,
        "kind": "question",
        "question_ref": "5.1.3",
        "marks": 1,
        "topic": "Taalstrukture: Homonieme",
        "passage": PASSAGE_TEKS_F,
        "question": "Gebruik die HOMONIEM van bak in 'n sin sodat die betekenis duidelik is.",
        "memo": """* $\\checkmark$ Enige sin waarin die ander betekenis van bak duidelik blyk, bv.:
  - Ek meng die deeg in die bak.
  - Ons bak in die son.
  - Ek hou my hande bak.
  - Sy hou daarvan om vir ander poetse te bak.
  - Hy het 'n bak idee.
  - 'n Poets bak.
  - Die tas is agter in die bak.
  - Die seun se bene is bak.""",
        "final_answer": "Sy meng die koekbeslag in 'n groot bak.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{SOURCE_ID}-5.1.4",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "language": LANGUAGE,
        "track": TRACK,
        "kind": "question",
        "question_ref": "5.1.4",
        "marks": 1,
        "topic": "Taalstrukture: Deelwoorde",
        "passage": PASSAGE_TEKS_F,
        "question": "Vorm 'n DEELWOORD van die werkwoord tussen hakies:\n\nDie (voltooi) koek is in die Sandton City-winkelsentrum uitgestal.",
        "memo": "* $\\checkmark$ voltooide",
        "final_answer": "voltooide",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{SOURCE_ID}-5.1.5",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "language": LANGUAGE,
        "track": TRACK,
        "kind": "question",
        "question_ref": "5.1.5",
        "marks": 1,
        "topic": "Taalstrukture: Toekomende tyd",
        "passage": PASSAGE_TEKS_F,
        "question": "Skryf die sin in die TOEKOMENDE TYD oor:\n\nCupcakes of Hope doen elke jaar iets vir kinders met kanker.",
        "memo": "* $\\checkmark$ Cupcakes of Hope sal/gaan elke jaar iets doen vir kinders met kanker. / Cupcakes of Hope sal/gaan elke jaar iets vir kinders met kanker doen. / Cupcakes of Hope sal/gaan vir kinders met kanker elke jaar iets doen. *(Enige EEN)*",
        "final_answer": "Cupcakes of Hope sal elke jaar iets vir kinders met kanker doen.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{SOURCE_ID}-5.1.6",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "language": LANGUAGE,
        "track": TRACK,
        "kind": "question",
        "question_ref": "5.1.6",
        "marks": 1,
        "topic": "Taalstrukture: Woordomskrywing / Eén woord vir 'n frase",
        "passage": PASSAGE_TEKS_F,
        "question": "Gee EEN WOORD vir die woorde tussen hakies:\n\nHierdie koek is gebak om Mandela se geboortedag 'n (honderd jaar) gelede te vier.",
        "memo": "* $\\checkmark$ eeu",
        "final_answer": "eeu",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{SOURCE_ID}-5.1.7",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "language": LANGUAGE,
        "track": TRACK,
        "kind": "question",
        "question_ref": "5.1.7",
        "marks": 1,
        "topic": "Taalstrukture: Meervoude",
        "passage": PASSAGE_TEKS_F,
        "question": "Gee die MEERVOUD van die woord tussen hakies:\n\nSandy sê sulke (geleentheid) is baie spesiaal.",
        "memo": "* $\\checkmark$ geleenthede",
        "final_answer": "geleenthede",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{SOURCE_ID}-5.1.8",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "language": LANGUAGE,
        "track": TRACK,
        "kind": "question",
        "question_ref": "5.1.8",
        "marks": 1,
        "topic": "Taalstrukture: Besitlike voornaamwoorde",
        "passage": PASSAGE_TEKS_F,
        "question": "Vul die ontbrekende VOORNAAMWOORD in:\n\nMandela het gesê dat dit in mense se hande is om 'n verskil in (…) eie gemeenskap te maak.",
        "memo": "* $\\checkmark$ hulle / hul",
        "final_answer": "hulle (of: hul)",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{SOURCE_ID}-5.1.9",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "language": LANGUAGE,
        "track": TRACK,
        "kind": "question",
        "question_ref": "5.1.9",
        "marks": 1,
        "topic": "Taalstrukture: Trappe van vergelyking",
        "passage": PASSAGE_TEKS_F,
        "question": "Gee die KORREKTE VORM van die woord tussen hakies:\n\nDie mense van Cupcakes of Hope doen die (goed) wat hulle kan om 'n verskil in die gemeenskap te maak.",
        "memo": "* $\\checkmark$ beste",
        "final_answer": "beste",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{SOURCE_ID}-5.1.10",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "language": LANGUAGE,
        "track": TRACK,
        "kind": "question",
        "question_ref": "5.1.10",
        "marks": 1,
        "topic": "Taalstrukture: Woordvorming (Afleiding / Selfstandige naamwoord)",
        "passage": PASSAGE_TEKS_F,
        "question": "Vorm 'n SELFSTANDIGE NAAMWOORD van die woord tussen hakies:\n\nHulle wil 'n (inspireer) vir meer mense wees om Cupcake-engele te word.",
        "memo": "* $\\checkmark$ inspirasie",
        "final_answer": "inspirasie",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{SOURCE_ID}-5.1.11",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "language": LANGUAGE,
        "track": TRACK,
        "kind": "question",
        "question_ref": "5.1.11",
        "marks": 1,
        "topic": "Taalstrukture: Antonieme",
        "passage": PASSAGE_TEKS_F,
        "question": "Gee 'n ANTONIEM vir die woord tussen hakies:\n\nDit maak 'n mens baie (ongelukkig).",
        "memo": "* $\\checkmark$ gelukkig / bly / opgewonde",
        "final_answer": "gelukkig (of: bly)",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{SOURCE_ID}-5.1.12",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "language": LANGUAGE,
        "track": TRACK,
        "kind": "question",
        "question_ref": "5.1.12",
        "marks": 1,
        "topic": "Taalstrukture: Infinitief (om te)",
        "passage": PASSAGE_TEKS_F,
        "question": "Skryf die gedeelte tussen hakies in die INFINITIEF:\n\n'n Kankerlyertjie se ma was daar (die organisasie vir hulle werk bedank).",
        "memo": "* $\\checkmark$ om die organisasie vir hulle werk te bedank. / om die organisasie te bedank vir hulle werk. *(Enige EEN)*",
        "final_answer": "om die organisasie vir hulle werk te bedank",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{SOURCE_ID}-5.1.13",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "language": LANGUAGE,
        "track": TRACK,
        "kind": "question",
        "question_ref": "5.1.13",
        "marks": 1,
        "topic": "Taalstrukture: Woordkeuse en tydsaanduiding",
        "passage": PASSAGE_TEKS_F,
        "question": "Verbeter die foutiewe WOORDKEUSE in die sin:\n\nCupcakes of Hope het gelede jaar 'n wêreldrekord vir die hoogste kolwyntjietoring opgestel.",
        "memo": "* $\\checkmark$ verlede / die vorige / laas (jaar) *(nie laaste jaar nie)*",
        "final_answer": "verlede (of: die vorige / laas)",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{SOURCE_ID}-5.1.14",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "language": LANGUAGE,
        "track": TRACK,
        "kind": "question",
        "question_ref": "5.1.14",
        "marks": 1,
        "topic": "Taalstrukture: Verkleinwoorde",
        "passage": PASSAGE_TEKS_F,
        "question": "Gee die VERKLEINWOORD van die woord tussen hakies:\n\nDit was nie 'n klein (toring) nie.",
        "memo": "* $\\checkmark$ torinkie",
        "final_answer": "torinkie",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },

    # ----------------------------------------------------
    # TEKS G: PRENT (6 punte)
    # ----------------------------------------------------
    {
        "item_id": f"{SOURCE_ID}-5.2.1",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "language": LANGUAGE,
        "track": TRACK,
        "kind": "multiple_choice",
        "question_ref": "5.2.1",
        "marks": 1,
        "topic": "Taalstrukture: Woordkeuse (klante vs. besoekers)",
        "passage": PASSAGE_TEKS_G,
        "question": "Kies die korrekte WOORD tussen hakies:\n\nDie winkelbestuurder wag vir die laaste (besoekers/klante) om die winkel te verlaat.",
        "memo": "* $\\checkmark$ klante",
        "final_answer": "klante",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{SOURCE_ID}-5.2.2",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "language": LANGUAGE,
        "track": TRACK,
        "kind": "question",
        "question_ref": "5.2.2",
        "marks": 1,
        "topic": "Taalstrukture: Woordeskat (Geografiese terme)",
        "passage": PASSAGE_TEKS_G,
        "question": "VOLTOOI die sin:\n\nOns gebruik die … om te kyk waar elke land in die wêreld is.",
        "memo": "* $\\checkmark$ aardbol / globe / wêreldbol / bolkaart *(nie -bal nie)*",
        "final_answer": "aardbol (of: wêreldbol / globe)",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{SOURCE_ID}-5.2.3",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "language": LANGUAGE,
        "track": TRACK,
        "kind": "question",
        "question_ref": "5.2.3",
        "marks": 1,
        "topic": "Taalstrukture: Persoonsname / Beroepe",
        "passage": PASSAGE_TEKS_G,
        "question": "Gee die PERSOONSNAAM van die woorde tussen hakies:\n\nDie hotel se (persoon wat die kos maak) dra elke dag 'n skoon uniform.",
        "memo": "* $\\checkmark$ kok / sjef / chef *(Enige EEN)*",
        "final_answer": "kok (of: sjef)",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{SOURCE_ID}-5.2.4",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "language": LANGUAGE,
        "track": TRACK,
        "kind": "question",
        "question_ref": "5.2.4",
        "marks": 1,
        "topic": "Taalstrukture: Lettergreepverdeling",
        "passage": PASSAGE_TEKS_G,
        "question": "Verdeel die woord tussen hakies in LETTERGREPE:\n\nDie (verpleegster) het die dokter se verslag in haar hand.",
        "memo": "* $\\checkmark$ ver-pleeg-ster / ver+pleeg+ster *(Kandidate kan dit op enige aanvaarbare wyse aandui, solank die lettergrepe duidelik is.)*",
        "final_answer": "ver-pleeg-ster",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{SOURCE_ID}-5.2.5",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "language": LANGUAGE,
        "track": TRACK,
        "kind": "question",
        "question_ref": "5.2.5",
        "marks": 1,
        "topic": "Taalstrukture: Leestekens (Komma by aangesproke persoon)",
        "passage": PASSAGE_TEKS_G,
        "question": "Vul die ontbrekende LEESTEKEN in. Skryf die sin oor en onderstreep die leesteken:\n\nDie dame sê: \"Meneer hier is u geskenk.\"",
        "memo": "* $\\checkmark$ Die dame sê: \"Meneer, hier is u geskenk.\"",
        "final_answer": "Die dame sê: \"Meneer, hier is u geskenk.\" (komma na Meneer)",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{SOURCE_ID}-5.2.6",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "language": LANGUAGE,
        "track": TRACK,
        "kind": "multiple_choice",
        "question_ref": "5.2.6",
        "marks": 1,
        "topic": "Taalstrukture: Homofone en spelling (waardeer vs. waardeur)",
        "passage": PASSAGE_TEKS_G,
        "question": "Kies die korrekte SPELLING tussen hakies:\n\nOns moet altyd 'n geskenk (waardeur/waardeer).",
        "memo": "* $\\checkmark$ waardeer",
        "final_answer": "waardeer",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    }
]

def verify_and_save():
    total_marks = sum(item["marks"] for item in items)
    print(f"Total items: {len(items)}")
    print(f"Total marks: {total_marks} (Expected: 80)")
    assert total_marks == 80, f"Mark sum error! Expected 80, got {total_marks}"

    # Verify KaTeX dollar balancing in each item
    for item in items:
        for field in ["question", "memo", "final_answer", "passage"]:
            text = item.get(field, "")
            # Count dollar signs not preceded by backslash
            # (In KaTeX, math is $...$ or $$...$$)
            dollars = re.findall(r"(?<!\\)\$", text)
            if len(dollars) % 2 != 0:
                print(f"ERROR: Unbalanced dollar in item {item['item_id']}, field {field}")
                print(f"Text: {text}")
                raise ValueError(f"Unbalanced dollar sign in {item['item_id']} field {field}")

    # Output paths
    paths = [
        "workspace/items/afrikaans_fal/dbe-afrikaans_fal-g12-p1-2020-nov.jsonl",
        "workspace/items/dbe-afrikaans_fal-g12-p1-2020-nov.jsonl",
        "sa-tutor-kit/sa-tutor-kit/workspace/items/afrikaans_fal/dbe-afrikaans_fal-g12-p1-2020-nov.jsonl",
        "sa-tutor-kit/sa-tutor-kit/workspace/items/dbe-afrikaans_fal-g12-p1-2020-nov.jsonl"
    ]

    for p in paths:
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8") as f:
            for item in items:
                f.write(json.dumps(item, ensure_ascii=False) + "\n")
        print(f"Wrote {len(items)} items to {p}")

if __name__ == "__main__":
    verify_and_save()
