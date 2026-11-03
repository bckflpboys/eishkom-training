# Sources: where to get data, what you may do with it, and where to learn teaching craft

Licences change and web pages move. **Read the licence on the page the day you download**, write it in `workspace/sources/sources.csv`, and keep the file. This is not legal advice.

## 0. The licence ladder (read this first)

| Colour | Licences | What you can do |
|---|---|---|
| Green | CC0, CC BY, Open Government Licence v3.0, MIT, Apache 2.0 | Adapt and train on it, even in a product you sell, with the credit line they ask for |
| Amber | CC BY-SA (share-alike), CC BY-NC (non-commercial), CC BY-ND (no derivatives), "© Department of Basic Education" | Use for the **eval set** and as **seeds** (see below). Do not paste it into a model you sell without permission |
| Red | Bought textbooks, paywalled sites, other companies' apps, forum scrapes, "all rights reserved" | Do not use |

**Seeds, not copies.** Facts and methods are not copyrightable; the exact text is. For amber sources let the teacher write ORIGINAL questions of the same type and difficulty (`mode: original` in `pipeline/plan.py`). The model still learns the structure and the skills, and `verify_code` checks the new answers independently. Keep `source_ref` on every record so one source can be removed later.

**Closed AI models.** Anthropic, OpenAI and Google restrict using their outputs to train competing models (check each current Terms page). Prefer open-weight teachers whose licence allows it (DeepSeek, Qwen, Gemma), and read the licence text, not a summary.

## A. South African sources (most important)

| Source | Where | Licence / terms | Use it for |
|---|---|---|---|
| DBE past exam papers and memos (NSC Gr 12, Gr 10 and 11 exams) | education.gov.za, Curriculum, National Senior Certificate Exams | © Department of Basic Education. The archive pages say old papers may be used for classroom enrichment and revision. Ask DBE in writing before using them in a commercial product | **Eval set** (hold out the newest papers), seeds for original questions |
| Provincial paper libraries | WCED ePortal (NSC past papers and memos), ecexams.co.za (Eastern Cape) | same | same; Eastern Cape also publishes **Chief Markers' reports** |
| **NSC Diagnostic Reports** (every year, by subject) | education.gov.za, Reports | DBE publication | **The best source for misconceptions.** For each question they say what learners got wrong and how teachers should fix it. Turn them into `workspace/config/misconceptions.jsonl` entries and into teacher-prompt guidance. Do not train on the raw text |
| **Examination Guidelines** (per subject) | education.gov.za | DBE | How papers are built, cognitive levels, command words: the basis for `answer_structure` and `exam_technique` data |
| CAPS documents and Annual Teaching Plans | education.gov.za | DBE | The topic list per grade and term (`caps_ref`, `topic`, which topics to plan) |
| ANA papers (Annual National Assessments, Gr 4-9, 2011-2014), if still online | education.gov.za archive | DBE | Gr 7-9 questions in maths and languages |
| **Siyavula open textbooks** (Mathematics Gr 10-12 in English **and Afrikaans**, Physical Sciences, Natural Sciences) and their **teacher guides** | siyavula.com, Open textbooks | **The branded Everything Maths/Science books are CC BY-ND (no adapting). The unbranded versions are CC BY.** Download the UNBRANDED ones | Worked examples, the correct **Afrikaans maths and science terms**, and the teacher guides' teaching notes. This is your best green source |
| DBE Mind the Gap, WCED worksheets, Thutong portal | education.gov.za, wcedeportal.westerncape.gov.za | mostly unclear | Seeds and eval only |
| Nal'ibali and African Storybook | nalibali.org, africanstorybook.org | CC BY (check each story) | Reading passages for English and Afrikaans comprehension |
| Project Gutenberg, Standard Ebooks | gutenberg.org | public domain | English passages for comprehension and writing practice |
| SADiLaR language corpora (NCHLT etc.) | sadilar.org | licence differs per resource: check | Afrikaans (and later Zulu, Xhosa, Setswana) text for language work |

## B. International sources (good for "show your steps" and how teachers explain)

| Source | Licence | Use it for |
|---|---|---|
| **Oak National Academy** (England, ages 11-16: maths, science, English). Lessons with **video transcripts**, slide decks, quizzes, worksheets. Has an API | **Open Government Licence v3.0**: commercial use and adaptation allowed with attribution. Use their attribution wording | Real teachers explaining step by step: seeds for `worked_example`, `step_walkthrough`, `think_aloud`. England's notation differs from CAPS (watch decimals, vocabulary) |
| **OpenStax** (Prealgebra, Algebra, Trigonometry, Precalculus, Physics, Chemistry, Biology) | mostly CC BY 4.0 (check each book) | Worked examples and answer keys, Gr 9+ level |
| Khan Academy, EngageNY/Eureka Math, CK-12 | CC BY-NC(-SA): **non-commercial** | Amber: eval or seeds only |
| **GSM8K** (grade-school word problems with step solutions), **MATH** (competition problems with step solutions) | MIT | Problem sources and a look at how steps are written. Good for Gr 7-9 word problems |
| NuminaMath, OpenR1-Math, MetaMathQA, Orca-Math | Apache 2.0 / MIT on the dataset, **but the solutions were written by other AI models**: read each dataset card for the generator and its terms | Questions and final answers as seeds. Do not copy their solutions wholesale |
| **MathDial** (ETH Zurich): about 3,000 teacher and student dialogues on multi-step word problems where the teacher guides with questions instead of telling | check the repository's licence file | The best public example of **scaffolding moves**: study it, and copy its dialogue shape (focus, probe, tell only when needed) into your teacher prompt |

Worth searching (I have not verified their licences or availability): math-tutoring dialogue sets built from teacher-student conversations, the Teacher-Student Chatroom Corpus (English language tutoring), reading-comprehension sets such as RACE, and the Kaggle essay-scoring sets. If you cannot verify the licence, treat it as amber.

## C. Where to learn good teaching (not training text: use these to write the spec, rubric and teacher prompt)

Free, and short enough to read in an evening each:
- **Rosenshine, "Principles of Instruction"** (American Educator, 2012): ten principles from research and master teachers.
- **Education Endowment Foundation (EEF)**: Teaching and Learning Toolkit and its guidance reports on maths, literacy, feedback and metacognition.
- **Dunlosky et al. (2013), "Improving Students' Learning With Effective Learning Techniques"**: which study methods work (practice testing and spacing) and which do not (highlighting, rereading).
- **The Learning Scientists** (learningscientists.org): six strategies with plain-language posters.
- **NSW CESE**, "Cognitive load theory in practice": why worked examples and small steps help novices.
- **NCETM** (UK), "Five big ideas in teaching for mastery", and **NCTM**, *Principles to Actions*: the effective mathematics teaching practices.
- Books worth owning: Polya, *How to Solve It* (the four-step method behind `polya_four_steps`); Brown, Roediger and McDaniel, *Make It Stick*.
- Talk to two or three real teachers (a maths teacher, an English teacher, an Afrikaans teacher). Ask them for the three mistakes they see every year and the trick they use to fix each. Write those down as misconceptions and techniques. This is the most valuable hour you will spend.

## D. What must never go into training data

- Anything with a learner's name, address, school, phone number, ID number or face. Photos for the vision phase need written consent from a parent or the school, and no faces or names.
- Text you copied from a paid book, a tutoring site, a forum (Brainly and similar) or another company's AI answers.
- Chat transcripts with real children.

## E. How each source plugs into the pipeline

| You have | `kind` in sources.csv | Next step | It becomes |
|---|---|---|---|
| A past paper + its memo | `past_paper` (+ `pair_with` the memo) and `memo` | `extract_items.py --source <paper>` | Eval items (newest papers) and seeds |
| A textbook or teacher guide | `textbook` | `extract_items.py --kind textbook` | Worked examples and exercises with answers |
| An Oak lesson transcript | `textbook` | same | Examples of how teachers talk |
| A diagnostic report or chief markers' report | `diagnostic_report` | read it; write entries by hand | `misconceptions.jsonl` |
| An exam guideline | `exam_guideline` | read it | Teacher-prompt guidance for `answer_structure` |
| A reading passage | `textbook` (language subjects) | `extract_items.py --kind textbook` | Comprehension items |
| Real teacher-written solutions | any | put them in `items/` by hand as gold items | The most trusted seeds |
