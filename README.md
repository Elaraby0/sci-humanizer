# SciHumanizer

[![skills.sh](https://skills.sh/b/Elaraby0/sci-humanizer)](https://skills.sh/Elaraby0/sci-humanizer)

SciHumanizer is an agent skill for clear, natural, scientific
writing. It combines scientific-writing principles with targeted detection of
formulaic AI prose while protecting claims, numbers, citations, uncertainty,
and disciplinary terminology.

The skill can revise or draft manuscripts, abstracts, titles, introductions,
methods, results, discussions, literature reviews, grants, protocols, theses,
posters, figure legends, research correspondence, presentations, and
public-facing science communication.

## Install

Install with the [Skills CLI](https://skills.sh/docs/cli):

```bash
npx skills add Elaraby0/sci-humanizer
```

For a global Codex installation:

```bash
npx skills add Elaraby0/sci-humanizer --skill sci-humanizer -g -a codex -y
```

Then invoke it explicitly when useful:

```text
Use $sci-humanizer to revise this Results paragraph without changing any
numbers, citations, or the strength of the claims.
```

Its broad trigger description also allows compatible agents to select it
automatically for scientific and scholarly writing tasks.

## Output behavior

- For one or more paragraphs pasted into chat for revision, it returns two
  sections: **Tracked changes** and **Clean version**. Deletions use
  strikethrough; insertions use bold italics.
- For uploaded files, whole documents, or sections requested from scratch, it
  returns only the polished result unless the user requests another format.
- It does not invent facts, citations, statistics, methods, limitations, or
  interpretations.
- It preserves justified technical language, uncertainty, and context-sensitive
  passive voice instead of treating every stylistic signal as an error.

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

## Repository layout

```text
skills/sci-humanizer/   Installable skill and runtime references
tests/                  Behavioral and trigger evaluation cases
```

## Provenance and independence

This is an independent, unofficial project informed by Stanford University's
[*Writing in the Sciences*](https://www.coursera.org/learn/sciwrite) course and
adapted in part from Siqi Chen's MIT-licensed
[Humanizer](https://github.com/blader/humanizer). It is not affiliated with,
endorsed by, or an official product of Stanford University, Coursera, the
course authors, or the Humanizer project.

No Stanford course transcripts, slides, PDFs, or page images are included.
See [NOTICE.md](NOTICE.md) for the rights and attribution boundary.

## Contributing and security

Behavioral fixes and evidence-preserving improvements are welcome. See
[CONTRIBUTING.md](CONTRIBUTING.md). To report a security concern, see
[SECURITY.md](SECURITY.md).

## License

MIT. See [LICENSE](LICENSE) and [NOTICE.md](NOTICE.md).
