import json
import os
import re

source_id = "dbe-english_fal-g12-p1-2023-nov"
pair_source_id = "dbe-english_fal-g12-p1-2023-nov-memo"
subject = "english_fal"
grade = 12
language = "en"
track = "languages_fal"

# Shared Passages
passage_sec_a = """### TEXT A

**FAST FASHION'S FOOTPRINT**

1. Fast fashion refers to the quick and inexpensive production of clothing by mass-market retailers in response to the latest fashion trends. The fashion industry is vibrant and varied. It has grown significantly in recent years due to the popularity of fast fashion. The goal is to get new clothing styles from the runway$^1$ to the store as quickly and cheaply as possible to meet consumer demand for trendy and affordable clothing.

2. 'Clothing overconsumption is on the rise in Africa, including South Africa, and a major reason for this is the acceleration of the fast fashion cycle,' says Dr Lorna Christie, researcher at the Department of Life Sciences, College of Agriculture and Environmental Sciences (CAES). South Africa is a fashion-conscious nation and it shows in consumers' spending habits. In one financial year, South Africans spent R180 billion on clothing and textiles, which amounts to $18\\%$ of all retail sales in that year. As a strong consumer base, South Africa is contributing to pollution because of the massive amounts of waste the clothing industry generates.

3. Globally, fashion companies have drastically changed their release of new clothing collections. In the past, only two collections per year were available. Currently, some brands and fashion houses release two collections a month, or even more. This is also a growing trend in South Africa.

4. With fashion changing so often and so fast, it is not surprising that people are buying more clothing. Globally, clothing production has almost doubled since the year 2000. People are buying more garments than in the past, and they only keep the clothes for half as long. The fast fashion cycle is increasing even more, and people are purchasing clothing at an even faster rate. They discard clothing at a faster rate too.

5. The amount of clothing that gets thrown away every second of every day is equivalent to a truck filled with garbage. Discarded clothing contributes massively to pollution. The chemicals used in the manufacturing process are released, and because of all the synthetic fibres, clothes either decompose slowly or do not decompose at all.

6. Natural fibres are not any better, because the cultivation of cotton and other natural fibres requires the use of water, fertilisers, pesticides, as well as the energy for picking the fibre and processing it into yarns$^2$. Then, there is the dyeing process, which requires large amounts of water and chemicals, and the runoff$^3$ from this process can pollute waterways$^4$ and harm the environment.

7. Washing clothes releases $500\\ 000$ tons of microfibres into the ocean each year, which is the equivalent of $50$ billion plastic bottles. More than $10\\ 000$ litres of water is used when manufacturing a single pair of jeans. This is equivalent to the average drinking water for one person for five-and-a-half years. There is a further impact on the environment when garments are shipped and delivered to the point of sale as much fuel and power are used.

8. The fashion industry has a damaging effect on the environment, but everyone has the power to drive the change that will reduce the impact. Fashion designers must use eco-friendly, long-lasting materials when manufacturing clothes. This will lead to sustainable fashion which encourages the repair, recycling and donation of clothes. Discarding clothes in a rubbish dump must only be done as a last option.

9. Consumers must buy from sustainable$^5$ fashion brands which do not produce clothes for the fast fashion market. They must support small local businesses which do not contribute to pollution. Instead of buying an outfit that is going to be worn once, it is better if consumers rent such outfits. People must ensure that their desire to look good does not have a negative impact on the environment.

[Adapted from *www.unisa.ac.za*]

**GLOSSARY:**
- runway$^1$: the long narrow stage that models walk along in a fashion show
- yarn(s)$^2$: thread used for making cloth or for knitting
- runoff$^3$: rain or other liquid that flows off the land into rivers
- waterway(s)$^4$: a river or canal that boats travel on
- sustainable$^5$: capable of continuing for a long time

---

### TEXT B

**PERCENTAGE OF WATER USED FOR DIFFERENT PURPOSES IN FIVE CONTINENTS**

[Diagram description: Five circular pie charts comparing the distribution of water consumption across three sectors (Domestic use, Agricultural use, Industrial use) for five continents. A legend at the bottom defines the shading:
- Solid black shading = Domestic use
- Diagonal hatching / striped shading = Agricultural use
- Plain white / unshaded = Industrial use]

- **North America:**
  - Industrial use: $48\\%$
  - Agricultural use: $39\\%$
  - Domestic use: $13\\%$
- **South America:**
  - Agricultural use: $71\\%$
  - Domestic use: $19\\%$
  - Industrial use: $10\\%$
- **Europe:**
  - Industrial use: $53\\%$
  - Agricultural use: $32\\%$
  - Domestic use: $15\\%$
- **Africa:**
  - Agricultural use: $84\\%$
  - Domestic use: $9\\%$
  - Industrial use: $7\\%$
- **Asia:**
  - Agricultural use: $88\\%$
  - Domestic use: $7\\%$
  - Industrial use: $5\\%$

[Source: *www.pinterest.com*]"""

passage_sec_b = """### TEXT C

**THE RESTORATIVE POWER OF VASELINE**

Vaseline petroleum jelly (Vaseline) has been around for more than one hundred and fifty years; it is a true legend and has become popularly known as Vaseline in South Africa. The soothing power of Vaseline has been passed down from generation to generation. It is time to get excited about skincare and embrace the healing power of petroleum jelly. The affordable yet effective Vaseline is versatile.

The hydrating power of Vaseline is a good remedy for dry skin. Applying it to the body after a shower keeps the skin moisturised. For minor wounds such as cuts, scrapes, scratches and burns, use Vaseline to keep the wound moist as doing this will aid the healing process.

Vaseline is hypoallergenic; therefore, it is suitable for sensitive skin, making it a good skincare option for babies to prevent nappy rash. Do not let mosquito bites and bee stings get the upper hand. Put some Vaseline on the itchy spots for instant relief.

Rubbing a little Vaseline into the hair gives it instant shine and reduces the look of split ends. Removing chewing gum stuck in your hair is a nightmare. Coat the gum and surrounding hair with Vaseline and pull gently to remove the gum.

For teeth whitening, mix two tablespoons of baking soda with Vaseline and apply to dry teeth, using a toothbrush. Do not let snails and ants ruin your garden. Apply a combination of Vaseline and salt on the edges of flower pots to keep them protected.

[Adapted from *Benefits*, January 2022]"""

passage_sec_c_q3 = """### TEXT D

**ADVERTISEMENT: CAUTION FIRE DANGER**

[Visual & Layout Description:
- **Top banner:** Flames leaping above a black and white warning sign.
  - White text on a black block: "**CAUTION**"
  - Large distressed, cracked font on a white banner below: "**FIRE DANGER**" (the letter 'I' in 'FIRE' looks fractured like a flame, and the letter 'G' in 'DANGER' is tilted and falling downwards).
- **Upper right visual:** A circular vignette featuring a stylized black silhouette of a horned buck / antelope head surrounded by intense flames.
- **Subheading:** "**Fire is EVERYONE'S fight**" (with 'EVERYONE'S' in bold capital letters).
- **Central message box (white card):**
  "The Western Cape has had devastating fires. Help us prevent unplanned veld fires and protect the environment and people!
  
  To report all emergencies, you can call **112** from a cellphone or **10177** from a landline toll free."
- **Inset note (simulating a paper note pinned at the bottom-right):**
  "**DISTRICT EMERGENCY NUMBERS FOR REPORTING VELD FIRES**
  - City of Cape Town: 107 from a landline or 021 480 7700 from a cellphone
  - Overberg: 028 425 1690
  - West Coast: 022 433 8700
  - Eden: 044 805 5071
  - Central Karoo: 023 414 2603
  - Cape Winelands: 021 887 4446"
- **Black bar above footer:** "Thank you for your awareness and co-operation." with a Facebook badge: "Find CapeNature on: facebook".
- **Footer logos:** Four official partner logos displayed side by side:
  1. Western Cape Government (official coat of arms and provincial banner)
  2. Disaster Management (circular logo with triangle and 'DISASTER MANAGEMENT')
  3. FIRERESCUE SERVICES
  4. CapeNature (leaf/water emblem and URL www.capenature.co.za)]

[Adapted from *www.westerncape.gov.za*]"""

passage_sec_c_q4 = """### TEXT E

**GARFIELD by JIM DAVIES**

[Comic strip of 8 frames featuring Jon (a man) and Garfield (his cat):
- **FRAME 1:** Title frame showing the bold stylized banner "GARFIELD" surrounded by stars. Garfield is lying down comfortably, resting on top of the banner with paws folded peacefully.
- **FRAME 2:** Jon is seated holding a warm coffee mug in his hand, looking drowsy and relaxed with half-closed eyes. Behind him, Garfield is standing on his hind legs, eyes wide open and tail raised, bouncing up and down energetically.
- **FRAME 3:** Garfield leaps forward and smacks Jon on the back of his head with his paw. A large bold sound-effect word "**SMACK**" is displayed with impact stars. Jon is jolted forward, liquid splashes out of his mug, and stationery flies out of a pen-holder. Garfield thinks in a jagged thought-bubble: "LET'S PLAY!".
- **FRAME 4:** Jon turns his head back, frowning with an irritated and stern expression: "LEAVE ME ALONE, GARFIELD.". Garfield ignores him, continuing to dance with paws waving: "LET'S PLAY! LET'S PLAY!".
- **FRAME 5:** Jon gives in, smiling warmly with closed eyes: "OH, OKAY, WE'LL PLAY". Garfield is lying playfully on his back on the floor with all four paws raised in anticipation.
- **FRAME 6:** Jon crouches down and vigorously tickles Garfield's stomach with both hands, joyfully chanting: "TICKLE! TICKLE! TICKLE! TICKLE!". Garfield is wriggling and laughing out loud with wide open mouth: "HA! HA! HEE! HO!".
- **FRAME 7:** Suddenly, Garfield bites Jon's hand/arm! Jon screams in agony, head thrown back with movement lines and fingers spread wide in shock: "**OUCH!**".
- **FRAME 8:** Jon sits slumped back on the floor, thoroughly exhausted, traumatized and stunned, waving a weary hand: "I'M THROUGH PLAYING NOW". Garfield smugly and casually walks away on all fours with a smirk.]

[Source: *www.cartoons.com*]  
*NOTE: In this cartoon, the man's name is Jon and his cat is Garfield.*"""

passage_sec_c_q5_1 = """### TEXT F

**KEEPING BEES IS A BEE-UTIFUL HOBBY**

1. There **is** beekeepers who keep the critical bee populations healthy. They have managed swarms to prevent the number of bees from **diclining**. Keeping swarms is **an** hobby that requires only a small investment of time and money.

2. Honey is a wonderful ingredient with many uses. It can be harvested twice **on** one season. Beekeepers ensure that their bees are safe so they can continue producing honey and wax. The wax is used to make furniture polish and lip balms. Bees also play a major role in pollinating vital plants.

3. Len Boucher, chairman of a beekeeping association, shared his story about bees. He said, 'I turned the passion for bees into a business.' Boucher rescues swarms that need to be removed from areas where they pose a potential danger. He explained that they are not **allowed** to keep bees in densely populated areas like blocks of flats. It is unsafe for both the people and the bees.

4. Bees cannot be kept near a school, a church or a shopping centre. A beekeeping permit is required by anyone who wishes to become a beekeeper.

5. More **information** about keeping bees **or** the safe removal of swarms is available on the internet.

[Adapted from *www.northcliffmelvilletimes.co.za*]"""

passage_sec_c_q5_2 = """### TEXT G

**YOU ONLY HAVE ONE BODY.**  
**MAKE VEGETABLES YOUR HEALTHY CHOICE.**

[Diagram description: An educational health image showing a pair of human lungs artistically constructed from fresh, dark green leafy vegetable leaves (spinach or Swiss chard). The thick white central stalks / stems of the leaves join together at the top to resemble the human trachea and primary bronchi, while the white veins branch outward across the dark leafy green lobes, mimicking the bronchial network inside the left and right lungs.]

[Source: *www.coop.com*]"""

items = [
    # Section A: Comprehension
    {
        "item_id": f"{source_id}-1.1.1",
        "source_id": source_id,
        "pair_source_id": pair_source_id,
        "subject": subject,
        "grade": grade,
        "language": language,
        "track": track,
        "kind": "passage_questions",
        "question_ref": "1.1.1",
        "marks": 1,
        "topic": "Comprehension - Text A (Fast Fashion)",
        "passage": passage_sec_a,
        "question": "Refer to paragraph 1.\nQuote THREE consecutive words that suggest that fast fashion is exciting and different.",
        "memo": "'vibrant and varied' $\\checkmark$ / 'trendy and affordable' $\\checkmark$ (1)",
        "final_answer": "vibrant and varied",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{source_id}-1.1.2",
        "source_id": source_id,
        "pair_source_id": pair_source_id,
        "subject": subject,
        "grade": grade,
        "language": language,
        "track": track,
        "kind": "multiple_choice",
        "question_ref": "1.1.2",
        "marks": 1,
        "topic": "Comprehension - Text A (Vocabulary)",
        "passage": passage_sec_a,
        "question": "Refer to paragraph 1.\nChoose the correct answer to complete the following sentence.\n\nA more formal word for 'trendy' is ...\n\nA cool.  \nB outdated.  \nC remarkable.  \nD fashionable.",
        "memo": "D / fashionable $\\checkmark$ (1)",
        "final_answer": "D / fashionable",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{source_id}-1.2.1",
        "source_id": source_id,
        "pair_source_id": pair_source_id,
        "subject": subject,
        "grade": grade,
        "language": language,
        "track": track,
        "kind": "passage_questions",
        "question_ref": "1.2.1",
        "marks": 2,
        "topic": "Comprehension - Text A (Dr Lorna Christie / CAES)",
        "passage": passage_sec_a,
        "question": "Refer to paragraph 2.\nWhy does the writer mention Dr Lorna Christie? State TWO points.",
        "memo": "She conducts research (on fashion) $\\checkmark$ and her findings provide credibility to the article. $\\checkmark$ (2)",
        "final_answer": "She conducts research on fashion, and citing her findings gives authority and credibility to the article.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{source_id}-1.2.2",
        "source_id": source_id,
        "pair_source_id": pair_source_id,
        "subject": subject,
        "grade": grade,
        "language": language,
        "track": track,
        "kind": "passage_questions",
        "question_ref": "1.2.2",
        "marks": 2,
        "topic": "Comprehension - Text A (Fashion-conscious South Africa)",
        "passage": passage_sec_a,
        "question": "Refer to paragraph 2.\nWhat does the writer mean by, 'South Africa is a fashion-conscious nation' (lines 10–11). State TWO points.",
        "memo": "* South Africans are aware of the latest fashion trends. $\\checkmark$\n* They are interested in wearing stylish clothes. $\\checkmark$\n* They spend money on fashion. $\\checkmark$\n\n**NOTE:** Accept any TWO suitable answers. (2)",
        "final_answer": "South Africans are knowledgeable about current fashion trends and spend significant money on stylish clothing.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{source_id}-1.3.1",
        "source_id": source_id,
        "pair_source_id": pair_source_id,
        "subject": subject,
        "grade": grade,
        "language": language,
        "track": track,
        "kind": "passage_questions",
        "question_ref": "1.3.1",
        "marks": 1,
        "topic": "Comprehension - Text A (Global clothing trends)",
        "passage": passage_sec_a,
        "question": "Refer to paragraph 3.\nWhy is the following statement FALSE?\n\nThe trend of the frequent release of new clothing collections is unique to South Africa.",
        "memo": "The passage mentions that fashion companies world-wide/globally have increased the frequency of new clothing collections. $\\checkmark$ (1)",
        "final_answer": "The passage states that globally/worldwide, fashion companies have increased the frequency of releasing new clothing collections.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{source_id}-1.3.2",
        "source_id": source_id,
        "pair_source_id": pair_source_id,
        "subject": subject,
        "grade": grade,
        "language": language,
        "track": track,
        "kind": "passage_questions",
        "question_ref": "1.3.2",
        "marks": 1,
        "topic": "Comprehension - Text A (Vocabulary)",
        "passage": passage_sec_a,
        "question": "Refer to paragraph 3.\nIdentify ONE word which shows that throughout the world, fashion companies have significantly increased their new clothing releases.",
        "memo": "'drastically' $\\checkmark$ (1)",
        "final_answer": "drastically",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{source_id}-1.4.1",
        "source_id": source_id,
        "pair_source_id": pair_source_id,
        "subject": subject,
        "grade": grade,
        "language": language,
        "track": track,
        "kind": "passage_questions",
        "question_ref": "1.4.1",
        "marks": 2,
        "topic": "Comprehension - Text A (Production outcomes)",
        "passage": passage_sec_a,
        "question": "Refer to paragraph 4.\nWhat are TWO possible positive outcomes of the increase in clothing production?",
        "memo": "* more affordable clothing $\\checkmark$\n* more fashionable clothing $\\checkmark$\n* readily available clothing $\\checkmark$\n* improved economy $\\checkmark$\n* increase in jobs $\\checkmark$\n* increase in revenue $\\checkmark$\n\n**NOTE:** Accept any TWO suitable answers. (2)",
        "final_answer": "Clothing becomes more affordable and accessible to consumers, and increased manufacturing stimulates job creation and economic growth.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{source_id}-1.4.2",
        "source_id": source_id,
        "pair_source_id": pair_source_id,
        "subject": subject,
        "grade": grade,
        "language": language,
        "track": track,
        "kind": "passage_questions",
        "question_ref": "1.4.2",
        "marks": 2,
        "topic": "Comprehension - Text A (Changing consumer habits)",
        "passage": passage_sec_a,
        "question": "Refer to paragraph 4.\nUsing your OWN words, describe how the shopping habits of consumers have changed over time.",
        "memo": "People are buying more clothing/garments $\\checkmark$ and discarding them faster/purchase more frequently. $\\checkmark$ (2)",
        "final_answer": "Consumers now buy clothing much more frequently and in greater quantities, but keep and wear them for a much shorter time before throwing them away.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{source_id}-1.5",
        "source_id": source_id,
        "pair_source_id": pair_source_id,
        "subject": subject,
        "grade": grade,
        "language": language,
        "track": track,
        "kind": "passage_questions",
        "question_ref": "1.5",
        "marks": 2,
        "topic": "Comprehension - Text A (Decomposition of discarded clothing)",
        "passage": passage_sec_a,
        "question": "Refer to paragraph 5.\nExplain in your OWN words why discarded clothing decomposes slowly. State TWO points.",
        "memo": "* The chemical content used to manufacture the clothes reduces the rate of decomposition. $\\checkmark$\n* Artificial/synthetic fibres do not decompose easily/quickly. $\\checkmark$ (2)",
        "final_answer": "Synthetic fibres do not break down naturally, and the industrial chemicals applied during manufacturing inhibit decomposition.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{source_id}-1.6.1",
        "source_id": source_id,
        "pair_source_id": pair_source_id,
        "subject": subject,
        "grade": grade,
        "language": language,
        "track": track,
        "kind": "passage_questions",
        "question_ref": "1.6.1",
        "marks": 2,
        "topic": "Comprehension - Text A (Environmental impact of natural fibres)",
        "passage": passage_sec_a,
        "question": "Refer to paragraph 6.\nHow does the information in lines 31–33 ('Natural fibres are ... it into yarns') challenge the usual perception that buying natural products is better for the environment?",
        "memo": "To cultivate natural fibres, a lot of water is required $\\checkmark$ / fertiliser $\\checkmark$ / pesticides $\\checkmark$ are used / energy is required to pick and process the fibres. $\\checkmark$\n\n**NOTE:** Accept any TWO of the above answers. (2)",
        "final_answer": "It shows that growing and processing natural fibres requires enormous quantities of water and energy, as well as polluting chemical fertilisers and pesticides.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{source_id}-1.6.2",
        "source_id": source_id,
        "pair_source_id": pair_source_id,
        "subject": subject,
        "grade": grade,
        "language": language,
        "track": track,
        "kind": "passage_questions",
        "question_ref": "1.6.2",
        "marks": 2,
        "topic": "Comprehension - Text A (Dyeing process)",
        "passage": passage_sec_a,
        "question": "Refer to paragraph 6.\nExplain how the process of dyeing clothes affects the environment.",
        "memo": "* The chemicals used to dye clothes cause water pollution. $\\checkmark$\n* Dyeing requires large amounts of water, which impacts the availability of (drinking) water. $\\checkmark$ (2)",
        "final_answer": "Dyeing consumes vast amounts of water and releases toxic chemical runoff into waterways, harming aquatic life and reducing clean water resources.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{source_id}-1.7",
        "source_id": source_id,
        "pair_source_id": pair_source_id,
        "subject": subject,
        "grade": grade,
        "language": language,
        "track": track,
        "kind": "passage_questions",
        "question_ref": "1.7",
        "marks": 2,
        "topic": "Comprehension - Text A (Environmental impact of jeans)",
        "passage": passage_sec_a,
        "question": "Refer to paragraph 7.\nHow can the purchase of a single pair of jeans negatively impact the environment? State TWO points.",
        "memo": "* Washing the jeans releases microfibres into the ocean thus polluting it. $\\checkmark$\n* $10\\ 000$ litres of water go into the manufacturing of a single pair of jeans thereby reducing water resources. $\\checkmark$\n* The fuel used in the shipping and delivery of the jeans contributes to pollution. $\\checkmark$\n\n**NOTE:** Accept any TWO of the above answers. (2)",
        "final_answer": "Over $10\\ 000$ litres of water are used to produce a single pair, washing them releases microfibres into the ocean, and transporting them burns fuel that pollutes the environment.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{source_id}-1.8",
        "source_id": source_id,
        "pair_source_id": pair_source_id,
        "subject": subject,
        "grade": grade,
        "language": language,
        "track": track,
        "kind": "passage_questions",
        "question_ref": "1.8",
        "marks": 2,
        "topic": "Comprehension - Text A (Critical Evaluation: Fast fashion concerns)",
        "passage": passage_sec_a,
        "question": "Consider the text as a whole.\nDo you think that the environmental impact of the fashion industry is a serious concern that requires immediate action? Substantiate your response.",
        "memo": "**Open-ended. Accept a suitable answer, e.g.**\n\n**Yes.**\nThe manufacturing process results in water pollution and the amount of water used leads to the exhaustion of valuable resources. The pollution caused by dumping and overconsumption is devastating as rubbish dumps will be filled. If consumers do not change their behaviour as soon as possible, it will be too late to save the environment as the problem will escalate and resources will disappear. $\\checkmark\\checkmark$\n\n**OR**\n\n**No.**\nThere are other factors that have a more devastating impact. The environmental impact of the fashion industry provides no immediate threat to humans. The fashion industry provides employment which contributes to the economy and thus outweighs any possible negative impact. $\\checkmark\\checkmark$\n\n**NOTE:** Accept other suitable answers. A candidate can score 1 mark for an answer that is not well substantiated. Accept a combination answer. (2)",
        "final_answer": "Yes. Fast fashion causes severe depletion of scarce water reserves, massive chemical pollution of rivers and oceans, and fills landfills with non-biodegradable synthetic waste, demanding immediate sustainable action.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{source_id}-1.9",
        "source_id": source_id,
        "pair_source_id": pair_source_id,
        "subject": subject,
        "grade": grade,
        "language": language,
        "track": track,
        "kind": "passage_questions",
        "question_ref": "1.9",
        "marks": 2,
        "topic": "Comprehension - Text A (Suitability of Title)",
        "passage": passage_sec_a,
        "question": "Discuss the suitability of the title, 'FAST FASHION'S FOOTPRINT'.",
        "memo": "**Open-ended. Accept a suitable answer, e.g.**\n\nThe title is suitable because it is linked to the passage that discusses the negative effects of fast fashion on the environment. Footprints are what one leaves behind. According to the passage, fashion manufacturing leaves both negative and positive footprints. $\\checkmark\\checkmark$\n\n**OR**\n\nThe title is not suitable because it could be misunderstood if one reads it out of context. It could also be difficult to understand how fashion could possibly leave a 'footprint'. $\\checkmark\\checkmark$\n\n**NOTE:** Accept other suitable answers. A candidate can score 1 mark for an answer that is not well substantiated. Accept a combination answer. (2)",
        "final_answer": "The title is suitable because 'footprint' refers metaphorically to the lasting environmental impact or damage left behind by rapid, disposable clothing manufacturing.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{source_id}-1.10",
        "source_id": source_id,
        "pair_source_id": pair_source_id,
        "subject": subject,
        "grade": grade,
        "language": language,
        "track": track,
        "kind": "passage_questions",
        "question_ref": "1.10",
        "marks": 2,
        "topic": "Comprehension - Text B (Agricultural water usage)",
        "passage": passage_sec_a,
        "question": "Refer to TEXT B.\nIdentify the continent which uses the least amount of water for agricultural purposes. Give a reason for your answer.",
        "memo": "Europe. $\\checkmark$\nThe section of the pie graph which represents Agricultural use is the smallest. $\\checkmark$ / The percentage indicated ($32\\%$) is the lowest $\\checkmark$ for Agricultural use when compared to other continents. (2)",
        "final_answer": "Europe. Its agricultural water usage is only $32\\%$, which is the lowest percentage among all five continents shown.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{source_id}-1.11",
        "source_id": source_id,
        "pair_source_id": pair_source_id,
        "subject": subject,
        "grade": grade,
        "language": language,
        "track": track,
        "kind": "passage_questions",
        "question_ref": "1.11",
        "marks": 1,
        "topic": "Comprehension - Text B (Industrial water usage)",
        "passage": passage_sec_a,
        "question": "Refer to TEXT B.\nWhat does $48\\%$ suggest about North America's water usage?",
        "memo": "It suggests that North America uses the largest amount of water ($48\\%$) for industrial purposes. $\\checkmark$ (1)",
        "final_answer": "It indicates that North America consumes the highest proportion of its water ($48\\%$) for industrial purposes.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{source_id}-1.12",
        "source_id": source_id,
        "pair_source_id": pair_source_id,
        "subject": subject,
        "grade": grade,
        "language": language,
        "track": track,
        "kind": "passage_questions",
        "question_ref": "1.12",
        "marks": 1,
        "topic": "Comprehension - Text B (Graph Legend / Key)",
        "passage": passage_sec_a,
        "question": "Refer to TEXT B.\nWhy are the small boxes included at the bottom of TEXT B?",
        "memo": "They show what the different shadings represent in this graph / they serve as a key/legend to explain the shadings. $\\checkmark$ (1)",
        "final_answer": "They serve as a key or legend explaining what each shading pattern represents in the pie charts.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{source_id}-1.13",
        "source_id": source_id,
        "pair_source_id": pair_source_id,
        "subject": subject,
        "grade": grade,
        "language": language,
        "track": track,
        "kind": "passage_questions",
        "question_ref": "1.13",
        "marks": 2,
        "topic": "Comprehension - Text B (Evaluation of Pie Graphs)",
        "passage": passage_sec_a,
        "question": "Refer to TEXT B.\nIn your view, do the pie graphs in this text succeed in conveying relevant information? Substantiate your answer.",
        "memo": "**Open-ended. Accept a suitable answer, e.g.**\n\n**Yes.**\nThe pie graphs depict the percentage of water used for different purposes in five continents. They clearly show that some continents use more water for industrial purposes while others use more water for farming or domestic purposes. $\\checkmark\\checkmark$\n\n**OR**\n\n**No.**\nThe pie graphs do not convey a relevant message. Not everyone can easily analyse pie graphs/charts. Written words would have conveyed the information more effectively. $\\checkmark\\checkmark$\n\n**NOTE:** Accept other suitable answers. A candidate can score 1 mark for an answer that is not well substantiated. Accept a combination answer. (2)",
        "final_answer": "Yes. The pie graphs clearly illustrate the comparative proportions and exact percentages of water allocated across the three main sectors in five distinct continents.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },

    # Section B: Summary (Question 2)
    {
        "item_id": f"{source_id}-2",
        "source_id": source_id,
        "pair_source_id": pair_source_id,
        "subject": subject,
        "grade": grade,
        "language": language,
        "track": track,
        "kind": "passage_questions",
        "question_ref": "2",
        "marks": 10,
        "topic": "Summary Writing - Text C (The Restorative Power of Vaseline)",
        "passage": passage_sec_b,
        "question": """Vaseline is a household brand in South Africa. Not only is Vaseline petroleum jelly fantastic for soothing chapped lips, but it also has many other purposes.

Read TEXT C below and list SEVEN benefits of using Vaseline petroleum jelly.

#### INSTRUCTIONS:
1. Your summary must be written in point form.
2. List your SEVEN points in full sentences, using no more than 70 words.
3. Number your sentences from 1 to 7.
4. Write only ONE point per sentence.
5. Use your OWN words as far as possible.
6. Indicate the total number of words you have used in brackets at the end of your summary.""",
        "memo": """The following points form the answer to the question:

| QUOTATIONS | FACTS (Candidates may phrase the facts differently.) |
| :--- | :--- |
| 1. 'The hydrating power of Vaseline is a good remedy for dry skin.'/ 'Applying it to the body after a shower keeps the skin moisturised.' | 1. Vaseline is used to treat dry skin. / Vaseline helps to keep the skin moisturised. $\\checkmark$ |
| 2. 'For minor wounds such as cuts, scrapes, scratches and burns, use Vaseline to keep the wound moist as doing this will aid the healing process.' | 2. It keeps less serious wounds moist in order to assist with healing. / It heals less serious wounds. $\\checkmark$ |
| 3. 'Vaseline is hypoallergenic; therefore, it is suitable for sensitive skin, making it a good skincare option for babies to prevent nappy rash.' | 3. It can be used on sensitive skin. / It can be used to prevent nappy rash. $\\checkmark$ |
| 4. 'Put some Vaseline on the itchy spots for instant relief.' | 4. Vaseline promptly relieves itchiness (caused by insect bites). $\\checkmark$ |
| 5. 'Rubbing a little Vaseline into the hair gives it instant shine…' | 5. Applying Vaseline to the hair makes it shiny. $\\checkmark$ |
| 6. '…reduces the look of split ends.' | 6. It hides split ends. $\\checkmark$ |
| 7. 'Coat the gum and surrounding hair with Vaseline and pull gently to remove the gum.' | 7. Vaseline makes the removal of chewing gum from hair less challenging. $\\checkmark$ |
| 8. 'For teeth whitening, mix two tablespoons of baking soda with Vaseline and apply to dry teeth using a toothbrush.' | 8. A mixture of Vaseline and baking soda can be used to whiten teeth. $\\checkmark$ |
| 9. 'Apply a combination of Vaseline and salt on the edges of flower pots to keep them protected.' | 9. Applying a mixture of Vaseline and salt on the edges of flower pots will keep pests/snails and ants away. $\\checkmark$ |

#### MARKING THE SUMMARY:
* **Mark allocation:**
  * 7 marks for 7 points (1 mark per main point)
  * 3 marks for language
  * **Total marks: 10**

* **Distribution of language marks when a candidate has not quoted verbatim:**
  * 1–3 points correct: award 1 mark
  * 4–5 points correct: award 2 marks
  * 6–7 points correct: award 3 marks

* **Distribution of language marks when a candidate has quoted verbatim:**
  * 6–7 quotes: award 0 language marks
  * 4–5 quotes: award a maximum of 1 language mark
  * 2–3 quotes: award a maximum of 2 language marks

* **Word count:**
  * Markers are required to verify the number of words used.
  * Do not deduct marks if the candidate fails to indicate the word count or indicates it incorrectly.
  * If the word limit is exceeded, read up to the end of the sentence containing the 70th word and ignore the rest.""",
        "final_answer": """1. Vaseline effectively treats dry skin by retaining moisture after bathing.
2. It keeps minor cuts and burns moist to speed up healing.
3. It prevents nappy rash and protects sensitive baby skin.
4. Applying it provides fast relief from itchy bug bites and bee stings.
5. It adds shine to dull hair and conceals split ends.
6. It simplifies removing chewing gum trapped in hair.
7. Combined with baking soda, it acts as a teeth whitener.

(67 words)""",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },

    # Section C: Language Structures and Conventions
    # Question 3: Analysing an Advertisement
    {
        "item_id": f"{source_id}-3.1",
        "source_id": source_id,
        "pair_source_id": pair_source_id,
        "subject": subject,
        "grade": grade,
        "language": language,
        "track": track,
        "kind": "passage_questions",
        "question_ref": "3.1",
        "marks": 2,
        "topic": "Analysing an Advertisement - Headline Techniques",
        "passage": passage_sec_c_q3,
        "question": "Refer to the headline.\nHow does the advertiser attract the reader's attention? Give TWO points.",
        "memo": """The advertiser attracts the reader's attention by:
* using capital letters $\\checkmark$
* using bigger font $\\checkmark$
* using bold font $\\checkmark$
* making the letters in the words 'FIRE DANGER' appear 'damaged' $\\checkmark$
* making the letter G (in DANGER) appear to be falling $\\checkmark$
* using the words 'CAUTION' and 'FIRE DANGER' $\\checkmark$

**NOTE:** Accept any TWO of the above answers. (2)""",
        "final_answer": "By using large, bold capital letters and designing the letters in 'FIRE DANGER' to appear burnt or damaged, with the letter 'G' falling.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{source_id}-3.2",
        "source_id": source_id,
        "pair_source_id": pair_source_id,
        "subject": subject,
        "grade": grade,
        "language": language,
        "track": track,
        "kind": "multiple_choice",
        "question_ref": "3.2",
        "marks": 1,
        "topic": "Analysing an Advertisement - Function of Apostrophe",
        "passage": passage_sec_c_q3,
        "question": """Choose the correct answer to complete the following sentence.

Fire is everyone's fight.

The function of the apostrophe in the above sentence is to indicate ...

A omission.  
B contraction.  
C possession.  
D abbreviation.""",
        "memo": "C / possession. $\\checkmark$ (1)",
        "final_answer": "C / possession.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{source_id}-3.3",
        "source_id": source_id,
        "pair_source_id": pair_source_id,
        "subject": subject,
        "grade": grade,
        "language": language,
        "track": track,
        "kind": "passage_questions",
        "question_ref": "3.3",
        "marks": 1,
        "topic": "Analysing an Advertisement - Root Words",
        "passage": passage_sec_c_q3,
        "question": "Study the following subheading:\n\n*District emergency numbers for reporting veld fires*\n\nIdentify the root of the underlined word (*reporting*).",
        "memo": "report / port $\\checkmark$ (1)",
        "final_answer": "report",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{source_id}-3.4",
        "source_id": source_id,
        "pair_source_id": pair_source_id,
        "subject": subject,
        "grade": grade,
        "language": language,
        "track": track,
        "kind": "passage_questions",
        "question_ref": "3.4",
        "marks": 2,
        "topic": "Analysing an Advertisement - Emergency Numbers",
        "passage": passage_sec_c_q3,
        "question": "How does the inclusion of various telephone numbers support the message of the advertisement? State TWO points.",
        "memo": "The reader can call the nearest emergency service $\\checkmark$ from any location/district $\\checkmark$ to report veld fires. $\\checkmark$\n\n**NOTE:** Accept any TWO of the above answers. (2)",
        "final_answer": "It provides specific district numbers so anyone can immediately contact their closest local emergency service from any area to report fires promptly.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{source_id}-3.5",
        "source_id": source_id,
        "pair_source_id": pair_source_id,
        "subject": subject,
        "grade": grade,
        "language": language,
        "track": track,
        "kind": "passage_questions",
        "question_ref": "3.5",
        "marks": 2,
        "topic": "Analysing an Advertisement - Stakeholder Logos",
        "passage": passage_sec_c_q3,
        "question": "Why has the advertiser included the different logos at the bottom of this advertisement?",
        "memo": "To show that these organisations/stakeholders $\\checkmark$ support the call to prevent unplanned veld fires. $\\checkmark$ (2)",
        "final_answer": "To demonstrate that these official government bodies and emergency organisations endorse the campaign and are united in preventing veld fires.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{source_id}-3.6",
        "source_id": source_id,
        "pair_source_id": pair_source_id,
        "subject": subject,
        "grade": grade,
        "language": language,
        "track": track,
        "kind": "passage_questions",
        "question_ref": "3.6",
        "marks": 2,
        "topic": "Analysing an Advertisement - Visual Effectiveness",
        "passage": passage_sec_c_q3,
        "question": "Discuss whether the visual of the animal effectively conveys the message of the advertisement.",
        "memo": """**Open-ended. Accept a suitable answer, e.g.**

**Yes.**
The visual of the animal encircled by flames creates sympathy and could encourage people to be cautious about starting veld fires. They could also report veld fires thus protecting the animals from potential harm. $\\checkmark\\checkmark$

**OR**

**No.**
There is no clear link between the visual of the animal and the advertisement. It is an animated drawing and not a picture of a real animal. People like hunters would not be sympathetic towards the animal. No animals are mentioned in the written text of the advertisement. $\\checkmark\\checkmark$

**NOTE:** Do not award a mark for Yes or No. The above are merely examples. A candidate can score 1 mark for an answer that is not well substantiated. Accept a combination answer. (2)""",
        "final_answer": "Yes. The image of an innocent animal trapped in flames evokes emotional sympathy, reminding readers of the dire threat veld fires pose to wildlife and nature.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },

    # Question 4: Analysing a Cartoon
    {
        "item_id": f"{source_id}-4.1",
        "source_id": source_id,
        "pair_source_id": pair_source_id,
        "subject": subject,
        "grade": grade,
        "language": language,
        "track": track,
        "kind": "passage_questions",
        "question_ref": "4.1",
        "marks": 2,
        "topic": "Analysing a Cartoon - Body Language Comparison",
        "passage": passage_sec_c_q4,
        "question": "Refer to FRAME 2.\nHow is Jon's body language different to that of Garfield? State TWO points.",
        "memo": """* Jon's eyes are half-closed and Garfield's eyes are wide open. $\\checkmark\\checkmark$
* Jon is sitting while Garfield is jumping up and down. $\\checkmark\\checkmark$

**NOTE:**
* Accept ANY other suitable answer provided that the contrast is clear.
* Award 2 or 0 marks. (2)""",
        "final_answer": "Jon is sitting quietly with sleepy, half-closed eyes, whereas Garfield is on his feet jumping up and down with wide, alert eyes.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{source_id}-4.2",
        "source_id": source_id,
        "pair_source_id": pair_source_id,
        "subject": subject,
        "grade": grade,
        "language": language,
        "track": track,
        "kind": "passage_questions",
        "question_ref": "4.2",
        "marks": 2,
        "topic": "Analysing a Cartoon - Visual Clues of Impact",
        "passage": passage_sec_c_q4,
        "question": "Explain how the cartoonist conveys the idea that Garfield is bothering Jon in Frame 3.\nState TWO visual clues.",
        "memo": """* The movement lines show Garfield hitting Jon with his paw. $\\checkmark$
* The word 'SMACK' (in bold) emphasises that Garfield has startled Jon. $\\checkmark$
* The liquid in Jon's cup is spilling over because Garfield has pushed him. $\\checkmark$
* Jon is leaning forward indicating that he has been pushed. $\\checkmark$

**NOTE:** Accept any TWO of the above answers. (2)""",
        "final_answer": "Garfield's paw strikes Jon with visible movement lines, the bold sound effect 'SMACK' denotes impact, and coffee spills out of Jon's mug as he jolts forward.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{source_id}-4.3",
        "source_id": source_id,
        "pair_source_id": pair_source_id,
        "subject": subject,
        "grade": grade,
        "language": language,
        "track": track,
        "kind": "passage_questions",
        "question_ref": "4.3",
        "marks": 1,
        "topic": "Analysing a Cartoon - Contractions",
        "passage": passage_sec_c_q4,
        "question": "Refer to FRAME 5.\nRewrite the underlined contraction in full.\n\n'Oh, okay, **we'll** play.'",
        "memo": "we will / we shall $\\checkmark$ (1)",
        "final_answer": "we will",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{source_id}-4.4",
        "source_id": source_id,
        "pair_source_id": pair_source_id,
        "subject": subject,
        "grade": grade,
        "language": language,
        "track": track,
        "kind": "passage_questions",
        "question_ref": "4.4",
        "marks": 2,
        "topic": "Analysing a Cartoon - Verbal and Visual Clues",
        "passage": passage_sec_c_q4,
        "question": "Refer to FRAME 7.\nExplain how Jon's actions convey that he is in pain. Refer to ONE verbal and ONE visual clue in your answer.",
        "memo": """* **Verbal:** He shouts 'OUCH!' $\\checkmark$ / 'OUCH!' is written in bold. $\\checkmark$ / There is an exclamation mark. $\\checkmark$
* **Visual:** His mouth is wide open. $\\checkmark$ / The movement lines behind his head and back indicate that he tilts his head in (sudden) pain. $\\checkmark$ / Jon spreads out his fingers in pain. $\\checkmark$

**NOTE:** One verbal and one visual clue must be mentioned. (2)""",
        "final_answer": "Verbal: He shouts 'OUCH!' in bold capital letters with an exclamation mark. Visual: His mouth is open wide in a cry of agony and his fingers are spread out in shock.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{source_id}-4.5",
        "source_id": source_id,
        "pair_source_id": pair_source_id,
        "subject": subject,
        "grade": grade,
        "language": language,
        "track": track,
        "kind": "passage_questions",
        "question_ref": "4.5",
        "marks": 1,
        "topic": "Analysing a Cartoon - Homonyms / Homophones",
        "passage": passage_sec_c_q4,
        "question": "Study the following sentence.\n\n'I'm **through** playing now'\n\nUse a homonym for the word *through* in a sentence of your own.",
        "memo": "I looked through the window. $\\checkmark$ / The boy threw the ball. $\\checkmark$\n\n**NOTE:** Accept other suitable responses. (1)",
        "final_answer": "I looked through the window to see who was outside.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{source_id}-4.6",
        "source_id": source_id,
        "pair_source_id": pair_source_id,
        "subject": subject,
        "grade": grade,
        "language": language,
        "track": track,
        "kind": "passage_questions",
        "question_ref": "4.6",
        "marks": 2,
        "topic": "Analysing a Cartoon - Critical Response",
        "passage": passage_sec_c_q4,
        "question": "Do you sympathise with Jon in this cartoon? Discuss your view.",
        "memo": """**Open-ended. Accept a suitable answer, e.g.**

**Yes.**
Jon is enjoying his beverage when Garfield startles him. Garfield pesters Jon until he plays with him. They both appear to be enjoying the game. Garfield bites Jon to end the game and Jon does not deserve to be bitten. $\\checkmark\\checkmark$

**OR**

**No.**
Jon tickles Garfield. However, Garfield does not like being tickled (for too long). Jon should have been more careful when playing with an animal as cats are aggressive and unpredictable. $\\checkmark\\checkmark$

**NOTE:** Do not award a mark for Yes or No. The above are merely examples. A candidate can score 1 mark for an answer that is not well substantiated. Accept a combination answer. (2)""",
        "final_answer": "Yes. Jon was relaxing peacefully when Garfield repeatedly harassed him to play, and when Jon kindly obliged, Garfield violently bit him for no good reason.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },

    # Question 5: Language and Editing Skills
    # 5.1 (Text F)
    {
        "item_id": f"{source_id}-5.1.1a",
        "source_id": source_id,
        "pair_source_id": pair_source_id,
        "subject": subject,
        "grade": grade,
        "language": language,
        "track": track,
        "kind": "passage_questions",
        "question_ref": "5.1.1a",
        "marks": 1,
        "topic": "Language & Editing - Concord",
        "passage": passage_sec_c_q5_1,
        "question": "Correct the SINGLE error in the following sentence. Write down ONLY the question number and the word you have corrected.\n\nThere is beekeepers who keep the critical bee populations healthy.",
        "memo": "are $\\checkmark$ (1)",
        "final_answer": "are",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{source_id}-5.1.1b",
        "source_id": source_id,
        "pair_source_id": pair_source_id,
        "subject": subject,
        "grade": grade,
        "language": language,
        "track": track,
        "kind": "passage_questions",
        "question_ref": "5.1.1b",
        "marks": 1,
        "topic": "Language & Editing - Spelling",
        "passage": passage_sec_c_q5_1,
        "question": "Correct the SINGLE error in the following sentence. Write down ONLY the question number and the word you have corrected.\n\nThey have managed swarms to prevent the number of bees from diclining.",
        "memo": "declining $\\checkmark$ (1)",
        "final_answer": "declining",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{source_id}-5.1.1c",
        "source_id": source_id,
        "pair_source_id": pair_source_id,
        "subject": subject,
        "grade": grade,
        "language": language,
        "track": track,
        "kind": "passage_questions",
        "question_ref": "5.1.1c",
        "marks": 1,
        "topic": "Language & Editing - Indefinite Articles",
        "passage": passage_sec_c_q5_1,
        "question": "Correct the SINGLE error in the following sentence. Write down ONLY the question number and the word you have corrected.\n\nKeeping swarms is an hobby that requires only a small investment of time and money.",
        "memo": "a $\\checkmark$ (1)",
        "final_answer": "a",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{source_id}-5.1.1d",
        "source_id": source_id,
        "pair_source_id": pair_source_id,
        "subject": subject,
        "grade": grade,
        "language": language,
        "track": track,
        "kind": "passage_questions",
        "question_ref": "5.1.1d",
        "marks": 1,
        "topic": "Language & Editing - Prepositions",
        "passage": passage_sec_c_q5_1,
        "question": "Correct the SINGLE error in the following sentence. Write down ONLY the question number and the word you have corrected.\n\nIt can be harvested twice on one season.",
        "memo": "in $\\checkmark$ (1)",
        "final_answer": "in",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{source_id}-5.1.2",
        "source_id": source_id,
        "pair_source_id": pair_source_id,
        "subject": subject,
        "grade": grade,
        "language": language,
        "track": track,
        "kind": "passage_questions",
        "question_ref": "5.1.2",
        "marks": 1,
        "topic": "Language & Editing - Question Tags",
        "passage": passage_sec_c_q5_1,
        "question": "Complete the following tag question. Write down only the missing words.\n\nBeekeepers ensure that their bees are safe, ...?",
        "memo": "don't they / do they not $\\checkmark$ (1)",
        "final_answer": "don't they",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{source_id}-5.1.3",
        "source_id": source_id,
        "pair_source_id": pair_source_id,
        "subject": subject,
        "grade": grade,
        "language": language,
        "track": track,
        "kind": "passage_questions",
        "question_ref": "5.1.3",
        "marks": 1,
        "topic": "Language & Editing - Tense Transformation",
        "passage": passage_sec_c_q5_1,
        "question": "Rewrite the following sentence in the simple future tense:\n\nBees also play a major role in pollinating vital plants.",
        "memo": "Bees will also play a major role in pollinating vital plants. $\\checkmark$ (1)",
        "final_answer": "Bees will also play a major role in pollinating vital plants.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{source_id}-5.1.4",
        "source_id": source_id,
        "pair_source_id": pair_source_id,
        "subject": subject,
        "grade": grade,
        "language": language,
        "track": track,
        "kind": "passage_questions",
        "question_ref": "5.1.4",
        "marks": 3,
        "topic": "Language & Editing - Reported Speech",
        "passage": passage_sec_c_q5_1,
        "question": "Rewrite the following sentence in reported speech:\n\nHe said, 'I turned the passion for bees into a business.'",
        "memo": """He said (that) he $\\checkmark$ had turned $\\checkmark$ the passion for bees into a business. $\\checkmark$

**NOTE:** Award ONE mark for each underlined change and ONE mark for correct punctuation. (3)""",
        "final_answer": "He said that he had turned the passion for bees into a business.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{source_id}-5.1.5",
        "source_id": source_id,
        "pair_source_id": pair_source_id,
        "subject": subject,
        "grade": grade,
        "language": language,
        "track": track,
        "kind": "passage_questions",
        "question_ref": "5.1.5",
        "marks": 1,
        "topic": "Language & Editing - Synonyms",
        "passage": passage_sec_c_q5_1,
        "question": "Provide a synonym for the underlined word in the following sentence:\n\nBoucher **rescues** swarms that need to be removed from areas where they pose a potential danger.",
        "memo": "saves $\\checkmark$ (1)",
        "final_answer": "saves",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{source_id}-5.1.6",
        "source_id": source_id,
        "pair_source_id": pair_source_id,
        "subject": subject,
        "grade": grade,
        "language": language,
        "track": track,
        "kind": "passage_questions",
        "question_ref": "5.1.6",
        "marks": 1,
        "topic": "Language & Editing - Homophones",
        "passage": passage_sec_c_q5_1,
        "question": "Study the following sentence:\n\nHe explained that they were not **allowed** to keep bees in densely populated areas like blocks of flats.\n\nUse a homophone for the word *allowed* in a sentence of your own.",
        "memo": "He enjoys thinking aloud. $\\checkmark$ / The teacher read the poem aloud. $\\checkmark$\n\n**NOTE:** Accept other suitable responses. (1)",
        "final_answer": "The student read the poem aloud to the class.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{source_id}-5.1.7",
        "source_id": source_id,
        "pair_source_id": pair_source_id,
        "subject": subject,
        "grade": grade,
        "language": language,
        "track": track,
        "kind": "passage_questions",
        "question_ref": "5.1.7",
        "marks": 1,
        "topic": "Language & Editing - Active Voice",
        "passage": passage_sec_c_q5_1,
        "question": "Rewrite the following sentence in the active voice:\n\nA beekeeping permit is required by anyone who wishes to become a beekeeper.",
        "memo": "Anyone who wishes to become a beekeeper requires a beekeeping permit. $\\checkmark$ (1)",
        "final_answer": "Anyone who wishes to become a beekeeper requires a beekeeping permit.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{source_id}-5.1.8",
        "source_id": source_id,
        "pair_source_id": pair_source_id,
        "subject": subject,
        "grade": grade,
        "language": language,
        "track": track,
        "kind": "passage_questions",
        "question_ref": "5.1.8",
        "marks": 2,
        "topic": "Language & Editing - Parts of Speech",
        "passage": passage_sec_c_q5_1,
        "question": "Study the following sentence:\n\nMore **information** about keeping bees **or** the safe removal of swarms is available on the internet.\n\nState the part of speech of EACH of the underlined words (*information*, *or*) as used in this sentence.",
        "memo": "* information – noun $\\checkmark$\n* or – conjunction $\\checkmark$ (2)",
        "final_answer": "information: noun; or: conjunction",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },

    # 5.2 (Text G)
    {
        "item_id": f"{source_id}-5.2.1",
        "source_id": source_id,
        "pair_source_id": pair_source_id,
        "subject": subject,
        "grade": grade,
        "language": language,
        "track": track,
        "kind": "passage_questions",
        "question_ref": "5.2.1",
        "marks": 1,
        "topic": "Language & Editing - Negative Form",
        "passage": passage_sec_c_q5_2,
        "question": "Rewrite the following sentence in the negative form:\n\nMy siblings enjoy eating raw vegetables.",
        "memo": "My siblings don't/do not enjoy eating raw vegetables. $\\checkmark$ (1)",
        "final_answer": "My siblings do not enjoy eating raw vegetables.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{source_id}-5.2.2",
        "source_id": source_id,
        "pair_source_id": pair_source_id,
        "subject": subject,
        "grade": grade,
        "language": language,
        "track": track,
        "kind": "passage_questions",
        "question_ref": "5.2.2",
        "marks": 2,
        "topic": "Language & Editing - Sentence Synthesis ('Not only...')",
        "passage": passage_sec_c_q5_2,
        "question": """Combine the following sentences into a single sentence.

Spinach tastes good.  
Spinach improves digestion.

Begin with: **Not only ...**""",
        "memo": """Not only does spinach taste good, $\\checkmark$ (but) it also improves digestion. $\\checkmark$  
**OR**  
Not only does spinach improve digestion, $\\checkmark$ (but) it also tastes good. $\\checkmark$ (2)""",
        "final_answer": "Not only does spinach taste good, but it also improves digestion.",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{source_id}-5.2.3",
        "source_id": source_id,
        "pair_source_id": pair_source_id,
        "subject": subject,
        "grade": grade,
        "language": language,
        "track": track,
        "kind": "passage_questions",
        "question_ref": "5.2.3",
        "marks": 1,
        "topic": "Language & Editing - Degrees of Comparison",
        "passage": passage_sec_c_q5_2,
        "question": "Provide the correct degree of comparison in the following sentence:\n\nFresh vegetables from the garden are (**nutritious**) than frozen ones.",
        "memo": "more/less nutritious $\\checkmark$ (1)",
        "final_answer": "more nutritious",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{source_id}-5.2.4",
        "source_id": source_id,
        "pair_source_id": pair_source_id,
        "subject": subject,
        "grade": grade,
        "language": language,
        "track": track,
        "kind": "passage_questions",
        "question_ref": "5.2.4",
        "marks": 1,
        "topic": "Language & Editing - Adverb Formation",
        "passage": passage_sec_c_q5_2,
        "question": "Give the correct form of the word in brackets:\n\nEating healthy meals can (**significant**) improve one's breathing.",
        "memo": "significantly $\\checkmark$ (1)",
        "final_answer": "significantly",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    },
    {
        "item_id": f"{source_id}-5.2.5",
        "source_id": source_id,
        "pair_source_id": pair_source_id,
        "subject": subject,
        "grade": grade,
        "language": language,
        "track": track,
        "kind": "multiple_choice",
        "question_ref": "5.2.5",
        "marks": 1,
        "topic": "Language & Editing - Collective Nouns",
        "passage": passage_sec_c_q5_2,
        "question": """Choose the correct answer to complete the following sentence.

When you go to the market, please buy me a ... of spinach.

A bunch  
B bundle  
C bucket  
D bouquet""",
        "memo": "A / bunch $\\checkmark$ (1)",
        "final_answer": "A / bunch",
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    }
]

# Validation
total_marks = sum(item["marks"] for item in items)
print(f"Total items: {len(items)}")
print(f"Total marks: {total_marks}")
assert total_marks == 80, f"Expected 80 marks, got {total_marks}"

# KaTeX dollar balance validation
katex_errors = 0
for i, it in enumerate(items):
    for f in ["passage", "question", "memo", "final_answer"]:
        text = it[f]
        # Count non-escaped dollar signs
        dollars = len(re.findall(r"(?<!\\)\$", text))
        if dollars % 2 != 0:
            print(f"Unbalanced dollars in item {it['item_id']}, field {f}: count={dollars}")
            katex_errors += 1

print(f"KaTeX errors: {katex_errors}")
assert katex_errors == 0, f"Found {katex_errors} KaTeX dollar balance errors"

# Save to target paths
paths = [
    f"workspace/items/{subject}/{source_id}.jsonl",
    f"workspace/items/{source_id}.jsonl",
    f"sa-tutor-kit/sa-tutor-kit/workspace/items/{subject}/{source_id}.jsonl",
    f"sa-tutor-kit/sa-tutor-kit/workspace/items/{source_id}.jsonl"
]

# Write JSONL
lines = [json.dumps(it, ensure_ascii=False) for it in items]
content = "\n".join(lines) + "\n"

for p in paths:
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Successfully wrote {len(items)} items to {p}")
