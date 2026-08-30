# Extraction notes

## Scope inspected

The local corpus was inventoried before synthesis. It contains 870 files (about
174 MB): 842 rendered page images, 17 PDFs, 10 Markdown documents, and one CSV
manifest. The Markdown layer includes eight module documents, one consolidated
course document, and a README. The manifest identifies 64 transcript records
and 31 source assets. The consolidated document contains about 205,000 words.

The PDFs and page images are alternate renderings of content represented in the
module documents. The consolidated Markdown and module files were therefore the
primary extraction layer, while the manifest and filenames were used to verify
coverage and provenance. All eight modules and all transcript records listed in
the manifest were accounted for. The source corpus was not renamed or edited.

## Extraction method

The build used four passes:

1. Inventory file types, sizes, module boundaries, and manifest mappings.
2. Read the consolidated course by module and search across every module for
   recurring rules, exceptions, section guidance, examples, ethics topics, and
   writing-process advice.
3. Group the material into prose principles, genre-specific guidance,
   evidence/integrity safeguards, and source mappings.
4. Reconcile apparent contradictions by context and supplement time-sensitive
   policy gaps with current primary guidance.

The resulting skill is a synthesis, not a transcript dump. It keeps short,
useful course formulations and compact examples where they clarify a rule, but
does not reproduce lectures or slides wholesale.

## Major extracted themes

- Write to inform: clarity does not require ornate language.
- Cut clutter, choose strong verbs, and use active voice when it clarifies
  responsibility; retain passive voice when it serves emphasis or methods.
- Treat paragraphs as units of thought, reveal their function early, and rely
  on logic more than transition-word chains.
- Draft from a road map, revise structure before sentences, read aloud, and
  seek outside feedback.
- Build manuscripts around displays and results; make figures and tables
  self-contained; keep Results distinct from Methods and Discussion.
- Narrow Introductions from known information to the gap and question; open
  Discussions with the answer and close with a calibrated implication.
- Paraphrase from understanding, trace primary citations, avoid patchwriting,
  and decide authorship responsibilities early.
- Adapt science for public audiences by leading with the takeaway, unpacking
  jargon, and expressing risk with absolute quantities and common denominators.

## Contextual resolutions

- **Active versus passive voice:** active is the default when it improves
  clarity; passive remains legitimate when the object or procedure should lead.
- **Dashes:** the general Humanizer's blanket dash prohibition was not carried
  over. The course treats dashes as purposeful punctuation, so SciHumanizer
  diagnoses overuse but permits meaningful use.
- **Repetition versus synonym variety:** repeated technical keywords aid
  cohesion; needless rhetorical repetition remains clutter.
- **Jargon:** retain necessary field terms for specialists, define them for
  interdisciplinary readers, and unpack or remove them for the public.
- **Verb tense and person:** follow genre, chronology, venue rules, and meaning
  rather than applying a universal ban on first person or past tense.
- **Conciseness versus completeness:** remove words that do no work, never a
  qualifier, denominator, method, limitation, unit, or logical step needed for
  scientific interpretation.

## Current-policy supplements

The course's prose guidance is durable, but reporting standards, publication
ethics, authorship, and AI-disclosure policies change. The skill therefore
links to current primary sources rather than freezing historical details:

- ICMJE authorship, contributorship, confidentiality, and AI-assisted
  technology recommendations;
- the EQUATOR Network reporting-guideline library;
- the NISO CRediT taxonomy; and
- COPE publication-ethics resources.

These supplements do not replace a journal, institution, funder, or assignment
instruction. The specific current requirement takes priority.

## Humanizer integration

The original `humanizer` 2.11.2 skill remains unchanged. SciHumanizer adapts
its catalog of formulaic AI patterns and its emphasis on specificity and
natural rhythm, then constrains those ideas with scientific safeguards. Terms
that are generic in everyday prose may be necessary technical terms in science;
all pattern matches are therefore contextual signals rather than forbidden
tokens. SciHumanizer makes no claim that a revision will evade AI detection.

## Known limits

- The corpus is biomedical-heavy. The skill generalizes its reasoning to other
  scholarly fields but should follow discipline-specific genre conventions when
  provided.
- The diagnostic script uses regular expressions and cannot determine meaning,
  causality, plagiarism, authorship eligibility, or AI origin.
- Reporting standards and venue rules must be checked at the time of use.
- A prose editor cannot validate an underlying analysis without the data,
  methods, and appropriate statistical review.

For line-level provenance, see `source-map.md`.
