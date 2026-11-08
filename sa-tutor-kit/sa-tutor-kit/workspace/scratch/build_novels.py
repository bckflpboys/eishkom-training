# -*- coding: utf-8 -*-
"""
build_novels.py - Generates the 51 novel items for Afrikaans HL P2 Nov 2025.
Questions 6 to 13:
- Question 6: Onderwêreld (Fanie Viljoen) - Opstelvraag [25]
- Question 7: Onderwêreld (Fanie Viljoen) - Kontekstueel [25] (7.1, 7.2, 7.3, 7.4, 7.5, 7.6, 7.7.1, 7.7.2, 7.8, 7.9, 7.10)
- Question 8: Manaka Plek van die Horings (Pieter Pieterse) - Opstelvraag [25]
- Question 9: Manaka Plek van die Horings (Pieter Pieterse) - Kontekstueel [25] (9.1, 9.2, 9.3, 9.4, 9.5, 9.6, 9.7, 9.8, 9.9, 9.10, 9.11)
- Question 10: Vatmaar (A.H.M. Scholtz) - Opstelvraag [25]
- Question 11: Vatmaar (A.H.M. Scholtz) - Kontekstueel [25] (11.1, 11.2.1, 11.2.2, 11.3, 11.4, 11.5, 11.6, 11.7, 11.8, 11.9, 11.10, 11.11, 11.12)
- Question 12: Die kwart-voor-sewe-lelie (Eleanor Baker) - Opstelvraag [25]
- Question 13: Die kwart-voor-sewe-lelie (Eleanor Baker) - Kontekstueel [25] (13.1, 13.2, 13.3, 13.4.1, 13.4.2, 13.5, 13.6, 13.7.1, 13.7.2, 13.8, 13.9, 13.10)
"""

import json

SOURCE_ID = "dbe-afrikaans_hl-g12-p2-2025-nov"
MEMO_ID = "dbe-afrikaans_hl-g12-p2-2025-nov-memo"

NOVEL_RUBRIC = """### AFDELING B EN C: ASSESSERINGSRUBRIEK VIR OPSTELVRAAG – HUISTAAL: ROMAN EN DRAMA [25 PUNTE]

| Kriteria | Uitsonderlik | Knap | Gemiddeld | Elementêr | Onvoldoende |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **INHOUD**<br>Interpretasie van onderwerp. Diepte van argument, verantwoordbaarheid en insig in teks.<br>**(15 PUNTE)** | **12–15**<br>- Diepgaande interpretasie van onderwerp<br>- Uitsonderlike respons: 14–15; Uitstekende respons: 12–13<br>- Reeks treffende argumente wat behoorlik uit die roman/drama gerugsteun is<br>- Uitstekende begrip van die genre en teks | **9–11**<br>- Toon begrip van die onderwerp en het die onderwerp goed geïnterpreteer<br>- Respons redelik gedetailleerd<br>- Enkele deeglike argumente gegee, maar nie almal ewe goed gemotiveer nie<br>- Begrip van genre en teks duidelik | **6–8**<br>- Redelike interpretasie van die onderwerp; nie alle aspekte in detail ondersoek nie<br>- Enkele goeie punte ter ondersteuning van die onderwerp<br>- Enkele argumente word ondersteun, maar bewyse nie altyd oortuigend nie<br>- Basiese begrip van genre en teks | **4–5**<br>- Onbevredigende interpretasie van die onderwerp: byna geen aspekte in detail ondersoek nie<br>- Min punte wat die onderwerp ondersteun<br>- Baie min relevante argumente<br>- Weinig begrip van genre en teks | **0–3**<br>- Geen begrip van die onderwerp nie<br>- Swak poging om die vraag te beantwoord<br>- Argumente oortuig nie<br>- Leerder het nie die genre en teks onder die knie nie |
| **STRUKTUUR EN TAAL**<br>Struktuur, logiese vloei en aanbieding. Taalgebruik, toon en styl gebruik in opstel.<br>**(10 PUNTE)** | **8–10**<br>- Samehangende struktuur<br>- Argumente goed gestruktureer en daar is duidelike ontwikkeling<br>- Uitstekende inleiding en slot<br>- Inleiding, slot en ander paragrawe samehangend georganiseer<br>- Taalgebruik, toon en styl is volwasse, dit beïndruk en is korrek | **6–7**<br>- Duidelike struktuur<br>- Logiese vloei van argument<br>- Inleiding, slot en ander paragrawe samehangend georganiseer<br>- Taalgebruik, toon en styl is grootliks korrek | **4–5**<br>- Enkele bewyse van struktuur<br>- Logika en samehang is duidelik, maar met foute<br>- Paragrafering meestal korrek<br>- Enkele taalfoute; toon en styl meestal gepas | **2–3**<br>- Struktuur toon tekens van swak beplanning<br>- Argumente nie logies gerangskik nie<br>- Paragrafering foutief<br>- Taalfoute beduidend; toon en styl nie geskik nie | **0–1**<br>- Gebrek aan beplande struktuur belemmer vloei van argumente<br>- Argumente nie logies gerangskik nie<br>- Taalfoute en foutiewe styl laat hierdie skryfstuk misluk<br>- Paragrafering foutief<br>- Styl en toon nie geskik nie |
| **PUNTEVERSPREIDING** | **20–25** | **15–19** | **10–14** | **5–9** | **0–4** |
"""

PASSAGE_ONDERWERELD_CONTEXT = """### ONDERWÊRELD – Fanie Viljoen
[Konteks: Die jeugroman speel af by Lawson Kollege. Greg Owen, hoofseun en topatleet, word deur die nuwe matriekleerder Eckardt Wilken in die geheime onderwêreld van rekenaarkuberkrakery ingetrek. Ná Eckardt se geheimsinnige verdwyning ontdek Greg dat sy eie pa en die skoolhoof, Dokter Alec Pienaar (Project Nursery Rhyme), agter 'n dodelike korrupsiesameswering sit.]"""

PASSAGE_TEKS_A = """### TEKS A – ONDERWÊRELD (Fanie Viljoen)

```text
 1    Dis die dag ná ek gesien het hoe Eckardt die reisagent se systems hack. En die eerste 
 2 oggend dat Eckardt my kom wakker maak. 
 3    "Terwyl Zeus, die heerser van Olimpus, slapend gevou lê in Hipnos se vlerke, strand sy 
 4 seun, Herakles, se skip vandag weer op Kos," sê hy toe hy aan die deur klop. 
 5    "Wat de hel?" vra ek deur die slaap. 
 6    "Never mind. Roer jou gat en staan op," antwoord hy. 
 7    Ek maak een oog oop, lig myself op my elmboë. Eckardt is in sy oefenklere. Sweet glim 
 8 op sy lyf. "Is jy simpel? Het jy al gaan draf?" vra ek. 
 9    "Altyd. Enigste tyd om helder te dink, so vroeg in die môre. Toe, roer jou, dis byna tyd 
10 vir brekfis." 
11    Die dag sleep om. Pouse moet ek, in opdrag van Dok, die VRL aanvat oor hul 
12 "betreurenswaardige dissipline". Meneer Andersen daag halfpad deur die vergadering op. 
13 Spioeneer op ons, asof ons dit nie weet nie. 
14    "Wil meneer nog iets byvoeg?" vra ek toe ek klaar my preek afgesteek het. 
15    Hy skud sy kop en loop. 
16    "Good show," sê Kwanele toe hy ook loop, sy houding uitdagend. Ek gluur hom agterna. 
17     Ek kry vir Eckardt op pad na die Engelsklas. "Jy onthou nog van jou belofte van 
18 gisteraand, nè!" herinner ek hom.
```"""

PASSAGE_TEKS_B = """### TEKS B – ONDERWÊRELD (Fanie Viljoen)

```text
 1 Ek is vrek bang, maar ek weet ek moet die een of ander tyd huis toe bel. Ek sit seker 'n 
 2 halfuur lank met my selfoon in my hand, my ma se nommer op die skerm, maar ek druk 
 3 nie die groen knoppie om die konneksie te maak nie. My hand bewe. My hart ook. Ek wil 
 4 my ma nie teleurstel nie. Sy het soveel hoop vir my; 'n anderste hoop as my pa. 
 5    Maar uiteindelik het ek geen keuse nie. Kry dit net agter die rug, Greg. 
 6    "Hallo, Ma?" 
 7    Ek begin haar vertel van Eckardt, dat hy 'n hacker is, dat hy my geleer het. Van die 
 8 polisie wat my laptop gevat het. Ek bly stil oor Dok en die goed wat ek oor hom uitgevind 
 9 het. 
10    Ná 'n diep asemteug voeg ek by: "Ma, hulle dink ek het iets met Eckardt se verdwyning 
11 uit te waai."  
12    My ma struikel oor haar eie woorde. Ek kan die vrees in haar stem hoor. "Maar jy sou 
13 mos nie ..."  
14    "Natuurlik nie, Ma." 
15    "Hy was dan jou vriend ..." 
16    "Ma moenie vir Pa vertel nie, asseblief. Nie nou nie. Laat ek eers kyk wat ek kan 
17 uitvind." 
18    "Greg, die skool het hom reeds gebel. Hy is op pad na jou toe." 
19    Koue rillings loop oor my ruggraat. "Pa? Hiernatoe?" 
20    "Hy is woedend. Hy sê jy ruïneer die gesin se goeie naam. Ek wou hom keer, Greg, 
21 maar jy weet hoe hy is." 
22    Ek knik stom, al kan my ma my nie sien nie. Ek weet hoe my pa is. 
23    "Ek kom ook, Greg," sê my ma sag. "Ek kan jou nie alleen hierdeur laat gaan nie." 
24    "Nee, Ma, bly liewer by die huis. Pa sal net erger te kere gaan as Ma ook hier is." 
25    "Ek gee nie om nie, Greg. Ek kom."
```"""

PASSAGE_MANAKA_CONTEXT = """### MANAKA PLEK VAN DIE HORINGS – Pieter Pieterse
[Konteks: Die roman speel af in die Caprivi-moerasse by die Zambezirivier. Baas (Pieter) ontvlug sy verlede ná die moord op sy ouers en die verlies van sy familieplaas. Op Manaka herstel hy 'n pontboot en raak teen sy sin betrokke by die Lozi-gemeenskap, die sendelinge en Grace, wat sy sinisme oor geloof en die lewe uitdaag.]"""

PASSAGE_TEKS_C = """### TEKS C – MANAKA PLEK VAN DIE HORINGS (Pieter Pieterse)

```text
 1    "Yessa!" skreeu hy in die rigting van die worsboom. Hy klap vir Baas hande. Sy bene 
 2 hoepel teen die bult af. 
 3    "Kwê ..." toets die kwêvoël in die jakkalsbessie die atmosfeer. 
 4    "Ek sal baie graag vir jou 'n gebed wil doen, neef."  
 5    "Vir mý?" 
 6    "Daar kom 'n tyd in elke mens se lewe dat hy dit nodig het." 
 7    "Ag nee, wat, so erg is dit nie. Maar baie dankie vir die gedagte." Baas sien die skoene 
 8 van hom af wegdraai.  
 9    "Muluti Malila huil oor jou," hoor hy Grace sê. 
10    "Miskien huil hy oor homself." Baas roer nie. Hy kantel sy kop en maak weer sy oë 
11 toe. 
12    "As 'n mens oor iemand anders huil, dan huil jy eintlik oor jouself ook." Grace klim van 
13 die bak af. 
14    Die moerasfiskale roep. "Priscilla en Akwilla ..." sê sy. "Dis die name wat ek vir daardie 
15 twee voëls gegee het. Dit was toe jy siek was, in die tyd toe ek in jou huis gesit en wag 
16 het dat jy jou oë moet oopmaak. Dis 'n goeie naam vir hulle. Hulle is nooit ver van mekaar 
17 af nie."  
18    Die moerasfiskale hou op roep. Die kinders se gejil bedaar. Van die worsboom se kant 
19 af kom kitaarklanke. 'n Heldersoet stem begin uit die note vloei. "Amazing grace, how 
20 sweet the sound, that saved a wretch like me," sing Nanna. "I once was lost but now I'm 
21 found, was blind but now I see."    
22   Die naarheid stoot in Baas se keel op.
```"""

PASSAGE_TEKS_D = """### TEKS D – MANAKA PLEK VAN DIE HORINGS (Pieter Pieterse)

```text
 1     "Howzit?" Whitey klim af, 'n bottel brandewyn in die een hand en 'n outydse geweer 
 2 in die ander. "Gehoor jy het na my kom soek daar by my kamp. Toe dink ek ek sal maar 
 3 kom kyk hoe dit gaan. Jy het nie dalk water wat 'n mens hier kan bygooi nie?" Hy gee 
 4 die bottel vir Baas.  
 5    "Yes, Gracie," groet hy. 
 6    Grace vryf haar hande teen mekaar en knik haar knieë. 
 7    "Gaan jy vir jou kombuiskaste insit?" Baas wys na die planke. 
 8    "Eendag ... Miskien ... As ek 'n kombuis het. Hierdie is joune. Jy het daardie dag gesê 
 9 jy wil bankies bou. Ek het sommer stutpaaltjies ook saamgebring." 
10    Hulle sit die gewere neer, maak die drade los waarmee die planke aan die trekker 
11 vasgewoel is en pak dit onder die seil by die werkswinkel. Baas nooi Whitey 
12 slaaprondawel toe, steek die paraffienlampie aan en bêre sy geweer. Grace kom in met 
13 twee bekers. 
14    "Nou moet julle besluit. Ek stel voor julle gebruik die bekers vir koffie," sê sy. 
15    "Jy weet mos ek hou nie van koffie nie en koffie hou nie van my nie." 
16    Whitey sit sy geweer op die bed neer. Grace los die bekers langs die foto's op die 
17 swart trommel en gaan uit om water te gaan haal. 
18    "Ek gooi dop," sê Whitey. "Wat van jou?" 
19    "Nie nou nie, dankie." Baas tel die geweer op en bekyk dit. 
20    "Agtponder." Whitey gaan sit op die groen trommel.  
21    Baas se oë dwaal verby die man in die blou oorpak na die portret teen die muur.
```"""

PASSAGE_VATMAAR_CONTEXT = """### VATMAAR – AHM Scholtz
[Konteks: Die roman speel af in Vatmaar, 'n bruin gemeenskap naby Du Toitspan buite Kimberley. Kenneth Kleinhans, wat na Vatmaar kom met 'n gebroke hart ná die tragiese dood van sy geliefde Kaaitjie en hul ongebore baba, vind genesing deur homself onbaatsugtig te wy aan die opheffing van die gemeenskap, insluitend die oprigting van Kliniek Katrina en die vestiging van die dorpsokkerveld.]"""

PASSAGE_TEKS_E = """### TEKS E – VATMAAR (AHM Scholtz)

```text
 1      Die telefoonpale was al tot amper by die kliniek en die mense het gesê: Nog twee 
 2 weke en Vatmaar is met die Pan gekonnek. 
 3      Die sokkerveld is eerste ingewy. 
 4      Dit was 'n trotse Kenneth Kleinhans wat daardie Saterdagmiddag – met die hele 
 5 Vatmaar wat om die sokkerveld staan – die bal van Boitjie Afrika gekry het om op die 
 6 middellyn te gaan stel. 
 7      Toe hy terugstap, laat Teacher Elsa haar sakdoek val, iets wat min mense in  
 8 Vatmaar gedra het. Kenny tel dit op, waai die stof uit en gee dit vir haar. 
 9       Kenny met sy gebroke hart gee dit vir haar en sê: Your handkerchief, lady. Die  
10 woorde knel haar, sy word warm. Maar hierdie Elsa se begeerte, haar diepste wense – 
11 dit is die man vir my – kon hom nie aantas nie. 
12       Die Vatmaar Sunbeam-sokkerspan het teen Du Toitspan Wanderers se B-span 
13 gespeel en hulle een-nul gewen. Daarna was Vatmaar nooit weer dieselfde nie. Na die 
14 tyd was die aankykers moeër as die spelers want die meeste van hulle het saam met 
15 hulle se span en die bal op en af langs die veld gehardloop. Party oupas het na 'n kamma 
16 bal geskop elke keer as een van Vatmaar se spelers op die veld na die bal skop.  
17       Na die wedstryd is baie dinge afgepraat, soos lat die fluitjieman so grênd was. 
18       Suzan wat ook gaan kyk het, het vir Nellie Ndola gekry toe sy met die paaitjie  
19 terugstap. Sy het vinnig rondgekyk of sy nie vir Tommy Lewis sien nie.
```"""

PASSAGE_TEKS_F = """### TEKS F – VATMAAR (AHM Scholtz)

```text
 1 Die Du Toitspan-hospitaal het 'n brief vir die dorpsraad geskryf waarin hulle sê hulle sal 
 2 een of twee keer 'n week 'n verpleegster Vatmaar toe kan stuur, op een voorwaarde: 
 3 Die dorpsraad moet betaal vir die transport, of dit nou 'n kapkar of 'n mouterkar is. Net 
 4 vir 'n bicycle of 'n gewone perdekar hoef hulle nie te betaal nie. 
 5       Die dorpsraad het die hospitaal-superintendent bedank en die voorwaarde aanvaar. 
 6       Dit was weer 'n plesierige Mister Burns wat vir Kenny kom sê het: Here is the letter 
 7 from the town council. The clinic will be opened, not this Saturday but the next. Get ready 
 8 for the celebration, for there is a time to mourn and a time to be merry. 
 9       Kenny vra toe die domanie om op die agenda van die diens te sit dat die kliniek die 
10 volgende Saterdag deur die burgermeester van die Pan en sy raadslede oop verklaar 
11 sal word, en dat hulle baie bly sal wees as die hele Vatmaar na die feesvieringe kan 
12 kom. 
13       Kenny het vir Sus Bet geld gegee en haar gevra om die beste khadie te maak wat 
14 sy nog ooit gemaak het. Sy het gesê: Op een voorwaarde, dat Vatmaar se mense nie 
15 van die khadie drink nie. Laat dit net vir die mense van die Pan wees. 
16       Fair enough, sê Kenny. 
17       Ek verwag dat jy dit so sal hou, het Sus Bet gesê. 
18       Die gemmerbier sou deur Nurse-sister Gous gemaak word, en sy moes ook sorg vir 
19 genoeg vier-gelling-paraffienblikke vir die bier.
```"""

PASSAGE_KWART_CONTEXT = """### DIE KWART-VOOR-SEWE-LELIE – Eleanor Baker
[Konteks: Die roman volg Iris se lewensreis vanaf 'n eksentrieke, verstrooide gesin na volwassenheid. Iris worstel met haar identiteit, haar fantasiewêreld met die Engel, en die soeke na haar eie 'blomtyd'. Deur haar verhouding met Peter en haar interaksie met verskillende vroue (haar ma Els, susters Elsa en Kara, huishulp Johanna, en tant Ans) leer sy dat die lewe nie 'n grootse fantasie hoef te wees om betekenisvol te wees nie.]"""

PASSAGE_TEKS_G = """### TEKS G – DIE KWART-VOOR-SEWE-LELIE (Eleanor Baker)

```text
 1    "Het Ma gehoor wat ek gesê het?"  
 2    "Ja, darling." Sy het die bakkie vet vinnig in die yskas gesit asof die verwerking daarvan 
 3 nou die yskas se verantwoordelikheid is. "Ek weet Pa is op 'n dieet." 
 4    "Nie dit nie. Van my naam." 
 5    Sy het haar hande gewas en die hardevet onder haar naels uitgekrap. "Natuurlik het 
 6 ek gehoor." 
 7    "Dis mooi, nè?" 
 8    "Pragtig," het sy saamgestem en haar tong geklik toe sy agterkom die boud is wel in 
 9 die oond, maar die oond is nog nie aangeskakel nie. "So 'n mooi blom. Ek vind dit so 
10 jammer dat hulle net in die lente blom." 
11    Dis wat ek bedoel. Sy het my nie gehoor nie. Ek het haar maar gehelp aartappels skil. 
12 "Dis so," het ek gesê. "Net een keer per jaar." 
13 
14 My ma, wie se naam ook Elsa was, maar wat deur almal Els genoem is, het nooit daarin 
15 geslaag om die wêreld in haar hand vas te vat nie. Sy was soos iemand wat 'n bus verpas 
16 het en nie daarby kon berus nie. Haar hele lewe lank al hardloop sy agter die bus aan in 
17 die hoop dat sy hom gaan inhaal nes hy stadiger om 'n draai ry. Sy was nie die soort 
18 mens wat by die volgende halte sou gaan sit en wag op die volgende bus nie. Nog minder 
19 was sy die soort wat voluit gehardloop het. Nee, sy het op 'n ligte drafstappie beweeg, 
20 net effe uitasem, een en al stralende optimisme dat sy die bus wel gaan inhaal.
```"""

PASSAGE_TEKS_H = """### TEKS H – DIE KWART-VOOR-SEWE-LELIE (Eleanor Baker)

```text
 1 … "Sy bestuur 'n ysterwarewinkel en kan goed doen soos gebarste warmwatertenks 
 2 regmaak. En sweis en alles." 
 3        "Waarom wil sy dan gif drink?" het die tannie gevra. 
 4        "Ek dink sy is ongelukkig oor haar verhouding met Brian," het ek gesê. "Ek dink nie 
 5 dit het iets te doen met die besigheid nie, mevrou." 
 6        "Jy kan nie vir my mevrou sê nie," het sy gesê. "Een van die dae moet jy Ma sê. As 
 7 die orrel begin speel. Noem my tant Ans." 
 8        "Goed," het ek gesê. "Tant Ans." Oor die orrelspel het ek nie uitgewei nie. As ek sou 
 9 trou – en op daardie tydstip was selfs dit nog nie 'n uitgemaakte saak nie – sou dit vinnig 
10 en sonder ophef in 'n magistraatskantoor plaasvind. 
11        "Hoekom wil dié Brian nie met haar trou nie?" het die oom gevra. "Watse nonsens 
12 is dit?" 
13         "Dis 'n lang storie, oom. Hy het kinders." 
14         "Wag nou, hart," het tant Ans gekeer. "Hulle was goed vir ons kind in die vreemde." 
15         "Maar dis nonsens," het hy weer gesê. " 'n Mens trou of jy trou nie. Jy sit nie en kyk 
16 hoe die vrou dreig om haarself te vergiftig nie." 
17         Ek het my appeltert geëet. Dit was heerlik en ek het probeer proe wat dit was wat 
18 die tannie bygesit het sodat ek vir Johanna kon vertel. 
19         "Piet is darem nie so nie?" het die oom gevra.  
20         "Nee, oom." 
21         "Jy hou van hom?" 
22         "Ja, oom." 
23         Tant Ans het goedig gelag en haar dik grys hare van haar gesig gevee.
```"""


def get_novel_items():
    items = []

    # =========================================================================
    # VRAAG 6: ONDERWÊRELD – OPSTELVRAAG [25]
    # =========================================================================
    q6_memo = f"""VRAAG 6: ONDERWÊRELD – OPSTELVRAAG
Fanie Viljoen

Hierdie vraag word aan die hand van die aangehegte RUBRIEK VIR DIE NASIEN VAN DIE OPSTELVRAAG VIR DIE ROMAN EN DRAMA (bladsy 52) nagesien.

LET WEL:
• Dis 'n breë raamwerk van feite.
• Al die feite hoef nie genoem te word nie.

ARGUMENTE WORD AANGEBIED EN ONDERSTEUN OF GEÏLLUSTREER DEUR NA DIE TEKSTE TE VERWYS:

**Inleiding:**
Die kandidaat bied 'n gepaste inleiding aan.

**1. GREG SE INNERLIKE KONFLIK DRA BY TOT SY GELOOFWAARDIGHEID:**
- *Rou oor John se dood:* Greg se innerlike konflik maak hom geloofwaardig, want alhoewel hy sterk wil voorkom, rou hy nog oor sy broer John se selfdood. Hy moet sy hartseer wegsteek om sy pa tevrede te stel en sy ma bekommernis te spaar (Bl. 66: "Ek het nie gehuil toe John dood is nie. 'Jy sal nie!' het my pa beveel..."; Bl. 67: "Ek het vandag aan John gedink").
- *Trapper-ritueel:* Greg se innerlike stryd oor John se dood lei daartoe dat hy tydens die ontgroeningsritueel besluit om Eckardt nie in die donker tonnel te laat sak nie, omdat Eckardt se oë hom op daardie oomblik aan John herinner (Bl. 62–63: "Alles presies net soos my broer s'n... Toe trek ek hom self uit die donker gat").
- *Vasgevang in pa se verwagtings:* Greg voel vasgevang tussen sy pa se strawwe verwagtinge en die wete dat hy nie meer 'n spogstudent is nie (Bl. 55: "Maar ek doen dit om hom van my rug af te hou"; Bl. 106: "Ek verwag uitstekende resultate van jou..."). Hy deel nie sy pa se ambisie vir Turret Media nie (Bl. 48).
- *Eerlike wroeging oor leierskap:* Greg worstel met sy leierskap as hoofseun. Hy weet leiersposisies by Lawson Kollege word beïnvloed deur wie se pa die grootste skenkings maak (Bl. 58). Hy voel magteloos wanneer niemand hom ondersteun teen Dok Pienaar voor die rugbywedstryd nie (Bl. 76: "Nie een van die ander ouens het saam met my gestaan teen Dok nie. Is ek dan hulle leier?"). Hy voel skuldig dat hy dissipline versaak weens sy nagtelike kuberkrakery (Bl. 89).
- *Stryd tussen reg en verkeerd:* Wanneer 'n geveg in die wiskundeklas uitbreek, gryp hy nie in nie en wroeg daaroor (Bl. 56–57). Sy skoolwerk ly onder kuberkrakery en hy druip sy eerste wiskundetoets (Bl. 97, 99). Hy oorweeg selfs om sy punte op die skoolbediener te verander (Bl. 113).

**2. UITERLIKE KONFLIK BEKLEMTOON SY TOENEMENDE VASGEVANGENHEID:**
- *Konflik met sy pa:* Greg se pa eis volmaaktheid op die rugbyveld en akademies. Wanneer Greg weier om rugby te speel, ontketen dit hewige konfrontasie (Bl. 70–72). Sy pa dreig hom en beskuldig hom van ruggraatloosheid (Bl. 105–106).
- *Konflik met Nicole:* Sy verhouding met Nicole verbrokkel soos kuberkrakery en Eckardt se verdwyning hom verswelg; sy beskuldig hom van geheimsinnigheid en ontrouheid (Bl. 86, 92, 116–117).
- *Konflik met Eckardt:* Greg voel gemanipuleer en verraai deur Eckardt. Hy ontdek dat hy 'n pion was in Eckardt se wraakplan teen Dok Pienaar en Greg se pa (Bl. 72–73, 113–114, 159).
- *Konflik met Dokter Alec Pienaar:* Greg opponeer Dok Pienaar openlik oor Eckardt se verdwyning en verloor alle vertroue in die gesagsfiguur (Bl. 76–77). Dok dreig Greg om stil te bly oor Project Nursery Rhyme (Bl. 126–127).
- *Konflik met die polisie:* Die polisie ondervra hom as verdagte in Eckardt se verdwyning en lê beslag op sy skootrekenaar (Bl. 138–140).

**Slot:**
Die kandidaat bied 'n gepaste slot aan.

[25]

{NOVEL_RUBRIC}"""

    items.append({
        "item_id": f"{SOURCE_ID}-6",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "6",
        "marks": 25,
        "topic": "Roman: Onderwêreld (Fanie Viljoen) - Literêre Opstel",
        "passage": PASSAGE_ONDERWERELD_CONTEXT,
        "question": "Die hoofkarakter in die roman word deur middel van INNERLIKE en UITERLIKE KONFLIK gekarakteriseer.\n\nBespreek in 'n opstel van 400 tot 450 woorde hoe Greg se innerlike konflik tot sy geloofwaardigheid as hoofkarakter bydra EN hoe uiterlike konflik sy toenemende vasgevangenheid uitbeeld. [25]",
        "memo": q6_memo,
        "final_answer": "Greg se innerlike konflik (onverwerkte rou oor John, worsteling met sy pa se onrealistiese verwagtinge, leierskaptwyfel as hoofseun en morele wroeging oor kuberkrakery) maak hom 'n feilbare, geloofwaardige adolessent, terwyl sy uiterlike botsings met sy pa, Nicole, Dok Pienaar en die polisie sy toenemende vasgevangenheid in 'n netwerk van korrupsie en manipulasie beklemtoon.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # =========================================================================
    # VRAAG 7: ONDERWÊRELD – KONTEKSTUELE VRAAG [25]
    # =========================================================================
    # 7.1
    items.append({
        "item_id": f"{SOURCE_ID}-7.1",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "7.1",
        "marks": 2,
        "topic": "Roman: Onderwêreld (Fanie Viljoen) - Kontekstueel",
        "passage": PASSAGE_TEKS_A,
        "question": "Verwys na reël 1 en 2.\n\nWat wil Eckardt op hierdie stadium van die roman bereik as hy vir Greg wys dat hy 'n reisagentskap se systems kan hack EN wat is sy uiteindelike doel agter die oënskynlik onskuldige kuberkraakaktiwiteite? (2)",
        "memo": "* Eckardt wil vir Greg nuuskierig maak / sosiaal manipuleer om kuberkraakvaardighede te leer. $\\checkmark$\n\nEN\n\n* Eckardt se uiteindelike doel is om Greg te gebruik om Dok Pienaar en Greg se pa se onwettige kuberkrakery/Project Nursery Rhyme/korrupsieaktiwiteite te ontbloot / wraak te neem op Dok Pienaar en Greg se pa. $\\checkmark$",
        "final_answer": "Eckardt wil Greg nuuskierig maak en hom manipuleer om te leer hack; sy uiteindelike doel is om Greg as pion te gebruik om Dok Pienaar en Greg se pa se onwettige aktiwiteite (Project Nursery Rhyme) oop te vlek en wraak te neem.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 7.2
    items.append({
        "item_id": f"{SOURCE_ID}-7.2",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "7.2",
        "marks": 4,
        "topic": "Roman: Onderwêreld (Fanie Viljoen) - Kontekstueel",
        "passage": PASSAGE_TEKS_A,
        "question": "Verwys na Eckardt se groetwoorde in reël 3 en 4.\n\nVerduidelik hoe Eckardt se woorde \"slapend gevou lê\" letterlik EN figuurlik op Greg op hierdie stadium van die roman van toepassing is. In watter opsig kan die mitologiese naam \"Zeus\" enersyds na Greg self en andersyds na Greg se pa verwys? (4)",
        "memo": "* **Letterlik:** Greg is slaperig / slaap laat / lê nog in die bed toe Eckardt hom wakker maak. $\\checkmark$\n* **Figuurlik:** Greg is onbewus van die gevare / onbewus van Eckardt se ware motiewe / leef in salige onkunde oor die onderwêreld en korrupsie. $\\checkmark$\n\nEN\n\n* **Zeus as Greg:** Greg is die hoofseun van Lawson Kollege en beklee die hoogste magsposisie onder die leerders (soos Zeus op Olimpus). $\\checkmark$\n* **Zeus as Greg se pa:** Greg se pa is 'n magtige mediamagnaat wat mag en beheer uitoefen oor sy gesin en besigheid. $\\checkmark$",
        "final_answer": "Letterlik: Greg lê nog vas aan die slaap in sy bed; Figuurlik: Greg is onbewus van die gevaar en Eckardt se verborge wraakplan; Zeus as Greg: Hy is hoofseun met oënskynlike mag oor die skool; Zeus as pa: Sy pa is 'n magtige en dominerende mediamagnaat.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 7.3
    items.append({
        "item_id": f"{SOURCE_ID}-7.3",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "7.3",
        "marks": 3,
        "topic": "Roman: Onderwêreld (Fanie Viljoen) - Kontekstueel",
        "passage": PASSAGE_TEKS_A,
        "question": "Verwys na reël 8.\n\nDink jy Greg se reaksie op mnr. Andersen se vraag aan hom die dag voor die skool geopen het, was die waarheid teen die agtergrond van sy reaksie op Eckardt se drawwery? Motiveer jou antwoord. Noem nog TWEE aspekte van Eckardt as karakter wat hom van die ander matriekleerders onderskei. (3)",
        "memo": "Nee. Greg het vir mnr. Andersen voorgehou dat hy fiks en gereed is vir die seisoen / hard geoefen het, maar hy lê nog laat en slaap en prioritiseer nie fiksheid soos Eckardt nie. $\\checkmark$\n*(Die kandidaat kan nie 'n JA-antwoord aanbied nie.)*\n\nEN\n\nEnige TWEE van die volgende vir 1 punt elk:\n* Eckardt het eers in matriek by Lawson Kollege aangesluit $\\checkmark$\n* Hy kan diep gesprekke voer / het 'n wye algemene kennis $\\checkmark$\n* Hy is 'n buitestander / intens / lees baie $\\checkmark$\n* Hy neem nie aan sport deel nie $\\checkmark$\n* Sy uitsonderlike kennis oor rekenaars en kuberkrakery $\\checkmark$",
        "final_answer": "Nee, Greg het voorgegee dat hy fiks en gereed is, maar hy draf nie self vroegoggend nie; Twee aspekte van Eckardt: Hy neem nie aan skoolsport deel nie en hy beskik oor gevorderde kuber- en rekenaarkennis (of het eers in matriek aangesluit).",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 7.4
    items.append({
        "item_id": f"{SOURCE_ID}-7.4",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "7.4",
        "marks": 3,
        "topic": "Roman: Onderwêreld (Fanie Viljoen) - Kontekstueel",
        "passage": PASSAGE_TEKS_A,
        "question": "Verwys na reëls 11 tot 13.\n\nIn watter opsig is Greg se woorde oor die opdrag: \"Pouse moet ek, in opdrag van Dok,\" selfkarakteriserend? Dui Greg se agterdog teenoor mnr. Andersen op 'n probleem wat Greg met gesagsfigure het? Motiveer jou antwoord deur na TWEE ander botsings met gesagsfigure te verwys. (3)",
        "memo": "* Greg se woorde dui daarop dat hy nie selfgedrewe is nie / nie sy hoofseunskap ernstig opneem nie / nie inisiatief neem nie / bloot bevele van bo uitvoer. $\\checkmark$\n\nEN\n\n* Ja $\\checkmark$\n* TWEE ander botsings (enige twee vir 1 punt elk):\n  - Greg wantrou sy pa en bots met hom oor rugby, skoolwerk en hoofseunskap $\\checkmark$\n  - Greg opponeer Dok Pienaar oor Eckardt se verdwyning voor die rugbywedstryd $\\checkmark$\n  - Greg raak opstandig teenoor sersant Botha / inspekteur Cele tydens die polisie-ondervraging / verontagsaam die polisie se verbod op kuberkrakery $\\checkmark$",
        "final_answer": "Selfkarakterisering: Greg neem nie self inisiatief as leier nie, maar tree slegs op bevel van Dok op; Probleem met gesagsfigure: Ja, hy bots met sy pa oor rugby en akademiese druk, en konfronteer Dok Pienaar oor Eckardt se verdwyning (of daag die polisie uit).",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 7.5
    items.append({
        "item_id": f"{SOURCE_ID}-7.5",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "7.5",
        "marks": 2,
        "topic": "Roman: Onderwêreld (Fanie Viljoen) - Kontekstueel",
        "passage": PASSAGE_TEKS_B,
        "question": "Verwys na reëls 3 en 4: \"Sy het soveel hoop vir my; 'n anderste hoop as my pa.\"\n\nIn watter opsig verskil Greg se ma se hoop vir hom van dié van sy pa? (2)",
        "memo": "* Greg se ma hoop (veral ná John se selfdood) dat Greg gelukkig sal wees en emosioneel heel sal bly / nie ook selfdood sal oorweeg nie. $\\checkmark$\n* Greg se pa hoop dat Greg akademies en op die rugbyveld sal presteer sodat hy die nuwe opvolger vir Turret Media kan word / 'n vertoonstuk vir sy eie sukses kan wees. $\\checkmark$",
        "final_answer": "Sy ma hoop dat hy emosioneel gelukkig en veilig sal wees (sonder selfmoordgedagtes), terwyl sy pa slegs materiële sukses, sportprestasie en opvolging by Turret Media van hom eis.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 7.6
    items.append({
        "item_id": f"{SOURCE_ID}-7.6",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "7.6",
        "marks": 1,
        "topic": "Roman: Onderwêreld (Fanie Viljoen) - Kontekstueel",
        "passage": PASSAGE_TEKS_B,
        "question": "Verwys na reël 19: \"Koue rillings loop oor my ruggraat.\"\n\nWaarom is Greg se reaksie ironies teen die agtergrond van sy pa se vroeëre woorde aan hom? (1)",
        "memo": "Aangesien Greg hom so vererg het vir sy pa se insinuasie dat hy nie 'n ruggraat het nie, sou 'n mens verwag dat Greg beheer neem / vaste besluite kan maak oor konflikkwessies, MAAR hy is steeds bang / huiwerig / het steeds nie 'n ruggraat wanneer hy met sy pa gekonfronteer word nie. $\\checkmark$\n*(Die kandidaat moet beide kante van die ironie aandui.)*",
        "final_answer": "Sy pa het hom daarvan beskuldig dat hy nie 'n ruggraat het nie; dit is ironies dat Greg juis nou bewerig en vreesbevange raak (koue rillings oor sy ruggraat) pleks van vasberade optree.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 7.7.1
    items.append({
        "item_id": f"{SOURCE_ID}-7.7.1",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "7.7.1",
        "marks": 3,
        "topic": "Roman: Onderwêreld (Fanie Viljoen) - Kontekstueel",
        "passage": PASSAGE_TEKS_B,
        "question": "Verwys na reëls 7 tot 9.\n\n7.7.1 Noem DRIE dinge wat Greg oor Dok Pienaar uitgevind het wat hy van sy ma weerhou het. (3)",
        "memo": "Enige DRIE van die volgende vir 1 punt elk:\n* Greg ontdek Dok Pienaar is die Butcher / kuberleier $\\checkmark$\n* Greg ontdek Dok Pienaar is aan die stuur van Project Nursery Rhyme $\\checkmark$\n* Greg ontdek Dok Pienaar is (saam met Greg se pa) verantwoordelik vir die verspreiding van die voëlgriepvirus/epidemie $\\checkmark$\n* Greg ontdek Dok Pienaar besit 'n farmaseutiese maatskappy (Plus Ultramed) $\\checkmark$\n* Greg vind uit Dok Pienaar het 'n vorige saak van binnekennishandel (\"insider trading\") teen hom $\\checkmark$\n* Greg vind uit dat Dok Pienaar destyds die regter omgekoop het om die saak te laat verdwyn $\\checkmark$",
        "final_answer": "Drie dinge: Dok Pienaar is die kuberbaas 'die Butcher'; hy bestuur Project Nursery Rhyme wat 'n voëlgriepvirus versprei het; hy besit Plus Ultramed en het voorheen 'n regter omgekoop om 'n bedrogsaak te skrap.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 7.7.2
    items.append({
        "item_id": f"{SOURCE_ID}-7.7.2",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "7.7.2",
        "marks": 2,
        "topic": "Roman: Onderwêreld (Fanie Viljoen) - Kontekstueel",
        "passage": PASSAGE_TEKS_B,
        "question": "Verwys na reëls 7 tot 9.\n\n7.7.2 Watter inligting sou Greg se ma aan hom kon gee wat 'n invloed op sy ondersoek na Dok Pienaar kon hê? Dink jy dié inligting sou die verloop van die roman beïnvloed het? Motiveer jou antwoord. (2)",
        "memo": "* Greg se ma sou hom kon meedeel dat Greg se pa en Dok Pienaar voorheen aangekla is vir bedrog / voorheen saamgewerk het / vennote was in bedenklike sake. $\\checkmark$\n\nEN\n\n* **Ja:** Indien Greg geweet het dat sy eie pa ook aandadig en skuldig is, sou hy moontlik gehuiwer het om die saak verder te ondersoek om sy gesin te beskerm. $\\checkmark$\n* **OF**\n* **Nee:** Die dryfkrag om Eckardt te vind en die waarheid uit te vind was reeds te sterk / die polisie het reeds beslag gelê op sy rekenaar sodat hy nie kon omdraai nie. $\\checkmark$",
        "final_answer": "Inligting: Dat sy pa en Dok Pienaar vennote was in 'n vroeëre korrupsiesaak; Invloed: Ja (hy sou huiwer om sy eie pa te ontbloot) OF Nee (sy begeerte om Eckardt te vind en sy eie onskuld te bewys was te sterk).",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 7.8
    items.append({
        "item_id": f"{SOURCE_ID}-7.8",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "7.8",
        "marks": 1,
        "topic": "Roman: Onderwêreld (Fanie Viljoen) - Kontekstueel",
        "passage": PASSAGE_TEKS_B,
        "question": "Verwys na reël 16: \"Ma moenie vir Pa vertel nie, asseblief.\"\n\nWatter ooreenkoms toon Greg se versoek met die verhouding tussen Eckardt en sy pa? (1)",
        "memo": "Eckardt se pa het hóm ook gevra om nie vir sy ma van die selfdoodpoging/finansiële ruïnering te vertel nie / albei gesinne word gekenmerk deur geheime tussen pa en seun wat vir die ma weerhou word. $\\checkmark$",
        "final_answer": "Eckardt se pa het ook vir Eckardt gevra om sy selfmoordpoging en mislukkings van sy ma geheim te hou.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 7.9
    items.append({
        "item_id": f"{SOURCE_ID}-7.9",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "7.9",
        "marks": 2,
        "topic": "Roman: Onderwêreld (Fanie Viljoen) - Kontekstueel",
        "passage": PASSAGE_TEKS_B,
        "question": "Verwys na reël 25: \"Ek gee nie om nie, Greg. Ek kom.\"\n\nIn watter opsig verskil Greg se ma se houding teenoor Lawson Kollege op hierdie stadium met haar latere optrede teenoor die skool? Dink jy dié verandering in optrede is geregverdig? Motiveer jou antwoord. (2)",
        "memo": "* Aanvanklik is Greg se ma besorgd oor die gesin se goeie naam en Greg se posisie by Lawson Kollege, terwyl sy haar later sterk teen die skool uitspreek / dreig om Greg dadelik uit die skool te haal / meer besorgd oor Greg se welstand is as oor die skool se beeld. $\\checkmark$\n\nEN\n\n* **Ja:** Wanneer sy ontdek dat Dok Pienaar gearresteer is weens Project Nursery Rhyme en dat misdaad binne die skool floreer, besef sy dat haar kind se lewe en welstand belangriker is as die skool se aansien. $\\checkmark$\n*(Die kandidaat kan nie 'n NEE-antwoord aanbied nie.)*",
        "final_answer": "Verskil: Aanvanklik buig sy voor die skool en pa se aansien, maar later daag sy Lawson Kollege uit en wil sy Greg dadelik verwyder; Regverdig: Ja, want sy besef die skoolomgewing onder Dok Pienaar is korrup en gevaarlik vir haar kind.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 7.10
    items.append({
        "item_id": f"{SOURCE_ID}-7.10",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "7.10",
        "marks": 2,
        "topic": "Roman: Onderwêreld (Fanie Viljoen) - Kontekstueel",
        "passage": PASSAGE_TEKS_A + "\n\n" + PASSAGE_TEKS_B,
        "question": "Herlees die volgende reëls:\n\nTEKS A (reël 17 en 18): \"Ek kry vir Eckardt op pad na die Engelsklas. 'Jy onthou nog van jou belofte van gisteraand, nè!' herinner ek hom.\"\nTEKS B (reël 7): \"Ek begin haar vertel van Eckardt, dat hy 'n hacker is, dat hy my geleer het.\"\n\nNa watter onderwêreld verwys TEKS A en TEKS B? Hoe het Greg se woorde in TEKS A 'n direkte invloed op die gebeure in TEKS B gehad? (2)",
        "memo": "* Die onderwêreld van kuberkrakery / rekenaarmisdaad. $\\checkmark$\n\nEN\n\n* In TEKS A herinner Greg vir Eckardt aan sy belofte om hom te leer hack, wat daartoe lei dat Greg aktief begin kuberkraak en gevolglik in TEKS B deur die polisie ondersoek word en sy rekenaar gekonfiskeer word. $\\checkmark$",
        "final_answer": "Onderwêreld: Die donker onderwêreld van rekenaarkuberkrakery; Invloed: Greg se aandrang om te leer hack lei regstreeks daartoe dat hy 'n hacker word en later deur die polisie ondervra word wanneer Eckardt verdwyn.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # =========================================================================
    # VRAAG 8: MANAKA PLEK VAN DIE HORINGS – OPSTELVRAAG [25]
    # =========================================================================
    q8_memo = f"""VRAAG 8: MANAKA PLEK VAN DIE HORINGS – OPSTELVRAAG
Pieter Pieterse

Hierdie vraag word aan die hand van die aangehegte RUBRIEK VIR DIE NASIEN VAN DIE OPSTELVRAAG VIR DIE ROMAN EN DRAMA (bladsy 52) nagesien.

LET WEL:
• Dis 'n breë raamwerk van feite.
• Al die feite hoef nie genoem te word nie.

ARGUMENTE WORD AANGEBIED EN ONDERSTEUN OF GEÏLLUSTREER DEUR NA DIE TEKSTE TE VERWYS:

**Inleiding:**
Die kandidaat bied 'n gepaste inleiding aan.

**1. BAAS SE INNERLIKE KONFLIK DRA BY TOT SY GELOOFWAARDIGHEID:**
- *Geloofstwyfel en verlies:* Baas se innerlike konflik spruit uit die traumatiese moord op sy ouers en die verlies van hul familieplaas. Dit maak hom 'n bitter, siniese en geloofwaardige karakter wat God blameer en weier om te bid (Bl. 11, 41: "Vir my gebid?").
- *Herinneringe en trauma:* Die lied Amazing Grace en die kitaarspel ontketen erge naarheid en skuldgevoelens omdat dit hom herinner aan sy ouers se geloof en sy eie afvalligheid (Bl. 80, 115).
- *Liefde teenoor isolasie:* Baas worstel met sy groeiende gevoelens vir Grace. Hy wil haar beskerm en naby hom hou, maar vrees emosionele verbintenis weens sy vrees om weer iemand te verloor (Bl. 95, 142).
- *Aanvaarding van roeping:* Hy worstel met sy familie-erflating – sy oupagrootjie se droom om 'n sendingstasie en skuiling op Manaka te bou – terwyl hy self net wil vlug en buffels jag (Bl. 67, 134).

**2. UITERLIKE KONFLIK VERSTERK SY GEVOEL VAN MAGTELOOSHEID:**
- *Konflik met Kebbey:* Baas bots met die hoofindoena Kebbey oor die pontboot en oor Grace. Wanneer Kebbey geld by Baas eis om met Grace te trou, voel Baas magteloos omdat hy Grace wil beskerm maar nie die tradisies van die khuta kan beheer nie (Bl. 188–189).
- *Konflik met die sendelinge (Muluti Malila):* Baas stoot die sendelinge weg wanneer hulle vir hom wil bid of dienste wil hou, wat sy isolasie vergroot (Bl. 78–79).
- *Konflik met Whitey:* Whitey se drankmisbruik en onvoorspelbare aankomste bring spanning, maar konfronteer Baas ook met die familiebloedlyn en gewere wat hulle deel (Bl. 120–123).
- *Konflik met die natuur en buffels:* Baas se jag op die buffel Morena versinnebeeld sy stryd teen die dood en vernietiging; die buffel se horings word 'n simbool van sowel mag as magteloosheid op Manaka (Bl. 156–160).

**Slot:**
Die kandidaat bied 'n gepaste slot aan.

[25]

{NOVEL_RUBRIC}"""

    items.append({
        "item_id": f"{SOURCE_ID}-8",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "8",
        "marks": 25,
        "topic": "Roman: Manaka Plek van die Horings (Pieter Pieterse) - Literêre Opstel",
        "passage": PASSAGE_MANAKA_CONTEXT,
        "question": "Die hoofkarakter in die roman word deur middel van INNERLIKE en UITERLIKE KONFLIK gekarakteriseer.\n\nBespreek in 'n opstel van 400 tot 450 woorde hoe Baas se innerlike konflik tot sy geloofwaardigheid as hoofkarakter bydra EN hoe uiterlike konflik sy toenemende gevoel van magteloosheid versterk. [25]",
        "memo": q8_memo,
        "final_answer": "Baas se innerlike konflik oor sy ouers se gewelddadige dood, sy verlies aan geloof en sy ontluikende gevoelens vir Grace maak hom 'n eg menslike en geloofwaardige karakter, terwyl uiterlike botsings met Kebbey, Muluti Malila en die ongenaakbare Caprivi-omgewing sy magteloosheid en stryd om oorlewing versterk.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # =========================================================================
    # VRAAG 9: MANAKA PLEK VAN DIE HORINGS – KONTEKSTUELE VRAAG [25]
    # =========================================================================
    # 9.1
    items.append({
        "item_id": f"{SOURCE_ID}-9.1",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "9.1",
        "marks": 1,
        "topic": "Roman: Manaka Plek van die Horings (Pieter Pieterse) - Kontekstueel",
        "passage": PASSAGE_TEKS_C,
        "question": "Wie is dit wat vir Baas hande klap en dan teen die bult af \"hoepel\"? (1)",
        "memo": "Meneer Johnnie $\\checkmark$",
        "final_answer": "Meneer Johnnie",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 9.2
    items.append({
        "item_id": f"{SOURCE_ID}-9.2",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "9.2",
        "marks": 4,
        "topic": "Roman: Manaka Plek van die Horings (Pieter Pieterse) - Kontekstueel",
        "passage": PASSAGE_TEKS_C,
        "question": "Verwys na reël 4: \"Ek sal baie graag vir jou 'n gebed wil doen, neef.\"\n\nWaarom sou die leser kon dink dat muluti Malila vir Baas móét bid? Noem TWEE sake. Watter ander TWEE mense het ook beleef dat Baas hulle van hom wegstoot toe hulle oor geloof wil praat? (4)",
        "memo": "* TWEE sake waarom Malila vir Baas moet bid (enige twee vir 1 punt elk):\n  - Baas twyfel op hierdie stadium aan sy geloof / Christenskap $\\checkmark$\n  - Baas wil nie glo dat hy met 'n doel/rede na Manaka gestuur is nie $\\checkmark$\n  - Baas weier om saam met die sendelinge 'n tafelgebed te doen $\\checkmark$\n\nEN\n\n* TWEE ander mense:\n  - Grace $\\checkmark$\n  - Ouma Essie $\\checkmark$",
        "final_answer": "Redes vir gebed: Baas twyfel aan God en weier om saam met die sendelinge te bid; Twee ander mense: Grace en Ouma Essie.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 9.3
    items.append({
        "item_id": f"{SOURCE_ID}-9.3",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "9.3",
        "marks": 2,
        "topic": "Roman: Manaka Plek van die Horings (Pieter Pieterse) - Kontekstueel",
        "passage": PASSAGE_TEKS_C,
        "question": "Wat, dink jy, kan as oorsaak vir Baas se sinisme oor geloof beskou word? Gee TWEE feite. (2)",
        "memo": "TWEE feite (1 punt elk):\n* Die wrede moord op Baas se ouers $\\checkmark$\n* Die verlies van Baas se familieplaas $\\checkmark$\n\n*(Die kandidaat bied 'n soortgelyke antwoord vir EEN punt elk aan.)*",
        "final_answer": "Die gewelddadige moord op sy ouers en die verlies van sy geliefde familieplaas.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 9.4
    items.append({
        "item_id": f"{SOURCE_ID}-9.4",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "9.4",
        "marks": 3,
        "topic": "Roman: Manaka Plek van die Horings (Pieter Pieterse) - Kontekstueel",
        "passage": PASSAGE_TEKS_C,
        "question": "Verwys na reëls 14 tot 17.\n\nWaarom raak Grace by Baas se lewe betrokke EN op watter TWEE maniere vergemaklik sy Baas se lewe ná die koms van die sendelinge? (3)",
        "memo": "* Grace voel dat sy haar lewe aan Baas verskuldig is omdat hy haar lewe gered en versorg het toe sy ernstig siek was aan malaria. $\\checkmark$\n\nEN\n\n* TWEE maniere waarop sy sy lewe vergemaklik (enige twee vir 1 punt elk):\n  - Grace versorg sy honde $\\checkmark$\n  - Grace hanteer die vleisverkope $\\checkmark$\n  - Grace tree as tolk op wanneer Baas met die Lozi's / khuta moet praat $\\checkmark$\n  - Grace neem beheer oor sy ruilhandel $\\checkmark$",
        "final_answer": "Rede: Baas het haar lewe gered toe sy malaria gehad het; Twee maniere: Sy versorg sy honde en tree as tolk op in sy onderhandelinge met die Lozi-gemeenskap (of hanteer vleisverkope en ruilhandel).",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 9.5
    items.append({
        "item_id": f"{SOURCE_ID}-9.5",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "9.5",
        "marks": 2,
        "topic": "Roman: Manaka Plek van die Horings (Pieter Pieterse) - Kontekstueel",
        "passage": PASSAGE_TEKS_C,
        "question": "Verwys na reël 18: \"Die moerasfiskale hou op roep.\"\n\nBespreek TWEE funksies wat die feit dat die moerasfiskale ophou roep, binne die konteks van die teks het. (2)",
        "memo": "TWEE funksies (enige twee vir 1 punt elk):\n* Die skielike stilte veroorsaak dat Baas die kitaarklanke en Nanna se stem duidelik hoor $\\checkmark$\n* Dit dwing hom om te luister na die woorde van Amazing Grace wat hom aan sy verlede en geloof herinner $\\checkmark$\n* Dit beklemtoon die emosionele spanning en konfrontasie met sy eie herinneringe en sy gemis aan sy ouers $\\checkmark$\n\n*(Die kandidaat bied enige TWEE antwoorde vir EEN punt elk aan.)*",
        "final_answer": "Die stilte skep 'n atmosfeer waarin Baas die woorde van Amazing Grace helder kan hoor, wat hom dwing om sy verlede, sy skuldgevoelens en sy gemis aan sy ouers in die oë te kyk.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 9.6
    items.append({
        "item_id": f"{SOURCE_ID}-9.6",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "9.6",
        "marks": 3,
        "topic": "Roman: Manaka Plek van die Horings (Pieter Pieterse) - Kontekstueel",
        "passage": PASSAGE_TEKS_C,
        "question": "In watter opsig, dink jy, kan die lied Amazing Grace, wat as herhalende motief in die roman voorkom, enersyds as 'n beskuldiging EN andersyds as 'n waarskuwing beskou word? Watter emosie wat deur die lied opgeroep word, veroorsaak die \"naarheid\" (reël 22)? (3)",
        "memo": "* **Beskuldiging:** Baas voel skuldig omdat hy in sy geloof twyfel, nie sy roeping wil aanvaar nie, en sy ouers se Christelike waardes en opvoeding versaak het. $\\checkmark$\n* **Waarskuwing:** Die lied waarsku hom dat hy sy rug op God se genade en die ewige lewe gedraai het en as 'n verlorene kan sterf as hy nie tot inkeer kom nie. $\\checkmark$\n\nEN\n\n* **Emosie:** Ontsteltenis / intense hartseer / skuldgevoel $\\checkmark$",
        "final_answer": "Beskuldiging: Dit kla hom aan omdat hy sy ouers se geloof en sy roeping versaak het; Waarskuwing: Dit waarsku dat hy sonder God se genade geestelik verlore sal bly; Emosie: Intense skuldgevoel en ontsteltenis.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 9.7
    items.append({
        "item_id": f"{SOURCE_ID}-9.7",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "9.7",
        "marks": 2,
        "topic": "Roman: Manaka Plek van die Horings (Pieter Pieterse) - Kontekstueel",
        "passage": PASSAGE_TEKS_D,
        "question": "Verwys na reëls 1 tot 4.\n\nVerduidelik in watter opsig Whitey se aankoms op Manaka selfkarakteriserend is. Hoe skakel hierdie optrede met Baas se eerste ontmoeting met Whitey? (2)",
        "memo": "* Whitey openbaar die karaktertrek van hulpvaardigheid en omgee – hy bring planke en stutpaaltjies om Baas te help. $\\checkmark$\n* **Skakeling met eerste ontmoeting:** Baas het vir Whitey ontmoet toe Whitey vir hom en Grace 'n gratis saamrygeleentheid van die hospitaal af gegee het en geweier het om geld daarvoor te aanvaar. $\\checkmark$\n\nOF\n\n* Whitey daag op met 'n bottel brandewyn, wat sy liefde vir en afhanklikheid van drank weerspieël. $\\checkmark$\n* **Skakeling met eerste ontmoeting:** Toe Baas hom die eerste keer ontmoet het, het Whitey onder die invloed van drank bestuur. $\\checkmark$",
        "final_answer": "Selfkarakteriserend: Whitey is goedgeaard en hulpvaardig (bring planke); Skakeling: Hy het Baas en Grace die eerste keer gratis van die hospitaal af opgelaai (OF sy brandewyn weerspieël sy drankprobleem net soos toe hy dronk bestuur het toe hulle mekaar ontmoet het).",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 9.8
    items.append({
        "item_id": f"{SOURCE_ID}-9.8",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "9.8",
        "marks": 1,
        "topic": "Roman: Manaka Plek van die Horings (Pieter Pieterse) - Kontekstueel",
        "passage": PASSAGE_TEKS_D,
        "question": "Verwys na reël 8 en 9: \"Jy het daardie dag gesê jy wil bankies bou.\"\n\nWaarom is dit ironies dat Baas op daardie stadium van die roman al die indruk geskep het dat hy die bankies onder die worsboom wil herbou? (1)",
        "memo": "'n Mens sou verwag dat Baas, wat op daardie stadium nog heeltemal teen geloof gekant was, niks met die kerkdiens of sendingstasie te doen sou wou hê nie, MAAR hy herbou juis die kerk se bankies waar mense vir dienste sit. $\\checkmark$\n*(Die kandidaat moet beide kante van die ironie aandui.)*",
        "final_answer": "Dit is ironies dat Baas, wat enige kontak met godsdiens en gebed hardkoppig verwerp, self die bankies bou sodat mense kerkdienste onder die worsboom kan bywoon.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 9.9
    items.append({
        "item_id": f"{SOURCE_ID}-9.9",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "9.9",
        "marks": 3,
        "topic": "Roman: Manaka Plek van die Horings (Pieter Pieterse) - Kontekstueel",
        "passage": PASSAGE_TEKS_D,
        "question": "Daar word telkens na gewere in hierdie teks verwys.\n\nWatter belangrike rol speel Baas EN Whitey se gewere ten opsigte van hulle twee se verbintenis met mekaar? In watter opsig was Baas se geweer instrumenteel tot sy koms na Manaka EN hoe skakel dit met die naam van die roman? (3)",
        "memo": "* **Rol van gewere in verbintenis:** Beide Whitey en Baas se antieke gewere is erflukse wat van dieselfde oupagrootjie afkomstig is, wat bewys dat hulle familie en neefs is. $\\checkmark$\n* **Instrumenteel tot koms:** Baas het sy Mott Mauser-geweer na Manaka saamgebring om buffels te jag en sy wraak/hartseer uit te leef. $\\checkmark$\n* **Skakeling met titel:** Manaka beteken \"Plek van die horings\"; Baas kap die buffel Morena se horings (en ander buffelhorings) by die naambordjie vas. $\\checkmark$",
        "final_answer": "Verbintenis: Albei se gewere kom van hul gedeelde oupagrootjie wat hul familieband bevestig; Koms na Manaka: Baas het sy geweer gebring om buffels te jag; Titel: 'Manaka' beteken Plek van die horings, waar hy die buffelhorings aanbring.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 9.10
    items.append({
        "item_id": f"{SOURCE_ID}-9.10",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "9.10",
        "marks": 2,
        "topic": "Roman: Manaka Plek van die Horings (Pieter Pieterse) - Kontekstueel",
        "passage": PASSAGE_TEKS_D,
        "question": "Wie se portret hang in Baas se woonplek teen die muur? Dink jy dit is geregverdig dat dié portret daar hang en nie een van sy ouers nie? Motiveer jou antwoord. (2)",
        "memo": "* Baas se oupagrootjie se portret hang teen sy muur. $\\checkmark$\n\nEN\n\n* **Ja:** Dit is Baas se lewensdoel om sy oupagrootjie se droom op Manaka te verwesenlik / om 'n foto van sy ouers daar te hê bring te veel pyn en bitterheid oor hul moord mee. $\\checkmark$",
        "final_answer": "Portret: Sy oupagrootjie; Regverdig: Ja, want sy oupagrootjie se visie inspireer sy werk op Manaka, terwyl 'n portret van sy ouers hom te veel aan hul gewelddadige dood herinner.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 9.11
    items.append({
        "item_id": f"{SOURCE_ID}-9.11",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "9.11",
        "marks": 2,
        "topic": "Roman: Manaka Plek van die Horings (Pieter Pieterse) - Kontekstueel",
        "passage": PASSAGE_TEKS_C + "\n\n" + PASSAGE_TEKS_D,
        "question": "Herlees die volgende reëls:\n\nTEKS C (reël 10 en 11): \" 'Miskien huil hy oor homself.' Baas roer nie. Hy kantel sy kop en maak weer sy oë toe.\"\nTEKS D (reël 15): \"Jy weet mos ek hou nie van koffie nie en koffie hou nie van my nie.\"\n\nIn TEKS C praat Grace en Baas oor hoe 'n mens oor ander mense huil. Watter verwyt het Baas vroeër in die roman teenoor Grace geopper oor die dood van sy ouers? Dink jy Whitey help Baas om dié houding van hom af te skud? Motiveer jou antwoord deur na TEKS D te verwys. (2)",
        "memo": "* Baas het Grace verwyt dat sy van hom verwag om haar mense te help nadat sy ouers deur \"barbare\" vermoor is (terwyl haar eie ouers ook vermoor is). $\\checkmark$\n\nEN\n\n* **Ja:** Whitey vertel vir Baas dat Grace se ouers in 'n landmynontploffing gesterf het en laat Baas skuldig voel oor sy ongevoeligheid / Whitey se besoek en hul gedeelde familie-erflating help Baas besef dat dit sy bestemming is om mense te help. $\\checkmark$",
        "final_answer": "Verwyt: Baas het haar verwyt dat sy van hom verwag om haar mense te dien nadat sy ouers vermoor is; Whitey se hulp: Ja, Whitey help hom besef dat Grace ook tragiese verlies gely het en dat diensbaarheid in hul familie se bloed is.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # =========================================================================
    # VRAAG 10: VATMAAR – OPSTELVRAAG [25]
    # =========================================================================
    q10_memo = f"""VRAAG 10: VATMAAR – OPSTELVRAAG
AHM Scholtz

Hierdie vraag word aan die hand van die aangehegte RUBRIEK VIR DIE NASIEN VAN DIE OPSTELVRAAG VIR DIE ROMAN EN DRAMA (bladsy 52) nagesien.

LET WEL:
• Dis 'n breë raamwerk van feite.
• Al die feite hoef nie genoem te word nie.

ARGUMENTE WORD AANGEBIED EN ONDERSTEUN OF GEÏLLUSTREER DEUR NA DIE TEKSTE TE VERWYS:

**Inleiding:**
Die kandidaat bied 'n gepaste inleiding aan.

**1. KENNETH SE INNERLIKE KONFLIK:**
- *Groot hartseer oor Kaaitjie:* Kenneth arriveer in Vatmaar met 'n gebroke hart ná die dood van Kaaitjie en hul ongebore baba. Hy worstel met rou en skuldgevoelens omdat hy haar nie kon red nie.
- *Afstand en selfbeskerming:* Sy pyn veroorsaak dat hy aanvanklik emosionele afstand van ander bewaar (soos teenoor Teacher Elsa se toenadering).
- *Stryd met identiteit:* As buitestander en bruinman in 'n rassistiese samelewing moet hy sy eie plek en waarde vind te midde van armoede en vooroordele.

**2. POSITIEWE VERSKIL IN DIE MENSE SE LEWENS:**
- *Bou van Kliniek Katrina:* Kenneth neem die inisiatief om 'n kliniek in Vatmaar op te rig sodat niemand weer weens 'n gebrek aan basiese mediese sorg hoef te sterf soos Kaaitjie nie. Hy bewerkstellig samewerking met die hospitaal en dorpsraad.
- *Sokkerveld en sportontwikkeling:* Hy meet die sokkerveld uit, skenk kalk en pale, en organiseer fondse. Dit bring gesonde ontspanning en dorptrots vir die Vatmaar Sunbeam-span.
- *Karakterverandering by Boitjie Afrika:* Kenneth se leiding inspireer Boitjie om op te hou dagga rook en 'n gerespekteerde sokkerafrigter en leiersfiguur te word.
- *Bemagtiging van die gemeenskap:* Hy help ongeletterde inwoners soos Boitjie om amptelike briewe aan die dorpsraad te skryf en leer hulle om hul stem dik te maak.
- *Sosiale kohesie:* Hy bring mense van verskillende agtergronde (Ou Chetty, Mister Burns, Sus Bet, die predikant) saam om 'n trotse, selfstandige gemeenskap te bou.

**Slot:**
Die kandidaat bied 'n gepaste slot aan.

[25]

{NOVEL_RUBRIC}"""

    items.append({
        "item_id": f"{SOURCE_ID}-10",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "10",
        "marks": 25,
        "topic": "Roman: Vatmaar (A.H.M. Scholtz) - Literêre Opstel",
        "passage": PASSAGE_VATMAAR_CONTEXT,
        "question": "In die roman, Vatmaar, slaag Kenneth Kleinhans daarin om, ten spyte van sy eie innerlike konflik, 'n positiewe verskil in die mense om hom se lewens te maak.\n\nBespreek hierdie stelling in 'n opstel van 400 tot 450 woorde. [25]",
        "memo": q10_memo,
        "final_answer": "Ten spyte van Kenneth Kleinhans se diep hartseer en emosionele isolasie ná Kaaitjie se dood, kanaliseer hy sy pyn in onbaatsugtige diens aan Vatmaar: hy rig Kliniek Katrina op om lewens te red, meet die sokkerveld uit wat dorptrots en ontspanning bring, help Boitjie Afrika om sy lewe te hervorm, en bemagtig die gemeenskap deur amptelike briewe en selfrespek.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # =========================================================================
    # VRAAG 11: VATMAAR – KONTEKSTUELE VRAAG [25]
    # =========================================================================
    # 11.1
    items.append({
        "item_id": f"{SOURCE_ID}-11.1",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "11.1",
        "marks": 2,
        "topic": "Roman: Vatmaar (A.H.M. Scholtz) - Kontekstueel",
        "passage": PASSAGE_TEKS_E,
        "question": "Wat was die naam van die kliniek EN wat wou Kenneth Kleinhans met die bou van die kliniek bereik? (2)",
        "memo": "* Kliniek Katrina $\\checkmark$\n\nEN\n\n* Kenneth wou Kaaitjie se nagedagtenis eer / sorg dat daar basiese gesondheidsorg in Vatmaar is / seker maak dat niemand in die toekoms in Vatmaar sonder behoorlike gesondheidsorg (soos Kaaitjie) sou sterf nie. $\\checkmark$",
        "final_answer": "Naam: Kliniek Katrina; Doel: Om Kaaitjie se nagedagtenis te eer en te verseker dat niemand weer in Vatmaar weens 'n gebrek aan gesondheidsorg sterf nie.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 11.2.1
    items.append({
        "item_id": f"{SOURCE_ID}-11.2.1",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "11.2.1",
        "marks": 2,
        "topic": "Roman: Vatmaar (A.H.M. Scholtz) - Kontekstueel",
        "passage": PASSAGE_TEKS_E,
        "question": "Verwys na reëls 4 tot 6.\n\n11.2.1 Is dit geregverdig om op grond van hierdie gedeelte af te lei dat die mense van Vatmaar nie vir Kenneth as 'n buitestander beskou het nie? Motiveer jou antwoord deur na TWEE ander geleenthede te verwys waartydens die mense van Vatmaar hulle houding oor Kenneth duidelik getoon het. (2)",
        "memo": "Ja, want (enige TWEE geleenthede vir 1 punt elk):\n* Suzan spreek Kenny as \"ouboet\" met respek aan $\\checkmark$\n* Die Vatmaarmans hanteer Kenny by die werk met respek $\\checkmark$\n* Vatmaar se mense het Kenny aanvaar toe hulle hoor hy was Kaaitjie se geliefde $\\checkmark$\n* Kenny tree as erkende leier in Vatmaar op toe die kliniek gebou word $\\checkmark$\n\n*(Die kandidaat bied TWEE soortgelyke antwoorde vir EEN punt elk aan. Die kandidaat kan nie 'n Nee-antwoord aanbied nie.)*",
        "final_answer": "Ja; Twee geleenthede: Suzan spreek hom eerbiedig as 'ouboet' aan, en die dorpenaars aanvaar en respekteer hom as leier tydens die bou van die kliniek.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 11.2.2
    items.append({
        "item_id": f"{SOURCE_ID}-11.2.2",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "11.2.2",
        "marks": 3,
        "topic": "Roman: Vatmaar (A.H.M. Scholtz) - Kontekstueel",
        "passage": PASSAGE_TEKS_E,
        "question": "Verwys na reëls 4 tot 6.\n\n11.2.2 In watter opsigte het Boitjie Afrika, Kenneth Kleinhans en Ou Chetty onderskeidelik saamgewerk om die eerste sokkerwedstryd van Vatmaar te verwesenlik? Verwys in jou antwoord na AL DRIE karakters se bydrae in dié verband. (3)",
        "memo": "* **Boitjie Afrika:** Stigterslid van die span / tree op as afrigter / het die amptelike brief oorgeskryf. $\\checkmark$\n* **Kenneth Kleinhans:** Het die sokkerveld uitgemeet / die area aangewys / kalk en doelpale geskenk / die brief vir Boitjie geskryf. $\\checkmark$\n* **Ou Chetty:** Het die regte sokkerbal geborg / geskenk. $\\checkmark$",
        "final_answer": "Boitjie Afrika het die span gestig en afgerig; Kenneth Kleinhans het die veld uitgemeet en die brief geskryf; Ou Chetty het die amptelike sokkerbal geborg.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 11.3
    items.append({
        "item_id": f"{SOURCE_ID}-11.3",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "11.3",
        "marks": 2,
        "topic": "Roman: Vatmaar (A.H.M. Scholtz) - Kontekstueel",
        "passage": PASSAGE_TEKS_E,
        "question": "Dink jy dat Boitjie Afrika namate die roman vorder karakterontwikkeling ondergaan? Motiveer jou antwoord met TWEE feite. (2)",
        "memo": "Ja $\\checkmark$\nTWEE feite (enige twee vir 1 punt elk):\n* Waar hy voorheen selfsugtig en 'n strawwe daggaroker was, hou hy op met dagga en wy hom toe aan sokkerafrigting $\\checkmark$\n* Waar hy voorheen net op homself gefokus het, tree hy as leiersfiguur op en help by die brandende huis $\\checkmark$\n* Hy is nie meer verwaand nie, maar word 'n gerespekteerde, verantwoordelike lid van die gemeenskap $\\checkmark$\n\n*(Die kandidaat moet karakterontwikkeling in sy/haar antwoord aandui. Die kandidaat kan nie 'n NEE-antwoord aanbied nie.)*",
        "final_answer": "Ja; Hy hou op dagga rook en fokus op die opheffing van die jeug as sokkerafrigter, en hy tree dapper as redder en leier na vore toe die huis brand.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 11.4
    items.append({
        "item_id": f"{SOURCE_ID}-11.4",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "11.4",
        "marks": 1,
        "topic": "Roman: Vatmaar (A.H.M. Scholtz) - Kontekstueel",
        "passage": PASSAGE_TEKS_E,
        "question": "Verwys na reël 8.\n\nIn watter opsig is Kenneth se optrede in dié situasie selfkarakteriserend? (1)",
        "memo": "Kenny se bedagsaamheid / goedgemanierdheid / hoflikheid / respek blyk uit sy handeling om Elsa se sakdoek op te tel en die stof uit te waai. $\\checkmark$",
        "final_answer": "Dit toon sy natuurlike hoflikheid, goeie maniere en bedagsaamheid.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 11.5
    items.append({
        "item_id": f"{SOURCE_ID}-11.5",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "11.5",
        "marks": 1,
        "topic": "Roman: Vatmaar (A.H.M. Scholtz) - Kontekstueel",
        "passage": PASSAGE_TEKS_E,
        "question": "Verwys na Teacher Elsa se gedagtes in reël 10 en 11.\n\nHoekom is hierdie gedagtes ironies teen die agtergrond van haar houding teenoor Nellie Ndola vroeër in die roman? (1)",
        "memo": "'n Mens sou verwag dat Teacher Elsa, wat afbrekend krities oor Tommy se verhouding met Nellie Ndola was en Nellie verwerp het omdat sy swart is, nooit 'n verhouding oor kleurgrense sou oorweeg nie, MAAR nou besluit Elsa dat Kenny (wat 'n bruinman is) die man vir haar is. $\\checkmark$\n*(Die kandidaat moet beide kante van die ironie aandui.)*",
        "final_answer": "Dis ironies dat sy Tommy en Nellie se interrasverhouding fel veroordeel het, maar nou self begeer om 'n verhouding met 'n bruinman (Kenny) aan te knoop.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 11.6
    items.append({
        "item_id": f"{SOURCE_ID}-11.6",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "11.6",
        "marks": 3,
        "topic": "Roman: Vatmaar (A.H.M. Scholtz) - Kontekstueel",
        "passage": PASSAGE_TEKS_E,
        "question": "Verwys na reël 19.\n\nWat word geïmpliseer deur die feit dat Suzan vinnig rondkyk of sy nie vir Tommy Lewis sien nie? In watter opsig het Tommy enersyds Nellie Ndola EN andersyds Nono se hart gebreek? (3)",
        "memo": "* Suzan assosieer Tommy met Nellie Ndola / weet dat Tommy 'n geheime verhouding met Nellie gehad het / dat Tommy die pa van Nellie se seun is. $\\checkmark$\n\nEN\n\n* **Nellie Ndola:** Tommy het Nellie swanger gemaak en haar toe gedwing om met Lucas te trou / het alle kontak met haar verbreek en haar verlaat. $\\checkmark$\n* **Nono:** Tommy het veroorsaak dat Nellie vir Lucas verlei het, waardeur Nono se huwelik verwoes en haar hart gebreek is. $\\checkmark$",
        "final_answer": "Implikasie: Suzan weet van Tommy en Nellie se verhouding en kind; Nellie se hart: Tommy het haar swanger gemaak en verwerp; Nono se hart: Sy optrede het daartoe gelei dat Lucas ontrou was aan Nono en haar huwelik verbrokkel het.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 11.7
    items.append({
        "item_id": f"{SOURCE_ID}-11.7",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "11.7",
        "marks": 2,
        "topic": "Roman: Vatmaar (A.H.M. Scholtz) - Kontekstueel",
        "passage": PASSAGE_TEKS_F,
        "question": "Watter ander brief van die stadsraad het vroeër in die roman 'n teleurstelling vir die gemeenskap van Vatmaar meegebring EN watter positiewe gevolg het dié brief vir die gemeenskap ingehou? (2)",
        "memo": "* Die brief van die stadsraad wat hulle ingelig het dat daar nie voorsiening gemaak is vir 'n kerkgebou op Vatmaar nie. $\\checkmark$\n\nEN\n\n* Die inwoners het saamgestaan en self geld ingesamel en gewerk om hulle eie kerkgebou op te rig. $\\checkmark$",
        "final_answer": "Brief: Die stadsraad se weiering om 'n kerkgebou te verskaf; Positiewe gevolg: Die gemeenskap het verenig en self geld ingesamel om hul eie kerk te bou.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 11.8
    items.append({
        "item_id": f"{SOURCE_ID}-11.8",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "11.8",
        "marks": 2,
        "topic": "Roman: Vatmaar (A.H.M. Scholtz) - Kontekstueel",
        "passage": PASSAGE_TEKS_F,
        "question": "Verwys na reël 6.\n\nNoem TWEE maniere hoe Mister Burns vir Kenneth met die oprigting van die kliniek bygestaan het. (2)",
        "memo": "TWEE maniere (1 punt elk):\n* Mister Burns het boumateriaal vir die kliniek voorsien $\\checkmark$\n* Mister Burns het self die brief vir die dorpsraad geskryf / gehelp met amptelike skakeling $\\checkmark$",
        "final_answer": "Hy het boumateriaal voorsien en self die amptelike brief aan die dorpsraad geskryf.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 11.9
    items.append({
        "item_id": f"{SOURCE_ID}-11.9",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "11.9",
        "marks": 1,
        "topic": "Roman: Vatmaar (A.H.M. Scholtz) - Kontekstueel",
        "passage": PASSAGE_TEKS_F,
        "question": "Verwys na reël 14 en 15.\n\nDink jy Sus Bet se voorwaarde spruit uit 'n afguns teenoor die mense van Vatmaar? Motiveer jou antwoord. (1)",
        "memo": "Nee $\\checkmark$\nSus Bet wou die mense van die Pan dronk maak / het geweet dat haar khadie baie sterker as gewoonlik sou wees / wou die mense van Vatmaar juis teen die sterk khadie en skande beskerm. $\\checkmark$\n*(Die kandidaat kan nie 'n JA-antwoord aanbied nie.)*",
        "final_answer": "Nee, sy wou die mense van Vatmaar teen die sterk brousels beskerm en eerder die hooghartige besoekers van die Pan 'n les leer.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 11.10
    items.append({
        "item_id": f"{SOURCE_ID}-11.10",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "11.10",
        "marks": 4,
        "topic": "Roman: Vatmaar (A.H.M. Scholtz) - Kontekstueel",
        "passage": PASSAGE_TEKS_F,
        "question": "Verwys na reël 13 tot 17.\n\nWatter VIER karaktereienskappe van Sus Bet word deur hierdie uittreksel uitgebeeld? (4)",
        "memo": "VIER karaktereienskappe (1 punt elk):\n* **Tradisievas:** Sus Bet maak die bier volgens die tradisionele resep $\\checkmark$\n* **Skelm-slim / vindingryk:** Sy beplan om die mense van die Pan 'n les te leer $\\checkmark$\n* **Manipulerend / beslis:** Sy stel streng voorwaardes dat Vatmaar se mense nie mag drink nie $\\checkmark$\n* **Behulpsaam / lojaal:** Sy willig in om haar beste khadie voor te berei vir die inwyding van die kliniek $\\checkmark$",
        "final_answer": "Tradisievas, skelm-slim (vindingryk), beslis (manipulerend) en behulpsaam teenoor Vatmaar.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 11.11
    items.append({
        "item_id": f"{SOURCE_ID}-11.11",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "11.11",
        "marks": 1,
        "topic": "Roman: Vatmaar (A.H.M. Scholtz) - Kontekstueel",
        "passage": PASSAGE_TEKS_F,
        "question": "Verwys na reëls 18 en 19.\n\nWaarom was dit 'n goeie idee om die gemmerbier deur Nurse-sister Gous te laat maak? (1)",
        "memo": "As verpleegster skep sy die verwagting dat die gemmerbier higiënies, gesonder en nie-bedwelmend/veiliger sal wees. $\\checkmark$",
        "final_answer": "As verpleegster waarborg sy dat die gemmerbier gesond, higiënies en nie-alkoholies sal wees.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 11.12
    items.append({
        "item_id": f"{SOURCE_ID}-11.12",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "11.12",
        "marks": 1,
        "topic": "Roman: Vatmaar (A.H.M. Scholtz) - Kontekstueel",
        "passage": PASSAGE_TEKS_E + "\n\n" + PASSAGE_TEKS_F,
        "question": "Herlees die volgende reëls:\n\nTEKS E (reël 9): \"Kenny met sy gebroke hart gee dit vir haar en sê: 'Your handkerchief, lady.' \"\nTEKS F (reël 7 en 8): \"Get ready for the celebration, for there is a time to mourn and a time to be merry.\"\n\nIn watter opsig sou die opening van die kliniek 'n einde aan Kenneth se gebroke hart kon bring? (1)",
        "memo": "Kenneth sou troos en heling vind in die wete dat daar nie meer moeders of babas soos Kaaitjie weens 'n gebrek aan gesondheidsorg sou sterf nie / dat hy sy persoonlike smart omgeskakel het in 'n blywende, lewegewende diens aan die gemeenskap. $\\checkmark$",
        "final_answer": "Dit bring heling omdat hy sy rou en smart omskep het in 'n kliniek wat toekomstige moeders en babas se lewens sal red.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # =========================================================================
    # VRAAG 12: DIE KWART-VOOR-SEWE-LELIE – OPSTELVRAAG [25]
    # =========================================================================
    q12_memo = f"""VRAAG 12: DIE KWART-VOOR-SEWE-LELIE – OPSTELVRAAG
Eleanor Baker

Hierdie vraag word aan die hand van die aangehegte RUBRIEK VIR DIE NASIEN VAN DIE OPSTELVRAAG VIR DIE ROMAN EN DRAMA (bladsy 52) nagesien.

LET WEL:
• Dis 'n breë raamwerk van feite.
• Al die feite hoef nie genoem te word nie.

ARGUMENTE WORD AANGEBIED EN ONDERSTEUN OF GEÏLLUSTREER DEUR NA DIE TEKSTE TE VERWYS:

**Inleiding:**
Die kandidaat bied 'n gepaste inleiding aan.

**1. IRIS SE INNERLIKE KONFLIK DRA BY TOT HAAR GELOOFWAARDIGHEID:**
- *Soeke na identiteit en betekenis:* Iris worstel met haar naam wat sowel 'n Griekse godin as 'n blom is wat net een keer per jaar blom. Sy wonder aanhoudend wanneer haar eie 'blomtyd' sal aanbreek.
- *Fantasiewêreld teenoor werklikheid:* Haar innerlike gesprekke met die Engel versinnebeeld haar soeke na sekuriteit en ontvlugting uit 'n chaotiese gesinslewe. Dit maak haar 'n fassinerende en geloofwaardige jong vrou.
- *Vrees vir die huwelik en konvensie:* Sy vrees om vasgevang te word in 'n banale huwelik soos haar ma s'n of 'n emosielose vennootskap soos dié van haar suster Elsa. Sy huiwer lank om Peter se liefde heelhartig te aanvaar.
- *Bettie se krisis:* Wanneer Bettie gif drink weens 'n verhouding, laat dit Iris besef dat uiterlike sukses nie geluk waarborg nie en dat sy Peter se opregte liefde moet waardeer.

**2. UITERLIKE KONFLIK LEI TOT KARAKTERGROEI:**
- *Konflik met haar ma (Els):* Iris beleef frustrasie omdat haar ma verstrooid is en selde regtig luister. Dit dwing Iris om vroeg reeds onafhanklik te word en verantwoordelikheid vir haar eie lewe te neem.
- *Konflik met susters Elsa en Kara:* Elsa se koue perfeksionisme en Kara se radikale feminisme daag Iris uit om haar eie waardes te formuleer sonder om bloot een van hul uiterstes na te boots.
- *Konflik met Peter:* Peter se aandrang op 'n vaste toekoms en huwelik dwing Iris om haar fantasiewêreld met die Engel af te lê en te kies vir 'n volwasse, werklike verhouding.
- *Interaksie met tant Ans en oom Piet:* Die ontmoeting met Peter se eenvoudige, warm ouers help haar om die waarde van 'n stabiele gesin te erken.

**Slot:**
Die kandidaat bied 'n gepaste slot aan.

[25]

{NOVEL_RUBRIC}"""

    items.append({
        "item_id": f"{SOURCE_ID}-12",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "12",
        "marks": 25,
        "topic": "Roman: Die kwart-voor-sewe-lelie (Eleanor Baker) - Literêre Opstel",
        "passage": PASSAGE_KWART_CONTEXT,
        "question": "Die hoofkarakter in die roman word deur middel van INNERLIKE en UITERLIKE KONFLIK gekarakteriseer.\n\nBespreek in 'n opstel van 400 tot 450 woorde hoe Iris se innerlike konflik bydra tot haar geloofwaardigheid as hoofkarakter EN hoe uiterlike konflik tot karaktergroei lei. [25]",
        "memo": q12_memo,
        "final_answer": "Iris se innerlike konflik oor haar identiteit, haar soeke na haar blomtyd en haar vlug na 'n fantasiewêreld met die Engel maak haar 'n geloofwaardige hoofkarakter, terwyl haar uiterlike botsings met haar verstrooide ma, haar susters en Peter haar dwing om volwassenheid te bereik en geluk in die werklikheid te vind.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # =========================================================================
    # VRAAG 13: DIE KWART-VOOR-SEWE-LELIE – KONTEKSTUELE VRAAG [25]
    # =========================================================================
    # 13.1
    items.append({
        "item_id": f"{SOURCE_ID}-13.1",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "13.1",
        "marks": 1,
        "topic": "Roman: Die kwart-voor-sewe-lelie (Eleanor Baker) - Kontekstueel",
        "passage": PASSAGE_TEKS_G,
        "question": "Na watter inligting rakende haar naam verwys Iris in reël 1? (1)",
        "memo": "Sy het vir haar ma vertel dat sy in die woordeboek ontdek het dat haar naam ook dié van 'n Griekse godin (boodskapper van die gode) is. $\\checkmark$",
        "final_answer": "Dat haar naam ook dié van 'n Griekse godin is.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 13.2
    items.append({
        "item_id": f"{SOURCE_ID}-13.2",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "13.2",
        "marks": 2,
        "topic": "Roman: Die kwart-voor-sewe-lelie (Eleanor Baker) - Kontekstueel",
        "passage": PASSAGE_TEKS_G,
        "question": "\"Sy het die bakkie vet vinnig in die yskas gesit asof die verwerking daarvan nou die yskas se verantwoordelikheid is.\" (Reël 2 en 3)\n\nHoe, dink jy, dra dié inligting oor Iris se ma tot karakterisering van die ma by? Watter persoon dra daartoe by dat Iris 'n ander idee van ma-wees het? Motiveer jou antwoord. (2)",
        "memo": "* Dit wys dat Iris se ma verstrooid is en nie gemaklik is met haar rol as tradisionele huisvrou/ma nie / dit spanningsvol vind om huishoudelike take te verrig. $\\checkmark$\n\nEN\n\n* Johanna (die huishulp), want sy is die praktiese versorger wat basies vir Iris en haar susters grootmaak en stabiliteit in die huis bied. $\\checkmark$",
        "final_answer": "Karakterisering van ma: Sy is onprakties, verstrooid en skuif huishoudelike pligte af; Ander ma-figuur: Johanna, wat as huishulp die kinders daagliks met sorg en praktiese stabiliteit grootmaak.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 13.3
    items.append({
        "item_id": f"{SOURCE_ID}-13.3",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "13.3",
        "marks": 3,
        "topic": "Roman: Die kwart-voor-sewe-lelie (Eleanor Baker) - Kontekstueel",
        "passage": PASSAGE_TEKS_G,
        "question": "\"So 'n mooi blom. Ek vind dit so jammer dat hulle net in die lente blom.\" (Reël 9 en 10)\n\nIn watter opsig was die ma se antwoord nie vir Iris verrassend nie? Dink jy hierdie woorde veroorsaak 'n wanpersepsie by Iris oor haar eie lewe? Motiveer jou antwoord met TWEE feite. (3)",
        "memo": "* Iris was daaraan gewoond dat haar ma nooit regtig na haar luister nie / dat haar ma se aandag altyd elders dwaal. $\\checkmark$\n\nEN\n\n* Ja $\\checkmark$\n* TWEE wanpersepsies (enige twee vir 1 punt elk):\n  - Iris glo dat sy net een enkele blomtyd in haar hele lewe sal beleef $\\checkmark$\n  - Sy dink 'n gewone gebeurtenis soos 'n huwelik met Peter sal haar blomtyd verongeluk $\\checkmark$\n  - Sy dink sy moet eksotiese dinge doen (soos Joe Pryor se aanbod) om haar blomtyd te ervaar $\\checkmark$\n\n*(Die kandidaat kan nie 'n NEE-antwoord aanbied nie.)*",
        "final_answer": "Nie verrassend nie: Iris is gewoond dat haar ma nie regtig luister nie; Wanpersepsies: Ja, sy glo sy het net een enkele blomtyd in haar lewe en dat 'n gewone huwelik met Peter haar blomtyd sal verongeluk.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 13.4.1
    items.append({
        "item_id": f"{SOURCE_ID}-13.4.1",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "13.4.1",
        "marks": 3,
        "topic": "Roman: Die kwart-voor-sewe-lelie (Eleanor Baker) - Kontekstueel",
        "passage": PASSAGE_TEKS_G,
        "question": "Verwys na reëls 13 tot 15.\n\n13.4.1 In watter opsig kan die ma nooit die wêreld in haar hand vasvat nie? Watter TWEE ooreenkomste toon Iris op hierdie stadium met haar ma? (3)",
        "memo": "* Die ma is verstrooid, leef in 'n droomwêreld en kry nooit beheer oor haar eie lewe of huishouding nie / jaag altyd 'n bus na wat sy nooit inhaal nie. $\\checkmark$\n\nEN\n\n* TWEE ooreenkomste met Iris (1 punt elk):\n  - Iris droom ook en wonder aanhoudend oor die betekenis van haar naam $\\checkmark$\n  - Iris leef ook in 'n fantasiewêreld (met haar Engel) en jaag 'n toekomstige blomtyd na pleks van in die werklikheid te leef $\\checkmark$",
        "final_answer": "Ma se onvermoë: Sy leef verstrooid en kry nooit beheer oor haar werklikheid nie; Ooreenkomste: Iris leef ook in 'n droomwêreld en jaag 'n onbereikbare 'blomtyd' na.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 13.4.2
    items.append({
        "item_id": f"{SOURCE_ID}-13.4.2",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "13.4.2",
        "marks": 3,
        "topic": "Roman: Die kwart-voor-sewe-lelie (Eleanor Baker) - Kontekstueel",
        "passage": PASSAGE_TEKS_G,
        "question": "Verwys na reëls 13 tot 15.\n\n13.4.2 Johanna, Elsa en Kara is deel van die ma se wêreld. Hoe word hierdie drie vroue onderskeidelik deur middel van Iris se weergawes aan die leser gekarakteriseer? (3)",
        "memo": "* **Johanna:** Praktiese raakvatter / betroubare versorger $\\checkmark$\n* **Elsa:** Ernstig / perfeksionisties / konvensioneel / prakties $\\checkmark$\n* **Kara:** Feministies / liberaal / opstandig teen tradisionele rolle $\\checkmark$",
        "final_answer": "Johanna: Praktiese en betroubare versorger; Elsa: Ernstige en koue perfeksionis; Kara: Vrygeestige en liberale feminis.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 13.5
    items.append({
        "item_id": f"{SOURCE_ID}-13.5",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "13.5",
        "marks": 2,
        "topic": "Roman: Die kwart-voor-sewe-lelie (Eleanor Baker) - Kontekstueel",
        "passage": PASSAGE_TEKS_G,
        "question": "Verwys na reëls 16 tot 19.\n\nIn hierdie reëls word Iris se ma se onrustige geaardheid verwoord. Watter ma kry Iris later in haar lewe by EN waarom kom Iris goed met haar oor die weg? (2)",
        "memo": "* Tant Ans (Peter se ma) $\\checkmark$\n\nEN\n\n* Tant Ans is 'n warm, liefdevolle en aanvaardende mens wat goed met ma Els oor die weg kom en vir Iris met deernis behandel. $\\checkmark$",
        "final_answer": "Tant Ans (Peter se ma); Iris kom goed met haar oor die weg omdat sy warm, rustig, liefdevol en aanvaardend is.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 13.6
    items.append({
        "item_id": f"{SOURCE_ID}-13.6",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "13.6",
        "marks": 1,
        "topic": "Roman: Die kwart-voor-sewe-lelie (Eleanor Baker) - Kontekstueel",
        "passage": PASSAGE_TEKS_G,
        "question": "Waarom is Iris se beskrywing van haar ma in reël 15 en 16 ironies? (1)",
        "memo": "'n Mens sou verwag dat Iris die futiele geaardheid van haar ma se gejaag na lug sal raaksien en vermy, MAAR sy doen presies dieselfde deur in 'n droomwêreld te leef en haar eie 'blomtyd' na te jaag pleks van die werklikheid te omhels. $\\checkmark$\n*(Die kandidaat moet beide kante van die ironie aandui.)*",
        "final_answer": "Dis ironies dat Iris haar ma se futiele gejaag agter 'n bus aan kritiseer, terwyl sy self presies dieselfde doen deur haar eie denkbeeldige 'blomtyd' na te jaag.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 13.7.1
    items.append({
        "item_id": f"{SOURCE_ID}-13.7.1",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "13.7.1",
        "marks": 2,
        "topic": "Roman: Die kwart-voor-sewe-lelie (Eleanor Baker) - Kontekstueel",
        "passage": PASSAGE_TEKS_H,
        "question": "Verwys na reëls 1 tot 3.\n\n13.7.1 Wie is die \"sy\" oor wie daar gepraat word EN in watter opsig het haar gifdrinkery vir Iris haar uiteindelike blomtyd laat beleef? (2)",
        "memo": "* Bettie (Brian se vriendin) $\\checkmark$\n\nEN\n\n* Bettie se gifdrinkery het Iris laat besef dat Peter se liefde kosbaar en uniek is / dat sy nêrens anders hoef te soek om te blom as in haar lewe saam met Peter nie. $\\checkmark$",
        "final_answer": "Persoon: Bettie; Effek: Dit laat Iris besef dat Peter kosbaar is en dat haar ware blomtyd in 'n egte lewe saam met hom lê.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 13.7.2
    items.append({
        "item_id": f"{SOURCE_ID}-13.7.2",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "13.7.2",
        "marks": 1,
        "topic": "Roman: Die kwart-voor-sewe-lelie (Eleanor Baker) - Kontekstueel",
        "passage": PASSAGE_TEKS_H,
        "question": "Verwys na reëls 1 tot 3.\n\n13.7.2 Wat impliseer die tannie met haar vraag in reël 3? (1)",
        "memo": "Sy impliseer dat 'n bekwame, selfstandige vrou (soos wat Iris beskryf) tevrede en gelukkig behoort te wees en nie rede het om haarself te vergiftig nie. $\\checkmark$",
        "final_answer": "Sy impliseer dat so 'n vaardige, onafhanklike vrou reeds alles het om gelukkig te wees en nie haar eie lewe behoort te wil neem nie.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 13.8
    items.append({
        "item_id": f"{SOURCE_ID}-13.8",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "13.8",
        "marks": 4,
        "topic": "Roman: Die kwart-voor-sewe-lelie (Eleanor Baker) - Kontekstueel",
        "passage": PASSAGE_TEKS_H,
        "question": "Verwys na reëls 8 tot 10.\n\nWatter rolle het Iris se ma, Elsa, Kara en Johanna onderskeidelik in Iris se persepsie oor die huwelik gespeel? (4)",
        "memo": "* **Iris se ma:** Haar onbetrokkenheid en chaotiese huwelik laat Iris dink dat gades maar elkeen hul eie koers kan gaan / laat haar besef sy wil nie so 'n verbrokkelde huwelik hê nie. $\\checkmark$\n* **Elsa:** Haar koue, praktiese en onemosionele huwelik laat Iris besluit dat sy nie bloot ter wille van konvensie wil trou nie. $\\checkmark$\n* **Kara:** Kara en Claude se passievolle liefde laat Iris verlang om ook so innig geliefd te wees en laat haar anders na die huwelik kyk. $\\checkmark$\n* **Johanna:** Johanna se uitlatings oor hoekom sy ongetroud gebly het, laat Iris aanvanklik besluit dat sy liewer nooit wil trou nie. $\\checkmark$",
        "final_answer": "Ma: Laat haar vrees vir 'n chaotiese verhouding; Elsa: Laat haar huiwer vir 'n koue, reëelmatige huwelik; Kara: Laat haar smag na egte passie en romanse; Johanna: Laat haar aanvanklik dink dis beter om ongetroud te bly.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 13.9
    items.append({
        "item_id": f"{SOURCE_ID}-13.9",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "13.9",
        "marks": 2,
        "topic": "Roman: Die kwart-voor-sewe-lelie (Eleanor Baker) - Kontekstueel",
        "passage": PASSAGE_TEKS_H,
        "question": "Verwys na die manier hoe Iris na Peter se ma en pa verwys (reël 6 en 7 asook reëls 19 tot 22).\n\nWatter karaktertrek van Iris blyk hieruit? Wat was haar voorwaarde aan die oom, voordat sy vir hom pa sal sê? (2)",
        "memo": "* **Karaktertrek:** Onafhanklik / versigtig / buitestander / fyn waarnemer wat nie sommer blindelings konvensies aanvaar nie. $\\checkmark$\n\nEN\n\n* **Voorwaarde:** Hy sal eers haar Engel moet aanvaar. $\\checkmark$",
        "final_answer": "Karaktertrek: Onafhanklik en versigtig; Voorwaarde: Hy moet eers haar Engel aanvaar voordat sy hom 'pa' sal noem.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    # 13.10
    items.append({
        "item_id": f"{SOURCE_ID}-13.10",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": "afrikaans_hl",
        "grade": 12,
        "language": "af",
        "track": "languages_hl",
        "kind": "passage_questions",
        "question_ref": "13.10",
        "marks": 1,
        "topic": "Roman: Die kwart-voor-sewe-lelie (Eleanor Baker) - Kontekstueel",
        "passage": PASSAGE_TEKS_G + "\n\n" + PASSAGE_TEKS_H,
        "question": "Herlees die volgende reëls:\n\nTEKS G (reëls 8 tot 10): \" 'Pragtig,' het sy saamgestem en haar tong geklik toe sy agterkom die boud is wel in die oond, maar die oond is nog nie aangeskakel nie. 'So 'n mooi blom.' \"\nTEKS H (reël 17 en 18): \"Ek het my appeltert geëet. Dit was heerlik en ek het probeer proe wat dit was wat die tannie bygesit het sodat ek vir Johanna kon vertel.\"\n\nDink jy Iris het in TEKS H vrede gevind ten opsigte van die innerlike konflik wat sy in TEKS G beleef het? Motiveer jou antwoord. (1)",
        "memo": "Ja $\\checkmark$\nIris het berusting gevind en vrede gemaak met haarself en haar naam; sy het gegroei en haar onsekerheid oor haar blomtyd verwerk deur eenvoudige genot in die werklikheid te vind (die appeltert geniet en aan Johanna dink). $\\checkmark$\n*(Die kandidaat kan nie 'n NEE-antwoord aanbied nie.)*",
        "final_answer": "Ja, sy het vrede gevind met haar werklikheid en haar soeke na 'n eksotiese blomtyd laat vaar om eenvoudige geluk saam met ander te ervaar.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education",
    })

    return items

if __name__ == "__main__":
    items = get_novel_items()
    print(f"Generated {len(items)} novel items.")
    print("Total marks:", sum(x["marks"] for x in items))
