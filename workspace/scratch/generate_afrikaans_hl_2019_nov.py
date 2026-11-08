# -*- coding: utf-8 -*-
"""
Generator script for dbe-afrikaans_hl-g12-p1-2019-nov
Subject: afrikaans_hl
Grade: 12
Expected Marks: 70
"""

import json
import os
import re

SOURCE_ID = "dbe-afrikaans_hl-g12-p1-2019-nov"
MEMO_ID = "dbe-afrikaans_hl-g12-p1-2019-nov-memo"
SUBJECT = "afrikaans_hl"
GRADE = 12
LANGUAGE = "af"
TRACK = "languages_hl"

# --- PASSAGES ---

TEKS_A = """### TEKS A: ARTIKEL

**IS AFRIKAANSE MUSIEK REGTIG SO VROT?**  
*Johan Myburg*

1. In 'n onlangse vlaag kritiek in briewe aan koerante, op nuuswebwerwe en sosialemediaforums waarin uitgevaar is teen Afrikaanse musiek, het sangers, liedjieskrywers en radiostasies behoorlik deurgeloop. Sangers is beskuldig van ''ritmelose en irriterende musiek''; liedjieskrywers is geroskam oor hulle ''herhalende, niksseggende en ligsinnige lirieke''. Radiostasies se programsamestellers van musiekprogramme is uitgekryt as ''bewusteloos'' omdat hulle blykbaar nie 'n benul het van wat goeie en slegte musiek is nie. Hulle moes hoor hulle doen nie die nodige navorsing om ordentlike materiaal te bekom nie.

2. Weggesteek tussen die stortvloed van bogenoemde klagtes kom die eeue-oue probleem weer na vore: wat is goed en wat is sleg, wat is reg en wat moet weg? Oor voorkeure, het die Romeine dit al lankal uitgemaak, kan 'n mens nooit 'n finale beslissing vel nie. 'n Mens se persoonlike voorkeure bly bloot subjektiewe menings, en dit kan tog nooit voorskriftelik van aard wees nie en behoort daarom tydens argumentvoering oor die gehalte van Afrikaanse musiek buite rekening gelaat te word. Een persoon se ordentlik en smaakvol is vir die ander hondvervelig; vir iemand is 'n spesifieke sanger se musiek 'n getjank, vir 'n ander weer, die toppunt van tere emosie.

3. Meningsverskille oor die gehalte van Afrikaanse musiek is nie iets van verbygaande aard nie. Met gereelde tussenposes is daar telkens golf op golf van kritiek wat opstoot en dikwels walle oorspoel, soos nou weer die geval is. Reeds in 2012 het Marike Verwey, 'n joernalis wie se spesialisveld Afrikaanse musiek is, in dié verband in Huisgenoot haar kwellings oor Afrikaanse musiek geopper. Van haar sterkste punte van kritiek was dat die mark oorstroom is met Afrikaanse musiek waarvan die lirieke van ''swak gehalte'' is, dat daar te min liriekskrywers is wat weet hoe om ''goeie musiek te skryf'' en dat ''te min sangers bereid is om vernuwende Afrikaanse musiek te sing''. <u>En nou, sewe jaar later, word steeds briewe hieroor geskryf,</u> grappe om braaivleisvure oor ''my-baby-baby-musiek'' gemaak en kritiek oor flou Afrikaanse musiek geopper.

4. Na aanleiding van Verwey se kwellings hierbo en in die ewige soeke na wat goeie Afrikaanse musiek nou eintlik is, reageer die Afrikaanse liedjieboer, Anton Goosen, dat daar nie werklik 'n resep bestaan om tussen goeie en swak musiek te onderskei nie. ''Vir my is dit belangrik dat 'n liedjie die luisteraar enduit geïnteresseerd moet hou, hetsy dit nou deur middel van die woorde of die wysie is. As 'n liedjie met jou práát, dán is dit 'n goeie 'song','' sê hy.

5. In verdere reaksie op Verwey se kritiek rakende die sogenaamde swak lirieke in Afrikaanse musiek, is die sanger/liedjieskrywer, Simoné Redcliff, baie uitgesproke: ''Asseblief, hekwagters, hou ryme en ritmes en diep gedagtes uit ons musiek! Swak lirieke is 'n klein opoffering in die belang van artistieke vryheid; los musiek sodat dit kan wees wat dit wil – musiek! Los diep gedagtes vir letterkundiges. Musiek wil nié poësie wees nie, asseblief!''

6. Estelle Loftus, stasiebestuurder van die Afrikaanse radiostasie, LFM*, verdedig die kritiek wat na die radiostasies geslinger word – veral dié oor hulle keuses van liedjies met niksseggende lirieke – deur te verduidelik dat LFM se luisteraars se musieksmaak die kriterium is wat gebruik word vir dié stasie se sogenaamde vullermusiek (musiek wat tussen programme gebruik word). LFM se musiek moet luisteraars goed laat voel, met ander woorde, musiek moet 'n opgeruimde wysie hê; musiek wat die luisteraar in 'n goeie luim kry, nié rock nie en ook nie stadiger of wroegende musiek nie. Om hierdie balans te handhaaf moet LFM se programopstellers gereeld die veranderinge in die Afrikaanse musiekmark dophou om seker te maak dat die stasie goeie musiek speel waarvan hulle luisteraars hou.

7. In reaksie op Verwey se kritiek dat sangers nie vernuwende Afrikaanse musiek wil sing nie, sonder Isaac Mtshali, grootbaas van Boom Recording Studios, van sy maatskappy se sangers uit wat werklik uit hulle pad gaan om vernuwend te werk, dikwels ten koste van finansiële voorspoed as gevolg van kleiner luistergetalle en CD-verkope. ''Kunstenaars soos David Kramer, Anton Goosen, Refentse en verál Les Javan is vernuwende sangers wat musikale brûe herstel, ook tussen bruin en wit musiekliefhebbers wat deel van 'n unieke musiekgeskiedenis vorm,'' sê hy.

8. Is Afrikaanse musiek dan rêrig so vrot? Wat musiekliefhebbers nie uit die oog moet verloor nie, is dat 'n beduidende segment luisteraars van Afrikaanse musiek nie noodwendig dieselfde hoë artistieke standaarde soos die kritici in gedagte het wanneer hulle na 'n liedjie luister nie. Hulle wil bloot na musiek met maklike lirieke luister wat hulle in die motor op pad huis toe in staat stel om te kan saamsing, en musiek waarvan die ritme hulle voete op 'n dansbaan laat jeuk.

9. Solank musiekliefhebbers en -luisteraars musiek koop en luister na wat hulle laat goed voel, is Afrikaanse musiek kerngesond. En as dit dan bokkie-sokkie-rokkie-lirieke en brabbelmusiek is, wie se ''smaak'' is dan nou regtig só verkeerd?

*\*LFM is die handelsnaam vir die nuwe deurnagradiostasie, Luister-FM.*  
*[Verwerk uit https://maroelamedia.co.za]*"""

TEKS_B = """### TEKS B: VISUELE TEKS (SPOTPRENT)

'n Spotprent oor Afrikaanse musiek en musieksmaak:
- In die middel is 'n energieke Afrikaanse sanger met wilde hare, 'n sonbril en 'n mikrofoon in sy hand wat uit volle bors sing en dans terwyl musieknote om hom sweef.
- Op sy T-hemp staan die woorde: "EK [hartjie] AFRIKAANS" (Ek is lief vir Afrikaans).
- Spraakborrel 1 (wat uit die sanger se mond kom):  
  "Jou oë is so blou, my baby, jou soene is so flou, my lovie ..."
- Spraakborrel 2 (aan die regterkant, wat 'n kritiese vereiste uitspreek):  
  "Goeie musiek móét rym en 'n lewendige ritme hê en móét vol metafore wees!"

*[Verwerk uit Volksblad, 1 September 2015]*"""

TEKS_AB = f"{TEKS_A}\n\n---\n\n{TEKS_B}"

TEKS_C = """### TEKS C: LEESTEKS VIR OPSOMMING

**OOM OLIFANT, JOU REUSEDIER**

Gewoonlik hou ek my hart vas as ek olifante en hulle gedrag in my tuin in Sabiepark dophou. Hulle verras my elke keer opnuut met iets anders as tydens hulle vorige besoeke. 

Olifante is sulke merkwaardige diere dat ek my vrye tyd dikwels gebruik om notas te neem terwyl ek my aan hulle positiewe kwaliteite verwonder. Hierdie diere openbaar in die eerste plek 'n humorsin wat my verstom. Daarom was my lekkerste glimlagervarings te danke aan olifantplatjies wat met hulle slurpe waterkanon-waterkanon speel. 

Nes mense se velle uitdroog, word olifante ook met hierdie selfde probleem gekonfronteer. Maar wat nou as hierdie diere nie ''olifantroom'' het nie? Dan word olifante planmakers: hulle rol in modderpoele om hierdie probleem die hoof te bied! En tydens hierdie ontspannende modderrituele het ek ook verbaas opgelet hoe vindingryk hierdie diere se kommunikasietegnieke is: flappende ore van die leierolifante is byvoorbeeld 'n teken dat gevaar dreig.

As 'n mens olifante se samesyn fyn dophou, sal jy agterkom dat 'n basiese familiegroep om een volwasse koei georganiseer word. Die manier waarop die trop hulle binne hierdie vaste sosiale struktuur gedra, is absoluut fassinerend. Die leierolifant en haar kalwers word byvoorbeeld onder andere toegelaat om altyd eerste te eet en te drink. As ander volwasse olifante hierdie patroon ontwrig, is die duiwel behoorlik los! 

Daarom is dit dan ook nie snaaks as jy bogenoemde in ag neem om die buitengewone band van welwillendheid tussen olifante in dieselfde trop te verstaan nie. 'n Olifantkoei sal byvoorbeeld dadelik die kalf van 'n ander koei as haar eie aanvaar as die situasie dit sou vereis. 

Indien 'n olifanttrop met 'n struikelblok gekonfronteer word, sal die leiers verskeie oplossings oorweeg as dit vir die trop geen gevaar inhou nie. 'n Mens verstom jou aan olifante se hoë intelligensievlakke. Hulle redeneer soos mense! En as hulle speel, speel hulle met 'n sorgvrye uitgelatenheid soos mensekinders. Ek geniet dit byvoorbeeld altyd wanneer hierdie grote diere en hulle kalfies hulle soos mense gedra. 

So, verspeelde vrye tyd, reken ek, is in orde as ek dit vergelyk met die ure se genot wat ek ervaar terwyl ek hierdie fantastiese kolosse bewonder.

*[Verwerk uit https://blogs.litnet.co.za/hvandeventer]*"""

TEKS_D = """### TEKS D: ADVERTENSIE

```text
1  AFRIKAANSKLASSE – 'n <u>verandering</u>!
2  <u>KIES</u> 'N VERANDERING NA POSITIEWE RESULTATE MET
3  MODERNE REKENAARGESTEUNDE LESSE EN
4  PERSOONLIKE AANDAG!
5  Ons interaktiewe lesse vergemaklik 
6  klaskameronderrig.
7  Tutors sal verseker dat jy jou 
8  kennis verder uitbrei.
9  Ons sistematiese benadering is as
10 dié top leermetode in Afrika* 
11 aangewys.
12 Kontak Piet vir meer 
13 inligting en vir 
14 spesiale aanbiedings!
15 Kaapstad
16 021 462 6358
17 piet@gmail.com
18 ONS VIER VANJAAR ONS
19 VYFDE BESTAANSJAAR.
20 *Via Africa-toekennings 2006‒2017
```
*(In regs onder van die advertensie is 'n illustrasie van twee leerders met die byskrif "Huistaal Graad 4–12" in 'n wolk.)*

*[Verwerk uit https://laerskoolpietduplooy.co.za]*"""

TEKS_E = """### TEKS E: STROKIESPRENT

**JEROME**

'n Strokiesprent met 8 raampies:
- **RAAMPIE 1:** Jerome sit op die bank met die telefoon teen sy oor en sê ontsteld: "Ravi, <u>ek sit met 'n truksvy!</u> Ek het jou gesê alle oumense is moeilik oor hulle karre!"
- **RAAMPIE 2:** Ravi antwoord kalm oor die foon: "Dis nie 'n probleem nie, Jerome, <u>ek tel jou op vir 'n koffietjie</u>."
- **RAAMPIE 3:** Ravi praat deur 'n helm. Jerome sê: "<u>Ravi, jy klink anders.</u>" Ravi verduidelik: "Ek het my oorloghelm opgesit, Jerome." Jerome vra: "En oorlog speel?"
- **RAAMPIE 4:** Jerome merk op: "<u>Dit laat jou stem eggo.</u>" Ravi antwoord geïrriteerd: "Ag, skoert!"
- **RAAMPIE 5:** Jerome staan op en roep vir sy ma: "Ek gaan uit, Ma." Sy ma kyk op en vra: "O, so?"
- **RAAMPIE 6:** Jerome antwoord: "Ons gaan <u>skoorsoek</u> en wegjaag."
- **RAAMPIE 7:** Ma dink by haarself: "Seuns gee 'n ma altyd grys hare."
- **RAAMPIE 8:** Ma groet hom: "<u>Geniet</u> dit, Jerome." Jerome swaai sy hand en sê: "Ek sal jou bel."

*[Verwerk uit https://gocomics.azcentral.com]*"""

TEKS_F = """### TEKS F: TYDSKRIFARTIKEL

**MET GOEIE VETKOEK KAN 'N MENS DIE WINTER VERSLAAN**

1. Wanneer dit by innerlike versterking kom, is ek nie 'n man van fieterjasies nie.

2. In die geval van 'n (5.2) vierpotig<u>e</u> dier begin ek by sy snoet en eindig by sy stert se punt. As dit by voedsel kom, is kieskeurigheid nie deel van my woordeskat nie. (5.3) <u>Ek verorber álles.</u>

3. Maar nou moet ek erken dat ek vir één (5.4) <u>eetding</u> in hierdie lewe 'n swak plek het – vetkoek.

4. Om hierby aan te sluit is ek geseën met 'n wederhelf wat nie ronde handjies het nie. Dikwels wonder ek of sy nie ingeboude suurdeeg in haar hande het nie.

5. Want 'n degie wat onder daardie twee gebalde vuiste in 'n knieskottel deurgeloop het, rys binne minute tot epidermiese proporsies. Dwarsoor die rant van die skottel. Soos lawa uit 'n vulkaan.

6. Haar eindprodukvetkoeke is <u>deur die bank</u> so veerlig soos heliumgevulde ballonne. Bedien dit nou met 'n stomende porsie sop, dan is jou stryd teen die winter reeds halfpad gewonne.

7. Selfbeheersing teen oordadigheid is dán die (5.8) <u>wagwoord</u>.

8. My liefde vir vetkoek het doer in my kinderdae begin. My tannie Angeline het 'n tuisnywerheid met 'n raaskopparaffienstofie, 'n sakkie meel en 'n paar blokkies Holsumvet begin.

9. En hier lê die winter nou weer vlak voor die deur. Ja-nee, sommige dinge is die moeite werd om na uit te sien.

*[Verwerk uit Die Burger, 19 Mei 2018]*"""


# --- ITEMS DATA ---

ITEMS = [
    # AFDELING A: LEESBEGRIP (30 punte)
    {
        "question_ref": "1.1",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Leesbegrip: Omvang van kritiek (TEKS A)",
        "passage": TEKS_A,
        "question": "Watter inligting in paragraaf 1 dui aan dat die kritiek oor Afrikaanse musiek wyd in omvang was?",
        "memo": "* $\\checkmark$ Die kritiek is in koerante / nuuswebwerwe / sosialemediaforums / verskeie media uitgespreek.",
        "final_answer": "Die kritiek het oor 'n wye verskeidenheid platforms versprei, insluitend briewe aan koerante, nuuswebwerwe en sosialemediaforums."
    },
    {
        "question_ref": "1.2",
        "marks": 2,
        "kind": "passage_questions",
        "topic": "Leesbegrip: Kreatiewe rolspelers en kritiek (TEKS A)",
        "passage": TEKS_A,
        "question": "Wie, wat by die kreatiewe proses van Afrikaanse musiek betrokke is, loop onder kritiek deur en wat is hierdie kritiek?",
        "memo": "* $\\checkmark$ **Sangers:** Hulle is beskuldig van 'ritmelose en irriterende musiek' (hulle musiek het geen ritme nie / dit irriteer).\n**OF**\n* $\\checkmark$ **Liedjieskrywers:** Hulle is geroskam oor hulle 'herhalende, niksseggende en ligsinnige lirieke'.\n* $\\checkmark$ Tweede punt vir die ooreenstemmende groep en kritiek.\n\n*(Die mense wat onder kritiek deurgeloop het en die gepaardgaande kritiek word onafhanklik geassesseer vir 2 punte.)*",
        "final_answer": "Die sangers en liedjieskrywers is by die kreatiewe proses betrokke. Die sangers word beskuldig van 'ritmelose en irriterende musiek', terwyl die liedjieskrywers geroskam word oor hul 'herhalende, niksseggende en ligsinnige lirieke'."
    },
    {
        "question_ref": "1.3",
        "marks": 3,
        "kind": "passage_questions",
        "topic": "Leesbegrip: Subjektiwiteit van voorkeure (TEKS A)",
        "passage": TEKS_A,
        "question": "Waarom kan daar oor voorkeure nooit 'n finale beslissing gevel word nie? Watter wenk gee die skrywer in paragraaf 2 in hierdie verband?",
        "memo": "* $\\checkmark$ Voorkeure is bloot subjektiewe menings wat nie op objektiewe kriteria berus nie / Menings kan nooit voorskriftelik van aard wees nie.\n* $\\checkmark$ Een persoon se ordentlik en smaakvol is vir 'n ander hondvervelig / Vir iemand is 'n spesifieke sanger se musiek 'n getjank, terwyl dit vir 'n ander die toppunt van tere emosie is / Niemand het die reg om voor te skryf waarvan iemand anders moet hou nie.\n*(Enige TWEE antwoorde vir 1 punt elk)*\n\n**EN** (Wenk:)\n* $\\checkmark$ Persoonlike voorkeure behoort tydens argumentvoering oor die gehalte van Afrikaanse musiek buite rekening gelaat te word.",
        "final_answer": "Daar kan nooit 'n finale beslissing oor voorkeure gevel word nie omdat 'n mens se voorkeure bloot subjektiewe menings is wat nooit voorskriftelik van aard kan wees nie; wat vir een persoon smaakvol is, is vir 'n ander hondvervelig. Die skrywer se wenk is dat persoonlike voorkeure tydens argumentvoering oor die gehalte van musiek buite rekening gelaat behoort te word."
    },
    {
        "question_ref": "1.4",
        "marks": 2,
        "kind": "passage_questions",
        "topic": "Leesbegrip: Figuurlike taalgebruik en metafore (TEKS A)",
        "passage": TEKS_A,
        "question": "''... golf op golf van kritiek ...'' en ''... dikwels walle oorspoel, ...'' (reël 20 en 21).\n\nDink jy die woordkeuse in hierdie aanhaling is binne konteks van die artikel effektief? Gee TWEE redes vir jou antwoord deur na elke aanhaling hierbo afsonderlik te verwys.",
        "memo": "* $\\checkmark$ **Ja:** ''golf op golf van kritiek ...'' dui op die hewige, herhalende en aanhoudende kritiek (soos opeenvolgende seegolwe) wat telkens oor 'n tydperk en uit verskeie oorde na vore kom.\n* $\\checkmark$ ''... dikwels walle oorspoel, ...'' is effektief omdat dit beklemtoon dat die kritiek so oorweldigend en buite beheer raak dat dit alle normale perke oorskry en nie gekeer kan word nie.\n\n*(Die kandidaat kan nie NEE as 'n antwoord aanbied nie. 1 punt per aanhaling se motivering.)*",
        "final_answer": "Ja, die woordkeuse is binne konteks baie effektief:\n1. '... golf op golf van kritiek ...' beskryf treffend hoe die kritiek herhalend en in opeenvolgende vlae uit verskillende oorde opstoot.\n2. '... dikwels walle oorspoel, ...' beklemtoon hoe die volume van kritiek so oorweldigend groot en intens word dat dit alle perke oorskry en nie gestuit kan word nie."
    },
    {
        "question_ref": "1.5",
        "marks": 4,
        "kind": "passage_questions",
        "topic": "Leesbegrip: Marike Verwey se kritiek en rol van samestellers (TEKS A)",
        "passage": TEKS_A,
        "question": "Noem kortliks Marike Verwey se hoofpunte van kritiek teenoor Afrikaanse musiek. Gee EEN rede waarom sy NIE kritiek teenoor radiostasies se programsamestellers van musiekprogramme lewer NIE.",
        "memo": "Hoofpunte van kritiek (3 punte):\n* $\\checkmark$ Die mark is oorstroom met Afrikaanse musiek waarvan die lirieke van swak gehalte is.\n* $\\checkmark$ Daar is te min liriekskrywers wat weet hoe om goeie musiek te skryf.\n* $\\checkmark$ Te min sangers is bereid om vernuwende Afrikaanse musiek te sing.\n\nRede waarom sy nie radiostasies se programsamestellers kritiseer nie (1 punt):\n* $\\checkmark$ Verwey is 'n joernalis wie se spesialisveld Afrikaanse musiek is (nie radioprogramsamestelling nie) / Programsamestellers vorm nie deel van die skeppende/kreatiewe proses van musiek nie / Daar bestaan nie 'n resep om te onderskei tussen goeie en swak musiek nie / Programsamestellers speel musiek waarvan luisteraars hou en is nie verantwoordelik vir die skepping van die liedjies nie.",
        "final_answer": "Marike Verwey se drie hoofpunte van kritiek is:\n1. Die Afrikaanse musiekmark is oorstroom met musiek waarvan die lirieke van swak gehalte is;\n2. Te min liriekskrywers weet hoe om werklik goeie musiek te skryf;\n3. Te min sangers is bereid om vernuwende Afrikaanse musiek te sing.\n\nSy lewer nie kritiek teen radiostasies se programsamestellers nie omdat programsamestellers nie by die kreatiewe proses van musiekskepping betrokke is nie, maar bloot speel waarvan hulle luisteraars hou."
    },
    {
        "question_ref": "1.6",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Leesbegrip: Verband tussen paragraaf 1 en 3 (TEKS A)",
        "passage": TEKS_A,
        "question": "Wat is die verband tussen die onderstreepte gedeelte in paragraaf 3 en die inhoud van paragraaf 1?",
        "memo": "* $\\checkmark$ Albei paragrawe maak melding van briewe wat geskryf word / Albei paragrawe verwys na openbare kritiek teen Afrikaanse musiek / Dit toon dat dieselfde klagtes en kritiek na al die jare steeds gehuldig en uitgespreek word.",
        "final_answer": "Albei paragrawe verwys na briewe waarin openbare kritiek teen Afrikaanse musiek uitgespreek word, wat aantoon dat dieselfde besware na sewe jaar steeds onveranderd bly."
    },
    {
        "question_ref": "1.7",
        "marks": 3,
        "kind": "passage_questions",
        "topic": "Leesbegrip: Simoné Redcliff se standpunt (TEKS A)",
        "passage": TEKS_A,
        "question": "Gee TWEE redes waarom Simoné Redcliff die kritici van Afrikaanse lirieke as ''hekwagters'' beskryf. Motiveer waarom juis Redcliff se uitsprake van “hekwagters” ongeloofwaardig is.",
        "memo": "TWEE redes vir die benaming 'hekwagters' (2 punte):\n* $\\checkmark$ Hulle wil voorskriftelik optree en namens ander besluit hoe lirieke geskryf moet word en hoe musiek moet klink.\n* $\\checkmark$ Hulle wil reëls (soos rym, ritme en diep intellektuele gedagtes/poësie) afdwing en ontneem kunstenaars van hul artistieke vryheid / Hulle wil toegang beheer en eenvoudige lirieke uitsluit.\n*(Enige TWEE redes vir 1 punt elk)*\n\nMotivering vir ongeloofwaardigheid (1 punt):\n* $\\checkmark$ Sy is self 'n sanger en liedjieskrywer wat lirieke skryf; sy is dus nie objektief nie maar bevooroordeeld / sy verdedig haar eie werk en belange.",
        "final_answer": "Twee redes waarom sy hulle as 'hekwagters' beskryf:\n1. Hulle wil voorskriftelik wees en namens ander bepaal hoe lirieke geskryf moet word;\n2. Hulle wil intellektuele vereistes soos rym, ritme en diep poëtiese gedagtes afdwing en ontneem kunstenaars daardeur van artistieke vryheid.\n\nHaar uitspraak is egter ongeloofwaardig omdat sy self 'n sanger en liedjieskrywer is wat haar eie lirieke en belange verdedig, wat haar oordeel subjektief maak."
    },
    {
        "question_ref": "1.8.1",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Leesbegrip: Radiostasie se verweer (TEKS A)",
        "passage": TEKS_A,
        "question": "Herlees paragraaf 6.\n\nWatter teenargument voer LFM aan ten opsigte van die kritiek waaronder radiostasies in paragraaf 1 deurloop?",
        "memo": "* $\\checkmark$ LFM voer aan dat hulle luisteraars se musieksmaak die maatstaf is; hulle programopstellers hou deurlopend die Afrikaanse musiekmark dop (doen navorsing) om seker te maak hulle speel opgeruimde musiek waarvan hul luisteraars hou en wat hulle goed laat voel (hulle is dus nie 'bewusteloos' nie).",
        "final_answer": "LFM voer aan dat hul luisteraars se musieksmaak die deurslaggewende kriterium is en dat hulle gereeld die musiekmark dophou om te verseker dat hulle musiek speel wat hul luisteraars goed laat voel."
    },
    {
        "question_ref": "1.8.2",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Leesbegrip: Evaluering van radiostasie-keuse (TEKS A)",
        "passage": TEKS_A,
        "question": "Herlees paragraaf 6.\n\nSal luisteraars na LFM wil luister nadat hulle die inligting in ag geneem het oor hoe hierdie radiostasie hulle musiek kies? Motiveer jou antwoord.",
        "memo": "* $\\checkmark$ **Ja:** Luisteraars sal wil luister omdat die musiek hulle goed laat voel, 'n opgeruimde wysie het en by hulle smaak pas sonder swaarmoedige of rockmusiek.\n**OF**\n* $\\checkmark$ **Nee:** Luisteraars wat juis van rockmusiek of ernstige, stadiger en diepsinnige musiek hou, sal nie daarna wil luister nie omdat die stasie dit doelbewus uitsluit.\n*(Enige EEN gemotiveerde antwoord vir 1 punt)*",
        "final_answer": "Ja, luisteraars sal graag wil luister omdat die stasie doelgerig opgeruimde musiek speel wat 'n goeie luim skep en hulle goed laat voel."
    },
    {
        "question_ref": "1.9",
        "marks": 3,
        "kind": "passage_questions",
        "topic": "Leesbegrip: Kommersiële vs. vernuwende musiek (TEKS A)",
        "passage": TEKS_A,
        "question": "Wat sal 'n positiewe gevolg vir die kunstenaars van Boom Recording Studios wees indien hulle NIE vernuwende musiek sing NIE? Sê ook hoekom sangers wat nie vernuwende musiek sing nie, vir Boom Recording Studios tot voordeel kan wees.",
        "memo": "Positiewe gevolg vir kunstenaars (1 punt):\n* $\\checkmark$ Hulle sal groter finansiële voorspoed geniet / meer CD's verkoop / groter luistergetalle bereik / wyer bekendheid onder die massas geniet.\n\nVoordeel vir Boom Recording Studios (2 punte):\n* $\\checkmark$ Die ateljee sal groter inkomste en finansiële wins genereer deur massaverkope.\n* $\\checkmark$ Die ateljee sal groter kommersiële lewensvatbaarheid en markaandeel/blootstelling verkry.\n*(TWEE redes vir 1 punt elk)*",
        "final_answer": "Vir die kunstenaars sal die positiewe gevolg groter finansiële voorspoed wees deur hoër CD-verkope en groter gehore.\n\nVir Boom Recording Studios is dit voordelig omdat:\n1. Die ateljee aansienlik meer winste en inkomste genereer danksy massaverkope;\n2. Dit die maatskappy groter kommersiële sukses en breë markblootstelling verseker."
    },
    {
        "question_ref": "1.10",
        "marks": 2,
        "kind": "passage_questions",
        "topic": "Leesbegrip: Brugbouers in musiek (TEKS A)",
        "passage": TEKS_A,
        "question": "Watter sanger word volgens die teks as brugbouer uitgesonder? Sê ook wat dit beteken om 'n brugbouer vir Afrikaanse musiek te wees.",
        "memo": "* $\\checkmark$ **Les Javan** (word verál uitgesonder).\n* $\\checkmark$ Dit beteken om musikale brûe te bou/herstel deur mense (veral bruin en wit musiekliefhebbers) deur middel van Afrikaanse musiek bymekaar te bring en deel van 'n unieke, inklusiewe musiekgeskiedenis te maak.",
        "final_answer": "Les Javan word uitgesonder. Om 'n brugbouer vir Afrikaanse musiek te wees, beteken dat sy musiek mense van verskillende rasse (spesifiek bruin en wit musiekliefhebbers) verenig en musikale brûe bou deur 'n gedeelde kultuur- en musiekgeskiedenis."
    },
    {
        "question_ref": "1.11",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Leesbegrip: Artistieke standaarde (TEKS A)",
        "passage": TEKS_A,
        "question": "Paragraaf 8 verwys na hoë artistieke standaarde wat kritici in gedagte het. Aan watter hoë artistieke standaard sal liedjieskrywers volgens die teks moet voldoen indien hulle kritici ten opsigte van gehaltemusiek tevrede wil stel?",
        "memo": "* $\\checkmark$ Die lirieke moet 'n dieper betekenis inhou / rym en ritme moet wyer as net die dansvloer strek / lirieke moet van hoë poëtiese gehalte wees.",
        "final_answer": "Liedjieskrywers sal lirieke met 'n dieper betekenis en poëtiese gehalte moet skryf wat verder strek as bloot maklike rympies vir die dansvloer."
    },
    {
        "question_ref": "1.12",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Leesbegrip: Regverdiging van kritiek (TEKS A)",
        "passage": TEKS_A,
        "question": "Dink jy die kritiek teen Afrikaanse musiek, soos in hierdie artikel, is geregverdig? Motiveer jou antwoord.",
        "memo": "* $\\checkmark$ **Ja:** Indien 'n mens nie hoë artistieke standaarde aan musiek stel nie, bestaan die gevaar dat musiek van swak gehalte die mark oorstroom en vernuwing stuit.\n**OF**\n* $\\checkmark$ **Nee:** Musiek het verskillende funksies; luisteraars soek dikwels bloot ligte vermaak wat hulle goed laat voel en waarop hulle kan dans, en smaak bly subjektief.\n*(Enige EEN gemotiveerde antwoord vir 1 punt)*",
        "final_answer": "Ja, die kritiek is geregverdig omdat kunstenaars aangemoedig moet word om vernuwende en betekenisvolle musiek van hoë gehalte te produseer sodat die genre nie in oppervlakkige rymelary stagneer nie."
    },
    {
        "question_ref": "1.13",
        "marks": 2,
        "kind": "passage_questions",
        "topic": "Leesbegrip: Visuele elemente en tema (TEKS B)",
        "passage": TEKS_B,
        "question": "Is die visuele aanduidings gepas om die tema van musiek uit te beeld? Gee TWEE redes vir jou antwoord.",
        "memo": "* $\\checkmark$ **Ja:** Die karakter hou 'n mikrofoon vas waarin hy sing.\n* $\\checkmark$ Die musieknote wat rondom hom geteken is, dui musiek aan / Die sanger se dans- en liggaamshouding wys dat hy op maat van musiek sing en beweeg.\n\n*(Die kandidaat kan nie NEE as antwoord aanbied nie. TWEE redes vir 1 punt elk.)*",
        "final_answer": "Ja, die visuele aanduidings is baie gepas:\n1. Die sanger hou 'n mikrofoon vas en sing uit volle bors terwyl hy ritmies beweeg;\n2. Daar is musieknote wat rondom hom geteken is om musiek en sang visueel voor te stel."
    },
    {
        "question_ref": "1.14",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Leesbegrip: Funksionaliteit van simbool (TEKS B)",
        "passage": TEKS_B,
        "question": "Is die hartjie saam met die woorde op die sanger se hemp funksioneel om die spotprent te verstaan? Motiveer jou antwoord.",
        "memo": "* $\\checkmark$ **Ja:** Die hartjie op die sanger se hemp simboliseer sy liefde vir Afrikaans/Afrikaanse musiek en verklaar waarom hy juis Afrikaanse liedjies sing.\n**OF**\n* $\\checkmark$ **Nee:** 'Afrikaans' kan bloot na die taal verwys, en selfs sonder die hartjie maak die lirieke in die spraakborrel dit duidelik dat hy Afrikaanse musiek sing.\n*(Enige EEN gemotiveerde antwoord vir 1 punt)*",
        "final_answer": "Ja, dit is funksioneel omdat die hartjie op sy hemp sy liefde en passie vir Afrikaans en Afrikaanse musiek beklemtoon en duidelik maak waarom hy die liedjie sing."
    },
    {
        "question_ref": "1.15",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Leesbegrip: Sintese van TEKS A en TEKS B",
        "passage": TEKS_AB,
        "question": "Die woorde van die liedjie in TEKS B hou verband met van die kritiek wat in paragraaf 1 van TEKS A genoem is. Bewys die korrektheid van hierdie stelling.",
        "memo": "* $\\checkmark$ Die lirieke in TEKS B ('Jou oë is so blou, my baby, jou soene is so flou, my lovie ...') is 'n tipiese voorbeeld van die herhalende, niksseggende en ligsinnige lirieke waaroor liedjieskrywers in paragraaf 1 geroskam word.",
        "final_answer": "In TEKS B sing die karakter oppervlakkige en ligsinnige rymwoorde ('blou/flou', 'baby/lovie'), wat presies ooreenstem met die kritiek in paragraaf 1 van TEKS A waar liedjieskrywers gekritiseer word oor 'herhalende, niksseggende en ligsinnige lirieke'."
    },
    {
        "question_ref": "1.16",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Leesbegrip: Woordverband tussen TEKS A en TEKS B",
        "passage": TEKS_AB,
        "question": "Met watter woord in paragraaf 5 van TEKS A hou SPRAAKBORREL 2 van TEKS B verband?",
        "memo": "* $\\checkmark$ \"hekwagters\" / \"poësie\" / \"kritiek\"",
        "final_answer": "\"hekwagters\" (of \"poësie\")"
    },

    # AFDELING B: OPSOMMING (10 punte)
    {
        "question_ref": "2",
        "marks": 10,
        "kind": "question",
        "topic": "Opsomming: Olifantgedrag (TEKS C)",
        "passage": TEKS_C,
        "question": "Lees die teks hieronder en maak 'n opsomming van SEWE voorbeelde van olifantgedrag wat die skrywer waargeneem het.\n\n**LET WEL:**\n1. Jou opsomming moet in jou eie woorde (in volsinne) in paragraafvorm aangebied word en mag nie meer as 90 woorde beslaan nie.\n2. Jy moet EEN samehangende paragraaf skryf.\n3. Dit is nie nodig om vir die opsomming 'n titel te gee nie.\n4. Dui die getal woorde aan wat jy vir die opsomming gebruik het.",
        "memo": "**Nasien van die opsomming:**\n* Punte word soos volg toegeken:\n  * 7 punte vir 7 feite (1 punt vir elke feit)\n  * 3 punte vir taal\n  * Puntetotaal: 10\n* Verspreiding van punte vir taal wanneer die kandidaat nie woordeliks aangehaal het nie:\n  * 1–3 feite korrek: ken 1 punt toe\n  * 4–5 feite korrek: ken 2 punte toe\n  * 6–7 feite korrek: ken 3 punte toe\n* Verspreiding van punte vir taal wanneer kandidaat woordeliks aangehaal het:\n  * 1–5 direkte aanhalings: ken 1 punt vir taal toe\n  * 6–7 direkte aanhalings: ken geen punte vir taal toe nie\n* Woordtelling: Maksimum 90 woorde. Lees tot by die laaste sin waarin die getal woorde oorskry word en ignoreer die res.\n\n**Feite-tabel (enige 7 van die volgende feite):**\n* $\\checkmark$ Feit 1: Olifante openbaar 'n humorsin as hulle met hulle slurpe waterkanon-waterkanon speel.\n* $\\checkmark$ Feit 2: Hulle rol in modderpoele om te verhoed dat hulle velle uitdroog.\n* $\\checkmark$ Feit 3: Olifante kommunikeer vindingryk deur hulle ore te flap as 'n teken dat gevaar dreig.\n* $\\checkmark$ Feit 4: Hulle organiseer hulleself om een volwasse koei om 'n basiese familiegroep te vorm.\n* $\\checkmark$ Feit 5: Die leierolifant en haar kalwers word toegelaat om altyd eerste te eet en te drink.\n* $\\checkmark$ Feit 6: 'n Olifantkoei aanvaar geredelik 'n kalf van 'n ander koei as haar eie wanneer nodig.\n* $\\checkmark$ Feit 7: Olifante speel met 'n sorgvrye uitgelatenheid nes mensekinders.",
        "final_answer": "Olifante openbaar 'n humorsin wanneer hulle met hul slurpe waterspeletjies speel. Om hul vel teen uitdroging te beskerm, rol hulle in modderpoele. Hulle kommunikeer vindingryk deur hul ore te flap wanneer gevaar dreig. Binne die trop organiseer olifante 'n vaste gesin om 'n volwasse koei, waar die leierkoei en haar kalfies eerste mag eet en drink. Verder aanvaar 'n koei geredelik 'n ander se kalf as haar eie. Laastens baljaar hierdie diere met 'n sorgvrye uitgelatenheid soos mensekinders.\n\n[78 woorde]"
    },

    # AFDELING C: TAALSTRUKTURE EN -KONVENSIES (30 punte)
    # VRAAG 3: ADVERTENSIE (TEKS D) - 10 punte
    {
        "question_ref": "3.1",
        "marks": 2,
        "kind": "passage_questions",
        "topic": "Taalstrukture en -konvensies: Verkleiningsvorm en stam (Advertensie)",
        "passage": TEKS_D,
        "question": "Gebruik die verkleiningsvorm van die onderstreepte woord (reël 1) in 'n sin van jou eie. Skryf dan die basisvorm/stam van hierdie woord neer.",
        "memo": "* $\\checkmark$ 'n Korrek gekonstrueerde sin met die korrek gespelde verkleiningsvorm \"veranderinkie\" (bv. Oorweeg 'n veranderinkie in jou studiemetodes).\n* $\\checkmark$ Basisvorm/stam: **ander**",
        "final_answer": "Voorbeeldsin: Selfs net 'n klein veranderinkie aan jou studieroetine kan wondere vir jou punte verrig.\nBasisvorm/stam: ander"
    },
    {
        "question_ref": "3.2",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Taalstrukture en -konvensies: Sterk verlede deelwoord (Advertensie)",
        "passage": TEKS_D,
        "question": "Gebruik die onderstreepte woord in reël 2 as 'n sterk verlede deelwoord in 'n verklarende sin.",
        "memo": "* $\\checkmark$ 'n Verklarende sin met die sterk verlede deelwoord \"gekose\" of \"verkose\" (bv. Die gekose komitee doen goeie werk. / Die verkose lede vergader vandag).",
        "final_answer": "Die nuut verkose leiersvergadering begin stiptelik om agtuur."
    },
    {
        "question_ref": "3.3",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Taalstrukture en -konvensies: Aanvoegende wyse (Advertensie)",
        "passage": TEKS_D,
        "question": "Herskryf reël 5 en 6 in die aanvoegende wyse.",
        "memo": "* $\\checkmark$ Ons interaktiewe lesse mag moontlik/dalk/miskien/heel waarskynlik klaskameronderrig vergemaklik. / Ons interaktiewe lesse kan (moontlik) klaskameronderrig vergemaklik. / Ons interaktiewe lesse sal moontlik/miskien klaskameronderrig vergemaklik. / Ons interaktiewe lesse behoort klaskameronderrig te vergemaklik. / As interaktiewe lesse tog maar klaskameronderrig sal vergemaklik.",
        "final_answer": "Ons interaktiewe lesse mag moontlik klaskameronderrig vergemaklik."
    },
    {
        "question_ref": "3.4",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Taalstrukture en -konvensies: Pleonasme (Advertensie)",
        "passage": TEKS_D,
        "question": "Verbeter die pleonasme deur reël 7 en 8 korrek oor te skryf.",
        "memo": "* $\\checkmark$ Tutors sal verseker dat jy jou kennis uitbrei. / Tutors sal verseker dat jy jou kennis verbeter.\n*(Die oorbodige woord 'verder' moet weggelaat word.)*",
        "final_answer": "Tutors sal verseker dat jy jou kennis uitbrei."
    },
    {
        "question_ref": "3.5",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Taalstrukture en -konvensies: Oorredende taal (Advertensie)",
        "passage": TEKS_D,
        "question": "Skryf die oorredende taal wat in reëls 9 tot 11 voorkom, neer.",
        "memo": "* $\\checkmark$ \"dié top\" (leermetode) / \"dié (top) leermetode\"\n*(Die akuut moet korrek op die woord 'dié' aangedui word.)*",
        "final_answer": "dié top (leermetode)"
    },
    {
        "question_ref": "3.6",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Taalstrukture en -konvensies: Feit of mening (Advertensie)",
        "passage": TEKS_D,
        "question": "Is die stelling in reëls 9 tot 11 'n feit of 'n mening? Motiveer jou antwoord.",
        "memo": "* $\\checkmark$ **Feit:** Die stelling word deur die asterisk aan die onderkant van die advertensie bevestig met 'n verwysing na die amptelike toekenning (Via Africa-toekennings 2006‒2017) wat aan die instansie toegeken is.",
        "final_answer": "Dit is 'n feit, want die toekenning word onderaan met 'n asterisk as die amptelike 'Via Africa-toekennings 2006‒2017' gestaaf."
    },
    {
        "question_ref": "3.7",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Taalstrukture en -konvensies: Lydende vorm (Advertensie)",
        "passage": TEKS_D,
        "question": "Herskryf die sin in reëls 12 tot 14 in die lydende (passiewe) vorm.",
        "memo": "* $\\checkmark$ Piet moet/kan vir meer inligting en vir spesiale aanbiedings gekontak word. / Vir meer inligting en spesiale aanbiedings moet Piet gekontak word. / Piet moet/kan gekontak word vir meer inligting en spesiale aanbiedings.",
        "final_answer": "Piet moet vir meer inligting en vir spesiale aanbiedings gekontak word."
    },
    {
        "question_ref": "3.8",
        "marks": 2,
        "kind": "passage_questions",
        "topic": "Taalstrukture en -konvensies: Teikenleser en oortuiging (Advertensie)",
        "passage": TEKS_D,
        "question": "Adverteerders fokus op 'n spesifieke teikenleser.\n\nWie is die teikenleser wat die adverteerder met hierdie advertensie wil bereik? Slaag die advertensie daarin om die teikenleser te oortuig om te reageer? Motiveer jou antwoord.",
        "memo": "Teikenleser (1 punt):\n* $\\checkmark$ Leerders (in graad 4–12) wat ekstra klasse in Afrikaans Huistaal wil neem / benodig / Ouers wat hulp soek vir hul kinders met Afrikaans Huistaal / Ouers van Laerskool Piet du Plooy / Onderwysers wat interaktiewe rekenaarlesse benodig.\n\nOortuigingskrag (1 punt):\n* $\\checkmark$ **Ja:** Kontakinligting is duidelik en prominent geplaas; die advertensie gebruik oorredende woorde ('dié top leermetode'); die toekennings bevestig gehalte; en die belofte van 'spesiale aanbiedings' en 'persoonlike aandag' spoor die leser aan om op te tree.\n*(Die kandidaat kan nie NEE as antwoord aanbied nie.)*",
        "final_answer": "Teikenleser: Leerders in graad 4 tot 12 wat addisionele leiding en lesse in Afrikaans Huistaal verlang (of hul ouers).\nOortuiging: Ja, die advertensie slaag daarin omdat dit duidelike kontakinligting verskaf, amptelike toekennings as bewys van sukses aanbied, en die voordeel van spesiale aanbiedings en persoonlike aandag beklemtoon."
    },

    # VRAAG 4: STROKIESPRENT (TEKS E) - 10 punte
    {
        "question_ref": "4.1",
        "marks": 2,
        "kind": "passage_questions",
        "topic": "Taalstrukture en -konvensies: Klankverspringing en idiomatiese betekenis (Strokiesprent)",
        "passage": TEKS_E,
        "question": "Skryf 'n woord in RAAMPIE 1 neer waarin klankverspringing/metatesis voorkom. Wat impliseer Jerome met die onderstreepte uitdrukking in hierdie raampie?",
        "memo": "* $\\checkmark$ **truksvy** (klankverspringing van 'turksvy').\n* $\\checkmark$ Jerome impliseer dat hy in 'n moeilike situasie / 'n tameletjie / 'n penarie sit omdat hy nie sy ma se motor kan leen soos hy beplan het nie.",
        "final_answer": "Woord met klankverspringing: truksvy\nImplikasie van 'sit met 'n truksvy': Jerome sit in 'n moeilike penarie of verknorsing omdat sy ma nie haar motor vir hom wil leen nie."
    },
    {
        "question_ref": "4.2",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Taalstrukture en -konvensies: Vooroordeel (Strokiesprent)",
        "passage": TEKS_E,
        "question": "\"Ek het jou gesê alle oumense is moeilik oor hulle karre!\" (RAAMPIE 1)\n\nStem jy saam dat Jerome hier bevooroordeeld is? Motiveer jou antwoord.",
        "memo": "* $\\checkmark$ **Ja:** Jerome veralgemeen onregverdig deur te sê dat 'alle' ouer mense moeilik is oor hulle voertuie, bloot omdat sy ma geweier het om haar motor aan hom te leen.\n**OF**\n* $\\checkmark$ **Nee:** Hy praat uit sy eie persoonlike ervaring met sy ma en ander volwassenes wat baie beskermend oor hulle besittings is.\n*(Enige EEN gemotiveerde antwoord vir 1 punt)*",
        "final_answer": "Ja, hy is bevooroordeeld omdat hy veralgemeen deur die woord 'alle' te gebruik en daarmee aanneem dat elke ouer mens sonder uitsondering moeilik oor motors is."
    },
    {
        "question_ref": "4.3",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Taalstrukture en -konvensies: Anglisisme (Strokiesprent)",
        "passage": TEKS_E,
        "question": "Verbeter die anglisisme deur die onderstreepte sin in RAAMPIE 2 te herskryf.",
        "memo": "* $\\checkmark$ Ek kom laai jou op vir 'n koffietjie. / Ek kom haal jou vir 'n koffietjie. / Ek kom haal jou om koffie te gaan drink. / Ek laai jou op om koffie te gaan drink. / Ek skiet jou vir 'n koffie. / Ek stiek jou vir 'n koffie.\n*(Die letterlike vertaling 'ek tel jou op' moet gekorrigeer word.)*",
        "final_answer": "Dis nie 'n probleem nie, Jerome, ek kom haal jou vir 'n koffietjie."
    },
    {
        "question_ref": "4.4",
        "marks": 2,
        "kind": "passage_questions",
        "topic": "Taalstrukture en -konvensies: Voegwoorde en betekenisfunksie (Strokiesprent)",
        "passage": TEKS_E,
        "question": "Verbind die onderstreepte sinne in RAAMPIE 3 en 4 met die voegwoord omdat. Watter betekenisfunksie het dié voegwoord in hierdie saamgestelde sin?",
        "memo": "* $\\checkmark$ Jy klink anders omdat dit jou stem laat eggo. / Omdat dit jou stem laat eggo, klink jy anders.\n* $\\checkmark$ Betekenisfunksie: Dit dui 'n rede / oorsaak aan (dit verduidelik die rede waarom Ravi se stem anders klink).",
        "final_answer": "Samestelling: Ravi, jy klink anders omdat dit jou stem laat eggo.\nBetekenisfunksie: Die voegwoord 'omdat' druk 'n rede of oorsaak uit."
    },
    {
        "question_ref": "4.5",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Taalstrukture en -konvensies: Spellingsreëls (Strokiesprent)",
        "passage": TEKS_E,
        "question": "Waarom is dit noodsaaklik dat \"eggo\" (RAAMPIE 4) met 'n dubbelkonsonant geskryf word?",
        "memo": "* $\\checkmark$ Die kort, beklemtoonde vokaal vereis 'n verdubbeling van die daaropvolgende konsonant sodat die uitspraak kort bly / As een 'g' weggelaat word, sal dit lei tot 'n betekenisverskil ('ego' beteken selfbeeld/eiewaan).",
        "final_answer": "Die kort, beklemtoonde vokaal vereis 'n dubbelkonsonant sodat die uitspraak kort bly; met slegs een 'g' verander die woord en betekenis na 'ego' (selfbeeld)."
    },
    {
        "question_ref": "4.6",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Taalstrukture en -konvensies: Skeibare werkwoord (Strokiesprent)",
        "passage": TEKS_E,
        "question": "Gebruik die onderstreepte werkwoord in RAAMPIE 6 as 'n skeibare werkwoord in 'n verduidelikende sin.",
        "memo": "* $\\checkmark$ Die seun soek altyd skoor met sy ma. / Hy het gister met die buurman skoorgesoek.\n*(Die werkwoord 'skoorsoek' moet skeibaar gebruik word; 'n infinitiefvorm word nie aanvaar nie.)*",
        "final_answer": "Jerome soek gedurig skoor met almal wanneer dinge nie na sy sin verloop nie."
    },
    {
        "question_ref": "4.7",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Taalstrukture en -konvensies: Stereotipering (Strokiesprent)",
        "passage": TEKS_E,
        "question": "Hoe word seuns in RAAMPIE 7 gestereotipeer?",
        "memo": "* $\\checkmark$ Seuns word gestereotipeer as moeilikheidmakers wat altyd ondeund is en hulle ma's gedurig sorge, spanning en grys hare besorg.",
        "final_answer": "Seuns word gestereotipeer as moeilikheidmakers wat altyd ondeund is en hulle moeders sorge en grys hare besorg."
    },
    {
        "question_ref": "4.8",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Taalstrukture en -konvensies: Klinkerwisseling (Strokiesprent)",
        "passage": TEKS_E,
        "question": "Vorm 'n selfstandige naamwoord van die onderstreepte werkwoord in RAAMPIE 8 deur middel van klinkerwisseling.",
        "memo": "* $\\checkmark$ **genot**\n*(Van die werkwoord 'geniet' na die selfstandige naamwoord 'genot' deur klinkerwisseling / ablaut.)*",
        "final_answer": "genot"
    },

    # VRAAG 5: ARTIKEL (TEKS F) - 10 punte
    {
        "question_ref": "5.1",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Taalstrukture en -konvensies: Diftonge (Tydskrifartikel)",
        "passage": TEKS_F,
        "question": "Skryf die diftong wat in die titel voorkom neer.",
        "memo": "* $\\checkmark$ **oei** (in die woord 'goeie')\n*(Indien die hele woord neergeskryf word, moet die diftong onderstreep wees.)*",
        "final_answer": "oei"
    },
    {
        "question_ref": "5.2",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Taalstrukture en -konvensies: Morfologie en verbuiging (Tydskrifartikel)",
        "passage": TEKS_F,
        "question": "Wat is die funksie van die onderstreepte agtervoegsel in paragraaf 2?",
        "memo": "* $\\checkmark$ Dit verbuig die byvoeglike naamwoord (verbuigings-e) / Dit vorm 'n attributiewe byvoeglike naamwoord wat voor die selfstandige naamwoord staan.",
        "final_answer": "Dit verbuig die byvoeglike naamwoord om as 'n attributiewe byvoeglike naamwoord voor die selfstandige naamwoord te funksioneer."
    },
    {
        "question_ref": "5.3",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Taalstrukture en -konvensies: Gevoelstaal na neutrale taal (Tydskrifartikel)",
        "passage": TEKS_F,
        "question": "Verander die onderstreepte sin in paragraaf 2 van gevoelstaal na neutrale taal.",
        "memo": "* $\\checkmark$ Ek eet alles. / Ek eet álles.\n*(Die emosioneel gelaaide werkwoord 'verorber' word vervang deur die neutrale werkwoord 'eet'.)*",
        "final_answer": "Ek eet alles."
    },
    {
        "question_ref": "5.4",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Taalstrukture en -konvensies: Meervoudsvorming (Tydskrifartikel)",
        "passage": TEKS_F,
        "question": "Gee die meervoud van die onderstreepte woord in paragraaf 3.",
        "memo": "* $\\checkmark$ **eetgoed**\n*(Die woord moet korrek gespel word; 'eetgoed' is die meervoud van 'eetding'.)*",
        "final_answer": "eetgoed"
    },
    {
        "question_ref": "5.5",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Taalstrukture en -konvensies: Byvoeglike bysin (Tydskrifartikel)",
        "passage": TEKS_F,
        "question": "Skryf 'n byvoeglike bysin uit paragraaf 4 neer.",
        "memo": "* $\\checkmark$ ... wat nie ronde handjies het nie.\n*(Indien die kandidaat die hele sin oorskryf, moet die byvoeglike bysin onderstreep word.)*",
        "final_answer": "... wat nie ronde handjies het nie"
    },
    {
        "question_ref": "5.6",
        "marks": 2,
        "kind": "passage_questions",
        "topic": "Taalstrukture en -konvensies: Leestekens - kommagebruik (Tydskrifartikel)",
        "passage": TEKS_F,
        "question": "Gee die rede vir die gebruik van die komma in onderskeidelik paragraaf 5 en paragraaf 8.",
        "memo": "* $\\checkmark$ **Paragraaf 5:** Die komma skei twee gesegdes / twee werkwoorde wat tot verskillende gesegdes behoort ('deurgeloop het, rys').\n* $\\checkmark$ **Paragraaf 8:** Die komma word tussen die opnoem van 'n lys of reeks items geplaas ('raaskopparaffienstofie, 'n sakkie meel en...').",
        "final_answer": "Paragraaf 5: Die komma skei twee opeenvolgende werkwoorde/gesegdes wat tot afsonderlike sinsdele behoort.\nParagraaf 8: Die komma skei die items in 'n reeks of opnoeming van bestanddele en toerusting."
    },
    {
        "question_ref": "5.7",
        "marks": 2,
        "kind": "passage_questions",
        "topic": "Taalstrukture en -konvensies: Idiomatiese vs. denotatiewe taal (Tydskrifartikel)",
        "passage": TEKS_F,
        "question": "Wat is die funksie van die onderstreepte verbindingswoorde in paragraaf 6? Gebruik ook dié onderstreepte woorde denotatief in 'n sin van jou eie.",
        "memo": "Funksie (1 punt):\n* $\\checkmark$ Dit dui op veralgemening / dit beklemtoon dat die vetkoeke sonder uitsondering deurgaans veerlig is / dit wys dit is van toepassing op elke vetkoek.\n\nDenotatiewe sin (1 punt):\n* $\\checkmark$ 'n Sin waarin 'deur die bank' letterlik (fisies) gebruik word (bv. Ek loop deur die bank na die kitsbank toe. / Boor 'n gat deur die bank sodat ons die kabels kan koppel).",
        "final_answer": "Funksie: Dit dui op veralgemening en beklemtoon dat die vetkoeke sonder enige uitsondering almal veerlig is.\nDenotatiewe sin: Ons het vinnig deur die bank gestap om by die kitsbank aan die oorkant van die gebou geld te trek."
    },
    {
        "question_ref": "5.8",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Taalstrukture en -konvensies: Samestellings met bepaler en kern (Tydskrifartikel)",
        "passage": TEKS_F,
        "question": "Gebruik die bepaler van die onderstreepte woord in paragraaf 7 as die kern van jou eie samestelling.",
        "memo": "* $\\checkmark$ Enige korrek gespelde nuwe samestelling met 'wag' as kern (tweede deel van die samestelling), bv. buurtwag / nagwag / skoolwag / lyfwag / grenswag / brandwag / erewag.\n*(Die bepaler in 'wagwoord' is 'wag'.)*",
        "final_answer": "buurtwag (of nagwag / lyfwag)"
    }
]


def validate_katex(text):
    """Verify that all KaTeX dollar delimiters are properly closed."""
    # Find all inline math: $...$ but not $$...$$
    # Quick check: count of single $ must be even (excluding $$)
    # Replace $$ with placeholder
    t = text.replace("$$", "\x00")
    dollars = t.count("$")
    return dollars % 2 == 0


def generate():
    total_marks = 0
    all_items = []
    
    for item in ITEMS:
        ref = item["question_ref"]
        marks = item["marks"]
        total_marks += marks
        
        obj = {
            "item_id": f"{SOURCE_ID}-{ref}",
            "source_id": SOURCE_ID,
            "pair_source_id": MEMO_ID,
            "subject": SUBJECT,
            "grade": GRADE,
            "language": LANGUAGE,
            "track": TRACK,
            "kind": item["kind"],
            "question_ref": ref,
            "marks": marks,
            "topic": item["topic"],
            "passage": item["passage"],
            "question": item["question"],
            "memo": item["memo"],
            "final_answer": item["final_answer"],
            "needs_review": False,
            "licence": "DBE copyright - check terms",
            "attribution": "Department of Basic Education"
        }
        
        # Verify KaTeX
        for key in ["passage", "question", "memo", "final_answer"]:
            val = obj[key]
            if not validate_katex(val):
                raise ValueError(f"Unclosed KaTeX dollar in item {ref}, field {key}")
                
        all_items.append(obj)
        
    print(f"Total items generated: {len(all_items)}")
    print(f"Total marks calculated: {total_marks} (Expected: 70)")
    assert total_marks == 70, f"Mark mismatch: {total_marks} != 70"
    
    # Save to both target locations
    path1 = os.path.join("workspace", "items", "afrikaans_hl", f"{SOURCE_ID}.jsonl")
    path2 = os.path.join("workspace", "items", f"{SOURCE_ID}.jsonl")
    
    os.makedirs(os.path.dirname(path1), exist_ok=True)
    os.makedirs(os.path.dirname(path2), exist_ok=True)
    
    with open(path1, "w", encoding="utf-8") as f1, open(path2, "w", encoding="utf-8") as f2:
        for obj in all_items:
            line = json.dumps(obj, ensure_ascii=False) + "\n"
            f1.write(line)
            f2.write(line)
            
    print(f"Successfully written to:\n  {path1}\n  {path2}")


if __name__ == "__main__":
    generate()
