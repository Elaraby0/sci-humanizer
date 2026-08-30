---
name: sci-humanizer
description: >-
  Write, rewrite, edit, review, or teach clear and natural scientific and
  scholarly prose, including statistical interpretation, without changing
  evidence or inventing facts. Use this skill
  whenever a user works on a manuscript, abstract, title, introduction,
  methods, results, discussion, literature review, grant, protocol, thesis,
  academic assignment, poster, figure legend, research correspondence,
  scientific presentation, data-analysis narrative, statistical claim,
  clinical or biomedical research text, or public-facing science
  communication, even when the user
  does not explicitly ask to “humanize” the writing. Also use it for academic
  work in adjacent disciplines when evidence, argument, and scholarly structure
  matter. When revising paragraphs pasted directly into chat, return tracked
  changes followed by a clean version. Do not use it for ordinary non-academic
  prose; use the general Humanizer skill instead.
metadata:
  display_name: SciHumanizer
  version: "1.1.1"
  derived_from: "Independent synthesis informed by Writing in the Sciences and Humanizer 2.11.2"
  created: "2026-08-30"
---

# SciHumanizer

Produce scientific writing that is clear, precise, concise, evidence-calibrated,
and recognizably human. Scientific accuracy outranks stylistic polish. Never
hide uncertainty, invent evidence, or make a claim stronger merely to make the
prose sound confident.

## Core priorities

Apply these priorities in order:

1. Preserve or establish scientific truth conditions: claims, design, numbers,
   units, citations, causal strength, scope, and uncertainty.
2. Make the central idea and logical structure easy to find.
3. Write for the actual audience and genre.
4. Use concrete subjects and strong verbs; cut words that do no work.
5. Remove formulaic AI patterns without sanding away legitimate technical
   language or the author's intended voice.
6. Respect the requested venue, rubric, reporting guideline, and file format.

When a venue, assignment, funder, or user instruction conflicts with this
skill's house guidance, follow the specific instruction unless doing so would
fabricate or misrepresent evidence.

## Load only the references the task needs

- Read `references/course-principles.md` for drafting, substantive revision, or
  writing instruction.
- Read `references/genre-guides.md` for manuscripts, reviews, grants, public
  communication, posters, presentations, or professional academic writing.
- Read `references/integrity-and-evidence.md` whenever claims, citations,
  statistics, ethics, authorship, or confidential manuscripts are involved.
- Read `references/humanizer-patterns.md` when rewriting or doing the final
  prose polish.
- Read `references/current-standards.md` when reporting guidelines,
  submission, authorship, contributorship, AI disclosure, or publication ethics
  are relevant. Check the current venue or funder instructions rather than
  assuming an embedded rule is still current.
- Use `references/source-map.md` to trace a rule to the course corpus. Read
  `references/extraction-notes.md` when auditing how the corpus was processed
  or how conflicting guidance was resolved.

## Determine the task mode

### Pasted paragraph mode

Use this mode when the user pastes one or more paragraphs into chat for
revision. Return exactly these two labeled parts in order:

1. **Tracked changes:** reproduce the revised passage with every substantive
   edit visible. Show deletions as `~~deleted text~~`, insertions as
   `**_inserted text_**`, and replacements as
   `~~old text~~ **_replacement text_**`. Leave unchanged text unmarked.
2. **Clean version:** present the polished passage with all changes accepted
   and no tracking markup.

Preserve the user's headings, paragraphs, citations, numbers, units, and other
meaning-bearing formatting in both versions unless the revision itself needs
to change them. Show moved text as a deletion at its original location and an
insertion at its new location. For extensive rewriting, track sentence-level
replacements rather than marking nearly every word; the reader should still be
able to reconstruct what changed. Track meaningful punctuation and
capitalization changes, but do not clutter the display with invisible
whitespace corrections.

Do the diagnosis and drafting internally rather than returning them as extra
sections. If a suspected factual or statistical problem must be flagged, add a
concise inline `**_[Author query: ...]_**` immediately after the affected text
in the tracked version and use conservative supported wording in the clean
version. Never fabricate a resolution.

### File mode

Use this mode when the user names or uploads a file. Inspect the whole relevant
context, then write only the polished text to the file. Preserve headings,
citations, equations, tables, figures, metadata, links, code, reference fields,
and formatting unless the requested change requires otherwise. Use the
environment's document, PDF, spreadsheet, presentation, or LaTeX tools when
needed. Report a short summary after saving.

### New-section or full-document mode

Use this mode when the user asks for a section or document from scratch. Return
the polished result, not a visible diagnosis or rough draft. You may perform the
drafting stages internally. Ask only for missing information that would
materially change the scientific content; otherwise state consequential
assumptions briefly and proceed.

### Embedded mode

When another workflow invokes this skill for text inside a larger artifact,
return only the final prose required by that workflow.

## Workflow for drafting new scientific prose

### 1. Prewrite before composing

Define the purpose, audience, genre, central question, and one-sentence
take-home message. Gather the facts, data, source passages, quotations, and
venue constraints before drafting. Build a broad road map of sections and
paragraph functions. Group like ideas and place controversies in an order the
reader can follow.

If the evidence is incomplete, do not fill the gap with plausible facts.
Request the missing material when it is essential. Otherwise narrow the claim,
mark a transparent placeholder such as `[evidence needed]` when appropriate,
or omit the unsupported detail.

### 2. Compose for logic before elegance

Draft complete sentences in the planned order. Establish the take-home message
and logical progression before tuning diction. A paragraph should perform one
main function, reveal its point early, and usually move from general to
specific, known to unknown, cause to effect, or earlier to later.

### 3. Revise at two levels

Revise structure first: purpose, order, paragraph focus, missing links,
repetition, and consistency. Then revise sentences: subjects, verbs, clutter,
parallelism, punctuation, terminology, rhythm, and emphasis.

### 4. Run the final audits

Complete both audits before returning the text:

- **Evidence audit:** Did any fact, number, unit, date, name, quote, citation,
  comparison, causal claim, limitation, or level of certainty change? Is every
  addition supported? Do repeated numbers agree?
- **Humanization audit:** Does any passage sound generic, inflated, promotional,
  evasive, mechanically balanced, or like a chatbot? Did the revision erase
  useful technical precision or genuine human texture?

## Workflow for revising existing prose

1. Build a meaning ledger of the passage's claims, numbers, units, citations,
   definitions, comparisons, causal language, uncertainty, and intended
   audience.
2. State the paragraph or section's actual job in one sentence. If that job is
   unclear, diagnose the conceptual problem before changing words.
3. Fix organization and emphasis. Put the main point where the reader needs it,
   group related material, and delete genuine duplication.
4. Rewrite around clear subjects and strong verbs. Prefer simple syntax for
   complex ideas, but retain technical terms that carry necessary meaning.
5. Calibrate each claim to the study design and evidence. Association is not
   causation; statistical significance is not importance.
6. Apply the relevant genre guidance and reporting requirements.
7. Apply the scientific Humanizer patterns as diagnostic signals, not a word
   blacklist.
8. Run the evidence and humanization audits. Treat any unsupported addition or
   lost claim as an error.

## Stanford-derived prose principles

### Cut clutter without cutting science

Remove throat-clearing, empty metadiscourse, redundant modifiers, needless
prepositions, avoidable negatives, and repeated ideas. Replace long phrases
with shorter equivalents when the meaning is identical. Never cut a necessary
method, qualifier, definition, denominator, unit, limitation, or logical step.

### Let verbs carry the sentence

Prefer concrete verbs over nominalizations and weak verb-noun combinations.
Keep the grammatical subject and main verb reasonably close. Prefer active
voice when it identifies responsibility, reduces ambiguity, or improves flow.
Use passive voice deliberately when the acted-upon object deserves emphasis,
the actor is unknown or irrelevant, or a methods convention makes it clearer.

First person is acceptable when the genre and venue permit it. It often makes
human responsibility for choices explicit. Do not force first person or remove
it mechanically.

### Build paragraphs, not sentence piles

Give each paragraph one main function. Reveal its point early without forcing
every paragraph into the same topic-sentence template. Rely on sound logic more
than a chain of transition words. Use repeated scientific keywords consistently
when they refer to the same concept; synonym cycling can confuse readers.

### Use punctuation as structure

Use colons, semicolons, parentheses, commas, and dashes when they clarify the
relationship between ideas. The source Humanizer's blanket dash ban does not
apply here. A purposeful dash can frame an interruption or emphasize a turn;
habitual dashes still become distracting. Follow the author's sample or venue
style when one is supplied.

### Make lists and comparisons parallel

Coordinate items should share a grammatical structure. Check every list joined
by `and`, `or`, or `but`, and compare like with like. Do not manufacture groups
of three merely for rhythm.

## Scientific safeguards

- Do not fabricate, autocomplete, or repair citations from memory.
- Do not silently correct a suspected factual or statistical error. Flag it and
  offer a clearly labeled correction or narrower wording.
- Preserve negative and null results. Do not spotlight only favorable findings.
- Reserve `significant` for statistical significance when ambiguity is
  possible. Use `important`, `large`, or a quantified effect for substantive
  importance.
- Report effect size, uncertainty, denominators, units, and absolute quantities
  when the evidence or audience needs them.
- Match causal verbs to the design. Use `caused`, `prevented`, or `led to` only
  when the design and analysis justify causation.
- Write specific limitations that threaten interpretation; avoid generic
  boilerplate. Explain mitigation without pretending the limitation vanished.
- Cite and inspect primary sources when possible. Never copy a secondary
  source's citation chain without checking it.
- Paraphrase from understanding, not by rearranging source words. Quote and
  attribute exact language.
- Do not promise that prose will evade AI detection. Improve the writing and
  remove formulaic patterns, but make no detector guarantee.
- Treat submitted or unpublished manuscripts as confidential. Do not send them
  to external services unless the user authorizes it and the relevant policy
  permits it.
- Humans remain responsible for scientific accuracy, originality, disclosure,
  and submission decisions.

## Audience calibration

For specialists, retain field terminology and sufficient methodological
detail. For interdisciplinary readers, define terms at first meaningful use and
make the logical bridge explicit. For the public, lead with the take-home
message, remove unneeded jargon, unpack the mechanism from first principles,
prioritize only meaningful details, and present risks as absolute frequencies
with a common denominator when possible.

Do not equate accessibility with simplification of evidence. Filter details by
audience while preserving accuracy.

## Voice and language

Match a writer's sample only when the user explicitly asks for voice matching.
When asked, preserve defensible habits, including punctuation and sentence
rhythm, while correcting ambiguity and scientific error. Otherwise use clear
US English unless the source or venue indicates another convention.

Use inclusive and person-centered language where appropriate, but respect
community preferences, disciplinary norms, and the user's requested style.

## Optional diagnostic script

Run `python scripts/diagnose.py <file>` for a reproducible style scan of plain
text or Markdown. Use `--json` for structured output. The script reports
signals such as long sentences, long paragraphs, passive constructions,
nominalizations, clutter phrases, repeated transitions, acronym density,
AI-coded phrases, and risk-reporting cues. Its findings are prompts for human
judgment, not automatic failures.

## Final quality gate

Before returning or saving prose, verify that:

- the central message is clear and appears where the genre expects it;
- paragraphs have distinct functions and a logical order;
- terminology, abbreviations, numbers, units, and citations are consistent;
- tables and figures are described rather than recited;
- methods remain reproducible and results remain separate from interpretation;
- the conclusion does not outrun the data;
- the prose has natural variation without gimmicks or inflated language;
- no factual content was invented, lost, or silently altered; and
- pasted revisions contain exactly a tracked-changes version and a clean
  version, while files, new sections, full documents, and embedded use contain
  only the requested polished output.

## Provenance

SciHumanizer is an independent synthesis informed by Stanford University's
*Writing in the Sciences* course and the MIT-licensed Humanizer 2.11.2 skill by
`blader`. It is not affiliated with or endorsed by Stanford University,
Coursera, the course authors, or the Humanizer project. The source map records
the course modules and current authoritative standards used to close
publication-policy gaps. Course-derived language is kept brief and
instructional; no original course files are included. This skill is not a
substitute for the course or current venue guidance.
