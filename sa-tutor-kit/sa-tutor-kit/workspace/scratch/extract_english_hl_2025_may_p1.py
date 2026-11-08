#!/usr/bin/env python3
"""
extract_english_hl_2025_may_p1.py
Extracts DBE English Home Language Grade 12 Paper 1 May/June 2025
into atomic JSONL items following the Universal Document & Visual Extraction Standard (UDVES).
"""

import json
import re
import sys
from pathlib import Path

# Paths
ROOT = Path(__file__).resolve().parents[2] # sa-tutor-kit/sa-tutor-kit
ITEMS_ENGLISH_HL = ROOT / "workspace" / "items" / "english_hl" / "dbe-english_hl-g12-p1-2025-may.jsonl"
ITEMS_ROOT = ROOT / "workspace" / "items" / "dbe-english_hl-g12-p1-2025-may.jsonl"

SOURCE_ID = "dbe-english_hl-g12-p1-2025-may"
PAIR_SOURCE_ID = "dbe-english_hl-g12-p1-2025-may-memo"
SUBJECT = "english_hl"
GRADE = 12
LANGUAGE = "en"
TRACK = "languages_hl"
LICENCE = "DBE copyright - check terms"
ATTRIBUTION = "Department of Basic Education"

# --- PASSAGES ---

PASSAGE_TEXT_A = """TEXT A

HITCHHIKING: THE ALTERNATIVE FORM OF TRANSPORT THAT NOBODY USES
– Adam Weymouth

1. Petrol prices and youth unemployment are on the rise. So, why are people not thumbing it?

2. A recent survey published by the Automobile Association (AA) found that only 9 per cent of drivers would be likely to pick up a hitchhiker, compared to 25 per cent two years ago. The media took this as clear-cut confirmation of the death of hitchhiking. Yet, while it is true that there are fewer of us thumbing on the roads than there used to be, in my many years of hitching, I have never once been left stranded.

3. Last week I hitched a lift for a two-hour drive and chatted with a technician about economic woes, encouraged someone to take to the road themselves, and had a lecture on how to make my own diesel from potato fat. There are not many forms of transport where one can find such conversation, but regardless of this pleasure, hitchhiking should be thriving. With increasing petrol prices, people struggling to make ends meet, record-high youth unemployment and an urgent need to cut carbon emissions, a revival of hitchhiking seems to be long overdue. It has happened in other countries – part of Cuba's solution to its oil crisis was a boom in hitching.

4. In the eighties, a rash of horror movies is partly credited with the demise of hitchhiking. The best known is *The Hitcher*, starring Rutger Hauer as a psychotic and motiveless hitchhiker, pursuing a suitably tight-jeaned and wind-swept young man. It is his very lack of motive that makes him terrifying. The idea is that strangers are unknowable. You cannot risk trusting them because you cannot understand them.

5. But are we more scared of strangers than we used to be? It seems more complex than that because hitchhiking is not dead, just woefully under-practised. Perhaps the hitchhikers are more fearful of strangers than the drivers are. What if young adults – the supposedly tough and fearless twenty-somethings – are too scared to relinquish their control? According to the AA, 93 per cent of 18- to 24-year-olds surveyed have never hitched a ride. This is understandable from a generation that has grown up in a more controlled and ordered environment than any other generation. Perhaps, we cannot bear uncertainty and see strangers less like bringers of joy and more like Rutger Hauer. Certainly, I am picked up less by young drivers than by anyone else, and not because young people are less likely to own cars.

6. Undoubtedly, there is a risk in hitchhiking; pretending otherwise is *facile*$^{\\text{1}}$. However, hospitality can only be rendered risk-free by assessing one's guests carefully. We live in a world in which we attempt to control as much as possible. We do this, *perversely*$^{\\text{2}}$, by destroying the things – like a sense of community and openness to strangers – that truly keep us safe. One should take precautions, as one would with any travel, for example hitching with a friend, or only in the daytime, or only in countries where one speaks the language. But we should avoid living in a world where there is no trust in strangers and be mindful of the implications of creating such a world.

7. During the Second World War there was a boom of goodwill towards the servicemen and women hitching home on leave. The baton was taken up by the culture of the sixties, and those who had hitched through the wars now had cars and a debt to repay. Many of those who pick up hitchhikers were themselves hitchers in the sixties and seventies, and are looking to reciprocate the hospitality shown to them. They were strangers once, and they now open their doors to the strangers of today. So, the cycle continues, for the moment. Yet I wonder who will pick up the next generation of hitchhikers as they stand by the road for weeks on end with their signs dissolving in the rain. If this generation does not hitch, this cycle of hospitality slows to a halt, and fear of the stranger will know no bounds. Hitchhiking is not a dead art, but it may well be one generation away from extinction.

8. This is not an intellectual argument, but a practical one. Stick out your thumb and see what happens. Take a car off the roads, save yourself some money, and give drivers the opportunity to show their hospitality. Hitch to work one day or accompany someone who has hitchhiker before. And, if you are a driver, find a hitchhiker, stop and pick up a hitchhiker. Without beginning to cultivate a deep empathy for the stranger, and without learning to trust the unpredictable nature of the world, it would be hard to see what else humanity can achieve.

[Adapted from theecologist.org]

GLOSSARY:
$^{\\text{1}}$ *facile:* superficial/ignoring the complexities of an issue
$^{\\text{2}}$ *perversely:* rebelliously or irrationally"""

PASSAGE_TEXT_B = """TEXT B

[DIAGRAM: Visual Poster / Public Safety Awareness Campaign | Black-and-white photograph of a young woman seen from behind standing on the gravel shoulder of a desolate rural highway, extending her right arm and thumbing a ride. A dark duffel travel bag rests on the ground beside her. Ahead stretches a long, empty two-lane asphalt road flanked by dense forest trees, with a lone, distant vehicle approaching far down the road. | High-contrast white block text is superimposed across the upper center of the road:
"THIS RIDE
MAY TAKE YOU TO
A PLACE YOU
DON'T WANT TO GO"

Beneath her shadow, bold text reads:
"IF YOU ACCEPT RIDES FROM STRANGERS . . ."
followed by 5 safety guidelines:
> Let someone know where you are going, when you expect to get there and that you have arrived safely.
> Carry a mobile phone and identification with you at all times.
> If you hitchhike, use roads that are heavily travelled.
> Always note the description of anyone who offers you a ride, including their vehicle.
> Share information about suspicious persons with the police – you could SAVE a life!

At the bottom in a solid dark banner with high-contrast white text:
"TRUST your INSTINCTS.
If someone makes you feel uncomfortable, DON’T GET IN!"]

[Adapted from thenorthernview.com]"""

PASSAGE_TEXTS_A_AND_B = PASSAGE_TEXT_A + "\n\n---\n\n" + PASSAGE_TEXT_B

PASSAGE_TEXT_C = """TEXT C

THE UNIQUE WORLD OF FRUGAL LIVING

Being frugal means using less and performing many tiny tasks in a very inexpensive way to save more money, resources, and live a lower wastage lifestyle. It's also about choosing quality over quantity.

For years, frugal ideas have been popular, and some people enjoy discovering how to save money and resources. It has sometimes been associated with the assumption that the frugal lifestyle is usually achieved cheaply; however, this is not the case! It is about taking the time to care for your products and assets properly so that they last long past their expiration date.

In our new reality of recycling and up-cycling, it is a better alternative to choose to keep valuable items for charity, or to recycle. There is a wealth of information on the internet about repurposing, recycling and repairing things yourself, particularly in the do-it-yourself business.

Frugal living does not only focus on saving on material goods. Health is also an area to be explored. Going out every day to consume fast food and junk food is neither frugal nor healthy. Home-cooked meals are certainly more nourishing and less expensive than eating out, and planning meals and grocery budgets can help you save a significant amount of money monthly. Whenever you can, try to freeze items that freeze well, so that you have less wastage.

Keeping an eye out for discounts or promotions is another popular money-saving strategy and buying in bulk can save you money in the long run. Being frugal with your money means only buying what you need and sticking to that single rule. Unwanted goods can be sold online to make a few rands while also giving those items a second chance to be in their life cycle for a longer period.

Car-pooling means that more people become invested in saving. If your commute is not too far, walking or cycling to work might save you a lot of money, especially given the current fuel prices.

Frugal living does not imply being stingy; rather, it entails being extremely prudent and observant about where and how you spend your money.

[Adapted from wonga.co.za]"""

PASSAGE_TEXT_D = """TEXT D

[DIAGRAM: Print Advertisement | Social Cause Campaign by Raising the Roof | Black-and-white urban street scene. On the left pavement curb, an abandoned vintage upholstered armchair with tufted back and tapered wooden legs sits next to a cardboard box of discarded items in front of a residential picket fence and decorative wrought-iron gate. The asphalt road surface occupies the foreground. On the right-hand side, text in white lettering is superimposed over the dark asphalt with contrasting font weights:
Upper text in prominent, heavy BOLD slab-serif font:
"You see an
abandoned chair
on the street
and you think
'It has the potential
to be something
beautiful.'"

Lower text in much thinner, REGULAR-weight font:
"You see a homeless
youth on the street
and you think
'Don't make eye
contact.'"

At the bottom left, the organisation's logo displays a roofline silhouette with the slogan:
"RAISING THE ROOF
HOMELESS YOUTH HAVE NOTHING, BUT POTENTIAL."]

[Source: twitter.com]"""

PASSAGE_TEXT_E = """TEXT E: CARTOON

[DIAGRAM: Comic Strip | Hank Ketcham's Dennis the Menace titled "Wrap It Up!" | 9 Frames |
CHARACTERS:
- Dennis (young boy in striped t-shirt and bib overalls)
- Mrs Wilson (elderly woman with curly white hair, glasses, and polka-dot dress)
- Mr Wilson / George (elderly man, balding with side hair, mustache, grumpy demeanor)

FRAME 1 (Title Panel): Dennis playfully wraps Mr Wilson tightly like a mummy in Christmas wrapping paper with Christmas tree patterns, holding a roll of tape. Title text reads: "Hank Ketcham's Dennis the Menace" and "Wrap It Up!".
FRAME 2: Dennis sits comfortably and happily on Mrs Wilson's lap on an armchair in the living room, pointing enthusiastically at an open holiday catalog. Dennis's speech bubble: "THERE'S SO MANY COOL THINGS IN THIS CATALOG!" Mrs Wilson smiles down at him warmly.
FRAME 3: Dennis's voice carries over from the other room in a speech bubble: "I WISH I COULD GET 'EM ALL!" In the next room, Mr Wilson sips from a coffee mug, frowning deeply with narrowed eyes and intense suspicion. Mr Wilson's thought bubble reads: "I'LL BET YOU DO."
FRAME 4: Dennis points at an item in the catalog, calling out (speech bubble): "HOW ABOUT THIS ONE, MISSUS WILSON?" Mrs Wilson responds pleasantly: "THAT IS COLORFUL, DEAR." In the dining room, Mr Wilson sits at the table with his coffee cup and a vase of flowers, rolling his eyes upward with an exasperated expression, a small thought bubble floating above him.
FRAME 5: Close-up of Mrs Wilson looking at the catalog with Dennis sitting eagerly before her. Mrs Wilson's speech bubble: "BUT ALSO VERY EXPENSIVE!" Dennis smiles cheerfully and replies: "SO WHAT..."
FRAME 6: Dennis's speech bubble concludes from off-panel: "...IT'S CHRISTMAS!" In the dining area, Mr Wilson's face turns dark with furious anger, teeth clenched, eyebrows angled sharply, speech bubble: "OF ALL THE..."
FRAME 7: Dennis waves happily as he exits through the front door into the snow: "BYE!" Mrs Wilson stands at the doorway waving affectionately: "GOOD-BYE, SWEETHEART!" In the hallway background, Mr Wilson scowls darkly from behind a doorway, glaring after Dennis.
FRAME 8: Mr Wilson bursts into the room in a furious rage, shouting aggressively with a jagged speech bubble: "THAT GREEDY KID! ALL HE KNOWS IS GIMME, GIMME, GIMME!!" Mrs Wilson looks back at him calmly and matter-of-factly, stating in her speech bubble: "FOR YOUR INFORMATION, HE WAS PICKING A CHRISTMAS PRESENT FOR YOU." Mr Wilson's scowl suddenly freezes in shock, his eyes widening in stunned realization.
FRAME 9: Mrs Wilson serves a bowl of soup with a spoon to Mr Wilson at the dining table. Mr Wilson sits completely dumbfounded, speechless, and thoroughly embarrassed, sweat drops flying from his head. Mrs Wilson looks at him with a dry, knowing smirk and remarks: "HERE'S YOUR SOUP, GEORGE. I THOUGHT YOU'D LIKE IT COLD. MAYBE IT WILL HELP YOU TO CHILL OUT."]

[Source: comicskingdom.com]"""

PASSAGE_TEXT_F = """TEXT F

HOW HAS TIPPING CULTURE IN THE CITY CHANGED?

1. A few Decembers ago, a heart-warming trend emerged where patrons challenged each other to tip double their bill to give waitrons a Christmas bonus. Since then, Covid-19 along with rising inflation has seen a change in tipping culture.

2. While waitrons say their regulars religiously and faithfully tip the regulated 10% – or more if in a generous mood – others simply don't tip at all. A number of establishments have now introduced the practice of waitrons sharing their tips with the kitchen and cleaning staff.

3. While waitrons now earn a basic wage supplemented by tips they receive, many waitrons said they keep their basic wage for 'rainy days' when tips run dry. Snethemba Gwala, a waitron, said, 'The more experienced you are the better: you are able to serve many tables at once and correctly, which helps you to get good tips and you will find your customers come back and ask for you.'

4. Wendy Alberts, the CEO of Restaurants Association of South Africa (RASA) said the restaurant industry is well-supported, and good tips are dependent on good service.

[Adapted from citizen.co.za]"""


# --- ALL 36 ITEMS ---

ITEMS = [
    # SECTION A: QUESTION 1 (TEXTS A & B)
    {
        "question_ref": "1.1",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Comprehension: Vocabulary in context / Idiomatic expressions",
        "passage": PASSAGE_TEXT_A,
        "question": "Provide the meaning of the expression, 'thumbing it' in paragraph 1.",
        "memo": "'Thumbing it' means asking for a lift/hitching a ride/hitchhiking. (1)",
        "final_answer": "Asking for a lift / hitchhiking / hitching a ride.",
        "needs_review": False,
    },
    {
        "question_ref": "1.2",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Comprehension: Interpretation of statistics",
        "passage": PASSAGE_TEXT_A,
        "question": "What is indicated by the statistics in lines 4–5?",
        "memo": "The statistics indicate that the number of drivers willing to offer others a lift has decreased/very few people are willing to offer hitchhikers a lift/there is a decrease in hitchhiking. (1)",
        "final_answer": "A decrease in the number of drivers willing to offer hitchhikers a lift / a decline in the willingness of motorists to pick up hitchhikers.",
        "needs_review": False,
    },
    {
        "question_ref": "1.3",
        "marks": 2,
        "kind": "passage_questions",
        "topic": "Comprehension: Writer's attitude / Critique of media",
        "passage": PASSAGE_TEXT_A,
        "question": "Refer to lines 5–6: 'The media took this as clear-cut confirmation of the death of hitchhiking.'\nWhat comment is the writer making about the media?",
        "memo": "The media misrepresented the information (1) provided by the Automobile Association, by making the claim that hitchhiking is dead (1). (2)",
        "final_answer": "The writer comments that the media misrepresents and exaggerates the AA survey findings by sensationalising them into an absolute claim that hitchhiking is dead.",
        "needs_review": False,
    },
    {
        "question_ref": "1.4",
        "marks": 2,
        "kind": "passage_questions",
        "topic": "Comprehension: Anecdotal evidence / Writer's purpose",
        "passage": PASSAGE_TEXT_A,
        "question": "Explain why the writer has made reference to his experience of hitchhiking in paragraph 2.",
        "memo": "The writer is convincing us that despite the statistics/the media's pessimistic attitude towards hitchhiking (1), he has always secured a lift (1). (2)",
        "final_answer": "To counter the media's pessimistic narrative and prove through personal experience that hitchhiking remains viable, as he has never once been left stranded.",
        "needs_review": False,
    },
    {
        "question_ref": "1.5",
        "marks": 2,
        "kind": "passage_questions",
        "topic": "Comprehension: Societal benefits of hitchhiking",
        "passage": PASSAGE_TEXT_A,
        "question": "Refer to paragraph 3.\nIn your own words, explain how hitchhiking can benefit society.",
        "memo": "By hitchhiking, people reduce the impact on the environment (1) and the economic costs involved in travelling (1). Hitchhiking also leads to interesting conversation (1).\n*[Award only 1 mark for lifting.]*\n*[Award 2 marks for two distinct points.]* (2)",
        "final_answer": "It reduces environmental carbon emissions, eases financial hardship by saving travel expenses, and fosters engaging interpersonal conversations.",
        "needs_review": False,
    },
    {
        "question_ref": "1.6",
        "marks": 2,
        "kind": "passage_questions",
        "topic": "Comprehension: Impact of emotive diction",
        "passage": PASSAGE_TEXT_A,
        "question": "Refer to paragraph 4.\nDiscuss the impact of the emotive adjectives, like 'psychotic', 'motiveless' and 'unknowable', on the reader.",
        "memo": "The use of these adjectives creates a sense of panic and fear of strangers./\nThe diction reinforces the idea that strangers may not be trusted.\n*[Award 2 marks for two distinct points.]* (2)",
        "final_answer": "These words evoke intense fear and paranoia, reinforcing the reader's suspicion that strangers are dangerous, incomprehensible, and untrustworthy.",
        "needs_review": False,
    },
    {
        "question_ref": "1.7",
        "marks": 2,
        "kind": "passage_questions",
        "topic": "Comprehension: Function of rhetorical question",
        "passage": PASSAGE_TEXT_A,
        "question": "Refer to lines 26–28: 'What if young … relinquish their control?'\nSuggest why the writer poses this rhetorical question.",
        "memo": "The writer challenges/engages the reader to consider the notion that young people should overcome their fear of losing control/embrace the opportunity to hitchhike.\nOR\nThe rhetorical question allows the reader to consider whether young people are really as fearless and adventurous as they claim to be.\n*[Award only 1 mark for a generic response.]*\n*[Award 2 marks for two distinct points.]* (2)",
        "final_answer": "To challenge the stereotype that young adults are tough and fearless, prompting the reader to consider whether they are actually too afraid of losing control and uncertainty to hitchhike.",
        "needs_review": False,
    },
    {
        "question_ref": "1.8",
        "marks": 3,
        "kind": "passage_questions",
        "topic": "Comprehension: Evaluation of objectivity vs subjectivity",
        "passage": PASSAGE_TEXT_A,
        "question": "Comment on whether the writer's views, as presented in paragraph 5, are objective.",
        "memo": "The writer quotes statistics to create an impression of objectivity. However, he is subjective because he speculates ('It seems more complex ...') about the cause of the decline in hitchhiking among young adults. Furthermore, through his repeated use of the word 'perhaps', he finally presents anecdotal evidence to round off his argument which confirms his subjectivity.\n*[Award 3 marks only if a comment is made.]* (3)",
        "final_answer": "The writer's views are subjective: although he cites an AA statistic to create an appearance of factual objectivity, he relies on speculation ('perhaps', 'What if') and personal anecdotal experience to draw conclusions about young people's fear of strangers.",
        "needs_review": False,
    },
    {
        "question_ref": "1.9",
        "marks": 3,
        "kind": "passage_questions",
        "topic": "Comprehension: Critical discussion of assertion",
        "passage": PASSAGE_TEXT_A,
        "question": "'Hitchhiking is not a dead art, but it may well be one generation away from extinction' (lines 54–55).\nCritically discuss this assertion in the context of paragraph 7.",
        "memo": "By elevating hitchhiking to an 'art', the writer reiterates that it is enriching to both the hitchhiker and the driver. Earlier generations continued the practice of hitchhiking as an act of 'goodwill' and the need to 'reciprocate the hospitality' shown over time. However, due to generational differences, this practice is under threat ('one generation away from extinction'). Now, people are more cautious and this threatens the 'cycle of hospitality'.\n*[Award 3 marks only if there is a critical discussion.]* (3)",
        "final_answer": "The assertion emphasizes that hitchhiking is an enriching cultural 'cycle of hospitality' sustained across generations through reciprocal goodwill. Because the younger generation no longer participates due to fear and caution, this generational chain is breaking, putting the entire tradition at risk of dying out.",
        "needs_review": False,
    },
    {
        "question_ref": "1.10",
        "marks": 3,
        "kind": "passage_questions",
        "topic": "Comprehension: Effectiveness of persuasive writing style",
        "passage": PASSAGE_TEXT_A,
        "question": "In your view, is the writing style of paragraph 8 effective? Substantiate your answer with reference to ONE example.",
        "memo": "YES\nThe writer's use of stylistic devices strengthens his stance.\n* He begins by asserting that his argument is 'practical' as hitchhiking will allow the hitchhiker to save money and give people an opportunity to be generous.\n* This is supported by the use of imperatives – 'Stick out your thumb ...', 'Take a car ...', 'Hitch to work ...' – to encourage the practice of offering a stranger a lift.\n* The use of emotive phrases such as 'deep empathy' and 'trust the unpredictable' appeals to humanity's goodwill to take the risk.\n* The use of personal pronouns ('your thumb', 'yourself', 'you') engages the reader to participate in the act of hitchhiking, as either a hitchhiker or a driver.\n\n*[Credit mixed responses.]*\n*[A 'NO' response is unlikely. However, assess each response on its own merit.]*\n*[Award 3 marks only if the effectiveness of the writing style has been discussed.]* (3)",
        "final_answer": "Yes: The style is highly effective because the writer uses direct, urgent imperative commands such as 'Stick out your thumb' and 'Take a car off the roads', combined with second-person pronouns ('you', 'yourself'), transforming an abstract argument into a direct, persuasive call to action.",
        "needs_review": False,
    },
    {
        "question_ref": "1.11",
        "marks": 2,
        "kind": "passage_questions",
        "topic": "Visual Literacy: Atmosphere and mood in imagery",
        "passage": PASSAGE_TEXT_B,
        "question": "What atmosphere is created by the picture? Give a reason for your response.",
        "memo": "A sense of desolation/foreboding/uneasiness (1) is created by the single figure/long road/approaching vehicle/surrounding forest (1).\n*[Accept valid synonymous words/phrases.]* (2)",
        "final_answer": "An atmosphere of desolation, vulnerability, or foreboding, created by the lone female figure stranded on an empty country road flanked by isolated woods.",
        "needs_review": False,
    },
    {
        "question_ref": "1.12.1",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Figures of speech: Irony identification",
        "passage": PASSAGE_TEXT_B,
        "question": "Choose the most appropriate response from the list of options provided.\n\n'THIS RIDE MAY TAKE YOU TO A PLACE YOU DON'T WANT TO GO' is an example of …\nA litotes.\nB metaphor.\nC hyperbole.\nD irony.",
        "memo": "D – irony (1)",
        "final_answer": "D",
        "needs_review": False,
    },
    {
        "question_ref": "1.12.2",
        "marks": 3,
        "kind": "passage_questions",
        "topic": "Visual Literacy: Critical discussion of poster message",
        "passage": PASSAGE_TEXT_B,
        "question": "Critically discuss the above expression in the context of this poster.",
        "memo": "The young woman chooses to hitchhike and willingly places herself in the hands of a stranger. However, while she believes that she has a destination in mind, it is not under her control, as the driver chooses where to go. This can lead to other dangerous consequences beyond her initial choice/intention.\n*[Credit valid alternative responses.]* (3)",
        "final_answer": "The expression highlights the bitter irony that a hitchhiker seeking a lift to reach a desired destination surrenders all physical control to an unknown driver, potentially ending up abducted, harmed, or in grave danger rather than at their intended location.",
        "needs_review": False,
    },
    {
        "question_ref": "1.13",
        "marks": 3,
        "kind": "passage_questions",
        "topic": "Comprehension & Visual Literacy: Comparative synthesis of Texts A and B",
        "passage": PASSAGE_TEXTS_A_AND_B,
        "question": "Refer to paragraph 6 of TEXT A, and TEXT B.\nDoes TEXT B reinforce the writer's view expressed in paragraph 6 of TEXT A? Justify your answer.",
        "memo": "YES\nTEXT B cautions people about being too trusting of a stranger and provides a list of precautions to consider. This supports paragraph 6, where the writer advocates that one should take measures to ensure one's safety like 'assessing one's guests'. Furthermore, both the writer of TEXT A and the poster advise hitchhikers to be very cautious ('TRUST your INSTINCTS') about accepting the kindness of 'strangers', since to ignore the risk is naive ('facile').\nOR\nNO\nTEXT B presents a negative view of hitchhiking, where one instinctively avoids this practice. A menacing atmosphere, created by the emphatic conclusion ('TRUST your INSTINCTS ... DON'T GET IN!'), prevails in TEXT B. Yet, in paragraph 6 of TEXT A the writer encourages one to trust strangers and not to accept a world that promotes mistrust. The writer's blind faith/idealistic view of the goodness of humanity contrasts with the message of the poster.\n*[Credit mixed responses.]*\n*[Award 3 marks only if reference is made to paragraph 6 of TEXT A and TEXT B.]* (3)",
        "final_answer": "YES: Both texts acknowledge that hitchhiking carries inherent danger (Text A states it is 'facile' to pretend otherwise, while Text B issues grave warnings) and both advocate sensible precautions rather than reckless trust. (OR NO: Text B instils fear and total avoidance of strangers, whereas Text A warns against a paranoid world devoid of trust and community.)",
        "needs_review": False,
    },

    # SECTION B: QUESTION 2 (TEXT C SUMMARY)
    {
        "question_ref": "2",
        "marks": 10,
        "kind": "passage_questions",
        "topic": "Summary: How people can adopt a frugal lifestyle",
        "passage": PASSAGE_TEXT_C,
        "question": "TEXT C discusses the value of living frugally. Summarise, in your own words, **how people can adopt a frugal lifestyle.**\n\n**NOTE:**\n1. Your summary should include SEVEN points and NOT exceed 90 words.\n2. You must write a fluent paragraph.\n3. You are NOT required to include a title for the summary.\n4. Indicate your word count at the end of your summary.",
        "memo": """Use the following main points that the candidate should include in the summary as a guideline.
Any 7 valid points are to be credited in paragraph-form.
*(Sentences and/or sentence fragments must be coherent.)*

| NO. | QUOTATIONS | NO. | POINTS |
| :---: | :--- | :---: | :--- |
| 1 | 'It's also about choosing quality over quantity.' | 1 | It is more cost-effective to purchase quality products. |
| 2 | 'It is about taking the time to care for your products and assets properly so that they last long past their expiration date.' | 2 | People who live frugally take care of their possessions. |
| 3 | 'In our new reality of recycling and up-cycling, it is a better alternative to choose to keep valuable items for charity, or to recycle.'/'... repurposing, recycling, and repairing things yourself.' | 3 | Thrifty people repurpose, recycle and do their own repairs. |
| 4 | 'Home-cooked meals are certainly more nourishing and less expensive than eating out ...' | 4 | Money can be saved when one prepares meals at home, rather than eating out. |
| 5 | '... planning meals and grocery budgets can help you save a significant amount of money monthly.' | 5 | Careful planning and saving reduces one's monthly grocery budget. |
| 6 | 'Whenever you can, try to freeze items that freeze well, so that you have less wastage.' | 6 | Frugal people freeze their left-overs to prevent wastage. |
| 7 | 'Keeping an eye out for discounts or promotions is another popular money-saving strategy ...' | 7 | People who want to save money purchase goods at discounted prices. |
| 8 | '... buying in bulk can save you money in the long run.' | 8 | Bulk purchases are more economical. |
| 9 | 'Being frugal with your money means only buying what you need and sticking to that single rule.'/ '...using less and performing very tiny tasks in a very inexpensive way to save more money ...'/ '...it entails being extremely prudent and observant about where and how you spend your money.' | 9 | They consistently only buy what is needed. |
| 10 | 'Unwanted goods can be sold online to make a few rands ...' | 10 | Living frugally encourages people to sell unwanted goods online. |
| 11 | 'Car-pooling means that more people become invested in saving.' | 11 | Travelling together in one car allows more people to save. |
| 12 | 'If your commute is not too far, walking or cycling to work might save you a lot of money ...' | 12 | Frugal living motivates people to walk or cycle to work to save money. |

PARAGRAPH FORM (EXEMPLAR):
People who live frugally take care of their possessions, repurpose unwanted items through recycling and up-cycling and repair their damaged goods. They save when they prepare meals at home, and they freeze their left-overs. Careful planning and saving reduce their monthly grocery budget. People who want to save money purchase goods at discounted prices, buy in bulk and only buy what is needed. Living frugally encourages people to sell unwanted goods online. Furthermore, travelling together in one car, or walking or cycling to work allows more people to save. [89 words]

Mark allocation:
- 7 marks for 7 points (1 mark per main point)
- 3 marks for language
- Total marks: 10

Distribution of language marks when candidate has not quoted verbatim:
- 1–3 points correct: award 1 mark
- 4–5 points correct: award 2 marks
- 6–7 points correct: award 3 marks

Distribution of language marks when candidate has quoted verbatim:
- 6 to 7 quotes: award no language mark
- 4 to 5 quotes: award a maximum of 1 language mark
- 2 to 3 quotes: award a maximum of 2 language marks

Word Count:
- Markers must verify word count.
- Upper limit: 90 words.""",
        "final_answer": "A fluent paragraph of 7 points (max 90 words) covering care of assets, DIY/recycling, cooking at home, freezing leftovers, buying essentials in bulk/at discounts, selling unwanted items, and carpooling/walking.",
        "needs_review": False,
    },

    # SECTION C: QUESTION 3 (TEXT D ADVERTISEMENT)
    {
        "question_ref": "3.1.1",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Advertising: Idiomatic expression meaning",
        "passage": PASSAGE_TEXT_D,
        "question": "Refer to 'RAISING THE ROOF'.\nWhat is the meaning of the above expression?",
        "memo": "The expression means to make a noise/shout out. (1)",
        "final_answer": "To make a lot of noise / shout loudly / celebrate exuberantly.",
        "needs_review": False,
    },
    {
        "question_ref": "3.1.2",
        "marks": 2,
        "kind": "passage_questions",
        "topic": "Advertising: Literal and figurative wordplay",
        "passage": PASSAGE_TEXT_D,
        "question": "Refer to 'RAISING THE ROOF'.\nExplain how the expression is both literally and figuratively suitable, in the context of the advertisement.",
        "memo": "In the context of the advertisement, the organisation builds housing for homeless youth (1) and it makes people aware of the plight of these young people (1). (2)",
        "final_answer": "Literally, the organisation provides shelter and builds physical roofs/homes for homeless youth; figuratively, it makes noise and raises public awareness about youth homelessness.",
        "needs_review": False,
    },
    {
        "question_ref": "3.2",
        "marks": 2,
        "kind": "passage_questions",
        "topic": "Advertising: Typography and font choice",
        "passage": PASSAGE_TEXT_D,
        "question": "Refer to: 'You see an … make eye contact.'\nHow does the font on the right-hand side reinforce the advertiser's message?",
        "memo": "The bold font used by the advertiser draws the reader's attention, and this gives the inanimate article (chair) more value than the homeless youth, who is referred to in normal font./Minimal attention is given to the homeless youth because there are so many of them that they fade into the background (like the normal font); whereas seeing a chair on the pavement is unusual and therefore, more noticeable – like the bold font.\n*[Credit valid references made to the bold font versus normal font.]* (2)",
        "final_answer": "The bold font prominently foregrounds the discarded chair, making an inanimate object stand out and seem valuable, whereas the thin, normal font used for the homeless youth illustrates how vulnerable humans are overlooked and allowed to fade into the background.",
        "needs_review": False,
    },
    {
        "question_ref": "3.3",
        "marks": 3,
        "kind": "passage_questions",
        "topic": "Advertising: Visual image effectiveness",
        "passage": PASSAGE_TEXT_D,
        "question": "Is the visual image effective in conveying the message of the advertisement? Justify your response.",
        "memo": "YES\nThe discarded chair is foregrounded and is the focus of the visual. No homeless youth appear in the image, emphasising the point that they are unseen/ignored/not worthy of being seen/saved. The advertiser thus highlights how material objects receive greater recognition than homelessness.\nOR\nNO\nThe absence of the homeless youth makes the advertisement ineffective as their situation is not visible to the reader. The small font of the slogan, 'HOMELESS YOUTH HAVE NOTHING, BUT POTENTIAL' takes away the important message that the advertiser is trying to convey. The discarded chair becomes the focus instead of the homeless youth.\n*[Credit valid alternative/mixed responses.]*\n*[Award 3 marks for a well-developed response.]* (3)",
        "final_answer": "YES: The visual is effective because the discarded armchair is prominently foregrounded while homeless youth are completely absent, visually embodying the advertiser's message that society notices and sees potential in discarded furniture while ignoring homeless people.",
        "needs_review": False,
    },
    {
        "question_ref": "3.4",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Vocabulary: Synonyms in context",
        "passage": PASSAGE_TEXT_D,
        "question": "Provide a contextually correct synonym for the word 'abandoned'.",
        "memo": "discarded/dumped\n*[Accept valid alternative synonyms, in context.]* (1)",
        "final_answer": "Discarded / dumped / deserted.",
        "needs_review": False,
    },
    {
        "question_ref": "3.5",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Language: Root words / Etymology",
        "passage": PASSAGE_TEXT_D,
        "question": "What is the root word of 'potential'?",
        "memo": "potent (1)",
        "final_answer": "potent",
        "needs_review": False,
    },

    # SECTION C: QUESTION 4 (TEXT E CARTOON)
    {
        "question_ref": "4.1",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Cartoons: Character motivation and emotion",
        "passage": PASSAGE_TEXT_E,
        "question": "Why is Mr Wilson angry in FRAME 3?",
        "memo": "Mr Wilson is distrustful of Dennis's motives./Mr Wilson believes that Dennis is trying to manipulate Mrs Wilson/benefit himself. (1)",
        "final_answer": "He distrusts Dennis's motives and assumes Dennis is acting greedy, trying to get Mrs Wilson to buy everything for him.",
        "needs_review": False,
    },
    {
        "question_ref": "4.2",
        "marks": 2,
        "kind": "passage_questions",
        "topic": "Cartoons: Character attitude and relationship",
        "passage": PASSAGE_TEXT_E,
        "question": "Refer to FRAMES 2, 5 and 7.\nExplain what is revealed about Mrs Wilson's attitude towards Dennis.",
        "memo": "Mrs Wilson treats Dennis lovingly. He is sitting on her lap./She speaks to him in a gentle tone of voice./She refers to him as 'SWEETHEART'.\n*[Credit valid alternative responses.]*\n*[Award 1 mark for identification of the attitude and 1 mark for the explanation.]* (2)",
        "final_answer": "Mrs Wilson displays a warm, affectionate, and loving maternal attitude toward Dennis, evidenced by letting him sit on her lap, gently indulging his catalog browsing, and tenderly calling him 'SWEETHEART'.",
        "needs_review": False,
    },
    {
        "question_ref": "4.3",
        "marks": 2,
        "kind": "passage_questions",
        "topic": "Cartoons: Tone analysis",
        "passage": PASSAGE_TEXT_E,
        "question": "Discuss Dennis's tone in FRAMES 5 and 6.",
        "memo": "Dennis's tone is nonchalant/blasé/excited/demanding/entitled. He is comfortable/enthusiastic about sharing his views on how the Christmas season should be celebrated.\n*[Award 1 mark for the identification of tone and 1 mark for a discussion.]* (2)",
        "final_answer": "Dennis's tone is nonchalant, dismissive, or enthusiastically innocent ('SO WHAT... IT'S CHRISTMAS!'), showing that he blithely brushes off financial cost because Christmas justifies generous giving.",
        "needs_review": False,
    },
    {
        "question_ref": "4.4",
        "marks": 3,
        "kind": "passage_questions",
        "topic": "Cartoons: Humour and dramatic irony",
        "passage": PASSAGE_TEXT_E,
        "question": "With close reference to FRAME 9 and the cartoon as a whole, critically discuss how humour is conveyed.",
        "memo": "In FRAME 9 Mrs Wilson gently mocks Mr Wilson and his overreaction by suggesting that he needs to 'CHILL OUT'. She is referencing the irony of Mr Wilson's misinterpreting what he believed was Dennis's efforts to enrich himself – not realising that Dennis was searching for gifts to please Mr Wilson. The cartoon is humorous as Mr Wilson's preconceived ideas about Dennis fuel his anger/rage. He is still dumbfounded in Frame 9 as Mrs Wilson sarcastically offers him cold soup to literally cool off.\n*[Candidates may also make reference to the pun in 'Wrap It Up!']*\n*[Award 3 marks for a critical discussion.]* (3)",
        "final_answer": "Humour arises from dramatic irony and verbal wit: Mr Wilson worked himself into a furious rage assuming Dennis was being selfish, only to learn Dennis was choosing a gift for him. In Frame 9, Mrs Wilson serves cold soup and sarcastically puns that it will help him 'CHILL OUT', leaving him sweating and speechless in total embarrassment.",
        "needs_review": False,
    },
    {
        "question_ref": "4.5",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Grammar: Subject-verb concord",
        "passage": PASSAGE_TEXT_E,
        "question": "Rewrite Dennis's words in FRAME 2 so that the sentence is grammatically CORRECT.",
        "memo": "THERE ARE SO MANY COOL THINGS IN THIS CATALOG.\n*[Do not award marks for the correct spelling of 'CATALOG'.]* (1)",
        "final_answer": "There are so many cool things in this catalog.",
        "needs_review": False,
    },
    {
        "question_ref": "4.6",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Grammar: Reported speech / Indirect speech",
        "passage": PASSAGE_TEXT_E,
        "question": "Various options are provided as possible answers to the question below. Choose the correct answer and write only the letter (A–D) next to the question number (4.6).\n\nMrs Wilson's statement in FRAME 8, written in indirect speech, is:\nA Mrs Wilson said (to Mr Wilson) that Dennis had been picking a Christmas present for himself.\nB Mrs Wilson said (to Mr Wilson) that Dennis was picking a Christmas present for him.\nC Mrs Wilson said (to Mr Wilson) that Dennis had been picking a Christmas present for him.\nD Mrs Wilson said (to Mr Wilson) that Dennis had picked a Christmas present for you.",
        "memo": "C – Mrs Wilson said (to Mr Wilson) that Dennis had been picking a Christmas present for him. (1)",
        "final_answer": "C",
        "needs_review": False,
    },

    # SECTION C: QUESTION 5 (TEXT F LANGUAGE)
    {
        "question_ref": "5.1.1",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Grammar: Parts of speech",
        "passage": PASSAGE_TEXT_F,
        "question": "Refer to lines 1–2:\n'A few Decembers ago, a heart-warming trend emerged where patrons challenged each other to tip double their bill to give waitrons a Christmas bonus.'\n\nIdentify the part of speech of 'heart-warming'.",
        "memo": "compound adjective/adjective (1)",
        "final_answer": "Compound adjective / adjective",
        "needs_review": False,
    },
    {
        "question_ref": "5.1.2",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Grammar: Verb derivation",
        "passage": PASSAGE_TEXT_F,
        "question": "Refer to lines 1–2:\n'A few Decembers ago, a heart-warming trend emerged where patrons challenged each other to tip double their bill to give waitrons a Christmas bonus.'\n\nProvide the verb form of 'patron'.",
        "memo": "patronise (1)",
        "final_answer": "patronise",
        "needs_review": False,
    },
    {
        "question_ref": "5.1.3",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Grammar: Complex sentences / Clause analysis",
        "passage": PASSAGE_TEXT_F,
        "question": "Refer to lines 1–2:\n'A few Decembers ago, a heart-warming trend emerged where patrons challenged each other to tip double their bill to give waitrons a Christmas bonus.'\n\nWhy can the above sentence be classified as a complex sentence?",
        "memo": "The sentence has a main clause and a subordinate clause./The sentence comprises two clauses. (1)",
        "final_answer": "It contains an independent (main) clause and a dependent (subordinate) clause.",
        "needs_review": False,
    },
    {
        "question_ref": "5.2",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Punctuation: Function of dashes / Parenthesis",
        "passage": PASSAGE_TEXT_F,
        "question": "Provide the function of the dashes in lines 4–5.",
        "memo": "The dashes enclose additional information/parenthesis/an aside. (1)",
        "final_answer": "To indicate parenthesis / enclose additional explanatory information or an aside.",
        "needs_review": False,
    },
    {
        "question_ref": "5.3",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Editing: Redundancy / Tautology",
        "passage": PASSAGE_TEXT_F,
        "question": "Remove the redundancy in paragraph 2.",
        "memo": "Remove religiously or faithfully (1)",
        "final_answer": "Remove either 'religiously' or 'faithfully' (since both mean the same thing in this context).",
        "needs_review": False,
    },
    {
        "question_ref": "5.4",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Vocabulary: Idiomatic expressions in context",
        "passage": PASSAGE_TEXT_F,
        "question": "What does the idiomatic expression 'rainy days' (line 9) mean, in context?",
        "memo": "days of struggle/difficulty/challenges/strife/need\n*[Accept valid alternative responses, in context.]* (1)",
        "final_answer": "Times of financial hardship, difficulty, or unforeseen trouble/emergencies.",
        "needs_review": False,
    },
    {
        "question_ref": "5.5",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Morphology: Antonym prefixes",
        "passage": PASSAGE_TEXT_F,
        "question": "Supply the prefix required to form the antonym of 'experienced' (line 10).",
        "memo": "in-/inexperienced\n*[Accept un-/unexperienced.]* (1)",
        "final_answer": "in- (or un-)",
        "needs_review": False,
    },
    {
        "question_ref": "5.6",
        "marks": 2,
        "kind": "passage_questions",
        "topic": "Semantics: Ambiguity / Multiple meanings",
        "passage": PASSAGE_TEXT_F,
        "question": "'… which helps you to get good tips …' (lines 11–12)\n\nExplain how the above clause creates ambiguity.",
        "memo": "'Tips' could refer to more money (1) or more information/points/advice (1). (2)",
        "final_answer": "The word 'tips' has a double meaning: it can refer to financial gratuities (monetary rewards from customers) or to helpful pieces of advice and guidance.",
        "needs_review": False,
    },
    {
        "question_ref": "5.7",
        "marks": 1,
        "kind": "passage_questions",
        "topic": "Language conventions: Acronyms / Abbreviations",
        "passage": PASSAGE_TEXT_F,
        "question": "Write out CEO (line 13) in full.",
        "memo": "Chief Executive Officer (1)",
        "final_answer": "Chief Executive Officer",
        "needs_review": False,
    },
]


def check_latex_syntax(text):
    """Accurately check for broken LaTeX math blocks and syntax."""
    errors = []
    if re.search(r"\$\$[ \t]*\$\$", text):
        errors.append("Empty display math block")
    display_blocks = re.findall(r"\$\$.*?\$\$", text, flags=re.DOTALL)
    no_display = re.sub(r"\$\$.*?\$\$", " DISPLAYMATH ", text, flags=re.DOTALL)
    clean_no_display = no_display.replace(r"\$$", "ESCDOLLAR").replace(r"\$", "ESCDOLLAR")
    if clean_no_display.count("$$") % 2 != 0:
        errors.append("Unclosed display math block ($$)")
    inline_blocks = re.findall(r"(?<!\\)\$(?!\s)(.+?)(?<!\s)\$", no_display)
    broken_fracs = len(re.findall(r"\\frac(?![{\s\d])", text))
    if broken_fracs > 0:
        errors.append(f"Broken fraction commands: {broken_fracs}")
    return errors, len(display_blocks) + len(inline_blocks)


def main():
    print(f"Total items defined: {len(ITEMS)}")
    total_marks = sum(item["marks"] for item in ITEMS)
    print(f"Total marks: {total_marks} / 70")
    assert total_marks == 70, f"Expected 70 marks, got {total_marks}"
    assert len(ITEMS) == 36, f"Expected 36 items, got {len(ITEMS)}"

    # Construct final json objects
    final_records = []
    for item in ITEMS:
        qref = item["question_ref"]
        item_id = f"{SOURCE_ID}-{qref}"
        rec = {
            "item_id": item_id,
            "source_id": SOURCE_ID,
            "pair_source_id": PAIR_SOURCE_ID,
            "subject": SUBJECT,
            "grade": GRADE,
            "language": LANGUAGE,
            "track": TRACK,
            "kind": item["kind"],
            "question_ref": qref,
            "marks": item["marks"],
            "topic": item["topic"],
            "passage": item["passage"],
            "question": item["question"],
            "memo": item["memo"],
            "final_answer": item["final_answer"],
            "needs_review": item["needs_review"],
            "licence": LICENCE,
            "attribution": ATTRIBUTION,
        }

        # LaTeX syntax check on question, memo, passage
        for field in ["question", "memo", "passage", "final_answer"]:
            errs, count = check_latex_syntax(rec[field])
            if errs:
                print(f"LaTeX ERROR in item {item_id} field {field}: {errs}")
                sys.exit(1)

        final_records.append(rec)

    # Write dual files
    ITEMS_ENGLISH_HL.parent.mkdir(parents=True, exist_ok=True)
    ITEMS_ROOT.parent.mkdir(parents=True, exist_ok=True)

    with open(ITEMS_ENGLISH_HL, "w", encoding="utf-8") as f:
        for rec in final_records:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    print(f"Wrote {len(final_records)} items to {ITEMS_ENGLISH_HL}")

    with open(ITEMS_ROOT, "w", encoding="utf-8") as f:
        for rec in final_records:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    print(f"Wrote {len(final_records)} items to {ITEMS_ROOT}")

    # Verification
    for path in [ITEMS_ENGLISH_HL, ITEMS_ROOT]:
        assert path.exists(), f"File {path} does not exist"
        with open(path, "r", encoding="utf-8") as f:
            read_items = [json.loads(line) for line in f]
        assert len(read_items) == 36, f"File {path} has {len(read_items)} items instead of 36"
        read_marks = sum(r["marks"] for r in read_items)
        assert read_marks == 70, f"File {path} has {read_marks} marks instead of 70"
        print(f"Verified {path}: 36 items, {read_marks} marks, 100% valid JSON.")

    print("\nSUCCESS: All checks passed!")


if __name__ == "__main__":
    main()
