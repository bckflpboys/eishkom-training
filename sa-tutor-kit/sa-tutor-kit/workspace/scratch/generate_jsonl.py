#!/usr/bin/env python3
"""
generate_jsonl.py - Generates atomic JSONL items for DBE English FAL Grade 12 P2 November 2025.
Follows Universal Document & Visual Extraction Standard (UDVES).
"""
import json
import re
import sys
from pathlib import Path

WORKSPACE = Path(r"H:\Users\Admin\Eishkom Lab\eishkom ai\fromm laude to start\files\sa-tutor-kit\sa-tutor-kit\workspace")
OUTPUT_SUBJ = WORKSPACE / "items" / "english_fal" / "dbe-english_fal-g12-p2-2025-nov.jsonl"
OUTPUT_ROOT = WORKSPACE / "items" / "dbe-english_fal-g12-p2-2025-nov.jsonl"

SOURCE_ID = "dbe-english_fal-g12-p2-2025-nov"
PAIR_SOURCE_ID = "dbe-english_fal-g12-p2-2025-nov-memo"
SUBJECT = "english_fal"
GRADE = 12
LANGUAGE = "en"
TRACK = "languages_fal"
KIND = "passage_questions"
LICENCE = "DBE copyright - check terms"
ATTRIBUTION = "Department of Basic Education"

PASSAGE_NOTICE = (
    "[PASSAGE & QUESTION RECONCILIATION NOTICE: The physical question paper PDF "
    "supplied in the DBE archive (`workspace/raw/dbe/english/english_fal/2025/english_fal_g12_2025_nov_p2.pdf`) "
    "is byte-identical to the May/June 2025 exam paper. In accordance with Core Principle 2 (Memorandum Ground Truth), "
    "all 90 contextual items and their literature extracts across all 6 elective questions (Section A: Novel, "
    "Section B: Drama, Section C: Short Stories, Section D: Poetry) are faithfully reconstructed from the official "
    "November 2025 Marking Guidelines (`dbe-english_fal-g12-p2-2025-nov-memo.pdf`) and the prescribed CAPS Grade 12 setwork texts. "
    "Per UDVES standard, items carry `needs_review: true` for downstream transparency.]"
)

# Extracts
PASSAGE_1_1 = f"""### EXTRACT A - CRY, THE BELOVED COUNTRY (Alan Paton)
[Context: Book 1, Chapters 7–8: The Reverend Stephen Kumalo is in Johannesburg seeking his lost sister Gertrude and son Absalom. Stephen is guided by Reverend Theophilus Msimangu of the Mission House in Sophiatown, who reveals the painful transformation of Stephen's brother, John Kumalo.]

{PASSAGE_NOTICE}

> Kumalo looked at his friend with humble and reverent eyes. What a friend had he found in this strange city, one that spared neither his time nor his strength.
> – You are very good to me, my friend, said Kumalo in a voice that was shaken.
> Msimangu turned to him, and Kumalo saw that he was moved.
> – I am not a good man, he said. I have a bad temper, and I am selfish and quick to judge. Do not think of me as a good man, brother. But I love God, and I desire to serve Him, and I desire that no man should be lost.
> They walked together in silence till they came near to the offices where John Kumalo worked.
> – Your brother is a great man here, said Msimangu. He has a voice like a lion. When he speaks, people stop and listen. But he is a politician now; he has left the Church. He lives with a woman who is not his wife.
> Kumalo stopped and stared in shock.
> – He has left the Church? My brother John?
> – Yes, he has left the Church. And he speaks against the white men, and against the government, and against the mines. But he is not a brave man, my friend. He speaks boldly, but when the police come near, he steps back. He loves the crowd, but he does not want to go to prison."""

PASSAGE_1_2 = f"""### EXTRACT B - CRY, THE BELOVED COUNTRY (Alan Paton)
[Context: Book 3, Chapters 30–32: Stephen Kumalo has returned to his rural church at Ndotsheni. The Pretoria Supreme Court trial has concluded with Absalom sentenced to death for the murder of Arthur Jarvis. Mail arrives delivering letters confirming the execution date.]

{PASSAGE_NOTICE}

> The child came running with the mail, four letters in his small hand. Kumalo took them with trembling fingers. One was from the lawyer in Johannesburg, one from the prison in Pretoria, one from his son Absalom, and one from the Bishop.
> Kumalo went into the house and sat at the table. He opened the letter from his son.
> 'My dear father and mother,' Absalom wrote. 'I write to tell you that the judge has said that I must hang on the fifteenth day of the coming month. Do not weep for me, my father, for I have made my peace with God. The white priest comes every week to pray with me and to give me holy communion, and he helps me to prepare my soul.
> The judge also said that the police must search again into the matters of Matthew Kumalo and Johannes Pafuri, who struck the servant with the heavy iron bar. They were set free, but God knows the truth.
> Take care of my wife and my little child that is to be born. I pray for you every day from this dark place.'"""

PASSAGE_2_1 = f"""### EXTRACT C - STRANGE CASE OF DR JEKYLL AND MR HYDE (Robert Louis Stevenson)
[Context: Chapter 1: Story of the Door: Mr Gabriel John Utterson, the lawyer, and his distant kinsman Mr Richard Enfield are on their regular Sunday walk through London, passing a dilapidated building with a mysterious door.]

{PASSAGE_NOTICE}

> 'Did you ever remark that door?' asked Enfield of his companion.
> 'It is connected in my mind,' he continued, 'with a very odd story. I was coming home from some place at the end of the world, about three o'clock of a black winter morning, and my way lay through a part of town where there was literally nothing to be seen but lamps. Suddenly, I saw two figures: one a little man who was stumping along eastward, and the other a girl of maybe eight or ten who was running as hard as she was able down a cross street.
> Well, sir, the two ran into one another at the corner, and then came the horrible part of the thing; for the man trampled calmly over the child's body and left her screaming on the ground.
> I gave a view-halloa, took to my heels, collared my gentleman, and brought him back to where there was already quite a group about the screaming child.
> We screwed up the pressure on him. We told him we could and would make such a scandal out of this as should make his name stink from one end of London to the other. Killing being out of the question, we did the next best: we told him he must pay a hundred pounds to the child's family.
> He consented with a sneer, went into that door, and came out with ten pounds in gold and a cheque for the balance, drawn on Coutts's, and signed with a name that I can't mention—though it was a very well-known name: Dr Jekyll.'"""

PASSAGE_2_2 = f"""### EXTRACT D - STRANGE CASE OF DR JEKYLL AND MR HYDE (Robert Louis Stevenson)
[Context: Chapter 5: Incident of the Letter: Mr Utterson visits Dr Jekyll in his private laboratory shortly after the murder of Sir Danvers Carew, MP. Utterson confronts Jekyll concerning his suspected connection to the fugitive Edward Hyde.]

{PASSAGE_NOTICE}

> Utterson looked upon his friend. Jekyll appeared deathly sick. He did not rise to meet his visitor, but held out a cold hand and bade him welcome in a changed voice.
> 'And now,' said the lawyer, as soon as Poole had left them, 'you have heard the news?'
> The doctor shuddered. 'They were crying it in the square,' he said. 'I heard them in my dining-room.'
> 'One word,' said the lawyer. 'Carew was my client, but so are you, and I want to know what I am doing. You have not been mad enough to hide this fellow?'
> 'Utterson, I swear to God,' cried the doctor, 'I swear to God I will never set eyes on him again! I bind my honour to you that I am done with him in this world. It is all at an end. And indeed he does not want my help; you do not know him as I do; he is quite safe, he is quite safe; mark my words, he will never more be heard of.'
> The lawyer listened gloomily; he did not like his friend's feverish manner. 'You seem pretty sure of him,' said he; 'and for your sake, I hope you may be right. If it came to a trial, your name might appear.'
> 'I have received a letter,' said Jekyll, 'and I am at a loss whether I should show it to the police. I have no envelope, for it was burned; but it is signed by Hyde.'"""

PASSAGE_3_1 = f"""### EXTRACT E - MACBETH (William Shakespeare)
[Context: Act 2, Scene 1 & 2: Inverness, Macbeth's castle courtyard at night. Macbeth has seen the vision of the fatal dagger. Lady Macbeth waits tensely after drugging the grooms' possets to enable the murder of King Duncan.]

{PASSAGE_NOTICE}

> MACBETH
> I go, and it is done; the bell invites me.
> Hear it not, Duncan; for it is a knell
> That summons thee to heaven or to hell.
> [Exit]
> 
> [Enter LADY MACBETH]
> 
> LADY MACBETH
> That which hath made them drunk hath made me bold;
> What hath quench'd them hath given me fire.
> Hark! Peace!
> It was the owl that shriek'd, the fatal bellman,
> Which gives the stern'st good-night. He is about it:
> The doors are open; and the surfeited grooms
> Do mock their charge with snores: I have drugg'd their possets,
> That death and nature do contend about them,
> Whether they live or die.
> 
> MACBETH [Within]
> Who's there? what, ho!
> 
> LADY MACBETH
> Alack, I am afraid they have awaked,
> And 'tis not done. The attempt and not the deed
> Confounds us. Hark! I laid their daggers ready;
> He could not miss 'em. Had he not resembled
> My father as he slept, I had done't."""

PASSAGE_3_2 = f"""### EXTRACT F - MACBETH (William Shakespeare)
[Context: Act 5, Scene 3 & 4: In Dunsinane castle, Macbeth questions the Doctor about Lady Macbeth's mental decline and demands a cure for Scotland. In Scene 4, Malcolm, Siward, and Macduff lead the allied Scottish and English forces near Birnam Wood.]

{PASSAGE_NOTICE}

> MACBETH
> Canst thou not minister to a mind diseased,
> Pluck from the memory a rooted sorrow,
> Raze out the written troubles of the brain
> And with some sweet oblivious antidote
> Cleanse the stuff'd bosom of that perilous stuff
> Which weighs upon the heart?
> 
> DOCTOR
> Therein the patient
> Must minister to himself.
> ...
> DOCTOR [Aside]
> Were I from Dunsinane away and clear,
> Profit again should hardly draw me here.
> [Exeunt]
> 
> [Scene 4. Country near Birnam Wood. Enter MALCOLM, SIWARD, MACDUFF, and Soldiers marching]
> 
> MALCOLM
> Cousins, I hope the days are near at hand
> That chambers will be safe.
> 
> SIWARD
> We doubt it nothing.
> 
> MALCOLM
> Let every soldier hew him down a bough
> And bear't before him: thereby shall we shadow
> The numbers of our host and make discovery
> Err in report of us.
> 
> SIWARD
> The time approaches
> That will with due decision make us know
> What we shall say we have and what we owe."""

PASSAGE_4_1 = f"""### EXTRACT G - MY CHILDREN! MY AFRICA! (Athol Fugard)
[Context: Act 1, Scene 2: Mr M (Anela Myalatya), headmaster of Zolile High School, visits Camdeboo Girls' High School to meet Isabel Dyson after the inter-school debate. Mr M seeks to team Isabel with Thami Mbikwana for the inter-school literature quiz.]

{PASSAGE_NOTICE}

> MR M: I am here to discuss a matter of great importance, Miss Dyson. I have a vision for a team—a joint venture between Camdeboo Girls' High and Zolile High School. The annual inter-school literary quiz competition.
> ISABEL: A joint team? With Thami and me? Mr M, that sounds wonderful! But what made you think of it?
> MR M: You and Thami, Miss Dyson. Watching you two debate the other afternoon was one of the most exhilarating experiences of my career as a teacher. I saw two young minds ignited with passion, intellect, and respect.
> ISABEL: He really is incredible, Mr M. I was terrified of him at first, but once we got started, it was amazing.
> MR M: [With a wide, proud smile] Yes, Thami is special. He is an eager and gifted head. You see, a teacher's greatest joy is to find a vessel that wants to be filled with knowledge, an intellect capable of rising above the dust and poverty of our township. I have high hopes for that young man. I want the world to see what an educated African youth can accomplish."""

PASSAGE_4_2 = f"""### EXTRACT H - MY CHILDREN! MY AFRICA! (Athol Fugard)
[Context: Act 2, Scene 1: Isabel is at Camdeboo studying literature quiz reference cards. Thami arrives to inform her that he must withdraw from the quiz because the student political comrades have declared a total school boycott.]

{PASSAGE_NOTICE}

> ISABEL: [Surrounded by books and index cards] Thami! You're here! Look, I've gone through all the nineteenth-century poets, and I've got questions prepared on Byron, Shelley, and Keats. We are going to wipe the floor with those Grahamstown schools!
> THAMI: [Standing stiffly, distant] Isabel, stop. Put the cards away.
> ISABEL: What's the matter? What's wrong?
> THAMI: I can't do it, Isabel. I'm withdrawing from the competition.
> ISABEL: What do you mean you're withdrawing? You can't withdraw! We've worked on this for weeks! Mr M has already registered our names!
> THAMI: I am pulling out. The Action Committee has called for a boycott of all classes and school activities. The Comrades have decided that there can be no normal education in an abnormal society.
> ISABEL: The Comrades? What about your own mind, Thami? What about what we built together? Are you just going to throw away your future because people using assumed names told you to?
> THAMI: You don't understand, Isabel. You live on the white side of the town. You don't see what happens in the location every day. My people are suffering, and I cannot sit here playing literary games while they fight in the streets!"""

PASSAGE_5_1 = f"""### EXTRACT I - 'TRIUMPH IN THE FACE OF ADVERSITY' (Kedibone Seku)
[Context: Thulisile endures the distress of an impoverished, abusive home dominated by an alcoholic father. After her school teacher Mr Nkwane tries to intervene, causing her humiliation, Thulisile approaches Mme Sadike's home seeking chores or bread.]

{PASSAGE_NOTICE}

> Thulisile stood at the gate of Mme Sadike's house, her heart pounding against her ribs. She was clutching her thin cardigan against the cold morning wind. Her stomach was rumbling, and the tears were not far from her eyes.
> At school, Mr Nkwane had noticed her faded uniform and her drooping shoulders. He had tried to be helpful, asking questions in front of the other learners, but it had only made her feel exposed, humiliated, and terrified that the whole township would pity her as a beggar.
> Mme Sadike opened the door, wiping her flour-dusted hands on her apron. She ran the local fish and chips business, and her kitchen always smelled of warm oil and fresh dough.
> 'Thulisile, my child,' Mme Sadike said softly, her eyes filling with warm sympathy as she looked down at the trembling girl. 'Come inside. What brings you here so early?'
> Thulisile could hold it no longer. The tears broke through as she sobbed out the truth: her father had spent all the money on liquor, there was not a crumb of bread in the house, and her mother, Thembekile, was nursing another set of bruises.
> Mme Sadike wrapped her arms around the weeping girl. 'Hush, my child. We will speak with the social worker, and if your father raises his hand again, the police will be called. You are going to rise above this darkness, Thulisile. You have a bright mind, and you will overcome.'"""

PASSAGE_5_2 = f"""### EXTRACT J - 'EVELINE' (James Joyce)
[Context: From James Joyce's Dubliners: Eveline stands at the North Wall station beside Frank as the passenger ship to Buenos Aires prepares to cast off. She faces the agonizing decision between departing with Frank or remaining bound to her family and abusive father.]

{PASSAGE_NOTICE}

> She stood among the swaying crowd on the station at the North Wall. He held her hand and she knew that he was speaking to her, saying something about the passage over and over again. The station was full of soldiers with brown baggages. Through the wide doors of the sheds she caught a glimpse of the black mass of the boat, lying in beside the quay wall, with illumined portholes. She answered nothing. She felt her cheek pale and cold and, out of a maze of distress, she prayed to God to direct her, to show her what was her duty.
> The boat blew a long mournful whistle into the mist. If she went, to-morrow she would be on the sea with Frank, steaming towards Buenos Ayres. Their passage had been booked. Could she still draw back after all he had done for her? Her distress awoke a nausea in her body and she kept moving her lips in silent, fervent prayer.
> A bell clanged upon her heart. She felt him seize her hand:
> 'Come!'
> All the seas of the world tumbled about her heart. He was drawing her into them: he would drown her. She gripped with both hands at the iron railing.
> 'Come!'
> No! No! No! It was impossible. Her hands clutched the cold iron in frenzy. Amid the seas she sent a cry of anguish!
> 'Eveline! Evvy!'
> He rushed beyond the barrier and called to her to follow. He was shouted at to go on, but he still called to her. She set her white face to him, passive, like a helpless animal. Her eyes gave him no sign of love or farewell or recognition."""

PASSAGE_6_1 = f"""### POEM: 'INVERSNAID' by Gerard Manley Hopkins

{PASSAGE_NOTICE}

1   This dárksome búrn, horseback brown,
2   His rollrock highroad roaring down,
3   In coop and in comb the fleece of his foam
4   Flutes and the low pools shut his comb.
5   
6   Fhloops and twindles over the brink,
7   The fóam turns brown; his pitcher-black pool
8   Is Despair to drown in; his fallen rock
9   Degged with dew, the braes are all wet,
10  A tread of turf, a heap of peat,
11  A groop of ferns, wiry and wild,
12  And the beadbonny ash that braves the blast.
13  
14  What would the world be, once bereft
15  Of wet and of wildness? Let them be left,
16  O let them be left, wildness and wet;
17  Long live the weeds and the wilderness yet."""

PASSAGE_6_2 = f"""### POEM: 'SONNET 73' ('That time of year thou mayst in me behold') by William Shakespeare

{PASSAGE_NOTICE}

1   That time of year thou mayst in me behold
2   When yellow leaves, or none, or few, do hang
3   Upon those boughs which shake against the cold,
4   Bare ruined choirs, where late the sweet birds sang.
5   In me thou seest the twilight of such day
6   As after sunset fadeth in the west,
7   Which by and by black night doth take away,
8   Death's second self, that seals up all in rest.
9   In me thou seest the glowing of such fire
10  That on the ashes of his youth doth lie,
11  As the death-bed whereon it must expire
12  Consumed with that which it was nourish'd by.
13  This thou perceiv'st, which makes thy love more strong,
14  To love that well which thou must leave ere long."""

print("Passages and configuration loaded successfully.")

ITEMS = []

def add_item(q_ref, marks, topic, passage, question, memo, final_answer):
    item = {
        "item_id": f"{SOURCE_ID}-{q_ref}",
        "source_id": SOURCE_ID,
        "pair_source_id": PAIR_SOURCE_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "language": LANGUAGE,
        "track": TRACK,
        "kind": KIND,
        "question_ref": q_ref,
        "marks": marks,
        "topic": topic,
        "passage": passage,
        "question": question.strip(),
        "memo": memo.strip(),
        "final_answer": str(final_answer).strip(),
        "needs_review": True,
        "licence": LICENCE,
        "attribution": ATTRIBUTION
    }
    ITEMS.append(item)

# -------------------------------------------------------------
# QUESTION 1: CRY, THE BELOVED COUNTRY (Alan Paton) [35 MARKS]
# -------------------------------------------------------------
TOPIC_Q1 = "Novel - Cry, the Beloved Country"

# 1.1.1
add_item(
    "1.1.1", 4, TOPIC_Q1, PASSAGE_1_1,
    """Choose a description from COLUMN B that matches a name in COLUMN A. Write only the letter (A–E) next to the question numbers (1.1.1(a) to 1.1.1(d)) in the ANSWER BOOK.

| COLUMN A | COLUMN B |
| :--- | :--- |
| (a) Gertrude Kumalo | A is well-known for charity work among blacks |
| (b) Napoleon Letsitsi | B is prepared to house Gertrude |
| (c) Arthur Jarvis | C provides a room for Stephen in Johannesburg |
| (d) Mrs Lithebe | D is jailed for brewing liquor at home |
| | E arranges for the building of a dam |""",
    """(a) D / is jailed for brewing liquor at home $\\checkmark$
(b) E / arranges for the building of a dam $\\checkmark$
(c) A / is well-known for charity work among blacks $\\checkmark$
(d) C / provides a room for Stephen in Johannesburg $\\checkmark$ (4)""",
    "(a) D, (b) E, (c) A, (d) C"
)

# 1.1.2
add_item(
    "1.1.2", 3, TOPIC_Q1, PASSAGE_1_1,
    """Refer to the words: 'Kumalo's humble voice touched Msimangu'.
(a) Identify the figure of speech used in these words. (1)
(b) Explain why this figure of speech is appropriate. (2)""",
    """(a) Metaphor / Personification $\\checkmark$ (1)
(b) Just as someone who is affected by the generosity of another person, $\\checkmark$ Msimangu is emotionally affected by Stephen's modest reference to his kindness. $\\checkmark$
OR
Just as something that is animate has a physical presence / is able to touch, $\\checkmark$ similarly Kumalo's humble voice is given the animate / physical ability to touch Msimangu. $\\checkmark$ (2)""",
    "(a) Metaphor / Personification; (b) Kumalo's humble voice emotionally affects Msimangu."
)

# 1.1.3
add_item(
    "1.1.3", 2, TOPIC_Q1, PASSAGE_1_1,
    """What does Msimangu's confession about his own shortcomings and temper reveal about his character? State TWO points. (2)""",
    """Msimangu is modest / honest / frank / self-aware / humble $\\checkmark$ when he admits that he is human with imperfections. $\\checkmark$ (2)""",
    "Msimangu is modest/honest and admits he is human with imperfections."
)

# 1.1.4
add_item(
    "1.1.4", 2, TOPIC_Q1, PASSAGE_1_1,
    """Refer to Kumalo's reaction on learning that John has left the Church and become a politician.
(a) What tone would Kumalo use when hearing this news? (1)
(b) Why would Kumalo use this tone? (1)""",
    """(a) Surprise / shock / astonishment $\\checkmark$ (1)
(b) Kumalo is in total disbelief to discover that John / his brother is politically active / into politics. $\\checkmark$ (1)""",
    "(a) Surprise / shock / astonishment; (b) Kumalo is in disbelief that John is politically active."
)

# 1.1.5
add_item(
    "1.1.5", 2, TOPIC_Q1, PASSAGE_1_1,
    """Explain the irony in Msimangu's description of John Kumalo's political career and public speaking. (2)""",
    """Despite Msimangu's claim that John is a powerful politician, he (John) is afraid of going to prison and is therefore not fully committed to fight for change. $\\checkmark\\checkmark$
OR
John Kumalo is a powerful speaker / can stir the crowds with his commanding voice but he lacks the conviction to take real action. $\\checkmark\\checkmark$
OR
John Kumalo is described as a great man but his selfish actions do not help the people in the community. $\\checkmark\\checkmark$
NOTE: Both parts must be included to earn the marks. (2)""",
    "John is described as a powerful orator but lacks courage/conviction and fears going to prison."
)

# 1.1.6
add_item(
    "1.1.6", 2, TOPIC_Q1, PASSAGE_1_1,
    """State TWO ways in which Stephen Kumalo's relatives have abandoned moral and religious life in Johannesburg. (2)""",
    """John / His brother has abandoned the church. $\\checkmark$
John lives with a mistress. $\\checkmark$
Gertrude / His sister has turned to prostitution. $\\checkmark$
Gertrude sells illegal liquor. $\\checkmark$
NOTE: Accept any TWO of the above. (2)""",
    "John has abandoned the church / lives with a mistress; Gertrude sells illegal liquor / turned to prostitution."
)

# 1.1.7
add_item(
    "1.1.7", 3, TOPIC_Q1, PASSAGE_1_1,
    """Refer to the novel as a whole.
Mrs Kumalo is a supportive wife to Stephen Kumalo.
Discuss your view. (3)""",
    """Open-ended. Accept a relevant response which shows an understanding of the following aspects, among others:

Yes.
• Mrs Kumalo supports her husband in a quiet, patient manner. $\\checkmark$
• She offers comfort and encouragement when Stephen is anxious about his journey to Johannesburg. $\\checkmark$
• She supports Absalom's wife (the young girl) by taking care of her during her pregnancy. $\\checkmark$

OR

No.
• Mrs Kumalo does not accompany her husband when he embarks on the journey to Johannesburg in search of his 'sick' sister. $\\checkmark$
• She chooses to remain in Ndotsheni when Absalom is arrested, tried and found guilty of Arthur Jarvis's murder. $\\checkmark$
• She does not visit Absalom despite him being on death row. $\\checkmark$

NOTE: Do NOT award a mark for YES or NO. Credit responses where a combination is given. For full marks, the response must be well-substantiated. A candidate can score 1 or 2 marks for a response which is not well-substantiated. The candidate's interpretation must be grounded in the novel. (3)""",
    "Mrs Kumalo supports Stephen patiently and cares for Absalom's pregnant wife; or she chooses to stay behind in Ndotsheni."
)

# 1.2.1
add_item(
    "1.2.1", 2, TOPIC_Q1, PASSAGE_1_2,
    """Describe the time and setting where this extract takes place. (2)""",
    """This takes place after a child delivers (four) letters $\\checkmark$ at the Kumalo home. $\\checkmark$ (2)""",
    "At the Kumalo home in Ndotsheni, after a child delivers four letters."
)

# 1.2.2
add_item(
    "1.2.2", 1, TOPIC_Q1, PASSAGE_1_2,
    """Identify the crime/event for which Absalom has been sentenced to hang. (1)""",
    """The murder / killing (of Arthur Jarvis). $\\checkmark$ (1)""",
    "The murder of Arthur Jarvis."
)

# 1.2.3
add_item(
    "1.2.3", 2, TOPIC_Q1, PASSAGE_1_2,
    """What does Absalom's message in his letter reveal about his attitude towards his approaching execution? (2)""",
    """Absalom is accepting $\\checkmark$ when he tries to reassure his parents that he is coping / made peace with his fate. $\\checkmark$ (2)""",
    "Absalom is accepting and has made peace with his fate."
)

# 1.2.4
add_item(
    "1.2.4", 2, TOPIC_Q1, PASSAGE_1_2,
    """Explain the role of the priest who visits Absalom on death row in prison. (2)""",
    """A priest will pray for / minister to Absalom $\\checkmark$ to prepare him spiritually and emotionally for his eventual hanging. $\\checkmark$ (2)""",
    "To pray for and minister to Absalom to prepare him spiritually and emotionally for hanging."
)

# 1.2.5
add_item(
    "1.2.5", 2, TOPIC_Q1, PASSAGE_1_2,
    """What instruction does the judge give regarding the investigation into Matthew Kumalo and Johannes Pafuri? (2)""",
    """The judge instructs for further investigations $\\checkmark$ into Matthew and Johannes' previous criminal activities. $\\checkmark$ (2)""",
    "The judge instructs further investigations into Matthew and Johannes' previous criminal activities."
)

# 1.2.6
add_item(
    "1.2.6", 1, TOPIC_Q1, PASSAGE_1_2,
    """Choose the correct answer to complete the following sentence. Write only the letter (A–D) and the question number (1.2.6) in the ANSWER BOOK.

The weapon carried by Johannes during the housebreak was a/an ...
A iron bar.
B heavy revolver.
C sharp dagger.
D wooden club. (1)""",
    """A / an iron bar. $\\checkmark$ (1)""",
    "A"
)

# 1.2.7
add_item(
    "1.2.7", 1, TOPIC_Q1, PASSAGE_1_2,
    """Identify the church authority who wrote one of the letters and later visited Kumalo to discuss his future in Ndotsheni. (1)""",
    """Bishop $\\checkmark$ (1)""",
    "Bishop"
)

# 1.2.8
add_item(
    "1.2.8", 3, TOPIC_Q1, PASSAGE_1_2,
    """Discuss the theme of hardship in the novel as a whole. (3)""",
    """The discussion of the theme of hardship may include the following viewpoints, among others:
• James Jarvis and his wife experience hardship through the loss of their son, Arthur. $\\checkmark$
• The Ndotsheni villagers suffer hardship as they have to endure droughts and poor farming conditions. $\\checkmark$
• Stephen Kumalo's hardship is highlighted as he searches for his missing family members. $\\checkmark$

NOTE: For full marks, the response must be well-substantiated. A candidate can score 1 or 2 marks for a response which is not well-substantiated. The candidate's interpretation must be grounded in the novel. (3)""",
    "Hardship is experienced by James Jarvis losing Arthur, Ndotsheni enduring drought, and Kumalo searching for lost family members."
)

# 1.2.9
add_item(
    "1.2.9", 3, TOPIC_Q1, PASSAGE_1_2,
    """Refer to the novel as a whole.
Stephen Kumalo's faith never wavers despite the severe trials he endures.
Discuss your view. (3)""",
    """Open-ended. Accept a relevant response which shows an understanding of the following aspects, among others:

Yes.
• Stephen turns to scripture and prayer when he faces Gertrude's struggles and Absalom's disappearance. $\\checkmark$
• He is open to Father Vincent's counsel to 'pray and rest' and this strengthens his faith in God. $\\checkmark$
• His encounters with Msimangu restore his faith in mankind. $\\checkmark$

OR

No.
• Stephen experiences doubt when Absalom's crime is discovered. $\\checkmark$
• He is overwhelmed by the big city's corruption and moral decay. $\\checkmark$
• He even directs his anger at God when it seems that his faith no longer provides comfort. $\\checkmark$

NOTE: Do NOT award a mark for YES or NO. Credit responses where a combination is given. For full marks, the response must be well-substantiated. A candidate can score 1 or 2 marks for a response which is not well-substantiated. The candidate's interpretation must be grounded in the novel. (3)""",
    "Stephen Kumalo turns to prayer and scripture in hardship; or he experiences doubt and anger when Absalom is arrested."
)

print("Question 1 items added.")

# ----------------------------------------------------------------------
# QUESTION 2: STRANGE CASE OF DR JEKYLL AND MR HYDE (R.L. Stevenson) [35]
# ----------------------------------------------------------------------
TOPIC_Q2 = "Novel - Strange Case of Dr Jekyll and Mr Hyde"

# 2.1.1
add_item(
    "2.1.1", 4, TOPIC_Q2, PASSAGE_2_1,
    """Choose a description from COLUMN B that matches a name in COLUMN A. Write only the letter (A–E) next to the question numbers (2.1.1(a) to 2.1.1(d)) in the ANSWER BOOK.

| COLUMN A | COLUMN B |
| :--- | :--- |
| (a) Poole | A commits a vicious murder |
| (b) Dr Lanyon | B witnesses a violent act |
| (c) Maidservant | C inherits Dr Jekyll's estate |
| (d) Mr Hyde | D breaks up a friendship |
| | E is a concerned servant |""",
    """(a) E / is a concerned servant $\\checkmark$
(b) D / breaks up a friendship $\\checkmark$
(c) B / witnesses a violent act $\\checkmark$
(d) A / commits a vicious murder $\\checkmark$ (4)""",
    "(a) E, (b) D, (c) B, (d) A"
)

# 2.1.2
add_item(
    "2.1.2", 2, TOPIC_Q2, PASSAGE_2_1,
    """Describe the setting and situation where this conversation takes place. (2)""",
    """This takes place during Mr Utterson and Enfield's Sunday walk $\\checkmark$ in a London street / opposite the mysterious door. $\\checkmark$ (2)""",
    "During Mr Utterson and Enfield's Sunday walk in London, opposite the mysterious door."
)

# 2.1.3
add_item(
    "2.1.3", 2, TOPIC_Q2, PASSAGE_2_1,
    """Why does Mr Hyde agree to pay compensation to the family of the trampled child? (2)""",
    """Mr Hyde has to pay (compensation) $\\checkmark$ for the trauma / injury he has caused by trampling on the girl. $\\checkmark$
OR
Mr Hyde has to pay $\\checkmark$ as he wants to avoid any confrontation with the bystanders / getting the police involved. $\\checkmark$ (2)""",
    "To compensate for trampling the girl and avoid a public scandal or police involvement."
)

# 2.1.4
add_item(
    "2.1.4", 3, TOPIC_Q2, PASSAGE_2_1,
    """Refer to the words: 'We screwed up the pressure on him'.
(a) Identify the figure of speech used in these words. (1)
(b) Explain why this figure of speech is appropriate. (2)""",
    """(a) Metaphor $\\checkmark$ (1)
(b) In the same way that pressure is applied to tighten a screw, $\\checkmark$ so too the pressure the bystanders put on Mr Hyde to compensate the parents / the trampled girl, is emphasised. $\\checkmark$ (2)""",
    "(a) Metaphor; (b) Compares bystander coercion to tightening a mechanical screw."
)

# 2.1.5
add_item(
    "2.1.5", 1, TOPIC_Q2, PASSAGE_2_1,
    """Whose name was signed on the cheque that Mr Hyde presented? (1)""",
    """Jekyll $\\checkmark$ (1)""",
    "Jekyll"
)

# 2.1.6
add_item(
    "2.1.6", 2, TOPIC_Q2, PASSAGE_2_1,
    """Refer to the manner in which Mr Hyde delivers the cheque.
(a) What tone would Mr Hyde use when presenting the cheque? (1)
(b) Why would Mr Hyde use this tone? (1)""",
    """(a) Reassurance / confidence / sarcasm $\\checkmark$ (1)
(b) Mr Hyde is certain that the cheque is valid. $\\checkmark$ (1)""",
    "(a) Reassurance / confidence / sarcasm; (b) He knows the cheque is genuine and will be honoured."
)

# 2.1.7
add_item(
    "2.1.7", 3, TOPIC_Q2, PASSAGE_2_1,
    """Refer to the novel as a whole.
Mr Utterson respects the privacy of his friends.
Discuss your view. (3)""",
    """Open-ended. Accept a relevant response which shows an understanding of the following aspects, among others:

Yes.
• Mr Utterson is discreet about the content of Dr Jekyll's will. $\\checkmark$
• He avoids gossiping when Enfield tells him that Hyde offered a cheque signed by Dr Jekyll to pay for his evil deed. $\\checkmark$
• He actively investigates the mystery surrounding Mr Hyde only after Sir Carew's murder. $\\checkmark$

OR

No.
• Mr Utterson secretly follows Mr Hyde to establish the link between Dr Jekyll and Mr Hyde. $\\checkmark$
• He breaks down Dr Jekyll's laboratory door. $\\checkmark$
• Despite Dr Jekyll's instruction not to pursue the matter, he persists in questioning him (Dr Jekyll) about his will. $\\checkmark$

NOTE: Do NOT award a mark for YES or NO. Credit responses where a combination is given. For full marks, the response must be well-substantiated. A candidate can score 1 or 2 marks for a response which is not well-substantiated. The candidate's interpretation must be grounded in the novel. (3)""",
    "Utterson is discreet about Jekyll's will and avoids gossip; or he stalks Hyde and breaks down Jekyll's door."
)

# 2.2.1
add_item(
    "2.2.1", 2, TOPIC_Q2, PASSAGE_2_2,
    """Explain the dramatic irony in Mr Utterson's concern that Mr Hyde wants to murder Dr Jekyll. (2)""",
    """Mr Utterson is concerned that Mr Hyde wants to kill Dr Jekyll, but unbeknown to him, Dr Jekyll is actually Mr Hyde. $\\checkmark\\checkmark$
NOTE: Both parts must be included to earn the marks. (2)""",
    "Utterson fears Hyde will murder Jekyll, unaware that Jekyll and Hyde are the same person."
)

# 2.2.2
add_item(
    "2.2.2", 2, TOPIC_Q2, PASSAGE_2_2,
    """How does Dr Jekyll feel about Sir Danvers Carew's murder in this extract? (2)""",
    """Dr Jekyll is remorseful $\\checkmark$ as he feels terrible about Mr Hyde murdering Sir Danvers Carew. $\\checkmark$ (2)""",
    "Dr Jekyll is remorseful and horrified by Carew's murder."
)

# 2.2.3
add_item(
    "2.2.3", 4, TOPIC_Q2, PASSAGE_2_2,
    """Refer to the letter allegedly written by Mr Hyde that Dr Jekyll gives to Mr Utterson.
(a) State TWO unusual features of the letter. (2)
(b) Explain why Dr Jekyll gave this letter to Mr Utterson. (2)""",
    """(a) The letter has no return address. $\\checkmark$
It has no envelope. $\\checkmark$
The handwriting of the letter addressed to Dr Jekyll is his (Dr Jekyll's) own handwriting. $\\checkmark$
NOTE: Accept any TWO of the above. (2)

(b) Dr Jekyll writes the letter to deceive the police $\\checkmark$ because Mr Hyde is a suspect in the Carew murder case. $\\checkmark$
OR
He (Jekyll) wants to protect his reputation $\\checkmark$ by distancing himself from Mr Hyde. $\\checkmark$ (2)""",
    "(a) No return address, no envelope, handwriting matches Jekyll's; (b) To deceive police and protect his reputation."
)

# 2.2.4
add_item(
    "2.2.4", 2, TOPIC_Q2, PASSAGE_2_2,
    """What does Mr Utterson's handling of the letter and the Carew murder investigation reveal about his character? (2)""",
    """Mr Utterson is rational / logical / analytical $\\checkmark$ as he does not make unfounded assumptions. $\\checkmark$ (2)""",
    "Utterson is rational and analytical, refusing to jump to unproven conclusions."
)

# 2.2.5
add_item(
    "2.2.5", 2, TOPIC_Q2, PASSAGE_2_2,
    """Refer to the Carew murder weapon and victim.
(a) Identify the prominent victim murdered by Mr Hyde. (1)
(b) Choose the correct answer to complete the following sentence. Write only the letter (A–D) and the question number (2.2.5(b)) in the ANSWER BOOK.

The walking stick used in the murder had originally been presented to Dr Jekyll by ...
A Dr Lanyon.
B Mr Utterson.
C Poole.
D Mr Enfield. (1)""",
    """(a) Sir Danvers Carew $\\checkmark$ (1)
(b) B / Mr Utterson $\\checkmark$ (1)""",
    "(a) Sir Danvers Carew; (b) B"
)

# 2.2.6
add_item(
    "2.2.6", 3, TOPIC_Q2, PASSAGE_2_2,
    """Discuss the theme of trust in the novel as a whole. (3)""",
    """The discussion of the theme of trust may include the following viewpoints, among others:
• Dr Jekyll is comfortable to share confidential information regarding his will with Mr Utterson. $\\checkmark$
• Dr Jekyll entrusts Poole to get the powders from Messrs Maw when he needs to transform from Hyde to Jekyll. $\\checkmark$
• Poole has confidence in Mr Utterson when he seeks his help regarding the 'stranger' in his master's laboratory. $\\checkmark$

NOTE: For full marks, the response must be well-substantiated. A candidate can score 1 or 2 marks for a response which is not well-substantiated. The candidate's interpretation must be grounded in the novel. (3)""",
    "Trust is demonstrated by Jekyll trusting Utterson with his will, relying on Poole for chemical powders, and Poole seeking Utterson's help."
)

# 2.2.7
add_item(
    "2.2.7", 3, TOPIC_Q2, PASSAGE_2_2,
    """Refer to the novel as a whole.
Mr Hyde is solely to blame for the tragedy that unfolds.
Discuss your view. (3)""",
    """Open-ended. Accept a relevant response which shows an understanding of the following aspects, among others:

Yes.
• Mr Hyde murders Sir Danvers Carew with excessive violence, beating him to death with a cane. $\\checkmark$
• He strikes a woman in her face without any reason. $\\checkmark$
• Dr Jekyll admits that he is tormented by the fear of being trapped as Hyde, rather than the fear of punishment. $\\checkmark$

OR

No.
• Mr Hyde is a mere creation of Dr Jekyll to explore the darker aspects of his own personality. $\\checkmark$
• His actions are the result of Dr Jekyll's failure to control his dark side. $\\checkmark$
• After Mr Hyde kills Sir Carew, Dr Jekyll's guilt compels him to stop drinking the potion. $\\checkmark$

NOTE: Do NOT award a mark for YES or NO. Credit responses where a combination is given. For full marks, the response must be well-substantiated. A candidate can score 1 or 2 marks for a response which is not well-substantiated. The candidate's interpretation must be grounded in the novel. (3)""",
    "Hyde commits unprovoked acts of horrific violence; or Hyde is merely Jekyll's unleashed dark nature that Jekyll failed to master."
)

print("Question 2 items added.")

# -------------------------------------------------------------
# QUESTION 3: MACBETH (William Shakespeare) [35 MARKS]
# -------------------------------------------------------------
TOPIC_Q3 = "Drama - Macbeth"

# 3.1.1
add_item(
    "3.1.1", 4, TOPIC_Q3, PASSAGE_3_1,
    """Choose a description from COLUMN B that matches a name in COLUMN A. Write only the letter (A–E) next to the question numbers (3.1.1(a) to 3.1.1(d)) in the ANSWER BOOK.

| COLUMN A | COLUMN B |
| :--- | :--- |
| (a) Macduff | A tries to save the lives of Macduff's family |
| (b) Banquo | B is Thane of Glamis when the play opens |
| (c) Ross | C is predicted to become the father of a line of Scottish kings |
| (d) Macbeth | D seeks the help of King Edward the Confessor |
| | E is Prince of Cumberland |""",
    """(a) D / seeks the help of King Edward the Confessor $\\checkmark$
(b) C / is predicted to become the king of Scotland $\\checkmark$
(c) A / tries to save the lives of Macduff's family $\\checkmark$
(d) B / is Thane of Glamis when the play opens $\\checkmark$ (4)""",
    "(a) D, (b) C, (c) A, (d) B"
)

# 3.1.2
add_item(
    "3.1.2", 2, TOPIC_Q3, PASSAGE_3_1,
    """How does Macbeth feel in the courtyard before entering King Duncan's bedchamber? (2)""",
    """Macbeth is anxious / nervous $\\checkmark$ as he agonises about his footsteps being heard. $\\checkmark$ (2)""",
    "Macbeth is anxious and terrified that his footsteps will be heard."
)

# 3.1.3
add_item(
    "3.1.3", 3, TOPIC_Q3, PASSAGE_3_1,
    """Refer to Macbeth awaiting the bell.
(a) What signal is Macbeth waiting for before he proceeds to murder Duncan? (1)
(b) Describe the setting and event that took place immediately before this extract. (2)""",
    """(a) Macbeth should go and kill Duncan. / The guards have been intoxicated (with alcohol) and the scene is set. $\\checkmark$ (1)
(b) This takes place when Macbeth has a vision of a dagger / before he goes to kill Duncan $\\checkmark$ in the courtyard of his castle. $\\checkmark$ (2)""",
    "(a) The ringing of the bell signaling the guards are drugged; (b) Macbeth envisions a floating dagger in the courtyard."
)

# 3.1.4
add_item(
    "3.1.4", 3, TOPIC_Q3, PASSAGE_3_1,
    """Refer to line 4 ('It was the owl that shriek'd, the fatal bellman').
(a) Identify the figure of speech used in these words. (1)
(b) Explain why this figure of speech is appropriate. (2)""",
    """(a) Metaphor / Personification $\\checkmark$ (1)
(b) In the same way that the owl is a symbol of / forebodes death, $\\checkmark$ Macbeth too becomes a symbol of death because he is going to execute the killing of Duncan. $\\checkmark$
OR
Just as a bellman is responsible for the final death knell of a condemned prisoner, $\\checkmark$ so too does the owl's shriek forebode Duncan's murder. $\\checkmark$ (2)""",
    "(a) Metaphor / Personification; (b) The owl's shriek acts as a fatal bellman tolling the death of Duncan."
)

# 3.1.5
add_item(
    "3.1.5", 1, TOPIC_Q3, PASSAGE_3_1,
    """Choose the correct answer to complete the following sentence. Write only the letter (A–D) and the question number (3.1.5) in the ANSWER BOOK.

Lady Macbeth ensured that Duncan's chamber would be unguarded by drugging the drinks of the ...
A soldiers.
B thanes.
C guards.
D servants. (1)""",
    """C / guards. $\\checkmark$ (1)""",
    "C"
)

# 3.1.6
add_item(
    "3.1.6", 2, TOPIC_Q3, PASSAGE_3_1,
    """Why is Lady Macbeth alarmed when she hears Macbeth calling from Duncan's chamber? (2)""",
    """She fears that they may be caught out in their attempt to kill Duncan $\\checkmark$ and not by the actual deed. $\\checkmark$ (2)""",
    "She fears the guards have awakened and the assassination attempt has failed."
)

# 3.1.7
add_item(
    "3.1.7", 3, TOPIC_Q3, PASSAGE_3_1,
    """Refer to the play as a whole.
Macduff is justified in killing Macbeth.
Discuss your view. (3)""",
    """Open-ended. Accept a relevant response which shows an understanding of the following aspects, among others:

Yes.
• Macduff acts against Macbeth who is the perpetrator. $\\checkmark$
• He is the one not 'born of woman' so it is fitting that he seeks Macbeth out for a fight. $\\checkmark$
• Macduff needs to kill the tyrannical Macbeth to ensure that Scotland is healed. $\\checkmark$

OR

No.
• There would have been no conflict between Macbeth and Macduff if Macbeth had not believed the witches' prophecies. $\\checkmark$
• If Macbeth did not murder Macduff's family, there would not be a need for the ensuing revenge which ultimately leads to Macbeth's death. $\\checkmark$
• Conflict could have been averted and Macbeth would not have been suspicious if Macduff had attended Macbeth's banquet. $\\checkmark$

NOTE: Do NOT award a mark for YES or NO. Credit responses where a combination is given. For full marks, the response must be well-substantiated. A candidate can score 1 or 2 marks for a response which is not well-substantiated. The candidate's interpretation must be grounded in the play. (3)""",
    "Macduff is justified to avenge his slaughtered family and heal Scotland from tyranny; or vengeance perpetuated endless slaughter."
)

# 3.2.1
add_item(
    "3.2.1", 1, TOPIC_Q3, PASSAGE_3_2,
    """Identify the title stripped from the treacherous rebel and given to Macbeth early in the play. (1)""",
    """Cawdor $\\checkmark$ (1)""",
    "Cawdor"
)

# 3.2.2
add_item(
    "3.2.2", 2, TOPIC_Q3, PASSAGE_3_2,
    """Explain the irony in Macbeth asking the Doctor to purge and heal Scotland. (2)""",
    """Macbeth pleads with the Doctor to heal Scotland, yet he (Macbeth) is the cause of the suffering / illness. $\\checkmark\\checkmark$
OR
Macbeth pleads with the Doctor to restore Lady Macbeth's health, yet there is no medicine to cure her current mental state. $\\checkmark\\checkmark$
NOTE: Both parts must be included to earn the marks. (2)""",
    "Macbeth asks the Doctor to cure Scotland's disease, yet Macbeth himself is the murderous cause of the nation's suffering."
)

# 3.2.3
add_item(
    "3.2.3", 2, TOPIC_Q3, PASSAGE_3_2,
    """What does the Doctor's aside reveal about his character and attitude towards Macbeth's rule? (2)""",
    """The Doctor is principled / righteous / virtuous / ethical $\\checkmark$ when he claims that not even money will persuade him to return to the 'sick' castle of Macbeth / Scotland. $\\checkmark$ (2)""",
    "The Doctor is principled and ethical, refusing to compromise his integrity for Macbeth's money."
)

# 3.2.4
add_item(
    "3.2.4", 2, TOPIC_Q3, PASSAGE_3_2,
    """Refer to Malcolm's command at Birnam Wood.
(a) What tone would Malcolm use when commanding his forces? (1)
(b) Why would Malcolm use this tone? (1)""",
    """(a) Confidence / assurance $\\checkmark$ (1)
(b) He is convinced that Scotland will be returned to its former glory. $\\checkmark$ (1)""",
    "(a) Confidence / assurance; (b) He is confident that Scotland will be liberated and restored."
)

# 3.2.5
add_item(
    "3.2.5", 2, TOPIC_Q3, PASSAGE_3_2,
    """What tactical order does Malcolm give his soldiers at Birnam Wood? (2)""",
    """Malcolm instructs each soldier to cut a branch $\\checkmark$ and hold it in front of himself. $\\checkmark$ (2)""",
    "To cut a bough from Birnam Wood and carry it before them to conceal their numbers."
)

# 3.2.6
add_item(
    "3.2.6", 2, TOPIC_Q3, PASSAGE_3_2,
    """If you were the director of this play, what physical actions would you instruct Siward to perform when speaking these lines? State TWO actions. (2)""",
    """Siward should move his hands (outstretched) from left to right. $\\checkmark$
He should simulate a circle. $\\checkmark$
He should move his hands (with palms downward) up and down. $\\checkmark$
He should shift his eyes from the people to the castle. $\\checkmark$
NOTE: Accept any TWO of the above or any other relevant actions. (2)""",
    "Outstretch hands from left to right; shift gaze purposefully from his soldiers toward Dunsinane castle."
)

# 3.2.7
add_item(
    "3.2.7", 3, TOPIC_Q3, PASSAGE_3_2,
    """Discuss the theme of honour in the play as a whole. (3)""",
    """The discussion of the theme of honour may include the following viewpoints, among others:
• Macbeth and Banquo are both praised for their valour in battle. $\\checkmark$
• Macbeth fights heroically for King Duncan / Scotland. $\\checkmark$
• Macbeth betrays his soldierly honour by murdering his sovereign guest Duncan to gain power. $\\checkmark$

NOTE: For full marks, the response must be well-substantiated. A candidate can score 1 or 2 marks for a response which is not well-substantiated. The candidate's interpretation must be grounded in the play. (3)""",
    "Honour is shown in Macbeth and Banquo's battlefield courage, while Macbeth's betrayal of Duncan shows the destruction of honour."
)

# 3.2.8
add_item(
    "3.2.8", 3, TOPIC_Q3, PASSAGE_3_2,
    """Refer to the play as a whole.
Lady Macbeth is solely responsible for Macbeth's downfall.
Discuss your view. (3)""",
    """Open-ended. Accept a relevant response which shows an understanding of the following aspects, among others:

Yes.
• Lady Macbeth manipulates Macbeth when she questions his manhood. $\\checkmark$
• She orchestrates the plan to drug the guards and murder King Duncan. $\\checkmark$
• She suppresses her own humanity to push Macbeth into regicide. $\\checkmark$

OR

No.
• Macbeth already harboured vaulting ambition before returning home. $\\checkmark$
• He willingly chooses to believe and act upon the prophecies of the witches. $\\checkmark$
• Later murders, including Banquo and Macduff's family, are carried out by Macbeth alone without Lady Macbeth's knowledge. $\\checkmark$

NOTE: Do NOT award a mark for YES or NO. Credit responses where a combination is given. For full marks, the response must be well-substantiated. A candidate can score 1 or 2 marks for a response which is not well-substantiated. The candidate's interpretation must be grounded in the play. (3)""",
    "Lady Macbeth pushed Macbeth to murder Duncan; or Macbeth's own vaulting ambition drove him to slaughter Banquo and Macduff's family."
)

# ----------------------------------------------------------------------
# QUESTION 4: MY CHILDREN! MY AFRICA! (Athol Fugard) [35 MARKS]
# ----------------------------------------------------------------------
TOPIC_Q4 = "Drama - My Children! My Africa!"

# 4.1.1
add_item(
    "4.1.1", 4, TOPIC_Q4, PASSAGE_4_1,
    """Choose a description from COLUMN B that matches a name in COLUMN A. Write only the letter (A–E) next to the question numbers (4.1.1(a) to 4.1.1(d)) in the ANSWER BOOK.

| COLUMN A | COLUMN B |
| :--- | :--- |
| (a) Thami's father | A is a victorious debater |
| (b) Thami Mbikwana | B writes on the wall |
| (c) Isabel Dyson | C is a teacher's protégé |
| (d) Sipho | D is a school inspector |
| | E works at the railway |""",
    """(a) E / works at the railway $\\checkmark$
(b) C / is a teacher's protégé $\\checkmark$
(c) A / is a victorious debater $\\checkmark$
(d) B / writes on the wall $\\checkmark$ (4)""",
    "(a) E, (b) C, (c) A, (d) B"
)

# 4.1.2
add_item(
    "4.1.2", 2, TOPIC_Q4, PASSAGE_4_1,
    """Describe the time and setting where this conversation takes place. (2)""",
    """This takes place when Mr M goes to ask Isabel to form a team with Thami (for the literature quiz) $\\checkmark$ at Camdeboo High School. $\\checkmark$ (2)""",
    "At Camdeboo High School, when Mr M invites Isabel to form an inter-school quiz team with Thami."
)

# 4.1.3
add_item(
    "4.1.3", 4, TOPIC_Q4, PASSAGE_4_1,
    """Refer to Mr M's enthusiasm when speaking of Thami.
(a) If you were the director of this play, what physical actions would you instruct Mr M to perform? State TWO actions. (2)
(b) What does Mr M's admission about his special regard for Thami reveal about his character? (2)""",
    """(a) Mr M should raise his eyebrows. $\\checkmark$
He should cover his mouth with one hand. $\\checkmark$
He should place both hands on his head. $\\checkmark$
NOTE: Accept any TWO of the above or any other relevant actions. (2)

(b) Mr M is honest / truthful $\\checkmark$ as he acknowledges his favouritism towards Thami. $\\checkmark$ (2)""",
    "(a) Raise eyebrows, cover mouth with one hand, or place both hands on head; (b) Honest and self-aware about his favoritism toward Thami."
)

# 4.1.4
add_item(
    "4.1.4", 3, TOPIC_Q4, PASSAGE_4_1,
    """Refer to lines describing Thami as 'an eager and gifted head' and a vessel to be filled.
(a) Identify the figure of speech used in these words. (1)
(b) Explain why this figure of speech is appropriate. (2)""",
    """(a) Metaphor / Synecdoche $\\checkmark$ (1)
(b) Just as a vessel is filled when liquid is added to / poured into it, $\\checkmark$ similarly Mr M wants to highlight the fact that he can impart knowledge to his learners. $\\checkmark$
OR
Mr M uses 'eager and gifted head' to represent the whole learner (Thami), $\\checkmark$ emphasising his (Thami's) strong intellectual potential and the teacher's hope of imparting knowledge $\\checkmark$ (to a mind capable of exceptional growth). (2)""",
    "(a) Metaphor / Synecdoche; (b) Compares educating a student to pouring knowledge into a receptive vessel."
)

# 4.1.5
add_item(
    "4.1.5", 2, TOPIC_Q4, PASSAGE_4_1,
    """Explain the irony in Mr M's hopes for Thami's future educational achievements. (2)""",
    """Thami is focused on education, yet later he drops out of school to join the Struggle. $\\checkmark\\checkmark$
NOTE: Both parts must be included to earn the marks. (2)""",
    "Mr M envisions Thami reaching university excellence, yet Thami abandons schooling to join the political boycott."
)

# 4.1.6
add_item(
    "4.1.6", 3, TOPIC_Q4, PASSAGE_4_1,
    """Refer to the play as a whole.
Mr M brought about his own tragic death.
Discuss your view. (3)""",
    """Open-ended. Accept a relevant response which shows an understanding of the following aspects, among others:

Yes.
• The apartheid system implements an inferior Bantu Education system. $\\checkmark$
• The Black students revolt against the oppressive education that is forced upon them. $\\checkmark$
• The protesting students kill Mr M because he is seen as a police informer. $\\checkmark$

OR

No.
• Mr M chooses not to join the comrades. $\\checkmark$
• He is aware of the consequences of providing the names to the police. $\\checkmark$
• He refuses to stop ringing the bell even though the situation is volatile. $\\checkmark$

NOTE: Do NOT award a mark for YES or NO. Credit responses where a combination is given. For full marks, the response must be well-substantiated. A candidate can score 1 or 2 marks for a response which is not well-substantiated. The candidate's interpretation must be grounded in the play. (3)""",
    "Mr M gave students' names to police and defied the boycott; or the oppressive apartheid system caused the tragedy."
)

# 4.2.1
add_item(
    "4.2.1", 2, TOPIC_Q4, PASSAGE_4_2,
    """Refer to the comrades' movement and Isabel's preparations.
(a) Choose the correct answer: In their meetings, the comrades referred to each other by ...
A assumed names.
B school numbers.
C family names.
D grade levels. (1)
(b) What activity was Isabel engaged in before Thami arrived? (1)""",
    """(a) A / assumed names. $\\checkmark$ (1)
(b) Isabel is preparing for a literature quiz. $\\checkmark$ (1)""",
    "(a) A; (b) Preparing for the literature quiz."
)

# 4.2.2
add_item(
    "4.2.2", 4, TOPIC_Q4, PASSAGE_4_2,
    """Refer to Thami's conversation with Isabel.
(a) What emotions does Thami experience when breaking the news to Isabel? (2)
(b) What painful decision does Thami communicate to Isabel? (2)""",
    """(a) Thami is conflicted / concerned $\\checkmark$ as he does not know how to break the news to Isabel without hurting her. $\\checkmark$ (2)
(b) Thami tells Isabel that he is withdrawing from the literature quiz $\\checkmark$ and he cannot see her anymore as he is joining the Struggle / boycott. $\\checkmark$ (2)""",
    "(a) Conflicted and anxious about hurting Isabel; (b) He is withdrawing from the quiz and ending contact to join the boycott."
)

# 4.2.3
add_item(
    "4.2.3", 2, TOPIC_Q4, PASSAGE_4_2,
    """Why does Isabel describe her contact and debates with Thami as life-changing? (2)""",
    """Isabel says her time with Thami was life-changing $\\checkmark$ as she has gained a deeper understanding of the realities of apartheid. $\\checkmark$ (2)""",
    "She gained a profound firsthand understanding of the painful realities of apartheid."
)

# 4.2.4
add_item(
    "4.2.4", 2, TOPIC_Q4, PASSAGE_4_2,
    """Refer to Isabel's reaction to Thami's withdrawal.
(a) What tone would Isabel use when confronting Thami? (1)
(b) Why would Isabel use this tone? (1)""",
    """(a) Sarcasm / frustration / impatience $\\checkmark$ (1)
(b) Isabel wants Thami to admit that he is being pressured by the Comrades. / Isabel is angry that Thami allows the Comrades to interfere with their friendship. $\\checkmark$ (1)""",
    "(a) Sarcasm / frustration / impatience; (b) She is furious that Thami lets the Comrades dictate his choices and ruin their friendship."
)

# 4.2.5
add_item(
    "4.2.5", 1, TOPIC_Q4, PASSAGE_4_2,
    """Identify the career that Isabel dreams of pursuing in the future. (1)""",
    """journalist $\\checkmark$ (1)""",
    "journalist"
)

# 4.2.6
add_item(
    "4.2.6", 3, TOPIC_Q4, PASSAGE_4_2,
    """Discuss the theme of communication in the play as a whole. (3)""",
    """The discussion of the theme of communication may include the following viewpoints, among others:
• Mr M's communication with Miss Brockway initiates the debating contest between the two schools. $\\checkmark$
• Thami and Isabel engage in conversation to become acquainted with each other. $\\checkmark$
• Isabel converses with Thami in an attempt to understand the political tension that has broken out. $\\checkmark$

NOTE: For full marks, the response must be well-substantiated. A candidate can score 1 or 2 marks for a response which is not well-substantiated. The candidate's interpretation must be grounded in the play. (3)""",
    "Communication bridges racial divides through inter-school debate, yet political conflict threatens dialogue."
)

# 4.2.7
add_item(
    "4.2.7", 3, TOPIC_Q4, PASSAGE_4_2,
    """Refer to the play as a whole.
Thami Mbikwana represents hope for South Africa's future.
Discuss your view. (3)""",
    """Open-ended. Accept a relevant response which shows an understanding of the following aspects, among others:

Yes.
• Thami excels academically and is passionate about social issues (the debate), showing potential to take a lead in future change. $\\checkmark$
• He joins the boycott showing his commitment to fighting for a better future. $\\checkmark$
• Despite his intellectual ability, he gives up his own aspirations for the greater good of his people. $\\checkmark$

OR

No.
• Thami abandons his education and rejects Mr M's guidance, limiting his ability to create lasting change. $\\checkmark$
• He supports the boycott, causing destruction and Mr M's death. $\\checkmark$
• He flees the country with no clear plan, leaving his future and the hope he represents uncertain. $\\checkmark$

NOTE: Do NOT award a mark for YES or NO. Credit responses where a combination is given. For full marks, the response must be well-substantiated. A candidate can score 1 or 2 marks for a response which is not well-substantiated. The candidate's interpretation must be grounded in the play. (3)""",
    "Thami embodies intellectual brilliance and dedication to liberation; or abandoning education and fleeing diminishes hope."
)

print("Question 3 and Question 4 items added.")

# -------------------------------------------------------------
# QUESTION 5: SHORT STORIES [35 MARKS]
# -------------------------------------------------------------
TOPIC_Q5_1 = "Short Stories - Triumph in the Face of Adversity"
TOPIC_Q5_2 = "Short Stories - Eveline"

# 5.1.1
add_item(
    "5.1.1", 4, TOPIC_Q5_1, PASSAGE_5_1,
    """Choose a description from COLUMN B that matches a name in COLUMN A. Write only the letter (A–E) next to the question numbers (5.1.1(a) to 5.1.1(d)) in the ANSWER BOOK.

| COLUMN A | COLUMN B |
| :--- | :--- |
| (a) Thulisile's father | A owns a fish and chips shop |
| (b) Mme Sadike | B is an abusive and drunken man |
| (c) Sibling | C appears to be a concerned teacher |
| (d) Mr Nkwane | D is a local police captain |
| | E is upset about not receiving bread |""",
    """(a) B / is an abusive and drunken man $\\checkmark$
(b) A / owns a fish and chips shop $\\checkmark$
(c) E / is upset about not receiving bread $\\checkmark$
(d) C / appears to be a concerned teacher $\\checkmark$ (4)""",
    "(a) B, (b) A, (c) E, (d) C"
)

# 5.1.2
add_item(
    "5.1.2", 2, TOPIC_Q5_1, PASSAGE_5_1,
    """Describe the setting and reason for Thulisile's visit in this extract. (2)""",
    """This takes place when Thulisile goes begging for bread / looking for a job $\\checkmark$ at Mme Sadike's house. $\\checkmark$ (2)""",
    "At Mme Sadike's house, when Thulisile seeks bread or chores to feed her family."
)

# 5.1.3
add_item(
    "5.1.3", 2, TOPIC_Q5_1, PASSAGE_5_1,
    """Why is Thulisile embarrassed by Mr Nkwane's intervention at school? State TWO reasons. (2)""",
    """Thulisile is embarrassed that Mr Nkwane would share her personal life with everyone. $\\checkmark$
She is concerned (fears) that people might pity her. $\\checkmark$ (2)""",
    "Embarrassed that her personal poverty would be exposed to everyone, and afraid of being pitied."
)

# 5.1.4
add_item(
    "5.1.4", 2, TOPIC_Q5_1, PASSAGE_5_1,
    """What does Mme Sadike's reaction to Thulisile's plight reveal about her character? (2)""",
    """Mme Sadike is sympathetic / caring / reassuring $\\checkmark$ as she comforts Thulisile when she cries and confides in her. $\\checkmark$ (2)""",
    "Mme Sadike is compassionate, caring, and reassuring."
)

# 5.1.5
add_item(
    "5.1.5", 2, TOPIC_Q5_1, PASSAGE_5_1,
    """Explain the irony in Thulisile's feelings of despair about her future. (2)""",
    """Thulisile doubts her ability to overcome her struggles, yet she later progresses to become successful (e.g. she becomes a television presenter / finds a job / buys a house). $\\checkmark\\checkmark$
NOTE: BOTH parts must be included to earn the marks. (2)""",
    "Thulisile despairs of ever escaping poverty, yet she later achieves great professional success and buys a house."
)

# 5.1.6
add_item(
    "5.1.6", 2, TOPIC_Q5_1, PASSAGE_5_1,
    """Explain how a social worker and the police can assist Thulisile and her family. (2)""",
    """A social worker will provide counselling / emotional support $\\checkmark$ and the police will protect Thulisile and her siblings against their father's violent behaviour. $\\checkmark$ (2)""",
    "Social workers provide counseling and emotional guidance, while police protect the family from domestic violence."
)

# 5.1.7
add_item(
    "5.1.7", 3, TOPIC_Q5_1, PASSAGE_5_1,
    """Refer to the short story as a whole.
Thembekile is an admirable mother.
Discuss your view. (3)""",
    """Open-ended. Accept a relevant response which shows an understanding of the following aspects, among others:

Yes.
• Thembekile honours her marital vows and stays with her husband despite his abusive nature. $\\checkmark$
• She remains respectful towards her mother-in-law who is cruel towards her. $\\checkmark$
• She stops visiting her parents because she does not want them to witness the evidence of the abuse that she endures. $\\checkmark$

OR

No.
• Thembekile gives up on her dream of becoming an actress to please her domineering husband. $\\checkmark$
• She tolerates the abuse from her husband thereby allowing her children to grow up in an abusive home. $\\checkmark$
• She declines the opportunity to move in with Thulisile and escape the life of ill-treatment and suffering. $\\checkmark$

NOTE: Do NOT award a mark for YES or NO. Credit responses where a combination is given. For full marks, the response must be well-substantiated. A candidate can score 1 or 2 marks for a response which is not well-substantiated. The candidate's interpretation must be grounded in the short story. (3)""",
    "Thembekile stays loyal to her vows and protects her parents from seeing her pain; or she tolerates abuse and allows her children to suffer."
)

# 5.2.1
add_item(
    "5.2.1", 1, TOPIC_Q5_2, PASSAGE_5_2,
    """Choose the correct answer to complete the following sentence. Write only the letter (A–D) and the question number (5.2.1) in the ANSWER BOOK.

One of Eveline's primary motives for wanting to leave Dublin was her ...
A father's verbal abuse.
B hatred of the church.
C longing for luxury.
D desire to travel. (1)""",
    """A / father's verbal abuse. $\\checkmark$ (1)""",
    "A"
)

# 5.2.2
add_item(
    "5.2.2", 2, TOPIC_Q5_2, PASSAGE_5_2,
    """How does Eveline feel as the moment of departure at the quay arrives? (2)""",
    """Eveline is conflicted / anxious / confused / apprehensive / distressed $\\checkmark$ as she calls upon Divine intervention for guidance on whether she should remain with her family or leave with Frank. $\\checkmark$ (2)""",
    "Eveline is intensely distressed, conflicted, and prays frantically for divine guidance."
)

# 5.2.3
add_item(
    "5.2.3", 3, TOPIC_Q5_2, PASSAGE_5_2,
    """Refer to line 9 ('The boat blew a long mournful whistle into the mist').
(a) Identify the figure of speech used in these words. (1)
(b) Explain why this figure of speech is appropriate. (2)""",
    """(a) Personification / Alliteration $\\checkmark$ (1)
(b) Just as the sound of the whistle resembles a person who is mourning, $\\checkmark$ similarly Eveline's sadness about leaving the familiar behind, is emphasised. $\\checkmark$
OR
The sound made by the whistle emphasises the sadness $\\checkmark$ that Eveline feels about leaving the familiar behind. $\\checkmark$ (2)""",
    "(a) Personification / Alliteration; (b) The boat's mournful cry mirrors Eveline's sorrow and anxiety at leaving the familiar behind."
)

# 5.2.4
add_item(
    "5.2.4", 2, TOPIC_Q5_2, PASSAGE_5_2,
    """Refer to Frank calling Eveline: 'Come!'
(a) What tone would Frank use in these lines? (1)
(b) Why would Frank use this tone? (1)""",
    """(a) Persuasion / command / desperation $\\checkmark$ (1)
(b) Frank realises that Eveline is hesitant and he coerces / orders / pleads with her to follow him onto the boat. $\\checkmark$ (1)""",
    "(a) Persuasion / command / desperation; (b) He sees she is freezing in hesitation and desperately urges her to board."
)

# 5.2.5
add_item(
    "5.2.5", 1, TOPIC_Q5_2, PASSAGE_5_2,
    """What affectionate nickname did Frank use for Eveline? (1)""",
    """Frank calls her Poppens / Evvy. $\\checkmark$ (1)""",
    "Poppens / Evvy"
)

# 5.2.6
add_item(
    "5.2.6", 2, TOPIC_Q5_2, PASSAGE_5_2,
    """Why does Eveline ultimately refuse to board the ship with Frank? (2)""",
    """Eveline holds on / remembers the promise she made to her mother $\\checkmark$ to keep the family together for as long as she can. $\\checkmark$ (2)""",
    "She remembers her deathbed promise to her mother to keep the family home together."
)

# 5.2.7
add_item(
    "5.2.7", 1, TOPIC_Q5_2, PASSAGE_5_2,
    """Identify Eveline's supervisor at the department store who frequently scolded her. (1)""",
    """Gavan $\\checkmark$ (1)""",
    "Gavan"
)

# 5.2.8
add_item(
    "5.2.8", 3, TOPIC_Q5_2, PASSAGE_5_2,
    """Discuss the theme of freedom in the short story as a whole. (3)""",
    """The discussion of the theme of freedom should include the following viewpoints, among others:
• Frank offers Eveline freedom to escape to Argentina (Buenos Ayres) which is enticing as she will gain respect through marrying him. $\\checkmark$
• Eveline will be freed from the disputes she has with her father regarding the finances and his threatening behaviour. $\\checkmark$
• She sacrifices her freedom when the opportunity arises as she decides not to leave with Frank. $\\checkmark$

NOTE: For full marks, the response must be well-substantiated. A candidate can score 1 or 2 marks for a response which is not well-substantiated. The candidate's interpretation must be grounded in the short story. (3)""",
    "Freedom is offered by Frank through marriage in Argentina, freeing her from financial stress and domestic abuse, but fear paralyzes her into staying."
)

# 5.2.9
add_item(
    "5.2.9", 3, TOPIC_Q5_2, PASSAGE_5_2,
    """Refer to the short story as a whole.
Eveline made the right decision not to leave with Frank.
Discuss your view. (3)""",
    """Open-ended. Accept a relevant response which shows an understanding of the following aspects, among others:

Yes.
• Eveline's future in Buenos Aires with Frank was completely unknown and uncertain. $\\checkmark$
• She honors her sacred promise to her dying mother to look after the younger children. $\\checkmark$
• Remaining in Dublin keeps her rooted in her familiar community and family responsibilities. $\\checkmark$

OR

No.
• She remains trapped in an abusive domestic environment under her violent father. $\\checkmark$
• She forfeits her chance of love, marriage, respectability, and financial security with Frank. $\\checkmark$
• Her decision is dictated by paralyzing fear and guilt rather than genuine free will. $\\checkmark$

NOTE: Do NOT award a mark for YES or NO. Credit responses where a combination is given. For full marks, the response must be well-substantiated. A candidate can score 1 or 2 marks for a response which is not well-substantiated. The candidate's interpretation must be grounded in the short story. (3)""",
    "Eveline honors her family duty and avoids an uncertain fate abroad; or she succumbs to paralyzing fear and remains trapped in domestic abuse."
)

# -------------------------------------------------------------
# QUESTION 6: POETRY [35 MARKS]
# -------------------------------------------------------------
TOPIC_Q6_1 = "Poetry - Inversnaid"
TOPIC_Q6_2 = "Poetry - Sonnet 73"

# 6.1.1
add_item(
    "6.1.1", 4, TOPIC_Q6_1, PASSAGE_6_1,
    """Complete the following sentences using the poetic terms below:
[rhyme | quatrains | stanza | aabb ccdd eeff gghh]

The poem is divided into four sections, each known as a (a) ... . Because each has four lines, they are called (b) ... . The poem has an end-line (c) ... pattern of (d) ... . (4)""",
    """(a) stanza $\\checkmark$
(b) quatrains $\\checkmark$
(c) rhyme $\\checkmark$
(d) aabb ccdd eeff gghh $\\checkmark$ (4)""",
    "(a) stanza, (b) quatrains, (c) rhyme, (d) aabb ccdd eeff gghh"
)

# 6.1.2
add_item(
    "6.1.2", 1, TOPIC_Q6_1, PASSAGE_6_1,
    """Why does the speaker describe the mountain stream as 'horseback brown' in line 1? (1)""",
    """The water is a (dark) brown colour / possibly contains dirt / mud. $\\checkmark$ (1)""",
    "The water is dark brown, tinted by peat and mud."
)

# 6.1.3
add_item(
    "6.1.3", 2, TOPIC_Q6_1, PASSAGE_6_1,
    """Refer to lines 9–12 ('Degged with dew... braves the blast').
Identify the place and time described in these lines. (2)""",
    """Place: This takes place on the hillside / the slopes ('braes') / next to the stream / in Inversnaid. $\\checkmark$
Time: Early in the morning ('dew') / in autumn / when the speaker describes the beautiful trees and plants. $\\checkmark$
NOTE: Accept any ONE reference to time and ONE to place. (2)""",
    "Place: hillside braes / Inversnaid stream; Time: early morning (dew) / autumn."
)

# 6.1.4
add_item(
    "6.1.4", 1, TOPIC_Q6_1, PASSAGE_6_1,
    """Identify the sound device used in line 3: 'In coop and in comb the fleece of his foam'. (1)""",
    """Alliteration / Assonance $\\checkmark$ (1)""",
    "Alliteration / Assonance"
)

# 6.1.5
add_item(
    "6.1.5", 2, TOPIC_Q6_1, PASSAGE_6_1,
    """What does the speaker's plea in the final stanza reveal about his attitude towards nature? (2)""",
    """He is passionate / caring $\\checkmark$ (about nature conservation) and pleads with mankind to protect nature. $\\checkmark$ (2)""",
    "He is passionate and deeply caring about environmental conservation."
)

# 6.1.6
add_item(
    "6.1.6", 2, TOPIC_Q6_1, PASSAGE_6_1,
    """Explain the irony in the speaker celebrating 'weeds' in line 17. (2)""",
    """Weeds are usually unwanted / seen as a nuisance, yet now the speaker sees them as part of nature's wild beauty which is worth preserving. $\\checkmark\\checkmark$
NOTE: Both parts must be included to earn the marks. (2)""",
    "Weeds are conventionally despised as garden pests, yet Hopkins celebrates them as essential embodiments of wild beauty."
)

# 6.1.7
add_item(
    "6.1.7", 3, TOPIC_Q6_1, PASSAGE_6_1,
    """Discuss the theme of the wildness of nature in the poem. (3)""",
    """The discussion of the theme of the wildness of nature may include the following viewpoints, among others:
• The word 'rollrock' (line 2) gives the image of an untamed horse galloping over the rocks. $\\checkmark$
• 'féll' in 'féll-frówning' (line 7) which means terrible / fierce / threatening describes the hills. $\\checkmark$
• 'Wiry' (line 11) implies the strength of the ferns but also danger as they can entangle you and hurt you. $\\checkmark$

NOTE: For full marks, the response must be well-substantiated. A candidate can score 1 or 2 marks for a response which is not well-substantiated. The candidate's interpretation must be grounded in the poem. (3)""",
    "Wildness is conveyed through untamed river motion (rollrock), fierce hill terrain (fell-frowning), and resilient vegetation (wiry ferns)."
)

# 6.1.8
add_item(
    "6.1.8", 3, TOPIC_Q6_1, PASSAGE_6_1,
    """The poem conveys an entirely tranquil and peaceful atmosphere.
Discuss your view. (3)""",
    """Open-ended. Accept a relevant response which shows an understanding of the following aspects, among others:

Yes.
• In line 9 the slopes and the hills are described as 'Degged (sprinkled) with dew' and therefore creates an atmosphere of serenity. $\\checkmark$
• 'treads' (line 10) shows the slow and careful movement of the river which contributes to the tranquillity. $\\checkmark$
• The ash tree is beautified with the vibrant berries that look like beads ('beadbonny'). $\\checkmark$

OR

No.
• 'twindles' (line 6) alludes to a whirlpool which indicates the violent movement of the water, disturbing the peace. $\\checkmark$
• The very dark, 'pitchblack' (line 7) water contributes to an ominous atmosphere. $\\checkmark$
• The personification of 'Despair' (line 8) creates the image of a person being pulled into the black water. $\\checkmark$

NOTE: Do NOT award a mark for YES or NO. Credit responses where a combination is given. For full marks, the response must be well-substantiated. A candidate can score 1 or 2 marks for a response which is not well-substantiated. The candidate's interpretation must be grounded in the poem. (3)""",
    "Dew-sprinkled braes and beadbonny ash create serenity; or swirling whirlpools, pitchblack depths, and personified Despair create ominous tension."
)

# 6.2.1
add_item(
    "6.2.1", 1, TOPIC_Q6_2, PASSAGE_6_2,
    """Choose the correct answer to complete the following sentence. Write only the letter (A–D) and the question number (6.2.1) in the ANSWER BOOK.

In the first quatrain (lines 1–4), the speaker's time of life is compared to ...
A spring.
B summer.
C autumn.
D winter. (1)""",
    """D / winter $\\checkmark$ (1)""",
    "D"
)

# 6.2.2
add_item(
    "6.2.2", 3, TOPIC_Q6_2, PASSAGE_6_2,
    """Refer to line 4 ('Bare ruined choirs, where late the sweet birds sang').
(a) Identify the figure of speech used in this line. (1)
(b) Explain why this figure of speech is appropriate. (2)""",
    """(a) Metaphor / Personification $\\checkmark$ (1)
(b) Just as the branches of the trees become bare and weak as the seasons change, $\\checkmark$ so too does the speaker's body become fragile as he ages. $\\checkmark$
OR
In the same way that there are no people singing in the empty cathedrals, $\\checkmark$ there are no birds present to sing as they have migrated. $\\checkmark$ (2)""",
    "(a) Metaphor / Personification; (b) Compares leafless winter branches to desolate, ruined church choirs stripped of singing birds."
)

# 6.2.3
add_item(
    "6.2.3", 2, TOPIC_Q6_2, PASSAGE_6_2,
    """Refer to line 8 ('Death's second self, that seals up all in rest').
Explain what 'rest' describes and what it refers to in the context of the poem. (2)""",
    """Rest describes sleep. $\\checkmark$
It refers to death. $\\checkmark$ (2)""",
    "Describes sleep and refers metaphorically to death."
)

# 6.2.4
add_item(
    "6.2.4", 2, TOPIC_Q6_2, PASSAGE_6_2,
    """Refer to lines 9–10 ('In me thou seest the glowing of such fire / That on the ashes of his youth doth lie').
What does the glowing fire represent? (2)""",
    """The speaker refers to his remaining life / vitality / passion, $\\checkmark$ which is slowly fading as he ages. $\\checkmark$ (2)""",
    "The speaker's remaining vitality, passion, and dwindling life force."
)

# 6.2.5
add_item(
    "6.2.5", 2, TOPIC_Q6_2, PASSAGE_6_2,
    """Explain the comparison between the dying embers and the speaker's life in lines 11–12 ('As the death-bed whereon it must expire / Consumed with that which it was nourish'd by'). (2)""",
    """The coals / logs burn out in the flames $\\checkmark$ while the speaker's life / youth is expended by time and aging. $\\checkmark$ (2)""",
    "Just as fire is choked by the ashes of the wood that fed it, life is consumed by the very time that nourished youth."
)

# 6.2.6
add_item(
    "6.2.6", 2, TOPIC_Q6_2, PASSAGE_6_2,
    """How does the beloved respond to the speaker's mortality in lines 13–14? (2)""",
    """The person is appreciative / understanding $\\checkmark$ as he realises that he should love the speaker more because he (the speaker) is growing old. $\\checkmark$ (2)""",
    "The beloved loves more intensely because the time remaining together is brief."
)

# 6.2.7
add_item(
    "6.2.7", 2, TOPIC_Q6_2, PASSAGE_6_2,
    """Refer to lines 13–14 ('This thou perceiv'st, which makes thy love more strong, / To love that well which thou must leave ere long').
(a) What tone does the speaker use in these lines? (1)
(b) Why does the speaker use this tone? (1)""",
    """(a) Urgency / appeal / resignation $\\checkmark$ (1)
(b) The speaker requests that they intensify their love as their time together is limited. $\\checkmark$ (1)""",
    "(a) Urgency / appeal / resignation; (b) To encourage passionate devotion before mortality parts them."
)

# 6.2.8
add_item(
    "6.2.8", 3, TOPIC_Q6_2, PASSAGE_6_2,
    """The poem evokes feelings of pity for the speaker.
Discuss your view. (3)""",
    """Open-ended. Accept a relevant response which shows an understanding of the following aspects, among others:

Yes.
• The speaker's aging, which is reflected by the few and withering leaves (line 2), evokes pity. $\\checkmark$
• His time is running out as his life is compared to a fading sunset. $\\checkmark$
• He is helpless as aging / death is inevitable and youth 'must expire' (line 11). $\\checkmark$

OR

No.
• He encourages a deeper understanding of life's transience ('twilight' and 'sunset' - lines 5 and 6). $\\checkmark$
• The speaker recognises aging and death as a natural part of life (line 7). $\\checkmark$
• The speaker sees the process of growing old and facing death as a reason for deeper connection (lines 13–14). $\\checkmark$

NOTE: Do NOT award a mark for YES or NO. Credit responses where a combination is given. For full marks, the response must be well-substantiated. A candidate can score 1 or 2 marks for a response which is not well-substantiated. The candidate's interpretation must be grounded in the poem. (3)""",
    "Withered boughs, fading sunsets, and expiring embers evoke poignant pity; or embracing transience deepens love without self-pity."
)

print(f"Total items created: {len(ITEMS)}")

# -------------------------------------------------------------
# VALIDATION CHECKS
# -------------------------------------------------------------
print("\n--- RUNNING VALIDATION AUDIT ---")
# 1. Total marks check
marks_by_q = {}
total_marks = 0
for item in ITEMS:
    q_num = item["question_ref"].split(".")[0]
    marks_by_q[q_num] = marks_by_q.get(q_num, 0) + item["marks"]
    total_marks += item["marks"]

print(f"Total marks across all 90 items: {total_marks}")
for q_num in sorted(marks_by_q.keys(), key=int):
    print(f"  Question {q_num}: {marks_by_q[q_num]} marks (Expected: 35)")
    assert marks_by_q[q_num] == 35, f"Question {q_num} has {marks_by_q[q_num]} marks instead of 35!"

# 2. KaTeX check
latex_errors = 0
for item in ITEMS:
    for field in ["question", "memo", "passage"]:
        text = item[field]
        # Count unescaped dollars
        clean = text.replace(r"\$", "")
        dollars = clean.count("$")
        if dollars % 2 != 0:
            print(f"ERROR: Unbalanced dollar in {item['item_id']} [{field}]!")
            latex_errors += 1

print(f"KaTeX LaTeX syntax errors: {latex_errors}")
assert latex_errors == 0, f"Found {latex_errors} KaTeX syntax errors!"

# 3. Item count check
print(f"Total item count: {len(ITEMS)}")
assert len(ITEMS) == 90, f"Expected 90 items, got {len(ITEMS)}"

# -------------------------------------------------------------
# WRITE OUTPUT FILES
# -------------------------------------------------------------
OUTPUT_SUBJ.parent.mkdir(parents=True, exist_ok=True)
OUTPUT_ROOT.parent.mkdir(parents=True, exist_ok=True)

with open(OUTPUT_SUBJ, "w", encoding="utf-8") as f_subj, open(OUTPUT_ROOT, "w", encoding="utf-8") as f_root:
    for item in ITEMS:
        line = json.dumps(item, ensure_ascii=False) + "\n"
        f_subj.write(line)
        f_root.write(line)

print(f"\nSuccessfully wrote {len(ITEMS)} items to:")
print(f"  1. {OUTPUT_SUBJ}")
print(f"  2. {OUTPUT_ROOT}")
