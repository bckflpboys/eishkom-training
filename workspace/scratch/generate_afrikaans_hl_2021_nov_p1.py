import json
import os
import re

SOURCE_ID = "dbe-afrikaans_hl-g12-p1-2021-nov"
PAIR_SOURCE_ID = "dbe-afrikaans_hl-g12-p1-2021-nov-memo"
SUBJECT = "afrikaans_hl"
GRADE = 12
LANGUAGE = "af"
TRACK = "languages_hl"

# --- PASSAGES ---

PASSAGE_Q1 = """### TEKS A: ARTIKEL

**BANG VIR VERANDERING?**  
*Susan Goosen*

1. Elke jaar bring verandering. En ewe onvermydelik 'n vrees by sommige mense daarvoor. Trouens, vir baie mense bring verandering 'n soort angs mee wat hulle verlam. Nie alle mense is noodwendig intelligent genoeg en emosioneel gereed vir verandering nie, en daarom ook nie vir die aanpassings wat daarmee gepaard gaan nie.

2. Intelligensiekwosiënt (IK) en sy eweknie, emosionele kwosiënt (EK), word wyd as belangrike aanwysers vir suksesvolle aanpassing ná verandering erken. Albei verwys na 'n natuurlike intellektuele aanleg, boekekennis én mensekennis wat saam met mense-ervaring 'n rol speel in hoe iemand die uitdagings wat verandering en aanpassing meebring, gaan aanpak.

3. Wanneer die winde van verandering jou lewensbootjie omkeer, is daar dikwels net een van die twee moontlikhede: sink of swem. Daarom beklemtoon kenners deesdae ook die belangrikheid van 'n sogenaamde aanpasbaarheidskwosiënt (AK). Laasgenoemde verwys na jou vermoë om by nuwe situasies wat verandering meegebring het, aan te pas. Dit is 'n onderwerp waaroor min inligting beskikbaar is en daarom word dit met toenemende erns nagevors.

4. Oor die konsep van die belangrikheid van 'n AK, sê Lynette Beer, 'n lewensafrigter* van onder andere maatskappydirekteure in Pretoria: "Maatskappydirekteure stel deesdae al minder in mense se kwalifikasies belang, maar meer in hulle AK's. Tydens werksonderhoude is beroepsondervinding deesdae minder belangrik as die vermoë om potensiële probleemsituasies op te los. Daarom word vrae soos: 'Hoe sal jy die volgende situasie hanteer?' of 'Wat as die volgende gebeur?' gevra om vas te stel of jy opgewasse sal wees vir die uitdagings wat voortdurende verandering bring. Ou oplossings werk nie meer vir moderne probleme nie. En 'n onderneming wat nie by verandering kan bybly nie, gaan nie oorleef nie."

5. Lynette Beer sê voorts ook die volgende oor die aanpassings wat verandering meebring: <u>"Ons moet buite die boks dink."</u> Ter wille van oorlewing, ja, maar ook sodat ons ons gesinslede kan begelei en ondersteun. Die statistiek rakende veral depressie en ook stres, verslawing en trauma maak dit noodsaaklik om aanpassingsvaardighede aan te leer, tot voordeel van jouself en jou gesin. Persoonlike groei gaan hand aan hand met verandering én die aanpassings wat jy moet maak. Terselfdertyd kry 'n mens die onderskeidingsvermoë om te weet wanneer verandering dalk nié die antwoord is nie, of nié tot ons voordeel sal wees nie.

6. 'n Mens se AK help jou dus nie net tydens verandering om te oorleef nie, maar ook om te groei en te gedy, veral in tye wanneer groot veranderinge noodwendig drastiese aanpassings meebring.

7. Lynette Beer gee ook wenke aan diegene wat bang is dat hulle nie die uitdagings van verandering gaan oorleef nie en daarom hulle aanpassingsvaardighede wil inoefen: "Erken dat verandering normaal en dikwels nodig is. Neem vervolgens eienaarskap van die veranderingsproses. Stel dan 'n uitvoerbare aksieplan op. Gee laastens erkenning aan jou suksesse en persoonlike groei deur jouself op die skouer te klop."

8. Ngobezi Dwada, 'n maatskaplike werker en berader, sê ook dat grootskaalse veranderinge heelwat ingrypende aanpassings kan verg – veral in stresvolle werksomgewings wat voortdurend vars denkrigtings vereis. <u>As werknemers egter voorbereid is hierop,</u> kan hierdie veranderinge dan uiteindelik opwindend wees. "Daarom behoort die hooffokus tydens werksonderhoude júis te wees om te bepaal of die aansoeker oor die regte kwalifikasies beskik wat hom/haar in staat sal stel om probleemoplossend te dink. Maar ongelukkig reageer veral ouer mense nie goed wanneer hulle aanpassings in die gesig moet staar nie – dít as gevolg van 'n ingeboude weerstand teen verandering. En dit is veral ouer mense wat ongemaklik met die onbekende is. Dít maak dan aanpassings by veranderde omstandighede vir hulle dikwels vreesaanjaend. Hulle is dikwels bang dat hulle nie die vermoë of die vaardighede meer het om nuwe of veranderde situasies te kan hanteer nie."

9. Dr. Ike Gentleman, 'n lektor in bedryfsielkunde, wys egter in hierdie verband daarop dat daar wél mense is wat oor 'n ingebore aanpasbaarheid beskik en daarom beter op nuwe of veranderde situasies reageer. "Navorsers reken dat hierdie mense suksesvol is omdat hulle in die 'nou' lewe, en weet hoe om hulself aan die vloei van die lewe oor te gee. Hulle hanteer die stres van verandering en aanpassing makliker."

10. Dr. Gentleman verduidelik verder dat temperament, persoonlikheid, vaardigheid en voorkeure alles 'n rol speel by hoe aanpasbaar 'n persoon kan wees. "Aanvaar dat die lewe verrassings en eiesoortige uitdagings gaan meebring. Hierdie uitdagings kan uiteindelik daartoe bydra om jou menswees te slyp en te ontwikkel. Sodra ons hierdie vlak van aanvaarding bereik, kan ons veel makliker met nuwe situasies werk én aanbeweeg. Ons het moontlik nie altyd beheer oor wat om ons gebeur nie, maar ons kan wel ons reaksies daarop beheer."

11. Die geleerdes is dit dus eens: veranderinge in die lewe kan nie vermy word nie, maar hóé jy dit gaan hanteer, dís die groot geheim vir 'n suksesvolle lewe.

*\*lewensafrigter* – 'n persoon wie se werk dit is om die lewensgehalte van sy/haar kliënte te verbeter deur aan hulle loopbaanadvies te gee; ook om sy/haar kliënte met die aanpassing in nuwe situasies by te staan. Gee raad aan diegene in bestuursposisies oor aanstellings van personeel.  
*[Verwerk uit Lig, Desember 2019/Januarie 2020]*

---

### TEKS B: SPOTPRENT

[Visuele beskrywing van spotprent deur Fred Mouton]:
- **Agtergrond & Toneel:** 'n Buitelug-restaurantterras onder 'n gestreepte sonskerm (afdak). In die agtergrond sit ander restaurantgaste by tafels en eet en gesels; 'n figuur op 'n bromponie ry in die straat verby.
- **Teksblok A (links bo):**
  "'n Nuwe toep bied gebruikers die geleentheid om gratis te eet en selfs in stede soos Kaapstad, New York en Milaan gratis by gimnasiums te oefen. Daar is net één voorwaarde: jy móét 'n model wees!"
- **Voorgrond:** 'n Swaar oorgewig man met 'n ruie baard sit agteroor geleun op 'n klein stoeltjie by 'n ronde etenstafel. Hy dra 'n moulose frokkie (tank top), kortbroek en sandale. Sy reuse boepens peul heeltemal kaal uit oor sy kortbroek. In sy linkerhand hou hy 'n spyskaart vas waarop in groot letters "SPYSKAART" geskryf staan.
- **Kelner:** Agter die tafel staan 'n kelner met 'n wit voorskoot en 'n skinkbord met 'n sout-en-peperstel/kruiehouer. Hy kyk skepties, stuurs en met 'n uitdrukkinglose blik af na die slordige man.
- **Spraakborrel B (man aan kelner):**
  "Maar ek is 'n model ... As my baard jou pla – dis vir 'n advertensie. Ons sal jou ook kan gebruik. Werk net aan jou glimlag."
- **Spraakborrel C (regs onder):** 'n Klein muisie sit op die vloer langs die stoelpoot, kyk op na die man en dink/sê in 'n getande gedagte-/spraakborreltjie:
  "Ag nee ... regtig. Hy kon darem 'n langbroek aangetrek het."
- **Bronverwysing:** [Uit: Die Burger, 31 Januarie 2019]"""

PASSAGE_Q2 = """### TEKS C: ARTIKEL

**'N GELUKKIGER, STRESVRYE JY**

Het jy geweet dat jou liggaam natuurlike goedvoelchemikalieë bevat? Een hiervan is serotonien, 'n breinoordragstof wat jou kalm en gelukkig laat voel. Jy kan jou serotonienvlakke 'n hupstoot gee wanneer jy bietjie gespanne voel.

Jy het net 15 minute se oefening per dag nodig. Oefening help nie net met gewigsbeheer nie, maar ook om hartkwale te voorkom en stresvlakke te verlaag. Oefen dus gereeld om jou stresvlakke laag te hou. Maar oefening alleen is nie genoeg vir die mens se rustige gemoed nie! Doen elke dag iets lekker soos om byvoorbeeld 'n boek te lees. Dit hou serotonienvlakke in stand.

Jy ken mos daardie warm, gelukkige gevoel nadat jy heerlik geëet het? Dit is omdat sekere kossoorte jou brein se chemiese samestelling beïnvloed. Eet kossoorte wat jou later ontspanne sal laat voel. Hou egter in gedagte dat suiker, alkohol en kaffeïen jou serotonienvlakke 'n vinnige hupstoot gee. Wanneer jy te gereeld hiervan inneem, laat dit jou gespanne voel. Vermy ook die oormatige inname van hoë suiker- en kaffeïendrankies in 'n poging om jou stresvlakke normaal te hou.

Sorg dat jy 'n behoorlike nagrus inkry, want niks werk so goed om stres vaarwel te roep nie. Jou slaapkamer is die plek waar jy goeie nagrus moet kry. Slaap help beslis, maar as jy nie kwaliteitslaap inkry nie, staan jy dikwels meer gespanne op as wat jy aanvanklik was. Dit help nie jy slaap vir ure aaneen met 'n brein wat nog nie afgeskakel is nie.

Oggendsonlig stimuleer die produksie van goedvoelhormone. Verwerk stres met behulp van UV-strale. Stel jou aan soveel moontlik van die oggendsonlig se UV-strale bloot, want jou gemoedstoestand is soggens meer vatbaar vir die helende invloed van sonstrale. Jy hoef dus nie vir ure onder skadelike UV-strale te lê en sonbak nie.

Masserings is 'n algemene behandeling vir mense wat onder spanning verkeer. Onlangse navorsing deur die Universiteit van Miami se mediese skool wys dat 'n masseringsessie jou serotonienvlakke met 28% kan laat verhoog en kortisol (die streshormoon) met 21% laat verlaag. Besoek gereeld 'n masseur om die stram spiertjies uit te stryk sodat jy stresvry jou dagtaak kan aanpak.

Hoop jy weet nou hoe om van spanning ontslae te raak om met 'n huppel in jou stap die lewe aan te pak.

*[Verwerk uit Die Burger Naweek, 15 November 2019]*"""

PASSAGE_Q3 = """### TEKS D: ADVERTENSIE

[Reël 1] KOM IN DIE
[Reël 2] EILANDGEES
[Reël 3] Tropika gee jou 'n voorsmaak van die lekker lewe – proe dit self.
[Reël 4] Ontsnap na 'n eksotiese eilandlewe waar jy luilekker op die strand kan lê en
[Reël 5] luister hoe die branders breek.
[Reël 6] Min dinge klop daardie eilandgevoel, maar Tropika gee jou 'n proesel van die
[Reël 7] goeie lewe met sy verskeidenheid lipleklekker geure. Ontspan terwyl jy stadig
[Reël 8] <u>teug</u> aan die strelende smaak van Tropika.
[Visuele foto: 'n Tropiese strandtoneel met spierwit sand, palmtakke aan die regterkant, 'n kalm turkoois see waarin twee tradisionele langstertbote dryf. Op die sand in die voorgrond staan 'n reiskoffer met 'n sonhoed en sonbril daarop, 'n paar plakkies, 'n glasie met 'n strooitjie, en 'n kartonhouer Tropika Mango-Peach sap langs 'n oop klapperneutdrankie met 'n strooitjie.]
[Reël 9] **Wat is jou gunsteling?** Kies: mango-perske, lemoen, pynappel, Cool Red en
[Reël 10] nou – vir die heel lekkerste eilandgevoel – die nuwe Pina Colada.
[Reël 11] **Tropika** sê: "Slegs fynproewers drink hierdie verfrissende drankie – enige
[Reël 12] plek, enige tyd – om hulle saai lewens op te kikker."

[Visuele en tipografiese besonderhede:
- Reël 1 ("KOM IN DIE") verskyn in skuinsgedrukte seriftipe in hoofletters binne 'n grys reghoekige balk bo-aan.
- Reël 2 ("EILANDGEES") verskyn in reuse, wit 3D-skadutipe met swart buitelyne wat golwend soos seebranders vertoon.
- Die handelsnaam "Tropika" in reël 3, 6, 8 en 11 is vetgedruk.
- Die woord "teug" in reël 8 is onderstreep.]

*[Verwerk uit Tuis, Augustus 2020]*"""

PASSAGE_Q4 = """### TEKS E: STROKIESPRENT

**DIE LEWE IS NIE ALTYD 'N LIED NIE ...**  
*Deur Ray Billingsly*

[Visuele en verbale beskrywing van die 5 panele (Curtis-strokiesprent):

- **RAAMPIE 1:**
  'n Meisie met 'n brilletjie en donker hare wat in twee poniestertjies vasgemaak is, stap van links nader na twee seuns wat langs mekaar op 'n muurtjie/bankie sit in skooluniforms (hemde en skooldasse).
  Spraakborrel van die meisie: "Heita, <u>tjommies</u>! Ek kan nie glo julle twee kon iets anders regkry as om net rugby te speel nie! Om 'n e-posboodskap te stuur ... Sjoe!"
  *(Nota: die woord 'tjommies' is onderstreep.)*

- **RAAMPIE 2:**
  Bokant die meisie se kop verskyn 'n denkborrel met 'n groot vraagteken ("?"). Sy kyk verbaas en skepties met geknypte oë na die seuns.
  Die seun in die middel (gemerk met pyltjie "A") en sy vriend regs gee mekaar 'n energieke high-five met 'n stervormige klankeffek "KLAP". Seun A het 'n breë, trotse, selfvoldane en leedvermakerige glimlag op sy gesig.

- **RAAMPIE 3:**
  Die twee seuns gesels met mekaar en ignoreer die meisie doelbewus. Die seuns is sentraal in die raampie geteken terwyl slegs die boonste gedeelte van die meisie se kop klein links onder in die hoekie sigbaar is; die seuns maak geen oogkontak met haar nie.
  Spraakborrel van Seun A: "Nou gaan sy seker weer sorg dat hierdie ou storietjie voor pouse die hele skoolterrein vol lê ... Gmpf!"

- **RAAMPIE 4:**
  Die meisie is woedend. Haar mond is wawyd oopgesper en haar oë/wenkbroue is vererg saamgetrek. Haar spraakborrel is getand, in vetgedrukte hoofletters en eindig op twee uitroeptekens:
  "JULLE TWEE MOET OPPAS WAT JULLE VAN MY SÊ. EK <u>ROER</u> JULLE SOMMER NOU-NOU!!"
  *(Nota: die woord 'ROER' is onderstreep.)*
  Die twee seuns deins verskrik en verslae agteroor.

- **RAAMPIE 5:**
  Die regterhandse seun reageer spottend op haar woorde met 'n glimlag en wys sy vinger:
  "Ek is oortuig daarvan dat jy dit nie gaan regkry nie – jy het dan nie eers 'n lepel by jou nie. Kan ons jou daarmee help?"
  Seun A (gemerk met pyltjie "A") sit nou heeltemal verslae en moedeloos met sy kop vooroor gebuig en sy hand teen sy voorkop/gesig in diepe verleentheid en skaamte oor sy maat se flou woordspeling.]

*[Verwerk uit https://www.comicskingdom.com]*"""

PASSAGE_Q5 = """### TEKS F: ARTIKEL

**TIMBUKTU SKEP**

1. <u>Vyftig</u> kinders se gesigte het van trots gestraal nadat hulle die reaksie op hul kunswerke gesien het. Honderde mense het ingestroom om na hul handewerk te kom kyk, vrae te vra en van die kleurryke skeppings te koop wat hulle op die Ndebele-kombers voor hul leersentrum uitgestal het. Die kinders was bly en verheug oor die reaksie.

2. Die eerste Sondag van die maand is <u>markdag</u> by Victoria Yards, die nuwe stedelike ontwikkeling oos van Johannesburg se middestad. Dan ry mense meer as veertig kilometer na dié deel van die stad om 'n dag van kuns en kultuur, organiese kos en vermaak te geniet.

3. Dit was die eerste keer dat die kinders van die leersentrum, *Timbuktu in the Valley*, hier 'n fondsinsameling vir hul skool gehou het met versierings wat hulle met hul eie hande gemaak het.

4. Die organisasie se skryfbehoeftevennoot; Staedler, het die Fimo-kunstenaar, Riaan Marais, na hierdie sentrum gebring. "Sjoe, en het hierdie kinders van die buurt dít nou baie geniet!" het Mia Sonnekus, woordvoerder van Staedler gister in 'n onderhoud gesê.

5. *Timbuktu in the Valley* is twee jaar gelede tydens 'n nasionale (5.5) <u>inisiatief</u> gestig. Die hoofdoel was om plaaslike sosio-ekonomiese uitdagings te help oorkom. Daar word gereeld werksessies oor onderwerpe soos tuinmaak, kunsvlyt, herwinning, drama, kosmaak en kleiwerk aangebied om die (5.6) **jongspan** aan verskillende beroepe bloot te stel.

6. Die fokus is om vir plaaslike jongmense, wat swaarkry, meer geleenthede in die lewe te bied deur hulle met die nodige vaardighede toe te rus om 'n onafhanklike lewe te lei. Dit was die noodsaaklikste ding wat by hierdie <u>gemeenskapsprojek</u> moes gebeur en sal hopelik suksesvol wees.

*[Verwerk uit Huisgenoot, 26 Desember 2019]*"""

# --- ITEMS DEFINITION ---

raw_items = [
    # AFDELING A: LEESBEGRIP (Vraag 1) - Total 30 marks
    {
        "question_ref": "1.1",
        "marks": 2,
        "kind": "passage_questions",
        "topic": "Leesbegrip: Artikel en Visuele Teks",
        "passage": PASSAGE_Q1,
        "question": "Sommige mense het volgens paragraaf 1 geen keuse as om met nuwe uitdagings en die vrees daarvoor saam te leef nie.\n\nSkryf TWEE redes neer waarom angs baie mense as't ware verlam wanneer hulle met verandering gekonfronteer word.",
        "memo": "* $\\checkmark$ Mense is nie intelligent genoeg nie.\n* $\\checkmark$ Hulle is emosioneel nie gereed nie.",
        "final_answer": "Mense is nie intelligent genoeg nie en hulle is emosioneel nie gereed vir verandering nie.",
    },
    {
        "question_ref": "1.2.1",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Leesbegrip: Artikel en Visuele Teks",
        "passage": PASSAGE_Q1,
        "question": "\"... wanneer die winde van verandering jou lewensbootjie omkeer ...\" (paragraaf 3)\n\nWat beteken dié uitdrukking binne die konteks waarin dit gebruik word?",
        "memo": "* $\\checkmark$ Verandering veroorsaak probleme / uitdagings in jou lewe / keer jou lewe onderstebo.",
        "final_answer": "Verandering bring onverwagte probleme of uitdagings wat jou lewe heeltemal onderstebo keer.",
    },
    {
        "question_ref": "1.2.2",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Leesbegrip: Artikel en Visuele Teks",
        "passage": PASSAGE_Q1,
        "question": "Gee EEN eie rede waarom aanpasbaarheid in dié situasie as 'n oplossing aanbeveel word.",
        "memo": "* $\\checkmark$ Aanpasbaarheid sal 'n mens help om uitdagings (suksesvol) die hoof te bied / met selfvertroue aan te pak / Dit sal jou ook help om suksesvol by nuwe/onbekende situasies aan te pas / om te swem.\n\n*(Die kandidaat bied enige soortgelyke antwoord vir EEN punt aan. Die antwoord kan ook aangebied word as: As jy nie aanpas nie, ...)*",
        "final_answer": "Aanpasbaarheid help 'n mens om nuwe situasies en uitdagings suksesvol te oorkom sodat jy nie ondergaan nie (om te swem in plaas van sink).",
    },
    {
        "question_ref": "1.2.3",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Leesbegrip: Artikel en Visuele Teks",
        "passage": PASSAGE_Q1,
        "question": "Waarom word daar met toenemende erns oor die onderwerp van mense se aanpasbaarheidskwosiënte navorsing gedoen?",
        "memo": "* $\\checkmark$ Daar is min inligting oor die aspek van AK's beskikbaar (en dus word daar met toenemende erns navorsing daaroor gedoen).",
        "final_answer": "Daar is tans nog baie min inligting oor aanpasbaarheidskwosiënte (AK's) beskikbaar.",
    },
    {
        "question_ref": "1.3",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Leesbegrip: Artikel en Visuele Teks",
        "passage": PASSAGE_Q1,
        "question": "Beoordeel die geloofwaardigheid van Lynette Beer se stelling in paragraaf 4 oor maatskappydirekteure. Gee 'n rede vir jou beoordeling.",
        "memo": "* $\\checkmark$ Haar stelling is geloofwaardig, want sy help maatskappydirekteure (wat sukkel om by veranderinge aan te pas) in haar beroep as lewensafrigter / Sy is 'n lewensafrigter van onder andere maatskappydirekteure.",
        "final_answer": "Haar stelling is geloofwaardig omdat sy self 'n lewensafrigter van maatskappydirekteure is en daarom eerstehandse kennis dra van wat hulle in werknemers soek.",
    },
    {
        "question_ref": "1.4",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Leesbegrip: Artikel en Visuele Teks",
        "passage": PASSAGE_Q1,
        "question": "Herlees reëls 17–21 van paragraaf 4.\n\nWatter implikasie hou dit nóú vir werkaansoekers in as die fokus van vrae tydens werksonderhoude verander het?",
        "memo": "* $\\checkmark$ Werkaansoekers sal anders vir onderhoude voorberei / hul vaardighede moet wysig / kwalifikasies op die lange baan/agtergrond skuif / op aanpasbaarheid/vermoë om probleme op te los, moet fokus / moet leer om op hul voete te dink tydens 'n onderhoudsituasie / aan te pas by die onderhoudsituasie.",
        "final_answer": "Werkaansoekers moet op hul aanpasbaarheid en probleemoplossingsvermoë fokus en leer om op hul voete te dink, eerder as om net op hul kwalifikasies of vorige ervaring staat te maak.",
    },
    {
        "question_ref": "1.5",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Leesbegrip: Artikel en Visuele Teks",
        "passage": PASSAGE_Q1,
        "question": "Haal 'n sin uit paragraaf 4 aan wat met die onderstreepte sin in paragraaf 5 verband hou.",
        "memo": "* $\\checkmark$ \"Ou oplossings werk nie meer vir moderne probleme nie.\"",
        "final_answer": "\"Ou oplossings werk nie meer vir moderne probleme nie.\"",
    },
    {
        "question_ref": "1.6",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Leesbegrip: Artikel en Visuele Teks",
        "passage": PASSAGE_Q1,
        "question": "Herlees paragraaf 5.\n\nLynette Beer noem die aspek van depressie eerste wanneer sy na statistiek verwys wat aanpassingsvaardighede noodsaaklik maak. Gee 'n moontlike rede hiervoor binne verband van die teks.",
        "memo": "* $\\checkmark$ Depressie is die nagevolg van mense wat sukkel om by verandering aan te pas / Depressie is die gevolg van angs/vrees/weerstand teen verandering / Depressie is 'n belangrike faktor in / beïnvloed iemand se aanpassingsvaardighede.",
        "final_answer": "Depressie is een van die ernstigste nagevolge wanneer mense deur vrees verlam word en nie by verandering kan aanpas nie.",
    },
    {
        "question_ref": "1.7",
        "marks": 4,
        "kind": "passage_questions",
        "topic": "Leesbegrip: Artikel en Visuele Teks",
        "passage": PASSAGE_Q1,
        "question": "Watter wenke gee Lynette Beer aan mense om hul AK in te oefen?",
        "memo": "* $\\checkmark$ Erken dat verandering normaal is (en dikwels nodig is).\n* $\\checkmark$ Neem vervolgens eienaarskap van die veranderingsproses.\n* $\\checkmark$ Stel dan 'n uitvoerbare aksieplan op.\n* $\\checkmark$ Gee laastens erkenning aan jou suksesse en persoonlike groei (deur jouself op die skouer te klop).\n\n*(Die kandidaat bied VIER antwoorde vir EEN punt elk aan.)*",
        "final_answer": "1. Erken dat verandering normaal en dikwels nodig is;\n2. Neem eienaarskap van die veranderingsproses;\n3. Stel 'n uitvoerbare aksieplan op;\n4. Gee erkenning aan jou suksesse en persoonlike groei deur jouself op die skouer te klop.",
    },
    {
        "question_ref": "1.8",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Leesbegrip: Artikel en Visuele Teks",
        "passage": PASSAGE_Q1,
        "question": "Herlees paragraaf 4 en 8.\n\nWatter verskil blyk uit dié onderskeie paragrawe t.o.v. dit wat werkgewers in ag behoort te neem wanneer hulle met iemand 'n werksonderhoud voer?",
        "memo": "* $\\checkmark$ Paragraaf 4 verwys na die feit dat maatskappydirekteure nie meer so baie belangstel in aansoekers se kwalifikasies nie / op die aanpasbaarheidskwosiënt/probleemoplossingsvaardighede fokus, terwyl paragraaf 8 daarop wys dat jy oor die regte kwalifikasies moet beskik / kwalifikasies nie as ondergeskik gesien moet word nie.\n\n*(Die kandidaat bied albei kante van die verskil vir EEN punt aan.)*",
        "final_answer": "In paragraaf 4 stel werkgewers minder belang in kwalifikasies en fokus eerder op aanpasbaarheid en probleemoplossing, terwyl paragraaf 8 sê die hooffokus behoort júís te wees om te bepaal of die aansoeker oor die regte kwalifikasies beskik.",
    },
    {
        "question_ref": "1.9",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Leesbegrip: Artikel en Visuele Teks",
        "passage": PASSAGE_Q1,
        "question": "Watter afleiding kan 'n leser uit die onderstreepte sinsdeel in paragraaf 8 t.o.v. werknemers se werksverrigting maak?",
        "memo": "* $\\checkmark$ Werknemers wat voorbereid is met vars denkrigtings, sal in \"nuwe\"/stresvolle werksomgewings floreer / veranderinge as opwindend ervaar / Werknemers wat onvoorbereid is, ervaar stres / is bang.",
        "final_answer": "Werknemers wat behoorlik voorbereid is op nuwe eise en vars denkrigtings handhaaf, sal suksesvol presteer en verandering as opwindend ervaar.",
    },
    {
        "question_ref": "1.10",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Leesbegrip: Artikel en Visuele Teks",
        "passage": PASSAGE_Q1,
        "question": "Ngobezi Dwada kan van vooroordeel beskuldig word. Verduidelik hierdie stelling.",
        "memo": "* $\\checkmark$ Ngobezi Dwada het 'n vooropgestelde idee dat veral ouer mense ongemaklik met die onbekende is / dat aanpassings by veranderde omstandighede vir hulle dikwels vreesaanjaend is / dat hulle dikwels bang is dat hulle nie die vermoë/vaardighede het om nuwe/vreemde situasies te kan hanteer nie / Nie alle ouer mense is ongemaklik met die onbekende nie.\n\n*(Die kandidaat bied enige soortgelyke antwoord vir EEN punt aan. Die kandidaat kan 'n positiewe of negatiewe vooroordeel in die antwoord aanbied.)*",
        "final_answer": "Sy veralgemeen bevooroordeeld dat ouer mense 'n ingeboude weerstand teen verandering het en bang is vir nuwe situasies, wat nie op alle ouer mense van toepassing is nie.",
    },
    {
        "question_ref": "1.11.1",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Leesbegrip: Artikel en Visuele Teks",
        "passage": PASSAGE_Q1,
        "question": "Dr. Ike Gentleman huldig in paragraaf 9 'n spesifieke siening t.o.v. mense se aanpasbaarheid.\n\nIn watter opsig verskil dr. Gentleman se siening t.o.v. verandering en aanpassing van dié van me. Dwada?",
        "memo": "* $\\checkmark$ Dr. Ike Gentleman sê dat aanpasbaarheid by veranderinge 'n ingebore karaktereienskap by mense is, terwyl me. Ngobezi Dwada sê dat (ouer) mense 'n ingeboude weerstand teen verandering het / Gentleman sê aanpasbaarheid is ingebore, terwyl me. Ngobezi Dwada sê jy moet voorberei word vir verandering.\n\n*(Die kandidaat bied albei kante van die verskil vir EEN punt aan.)*",
        "final_answer": "Dr. Gentleman meen aanpasbaarheid is 'n ingebore eienskap wat mense help om in die \"nou\" te leef, terwyl me. Dwada glo dat mense 'n ingeboude weerstand teen verandering het en vooraf voorberei moet word.",
    },
    {
        "question_ref": "1.11.2",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Leesbegrip: Artikel en Visuele Teks",
        "passage": PASSAGE_Q1,
        "question": "Waarom sou 'n leser eerder dr. Gentleman se siening as gesaghebbend beskou?",
        "memo": "* $\\checkmark$ Dr. Gentleman is 'n lektor (in Bedryfsielkunde) / baseer sy siening op grond van wat navorsers/navorsing daaroor bekend gemaak het / 'n kenner op hierdie gebied.",
        "final_answer": "Hy is 'n lektor in bedryfsielkunde en baseer sy siening op wetenskaplike navorsing.",
    },
    {
        "question_ref": "1.11.3",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Leesbegrip: Artikel en Visuele Teks",
        "passage": PASSAGE_Q1,
        "question": "Wat bedoel dr. Gentleman as hy sê dat mense weet hoe om hulself aan die vloei van die lewe oor te gee?",
        "memo": "* $\\checkmark$ Mense aanvaar dat die lewe verandering/aanpassings gaan meebring.",
        "final_answer": "Hulle aanvaar dat verandering deel van die lewe is en pas spontaan daarby aan sonder om daarteen te stry.",
    },
    {
        "question_ref": "1.12",
        "marks": 2,
        "kind": "passage_questions",
        "topic": "Leesbegrip: Artikel en Visuele Teks",
        "passage": PASSAGE_Q1,
        "question": "Verwys na dr. Ike Gentleman se stelling in paragraaf 10.\n\nWat gaan die gevolge wees wanneer 'n mens aanvaar dat die lewe vol verrassings is?",
        "memo": "* $\\checkmark$ Nuwe situasies sal nie meer vir 'n mens 'n bedreiging inhou nie / Jy sal met jou lewe kan voortgaan, ondanks die uitdagings wat nuwe situasies meebring / Jy sal jou reaksies op uitdagings beter kan beheer / Jy sal die stres van verandering en aanpassing maklik kan hanteer.\n* $\\checkmark$ Dit dra daartoe by dat jou menswees geslyp word / Jou menswees word ontwikkel.\n\n*(Die kandidaat bied TWEE soortgelyke antwoorde vir EEN punt elk aan.)*",
        "final_answer": "'n Mens kan baie makliker met nuwe situasies werk en aanbeweeg, en hierdie uitdagings help om jou menswees te slyp en te ontwikkel.",
    },
    {
        "question_ref": "1.13",
        "marks": 2,
        "kind": "passage_questions",
        "topic": "Leesbegrip: Spotprent",
        "passage": PASSAGE_Q1,
        "question": "Watter visuele inligting skep 'n restaurantagtergrond?",
        "memo": "* $\\checkmark$ Enige TWEE van:\n  * Kelners bedien mense.\n  * Mense sit by restauranttafels.\n  * Mense eet.\n  * Die man hou 'n spyskaart in sy hand.\n  * Daar is eetgerei/kos op die tafel.\n\n*(Die kandidaat bied enige TWEE soortgelyke antwoorde vir EEN punt elk aan.)*",
        "final_answer": "Mense sit en eet by tafels op die terras, 'n kelner bedien hulle met 'n skinkbord, en die man hou 'n spyskaart vas.",
    },
    {
        "question_ref": "1.14",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Leesbegrip: Spotprent",
        "passage": PASSAGE_Q1,
        "question": "Waarom dink jy is die gratis kos slegs op modelle van toepassing?",
        "memo": "* $\\checkmark$ Modelle eet gewoonlik nie baie nie / Die restaurante sal nie groot verliese ly om modelle gratis te laat eet nie / Modelle wat daar eet, sal 'n positiewe beeld vir die restaurant skep.\n\n*(Die kandidaat bied enige soortgelyke antwoord vir EEN punt aan.)*",
        "final_answer": "Modelle eet gewoonlik baie min en hul teenwoordigheid verskaf gratis publisiteit en 'n glansryke beeld vir die restaurant.",
    },
    {
        "question_ref": "1.15",
        "marks": 2,
        "kind": "passage_questions",
        "topic": "Leesbegrip: Spotprent",
        "passage": PASSAGE_Q1,
        "question": "Is die man se verwagting om gratis te eet en die kelner se houding onderskeidelik geregverdig? Motiveer jou antwoord deur na die man en die kelner te verwys.",
        "memo": "* $\\checkmark$ Man: **Ja** (Die man sê hy is 'n model / Hy hoef nie aan die standaardvereistes vir 'n model te voldoen om een te wees nie) OF **Nee** (Die man lyk na 'n kansvatter wat net gratis kos soek).\n* $\\checkmark$ Kelner: **Ja** (Die kelner tree professioneel op / wil net sy werk doen / is skepties dat die slordige man 'n model is) OF **Nee** (Die kelner behoort nie nors/stuurs/afsydig teenoor die klant op te tree nie).\n\n*(Die kandidaat bied enige soortgelyke antwoorde vir EEN punt elk aan. Die man se verwagting en die kelner se houding word onafhanklik geassesseer.)*",
        "final_answer": "Man: Nee, hy lyk na 'n kansvatter met 'n onversorgde voorkoms wat glad nie aan modelvereistes voldoen nie; Kelner: Ja, die kelner is met reg skepties omdat die slordige man nie soos 'n tipiese model lyk nie.",
    },
    {
        "question_ref": "1.16",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Leesbegrip: Spotprent",
        "passage": PASSAGE_Q1,
        "question": "Lei die funksie van die beletselteken/ellips in SPRAAKBORREL B binne konteks van die spotprent af.",
        "memo": "* $\\checkmark$ Dit vestig die leser se aandag op die dramatiese verduideliking wat gaan volg oor waarom die man homself as 'n model sien / Dit laat die voorafgaande stelling insink / Tydsverloop waarin hy die kelner van die egtheid van sy woorde wil oortuig / Bou spanning/afwagting terwyl die man aan 'n idee dink om die kelner te oortuig / Kelner wil man nie glo nie; dus moes die man ná die ellips uitbrei / Soek woorde om sy voorkoms te regverdig dat hy 'n gratis maaltyd kan kry.\n\n*(Die antwoord moet binne konteks aangebied word.)*",
        "final_answer": "Dit dui 'n denkpouse aan waarin die man vinnig na woorde soek om 'n verskoning uit te dink sodat hy die skeptiese kelner kan oortuig dat hy 'n model is.",
    },
    {
        "question_ref": "1.17",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Leesbegrip: Artikel en Visuele Teks",
        "passage": PASSAGE_Q1,
        "question": "Herlees TEKS B en paragraaf 5 van TEKS A.\n\nSlaag die spotprentkunstenaar na jou mening daarin om die kwessie van 'n mens se aanpasbaarheidskwosiënt (AK) voldoende weer te gee indien die onderstreepte sin in paragraaf 5 (TEKS A) in ag geneem word? Motiveer jou antwoord.",
        "memo": "* $\\checkmark$ **Ja**\n  * Die spotprentkunstenaar dink buite die boks om hierdie man as model uit te beeld wat dan die aanpasbaarheid van die kelner sal uitbeeld.\n  * In die spotprent gebruik die man sy aanpasbaarheidskwosiënt (AK) om tot sy voordeel uit die boks te dink sodat hy 'n gratis ete kan kry.\n  * In die spotprent dink die restauranteienaar buite die boks om vir modelle 'n gratis ete aan te bied.\n\n*('n Nee-antwoord kan nie hier aanvaar word nie.)*",
        "final_answer": "Ja, die man pas homself slim by die situasie aan deur buite die boks te dink en te beweer sy baard is vir 'n advertensie om 'n gratis ete te kry.",
    },
    {
        "question_ref": "1.18.1",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Leesbegrip: Artikel en Visuele Teks",
        "passage": PASSAGE_Q1,
        "question": "Verwys na SPRAAKBORREL C van TEKS B.\n\n1.18.1 Sluit die muis se woorde by die slotsom in paragraaf 11 (TEKS A) aan? Motiveer jou antwoord.",
        "memo": "* $\\checkmark$ **Nee**\n  * Die muis wil nie verander nie; hy verwag dat die man formeel moet lyk, terwyl die restaurantopset informeel is.\n\n*(Die kandidaat kan nie 'n JA-antwoord aanbied nie.)*",
        "final_answer": "Nee, die muis toon weerstand teen verandering en verwag tradisionele formele kleredrag, terwyl paragraaf 11 sê dat sukses juis afhang van hoe buigsaam jy verandering hanteer.",
    },
    {
        "question_ref": "1.18.2",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Leesbegrip: Spotprent",
        "passage": PASSAGE_Q1,
        "question": "1.18.2 Wat is die geïmpliseerde boodskap van die muis se woorde in SPRAAKBORREL C?",
        "memo": "* $\\checkmark$ Die man lyk nie deftig genoeg vir 'n restaurant nie.",
        "final_answer": "Die man se slordige kortbroek en blootgestelde boepens is heeltemal onvanpas en nie deftig genoeg vir 'n restaurant nie.",
    },

    # AFDELING B: OPSOMMING (Vraag 2) - Total 10 marks
    {
        "question_ref": "2",
        "marks": 10,
        "kind": "question",
        "topic": "Opsomming: Wenke vir 'n stresvrye lewe",
        "passage": PASSAGE_Q2,
        "question": "Lees die teks hieronder en maak 'n opsomming van SEWE wenke om 'n stresvrye lewe te lei.\n\n**LET WEL:**\n1. Jou opsomming moet in jou eie woorde (in volsinne) in paragraafvorm aangebied word en mag nie meer as **90 woorde** beslaan nie.\n2. Jy moet EEN samehangende paragraaf skryf.\n3. Dit is nie nodig om vir die opsomming 'n titel te gee nie.\n4. Dui die getal woorde aan wat jy vir die opsomming gebruik het.",
        "memo": "* **Puntetoekenning:**\n  * 7 punte vir 7 wenke (1 punt per wenk)\n  * 3 punte vir taal\n  * **Totaal: 10 punte**\n\n* **Kernfeite uit teks:**\n  1. $\\checkmark$ Feit 1: Oefen gereeld om jou stres te verminder / stresvlakke laag te hou.\n  2. $\\checkmark$ Feit 2: Doen elke dag 'n lekker aktiwiteit wat vir jou aangenaam is om stres te verminder.\n  3. $\\checkmark$ Feit 3: Eet kossoorte wat jou laat ontspan, eerder as kossoorte wat jou serotonienvlakke te vinnig verhoog.\n  4. $\\checkmark$ Feit 4: Vermy te veel suiker- en kaffeïendrankies wat stresvlakke aanhelp.\n  5. $\\checkmark$ Feit 5: Sorg dat jy behoorlike kwaliteitslaap/nagrus inkry omdat dit stres verlig.\n  6. $\\checkmark$ Feit 6: Stel jou gereeld aan oggendsonlig se UV-strale bloot.\n  7. $\\checkmark$ Feit 7: Besoek 'n masseur / probeer massering as 'n manier om stres te verlig.\n\n* **Modelparagraaf (86 woorde):**\n  Jy moet gereeld oefen wat help om jou stresvlakke laag te hou, en jy moet ook elke dag 'n lekker aktiwiteit doen wat jou laat ontspan. Wees versigtig om nie te veel kossoorte te eet wat jou serotonienvlakke vinnig verhoog en tot stres lei nie. Probeer om nie te veel suiker- en kaffeïendrankies te drink wat stresvlakke aanhelp nie en sorg verder dat jy kwaliteitslaap inkry. Jy moet ook gereeld met oggendsonlig in aanraking te kom. Probeer laastens massering as 'n manier om stres te verlig.\n\n* **Taalrubriek:**\n  * 6–7 feite korrek: 3 punte vir taal\n  * 4–5 feite korrek: 2 punte vir taal\n  * 1–3 feite korrek: 1 punt vir taal\n  *(Aftrekking vir direkte aanhalings geld indien van toepassing)*",
        "final_answer": "Jy moet gereeld oefen om stres te verlaag en daagliks 'n aangename aktiwiteit doen wat jou gemoed rustig hou. Eet voedsame kos wat ontspanning bevorder en vermy te veel suiker- en kaffeïendrankies wat spanning aanwakker. Maak seker jy kry behoorlike kwaliteitslaap in sodat jou brein kan ontspan. Stel jou gereeld aan oggendsonlig bloot om goedvoelhormone te stimuleer. Laastens kan gereelde masseringsessies help om spierspanning te verlig en stres te verminder.",
    },

    # AFDELING C: VRAAG 3: ADVERTENSIE - Total 10 marks
    {
        "question_ref": "3.1",
        "marks": 2,
        "kind": "passage_questions",
        "topic": "Taalstrukture en -konvensies: Advertensie",
        "passage": PASSAGE_Q3,
        "question": "Plaas 'n gepaste skryfteken op die laaste woord in reël 1 van die opskrif en sê hoe dit die woordsoort verander.",
        "memo": "* $\\checkmark$ dié\n* $\\checkmark$ Dit verander die (bepaalde lid-)woord na 'n (aanwysende) voornaamwoord / aanwysende woord.",
        "final_answer": "dié; Dit verander die bepaalde lidwoord na 'n aanwysende voornaamwoord.",
    },
    {
        "question_ref": "3.2.1",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Taalstrukture en -konvensies: Advertensie",
        "passage": PASSAGE_Q3,
        "question": "Verwys na die groter letters en lettertipes in reël 1 en 2.\n\n3.2.1 Hoe beïnvloed die groter letters in reël 1 en 2 die leser?",
        "memo": "* $\\checkmark$ Dit trek die leser se aandag / Dit laat die leser op die advertensie fokus / Dit laat die leser wonder waaroor die advertensie handel / Die leser sien die advertensie dadelik raak.",
        "final_answer": "Dit trek onmiddellik die leser se aandag en laat hulle op die advertensie fokus.",
    },
    {
        "question_ref": "3.2.2",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Taalstrukture en -konvensies: Advertensie",
        "passage": PASSAGE_Q3,
        "question": "3.2.2 Sou jy die gebruik van die ander lettertipe in reël 2 as funksioneel beskou? Verduidelik jou antwoord kortliks.",
        "memo": "* $\\checkmark$ **Ja.** Dit ondersteun die gevoel dat jy op 'n eiland is / Dit sluit aan by 'n eilandgees / Die woorde is in die vorm van 'n golf (wat by die eiland aansluit) / Dit staan uit tussen die ander teks.\n  **OF**\n  **Nee.** Die lettertipe sluit nie by die eilandgees aan nie / Die woorde staan teen 'n ander agtergrond wat dit onnodig maak om nog 'n keer uit te hef.\n\n*(Die kandidaat bied 'n soortgelyke antwoord vir EEN punt aan.)*",
        "final_answer": "Ja, die golwende 3D-lettertipe boots seebranders na en versterk die ontspanne eilandgevoel.",
    },
    {
        "question_ref": "3.3",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Taalstrukture en -konvensies: Advertensie",
        "passage": PASSAGE_Q3,
        "question": "Hoe word die leser in reël 3 betrek?",
        "memo": "* $\\checkmark$ Deur die gebruik van die woorde \"jou\" / \"self\" / Die leser word direk aangespreek / Die leser word uitgenooi om self te proe.",
        "final_answer": "Die leser word direk aangespreek met woorde soos \"jou\" en \"self\" en uitgenooi om self te proe.",
    },
    {
        "question_ref": "3.4",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Taalstrukture en -konvensies: Advertensie",
        "passage": PASSAGE_Q3,
        "question": "Waarom maak die adverteerder van die woord **eksotiese** in reël 4 gebruik? Bied jou antwoord in 'n volsin aan.",
        "memo": "* $\\checkmark$ Dit is om die eilandlewe as buitengewoon/uniek/met 'n vreemde bekoring te beskryf / Dit is om die leser weg te voer / te oortuig.",
        "final_answer": "Die adverteerder gebruik die woord \"eksotiese\" om die eilandlewe as buitengewoon, uniek en aanloklik voor te stel sodat die leser daarna smag.",
    },
    {
        "question_ref": "3.5",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Taalstrukture en -konvensies: Advertensie",
        "passage": PASSAGE_Q3,
        "question": "Skryf 'n woord uit reël 7 neer waarmee die adverteerder die gebruiker oortuig om die produk te koop.",
        "memo": "* $\\checkmark$ \"lipleklekker\" / \"ontspan\"",
        "final_answer": "lipleklekker (of ontspan)",
    },
    {
        "question_ref": "3.6",
        "marks": 1,
        "kind": "multiple_choice",
        "topic": "Taalstrukture en -konvensies: Advertensie",
        "passage": PASSAGE_Q3,
        "question": "Kies die korrekte antwoord. Skryf net die vraagnommer (3.6) en die letter (A–D) neer.\n\nDie rede waarom die woord ''teug'' in reël 8 eerder as drink gebruik is, is omdat dit die …\nA. korrekte register van advertensietaal aandui.\nB. gepaste voorbeeld van 'n neutrale woord is.\nC. ontspanne atmosfeer van 'n eilandlewe ondersteun.\nD. emosionele behoefte van gebruikers aanspreek.",
        "memo": "* $\\checkmark$ C / die ontspanne atmosfeer van 'n eilandlewe ondersteun.",
        "final_answer": "C (die ontspanne atmosfeer van 'n eilandlewe ondersteun)",
    },
    {
        "question_ref": "3.7",
        "marks": 2,
        "kind": "passage_questions",
        "topic": "Taalstrukture en -konvensies: Advertensie",
        "passage": PASSAGE_Q3,
        "question": "Op grond waarvan is hierdie advertensie bevooroordeeld indien reël 11 en 12 in ag geneem word?",
        "memo": "* $\\checkmark$ Die adverteerder hef/sonder die \"fynproewers\" uit asof net hulle Tropika mag drink.\n* $\\checkmark$ Die adverteerder is bevooroordeeld oor die feit dat \"fynproewers\" se lewens vervelig is / Tropika kikker jou saai lewe op.",
        "final_answer": "Die advertensie sonder fynproewers uit asof slegs húlle die drankie drink, en oordeel bevooroordeeld dat mense se lewens saai en vervelig is sonder Tropika.",
    },

    # AFDELING C: VRAAG 4: STROKIESPRENT - Total 10 marks
    {
        "question_ref": "4.1",
        "marks": 1,
        "kind": "multiple_choice",
        "topic": "Taalstrukture en -konvensies: Strokiesprent",
        "passage": PASSAGE_Q4,
        "question": "Kies die korrekte antwoord. Skryf net die vraagnommer (4.1) en die letter (A–D) neer.\n\nDie eerste twee woorde van die strokie se titel is 'n …\nA. onderwerp.\nB. voorwerp.\nC. gesegde.\nD. byvoeglike bepaling.",
        "memo": "* $\\checkmark$ A / onderwerp",
        "final_answer": "A (onderwerp)",
    },
    {
        "question_ref": "4.2",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Taalstrukture en -konvensies: Strokiesprent",
        "passage": PASSAGE_Q4,
        "question": "Waarom is die onderstreepte woord in RAAMPIE 1 gepas?",
        "memo": "* $\\checkmark$ Die woord \"tjommies\" skep 'n informele gesprekstoon (wat by skoliere pas) / om by die geslag van die twee ander karakters te pas / Aangesien hulle nie vriende is nie, dui die woord op sarkasme.\n\n*(Die kandidaat bied enige soortgelyke antwoord vir EEN punt aan.)*",
        "final_answer": "Die woord \"tjommies\" pas by die informele register van skoliere (of dui op sarkasme omdat hulle nie eintlik maats is nie).",
    },
    {
        "question_ref": "4.3",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Taalstrukture en -konvensies: Strokiesprent",
        "passage": PASSAGE_Q4,
        "question": "Hoe behoort 'n leser die vraagteken bokant die meisie se kop in RAAMPIE 2 te verstaan?",
        "memo": "* $\\checkmark$ Die vraagteken dui op die meisie se onbegrip (van die twee seuns se onvanpaste reaksie/handeling) / verbasing oor hul high-five.",
        "final_answer": "Dit dui op haar verbasing en onbegrip oor die seuns se oordrewe triomfantlike reaksie vir iets eenvoudig.",
    },
    {
        "question_ref": "4.4",
        "marks": 2,
        "kind": "passage_questions",
        "topic": "Taalstrukture en -konvensies: Strokiesprent",
        "passage": PASSAGE_Q4,
        "question": "In RAAMPIE 3 is dit duidelik dat die twee seuns die meisie doelbewus nie by hulle gesprek wil insluit nie.\n\nWatter visuele en verbale inligting bied hierdie raampie om die stelling hierbo te ondersteun?",
        "memo": "* $\\checkmark$ **Visueel:** Hulle maak nie oogkontak met die meisie nie / Hulle gesels asof sy nie daar is nie / Slegs die gesiggie van die meisie word links onder in die hoekie van die raampie geteken, terwyl die twee seuns se volledige lyfies sentraal in die raampie geplaas is.\n* $\\checkmark$ **Verbaal:** Hulle gebruik die persoonlike voornaamwoord \"sy\" in plaas van \"jy\".",
        "final_answer": "Visueel: Die seuns kyk weg van haar af en sy word na die kantlyn/hoekie afgeskuif; Verbaal: Hulle praat van haar in die derde persoon as \"sy\" in plaas daarvan om haar direk as \"jy\" aan te spreek.",
    },
    {
        "question_ref": "4.5",
        "marks": 2,
        "kind": "passage_questions",
        "topic": "Taalstrukture en -konvensies: Strokiesprent",
        "passage": PASSAGE_Q4,
        "question": "Hoe weet die leser dat die meisie se stemtoon in RAAMPIE 4 kwaai is? Gee dan TWEE OPEENVOLGENDE woorde uit hierdie raampie wat by haar stemtoon aansluit.",
        "memo": "* $\\checkmark$ Donkergedrukte woorde / Ander skriftipe / Woorde in hoofletters gedruk / Twee uitroeptekens / getande spraakborrel / haar oopgesperde mond en woedende gesig.\n  *(Enige EEN vir 1 punt)*\n* $\\checkmark$ TWEE OPEENVOLGENDE woorde: \"ek roer\" / \"moet oppas\" / \"sommer nou-nou\".\n  *(Enige paar vir 1 punt)*",
        "final_answer": "Haar woorde is in vetgedrukte hoofletters geskryf met twee uitroeptekens; Twee opeenvolgende woorde: \"EK ROER\" (of \"MOET OPPAS\" / \"SOMMER NOU-NOU\").",
    },
    {
        "question_ref": "4.6",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Taalstrukture en -konvensies: Strokiesprent",
        "passage": PASSAGE_Q4,
        "question": "Verander die onderstreepte woord in RAAMPIE 4 na 'n teenwoordige deelwoord wat jy in 'n sin van jou eie gebruik.",
        "memo": "* $\\checkmark$ Die man se woorde by die begrafnis was roerend / Hy het baie roerende bates in sy testament nagelaat.\n\n*(Die kandidaat bied enige soortgelyke sin met \"roerend\" / \"roerende\" vir EEN punt aan.)*",
        "final_answer": "roerend / roerende (Voorbeeldsin: Die sangeres het 'n baie roerende vertolking van die lied gelewer.)",
    },
    {
        "question_ref": "4.7.1",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Taalstrukture en -konvensies: Strokiesprent",
        "passage": PASSAGE_Q4,
        "question": "Die seun (gemerk A) se liggaamstaal in RAAMPIE 5 en RAAMPIE 2 verskil.\n\n4.7.1 Motiveer hierdie stelling.",
        "memo": "* $\\checkmark$ In RAAMPIE 2 is die seun selfvoldaan / (leed-)vermakerig / gelukkig / trots / tevrede / in sy noppies / beïndruk met hom en sy maat, maar in RAAMPIE 5 lyk dit of hy skaam / moedeloos / in 'n verleentheid is.",
        "final_answer": "In Raampie 2 glimlag hy breed en gee 'n selfvoldane hoëvyf, terwyl hy in Raampie 5 sy hand moedeloos en verleë teen sy gesig hou van skaamte.",
    },
    {
        "question_ref": "4.7.2",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Taalstrukture en -konvensies: Strokiesprent",
        "passage": PASSAGE_Q4,
        "question": "4.7.2 Wat dink jy is 'n moontlike rede vir dié verandering?",
        "memo": "* $\\checkmark$ Hy skaam hom vir sy maat se (ondeurdagte) reaksie / Hy is moedeloos omdat sy maat se reaksie dalk 'n bevestiging is van dit wat die meisie in RAAMPIE 2 dink (dat hulle reaksie/antwoord ondeurdag is) / Hy lag oor sy maat se domheid.\n\n*(Die kandidaat bied enige soortgelyke antwoord vir EEN punt aan.)*",
        "final_answer": "Hy skaam hom vir sy maat se flou, letterlike opmerking oor die lepel wat hulle albei dom laat lyk.",
    },

    # AFDELING C: VRAAG 5: ARTIKEL - Total 10 marks
    {
        "question_ref": "5.1",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Taalstrukture en -konvensies: Artikel en Woordstrukture",
        "passage": PASSAGE_Q5,
        "question": "Benoem die onderstreepte telwoord in paragraaf 1.",
        "memo": "* $\\checkmark$ (bepaalde) hooftelwoord",
        "final_answer": "(bepaalde) hooftelwoord",
    },
    {
        "question_ref": "5.2",
        "marks": 2,
        "kind": "passage_questions",
        "topic": "Taalstrukture en -konvensies: Artikel en Woordstrukture",
        "passage": PASSAGE_Q5,
        "question": "Skryf die pleonasme in paragraaf 1 neer. Dink jy dié pleonasme is funksioneel in die sin? Motiveer jou antwoord.",
        "memo": "* $\\checkmark$ Die kinders was bly en verheug oor die reaksie (bly en verheug).\n* $\\checkmark$ **Ja:** Dit bevestig/versterk die kinders se geluk/opgewondenheid oor die reaksie op hul kunswerke.\n  **OF**\n  **Nee:** Pleonasme is 'n taalverskynsel wat op lompheid dui.\n\n*(Die kandidaat bied 'n soortgelyke antwoord vir EEN punt aan.)*",
        "final_answer": "bly en verheug; Ja, dit beklemtoon en versterk hoe intens gelukkig en opgewonde die kinders oor die ontvangs van hul kunswerke was.",
    },
    {
        "question_ref": "5.3",
        "marks": 2,
        "kind": "passage_questions",
        "topic": "Taalstrukture en -konvensies: Artikel en Woordstrukture",
        "passage": PASSAGE_Q5,
        "question": "Skryf die kern van die onderstreepte samestelling in paragraaf 2 neer. Vorm nou 'n bywoord daarvan en gebruik dit in 'n sin van jou eie.",
        "memo": "* $\\checkmark$ Dag (kern van 'markdag')\n* $\\checkmark$ Bywoord en sin: daagliks / bedags / vandag / eersdaags (bv. \"Ons ry daagliks bus skool toe en terug.\" / \"Ek werk bedags in die tuin.\" / \"Ek werk vandag in die tuin.\" / \"Ons kom eersdaags kuier.\")\n\n*(Die kandidaat kan nie 'daaglikse' as antwoord aanbied nie, aangesien dit 'n byvoeglike naamwoord is.)*",
        "final_answer": "Kern: dag; Bywoord en sin: daagliks (Die leerders stap daagliks skool toe).",
    },
    {
        "question_ref": "5.4",
        "marks": 2,
        "kind": "passage_questions",
        "topic": "Taalstrukture en -konvensies: Artikel en Woordstrukture",
        "passage": PASSAGE_Q5,
        "question": "Verbeter die leestekenfout by die parentese in paragraaf 4 deur die sin korrek neer te skryf en gee ook die funksie van dié parentese.",
        "memo": "* $\\checkmark$ Die organisasie se skryfbehoeftevennoot, Staedler, het die Fimo-kunstenaar, Riaan Marais, na hierdie sentrum gebring. (Die kommapunt na 'skryfbehoeftevennoot' moet 'n komma wees).\n* $\\checkmark$ Funksie: Die parentese dui aan na wie die skryfbehoeftevennoot verwys / verskaf bykomende verklarende inligting (apposisie/invoeging).\n\n**OF**\n\n* $\\checkmark$ Sjoe, en het hierdie kinders van die buurt dit nou geniet! het Mia Sonnekus, woordvoerder van Staedler, gister gesê.\n* $\\checkmark$ Funksie: Die parentese dui aan wie Staedler se woordvoerder is.",
        "final_answer": "Verbeterde sin: Die organisasie se skryfbehoeftevennoot, Staedler, het die Fimo-kunstenaar, Riaan Marais, na hierdie sentrum gebring.\nFunksie: Die parentese verskaf ekstra inligting wat verduidelik wie die skryfbehoeftevennoot is (apposisie/invoeging).",
    },
    {
        "question_ref": "5.5",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Taalstrukture en -konvensies: Artikel en Woordstrukture",
        "passage": PASSAGE_Q5,
        "question": "Verdeel die onderstreepte woord in paragraaf 5 in lettergrepe.",
        "memo": "* $\\checkmark$ i – ni – si – a – tief",
        "final_answer": "i-ni-si-a-tief",
    },
    {
        "question_ref": "5.6",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Taalstrukture en -konvensies: Artikel en Woordstrukture",
        "passage": PASSAGE_Q5,
        "question": "Gebruik die vetgedrukte woord in paragraaf 5 as twee woorde in 'n verklarende sin.",
        "memo": "* $\\checkmark$ Die Bulle het vanjaar 'n jong span. / Die span bestaan uit jong deelnemers. / Jong, dis 'n goeie span.\n\n*(Die kandidaat bied 'n eie verklarende sin aan waar \"jong span\" as twee afsonderlike woorde gebruik word.)*",
        "final_answer": "Die afrigter het vanjaar 'n baie jong span gekies om die skool te verteenwoordig.",
    },
    {
        "question_ref": "5.7",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Taalstrukture en -konvensies: Artikel en Woordstrukture",
        "passage": PASSAGE_Q5,
        "question": "Skryf die basisvorme/stamme van die onderstreepte woord in paragraaf 6.",
        "memo": "* $\\checkmark$ gemeen / gemeenskap en projek\n\n*(Die kandidaat moet beide die stamme vir EEN punt aanbied.)*",
        "final_answer": "gemeen (of gemeenskap) en projek",
    },
]

def check_katex_dollars(text):
    # check that dollar signs are balanced
    # ignore escaped dollars \$
    clean = re.sub(r'\\\$', '', text)
    count = clean.count('$')
    return count % 2 == 0

def main():
    items = []
    total_marks = 0
    katex_errors = 0

    section_marks = {
        "A": 0,
        "B": 0,
        "C_Q3": 0,
        "C_Q4": 0,
        "C_Q5": 0,
    }

    for raw in raw_items:
        q_ref = raw["question_ref"]
        item = {
            "item_id": f"{SOURCE_ID}-{q_ref}",
            "source_id": SOURCE_ID,
            "pair_source_id": PAIR_SOURCE_ID,
            "subject": SUBJECT,
            "grade": GRADE,
            "language": LANGUAGE,
            "track": TRACK,
            "kind": raw["kind"],
            "question_ref": q_ref,
            "marks": raw["marks"],
            "topic": raw["topic"],
            "passage": raw["passage"],
            "question": raw["question"],
            "memo": raw["memo"],
            "final_answer": raw["final_answer"],
            "needs_review": False,
            "licence": "DBE copyright - check terms",
            "attribution": "Department of Basic Education",
        }

        # Check KaTeX balance
        for field in ["question", "memo", "final_answer", "passage"]:
            if not check_katex_dollars(item[field]):
                print(f"ERROR: Unbalanced $ in item {item['item_id']}, field {field}")
                katex_errors += 1

        marks = item["marks"]
        total_marks += marks
        if q_ref.startswith("1."):
            section_marks["A"] += marks
        elif q_ref == "2":
            section_marks["B"] += marks
        elif q_ref.startswith("3."):
            section_marks["C_Q3"] += marks
        elif q_ref.startswith("4."):
            section_marks["C_Q4"] += marks
        elif q_ref.startswith("5."):
            section_marks["C_Q5"] += marks

        items.append(item)

    print(f"Total items: {len(items)}")
    print(f"Section marks: {section_marks}")
    print(f"Total marks: {total_marks}")
    print(f"KaTeX errors: {katex_errors}")

    assert len(items) == 47, f"Expected 47 items, got {len(items)}"
    assert section_marks["A"] == 30, f"Section A expected 30, got {section_marks['A']}"
    assert section_marks["B"] == 10, f"Section B expected 10, got {section_marks['B']}"
    assert section_marks["C_Q3"] == 10, f"Section C Q3 expected 10, got {section_marks['C_Q3']}"
    assert section_marks["C_Q4"] == 10, f"Section C Q4 expected 10, got {section_marks['C_Q4']}"
    assert section_marks["C_Q5"] == 10, f"Section C Q5 expected 10, got {section_marks['C_Q5']}"
    assert total_marks == 70, f"Total marks expected 70, got {total_marks}"
    assert katex_errors == 0, f"Expected 0 KaTeX errors, got {katex_errors}"

    # Target output paths
    path1 = os.path.join("workspace", "items", "afrikaans_hl", f"{SOURCE_ID}.jsonl")
    path2 = os.path.join("workspace", "items", f"{SOURCE_ID}.jsonl")

    os.makedirs(os.path.dirname(path1), exist_ok=True)
    os.makedirs(os.path.dirname(path2), exist_ok=True)

    with open(path1, "w", encoding="utf-8") as f1, open(path2, "w", encoding="utf-8") as f2:
        for it in items:
            line = json.dumps(it, ensure_ascii=False)
            f1.write(line + "\n")
            f2.write(line + "\n")

    print(f"Successfully wrote {len(items)} items to:")
    print(f"  {path1}")
    print(f"  {path2}")

if __name__ == "__main__":
    main()
