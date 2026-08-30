# Source map

This development map links SciHumanizer's major instructions to the analyzed
Stanford *Writing in the Sciences* course corpus. It distinguishes unique
instructional records from duplicate renderings. The source files described
below are not distributed with this repository.

## Corpus inventory

- 8 module Markdown files
- 64 transcript records
- 31 slide, handout, exercise, and demo-edit source assets in the manifest
- 17 converted PowerPoint PDFs
- 842 full-fidelity page JPEGs
- 1 consolidated `COMPLETE_COURSE.md`
- 1 `source_manifest.csv`
- approximately 205,000 words in the consolidated course

The module Markdown files are the canonical analysis layer because they contain
the transcript text, extracted slide text, links to page renderings, and source
asset names. `COMPLETE_COURSE.md` duplicates those modules for one-file
ingestion. JPEGs and converted PDFs preserve fidelity but should not be counted
as independent instructional sources.

No source file was renamed or modified during extraction.

## Module 1: Writing clearly

File: `Module_01_writing-clearly-principles-and-clarity.md`

| SciHumanizer principle | Course location |
|---|---|
| Communication before elegance; good writing can be learned | Transcript record 1, `subtitle.txt` |
| Talk the science through; write for readers; avoid boredom | Transcript record 1 |
| Separate first drafting from revision; cut ruthlessly | Transcript record 1 |
| Complex science can use simple language | Transcript records 2 and 3 |
| Verbs move sentences; nominalizations slow them | Transcript records 2 and 3 |
| Three core principles: cut clutter, prefer active voice, write with verbs | Transcript record 3, `subtitle (2).txt` |
| Cut empty openings, redundancy, adverbs, negatives, `there is/are`, and needless prepositions | Transcript records 4 and 5 |
| Avoid unnecessary acronyms and vague words | Transcript records 3 and 4 |
| Line-editing examples and whole-essay editing | Transcript records 6 and 7; Unit 1 slides and demo-edit asset |

Brief course phrases retained as useful labels include `cut clutter` and
`communicate an idea clearly and effectively`.

## Module 2: Strong sentences

File: `Module_02_strong-sentences-verbs-voice-and-flow.md`

| SciHumanizer principle | Course location |
|---|---|
| Active voice follows actor-action-recipient and can reveal responsibility | Transcript record 1, `subtitle (7).txt` |
| Active voice improves readability and exposes ambiguity | Transcript record 1 |
| Passive voice remains useful, especially in Methods | Transcript record 1 |
| `I` and `we` can be appropriate and make responsibility explicit | Transcript record 2, `subtitle (8).txt` |
| Use strong verbs; avoid nominalization and buried verbs | Transcript record 4, `subtitle (10).txt` |
| Keep subject and main verb close | Transcript records 4 and 5; Unit 2 slides |
| Sentence-editing practice | Transcript records 3 and 5; practice and demo-edit assets |
| Grammar conventions relevant to scientific manuscripts | Transcript record 6/7 region and Unit 2 slides |

Course-era grammar preferences, such as treating `data` only as plural, were
not embedded as universal rules. SciHumanizer follows current venue and
disciplinary usage.

## Module 3: Punctuation and paragraphs

File: `Module_03_punctuation-and-paragraphs-building-better-prose.md`

| SciHumanizer principle | Course location |
|---|---|
| Use dashes, colons, semicolons, and parentheses purposefully | Transcript record 1, `subtitle (14).txt`; Unit 3 slides |
| Merge sentences when punctuation clarifies their relationship | Transcript record 2, `subtitle (15).txt` |
| Make coordinated ideas and lists parallel | Transcript record 3, `subtitle (16).txt` |
| Treat the paragraph as the unit of composition | Transcript record 4, `subtitle (17).txt` |
| One main idea; give the point early; preserve readable white space | Transcript record 4 |
| Use logic rather than transition-word chains | Transcript record 4 |
| Flow from general to specific and in expected chronological order | Transcript record 4 |
| Outline the upshot of each sentence before editing a meandering paragraph | Transcript records 5 and 6/7 region |
| Repeat technical keywords consistently; control acronyms | Transcript record 7 region and Unit 3 slides |

This module is the basis for overriding Humanizer 2.11.2's blanket em/en dash
ban. SciHumanizer treats dashes as one punctuation tool and checks for overuse.

## Module 4: Writing process

File: `Module_04_the-writing-process-draft-revise-refine.md`

| SciHumanizer principle | Course location |
|---|---|
| Edit structure before sentence details | Transcript record 1, `subtitle (22).txt` |
| Separate prewriting, first drafting, and revision | Transcript record 2, `subtitle (23).txt` |
| Gather and organize evidence before composing | Transcript record 3/4 region, `subtitle (24).txt` |
| Create a broad road map and group like ideas | Transcript record 3/4 region |
| Draft quickly in complete sentences without polishing every line | Transcript record 4/5 region, `subtitle (25).txt` |
| Read aloud, run a verb check, cut, and seek outside feedback | Transcript record 6, `subtitle (27).txt` |
| Check numerical consistency across displays and text | Transcript record 6 |
| Trace claims to primary references and avoid citation chains | Transcript record 6 |

The course gives approximate time allocations to illustrate emphasis. The skill
keeps the sequence and rationale but does not impose fixed percentages.

## Module 5: Scientific manuscript

File: `Module_05_the-scientific-manuscript-from-results-to-abstract.md`

| SciHumanizer principle | Course location |
|---|---|
| Draft order: displays, Results, Methods, Introduction, Discussion, Abstract | Transcript record 1, `subtitle (31).txt` |
| Tables and figures form the paper's evidence story and should stand alone | Transcript record 1 |
| Use figures for patterns/visual impact and tables for exact values | Transcript record 1 |
| Use defensible precision, units, consistent labels, and explanatory legends | Transcript record 1 and Unit 5 slides |
| Results summarize patterns instead of reading tables line by line | Transcript record 2, `subtitle (32).txt` |
| Results complement displays, include key numbers and null findings, and remain separate from Methods/Discussion | Transcript record 2 |
| Past tense for completed work; present tense for what displays show | Transcript records 2, 4, and 7 |
| Methods as reproducible recipe; who/what/when/where/how/why; use subheadings and diagrams | Transcript record 4, `subtitle (34).txt` |
| Passive voice and necessary jargon are acceptable in Methods | Transcript record 4 |
| Introduction cone: known -> unknown -> question/aim -> approach | Transcript record 5, `subtitle (35).txt` |
| Introduction is focused, short, explicit about purpose, and not an exhaustive paper-by-paper review | Transcript record 5 |
| Discussion inverted cone: answer -> evidence/context -> limitations -> implications | Transcript record 7, `subtitle (37).txt` |
| Start and end Discussion with the main finding; avoid overreach and generic limitations | Transcript record 7 |
| Write Abstract last; make it standalone and consistent with the full paper | Transcript record 8, `subtitle (38).txt` |
| Abstract components: context, aim, minimal methods, key results, conclusion, implication | Transcript record 8 |

Formatting details tied to individual journals, including the course's common
three-horizontal-line table convention, were converted into `follow the current
target venue` rather than universal mandates.

## Module 6: Integrity and publication

File: `Module_06_publishing-with-integrity-ethics-authorship-and-submission.md`

| SciHumanizer principle | Course location |
|---|---|
| Copying, patchwriting, sentence-structure mimicry, and unattributed definitions are plagiarism | Transcript record 1, `subtitle (40).txt` |
| Draft paraphrases from understanding and inspect primary sources | Transcript record 1 |
| Text recycling and duplicate publication require caution | Transcript record 1 |
| Authorship carries public responsibility; decide contributions early | Transcript record 2, `subtitle (41).txt` |
| Avoid ghost and honorary authorship | Transcript record 2 |
| Choose a suitable journal and follow current author instructions | Transcript record 3, `subtitle (42).txt` |
| Review proofs; respond to reviewers point by point and respectfully | Transcript record 3 |
| Treat reviewer confusion as evidence that the manuscript may be unclear | Transcript record 3 |
| Make peer review constructive, specific, and focused on the work | Transcript record 7, `subtitle (46).txt` |
| Maintain a useful overview/major/minor structure in peer review | Transcript record 7 |
| Evaluate journal legitimacy rather than trusting solicitations or invented metrics | Transcript record 8, `subtitle (47).txt` |

The course's authorship and predatory-journal details were supplemented with
current ICMJE, CRediT, COPE, and venue guidance. Historical prevalence figures
and lists were not embedded as current facts.

## Module 7: Reviews, grants, and professional writing

File: `Module_07_beyond-the-research-paper-grants-reviews-and-professional-writing.md`

| SciHumanizer principle | Course location |
|---|---|
| Narrative review synthesizes recent primary literature around a defined theme | Transcript record 1, `subtitle (49).txt` |
| Prewriting and organization are especially important for reviews | Transcript record 1 |
| Organize a review by logical sections and write for a broad audience | Transcript record 1 |
| Use Specific Aims as the grant's conceptual road map | Transcript record 2, `subtitle (50).txt` |
| Align importance, gap, goal, hypothesis, aims, approach, and payoff | Transcript record 2 and record 3, `subtitle (51).txt` |
| Make the objective valuable regardless of how the hypothesis tests | Transcript records 2 and 3 |
| Seek iterative feedback from a broad audience and state what feedback is needed | Transcript records 2 and 3 |
| Research plan connects need to expected payoff and demonstrates feasibility | Transcript record 4, `subtitle (52).txt` region |
| Recommendation letters use independent judgment and concrete examples | Transcript record 5, `subtitle (53).txt` |
| Personal statements should be authentic, selective, and story-driven without fabrication | Transcript record 6, `subtitle (54).txt` |

Grant page limits and application requirements are treated as dynamic funder
rules, not permanent course facts.

## Module 8: Public science communication

File: `Module_08_writing-for-the-public-media-news-and-broader-audiences.md`

| SciHumanizer principle | Course location |
|---|---|
| Prepare clear take-home messages and anticipate public misinterpretation | Transcript record 1, `subtitle (56).txt` |
| Present risk using absolute quantities, whole-number frequencies, common denominators, and time frames | Transcript record 1 |
| Prepare interviews around a small set of accurate messages | Transcript record 2, `subtitle (57).txt` |
| Six public-writing moves: lead with result, remove jargon, unpack science, prioritize details, get to point, tell story | Transcript record 3, `subtitle (58).txt` |
| Accessibility filters detail without sacrificing accuracy | Transcript record 3 |
| Science-news structure: lead, nut graf, early quote, body, kicker | Transcript record 5, `subtitle (60).txt` |
| Quotes must remain faithful; interviews should elicit meaning and human context | Transcript record 6, `subtitle (61).txt` |
| Social communication should be purposeful, personal, accurate, and engaging | Transcript record 7, `subtitle (62).txt` region and social-media slides |

## Humanizer source

Source: `blader/humanizer`, installed as Humanizer 2.11.2 under the MIT License.

SciHumanizer retains its central safeguards:

- preserve claims;
- do not invent facts;
- match an explicitly requested voice;
- diagnose multiple AI patterns rather than treating one word as proof;
- remove inflated claims, vague sources, sales language, filler, formulaic
  structures, chatbot residue, and fake depth; and
- audit for lost or added factual content.

Scientific adaptations include:

- dashes are permitted purposefully;
- passive voice is context-sensitive;
- necessary technical terms are retained;
- hedging is calibrated rather than simply removed;
- terminology may repeat for scientific consistency; and
- file edits preserve citations, equations, tables, metadata, and reference
  fields.

## Current authoritative supplements

- ICMJE, current authorship and AI-assisted publishing recommendations.
- EQUATOR Network, current reporting-guideline library.
- CRediT, NISO contributor-role taxonomy.
- COPE, publication-ethics resources.

See `current-standards.md` for live links and the policy priority order.
