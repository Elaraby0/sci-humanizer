# SciHumanizer

[![skills.sh installs](https://skills.sh/b/Elaraby0/sci-humanizer)](https://skills.sh/Elaraby0/sci-humanizer)

SciHumanizer is an agent skill for clear, natural scientific writing. It
improves structure and style without inventing facts, changing results, or
making claims stronger than the study design allows. Because it is Markdown,
it works with any agent that supports skills.

## How it works

SciHumanizer combines practical scientific-writing principles with a targeted
audit for formulaic AI prose. It first protects the scientific content:
claims, study design, numbers, units, citations, causal strength, scope, and
uncertainty. It then improves the argument, paragraph structure, sentences,
and word choice before checking the revision against the original evidence.

The skill uses concrete subjects and strong verbs, cuts words that do no work,
and removes inflated or mechanical language. It does not treat every passive
construction, technical term, repeated keyword, hedge, or dash as an error.
Those choices are evaluated in context because scientific accuracy is more
important than cosmetic variation.

When you paste paragraphs into chat, SciHumanizer shows every substantive edit
and then provides a clean version. When you provide a file or ask it to write a
new section, it returns the polished text without an unnecessary redline unless
you request one.

## Installation

Install SciHumanizer with the [Skills CLI](https://skills.sh/docs/cli):

```bash
npx skills add Elaraby0/sci-humanizer
```

For a global Codex installation:

```bash
npx skills add Elaraby0/sci-humanizer --skill sci-humanizer -g -a codex -y
```

Leave off `-g` to install it only in the current project. Use `-a` to select a
different supported agent.

## Usage

Call the skill directly:

```text
Use $sci-humanizer to revise this Discussion paragraph without changing its
citations, numerical results, or level of certainty.

[paste your paragraph here]
```

Or ask in plain language:

```text
Polish this abstract for a biomedical journal. Preserve every result and
confidence interval, and do not add citations.
```

To revise a file, give the agent its path:

```text
Use $sci-humanizer to polish the prose in manuscript.docx while preserving the
tables, references, equations, units, and document formatting.
```

To draft new material, provide the evidence that the section may use:

```text
Use $sci-humanizer to write a concise Introduction from these notes. Do not add
facts, prevalence estimates, or citations that are not supplied.
```

### Match your voice

Include a representative writing sample when you want the revision to retain
your own rhythm, terminology, and stylistic preferences:

```text
Use $sci-humanizer.

Here is a sample of my writing for voice matching:
[paste two or three representative paragraphs]

Now revise this text without changing its scientific meaning:
[paste the text]
```

## What it improves

| Area | SciHumanizer's approach |
|---|---|
| Claim strength | Matches causal language and certainty to the design and evidence |
| Scientific structure | Makes the question, gap, findings, and interpretation easy to locate |
| Sentences | Uses clear subjects and strong verbs while preserving justified passive voice |
| Paragraphs | Gives each paragraph a distinct purpose and a logical progression |
| Clutter | Removes empty openings, redundancy, filler, buried verbs, and needless modifiers |
| Results | Reports patterns and key values without reciting tables or hiding null findings |
| Methods | Improves readability without removing details needed for reproducibility |
| Statistics | Preserves estimates, intervals, denominators, units, precision, and uncertainty |
| Citations | Keeps citation markers attached to the claims they support and flags missing evidence |
| AI-coded prose | Removes inflated importance, sales language, fake depth, vague sourcing, and chatbot residue |
| Technical language | Retains necessary terms and uses abbreviations consistently |
| Authorial voice | Follows a supplied writing sample instead of forcing a generic style |

## Output modes

### Pasted paragraphs

SciHumanizer returns exactly two versions:

1. **Tracked changes**, with deletions as `~~strikethrough~~`, insertions as
   `**_bold italics_**`, and replacements showing both.
2. **Clean version**, with all edits accepted and no tracking markup.

### Files and new sections

Uploaded files, full documents, and sections written from scratch receive only
the polished result unless the user asks for commentary, alternatives, or a
redline.

## Example

*The passage below is an illustrative example, not a report of a real study.*

**Before:**

> In order to determine whether the exposure caused the outcome, an analysis of
> the observational cohort was conducted. The highly significant findings
> clearly prove that the exposure leads to the outcome and underscore its
> transformative importance.

**Tracked changes:**

> ~~In order to determine whether the exposure caused the outcome, an analysis
> of the observational cohort was conducted.~~ **_We analyzed the observational
> cohort to assess the association between the exposure and the outcome._** The
> ~~highly significant findings clearly prove that the exposure leads to the
> outcome and underscore its transformative importance~~ **_findings support an
> association but do not establish causation_**.

**Clean version:**

> We analyzed the observational cohort to assess the association between the
> exposure and the outcome. The findings support an association but do not
> establish causation.

## Optional diagnostic script

The bundled script flags passages for human review without rewriting them:

```bash
python3 skills/sci-humanizer/scripts/diagnose.py manuscript.md
python3 skills/sci-humanizer/scripts/diagnose.py manuscript.md --json
```

It reports signals such as long sentences and paragraphs, nominalizations,
passive constructions, repeated transitions, acronym density, clutter phrases,
and selected AI-coded patterns. A flag is a prompt for judgment, not proof that
the writing is poor or AI-generated.

## Sources and provenance

- Stanford University's
  [*Writing in the Sciences*](https://www.coursera.org/learn/sciwrite) course
  informed the scientific-writing framework.
- Siqi Chen's MIT-licensed
  [Humanizer](https://github.com/blader/humanizer) informed the audit for
  formulaic AI prose.
- Current publication guidance is linked from the skill's reference files,
  including ICMJE, EQUATOR, NISO CRediT, and COPE.

SciHumanizer is an independent, unofficial project. It is not affiliated with,
endorsed by, or an official product of Stanford University, Coursera, the
course authors, or the Humanizer project. No Stanford transcripts, slides,
PDFs, videos, or page images are included. See [NOTICE.md](NOTICE.md) for the
rights and attribution boundary.

## Version history

<details>
<summary>Show release notes</summary>

- **1.1.1** — Initial public release with evidence-preserving scientific
  revision, tracked-and-clean output for pasted paragraphs, file-safe output
  behavior, diagnostic tooling, and behavioral evaluations.

</details>

## Authors

- [Ahmed ELaraby (@Elaraby0)](https://github.com/Elaraby0) — creator and
  maintainer.

## Contributors

- [Ahmed (@ahmedawak)](https://github.com/ahmedawak) — helped improve and
  update SciHumanizer.

## Contributing and security

Evidence-preserving improvements are welcome. Read
[CONTRIBUTING.md](CONTRIBUTING.md) before submitting a change. Report security
concerns privately as described in [SECURITY.md](SECURITY.md).

## License

MIT. See [LICENSE](LICENSE) and [NOTICE.md](NOTICE.md).

## Repository structure

```text
skills/sci-humanizer/   Installable skill and runtime references
tests/                  Behavioral and trigger evaluation cases
```
