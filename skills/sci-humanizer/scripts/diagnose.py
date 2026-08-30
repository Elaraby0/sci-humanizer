#!/usr/bin/env python3
"""Diagnostic style scan for scientific prose.

This script reports signals for human review. It does not rewrite text and does
not treat any signal as proof of poor or AI-generated writing.
"""

from __future__ import annotations

import argparse
import json
import re
import statistics
import sys
from collections import Counter
from pathlib import Path
from typing import Any


WORD_RE = re.compile(r"\b[\w'’-]+\b", re.UNICODE)
SENTENCE_RE = re.compile(r"(?<=[.!?])(?:[\"'”’\)\]]*)\s+(?=[A-Z0-9\"'“‘\(\[])")
PASSIVE_RE = re.compile(
    r"\b(?:am|is|are|was|were|be|been|being|gets?|got)\s+"
    r"(?:\w+ly\s+)?(?:\w+(?:ed|en|wn|ung|nt))\b",
    re.IGNORECASE,
)
ACRONYM_RE = re.compile(r"\b[A-Z][A-Z0-9-]{1,7}\b")
DEFINED_ACRONYM_RE = re.compile(
    r"\b(?:[A-Za-z][A-Za-z-]*\s+){1,8}\(([A-Z][A-Z0-9-]{1,7})\)"
)
NUMBER_RE = re.compile(
    r"(?<!\w)(?:[<>≤≥~≈]?\s*)?(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?%?"
)

CLUTTER_PHRASES = (
    "in order to",
    "due to the fact that",
    "at this point in time",
    "it is important to note that",
    "it should be emphasized that",
    "it is well known that",
    "has the ability to",
    "a large number of",
    "the fact that",
    "in the event that",
    "for the purpose of",
    "with regard to",
    "in the context of the present study",
    "as previously mentioned",
)

AI_CODED_PHRASES = (
    "stands as",
    "serves as a testament",
    "pivotal",
    "evolving landscape",
    "intricate interplay",
    "tapestry",
    "underscores the importance",
    "highlights the importance",
    "groundbreaking",
    "revolutionary",
    "transformative",
    "delve into",
    "let us explore",
    "let's explore",
    "the real question is",
    "at its core",
    "what really matters",
    "the future looks promising",
    "paves the way",
    "despite these challenges",
    "it is not just",
    "not merely",
    "not only",
    "to be clear",
    "this is not to say",
    "some might argue",
    "here's what you need to know",
    "i hope this helps",
    "let me know",
)

TRANSITIONS = (
    "additionally",
    "furthermore",
    "moreover",
    "however",
    "nevertheless",
    "therefore",
    "thus",
    "consequently",
    "interestingly",
    "importantly",
)

NOMINALIZATION_EXCEPTIONS = {
    "intervention",
    "population",
    "condition",
    "randomization",
    "regression",
    "transcription",
    "expression",
    "distribution",
    "association",
    "concentration",
    "measurement",
    "treatment",
    "experiment",
}


def read_text(path: str) -> str:
    if path == "-":
        return sys.stdin.read()
    return Path(path).read_text(encoding="utf-8")


def prose_only(text: str) -> str:
    """Remove fenced code and common Markdown/LaTeX noise from style metrics."""
    text = re.sub(r"```.*?```", " ", text, flags=re.DOTALL)
    text = re.sub(r"`[^`]+`", " ", text)
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", text)
    text = re.sub(r"\[[^\]]+\]\([^)]*\)", lambda m: m.group(0).split("]")[0][1:], text)
    text = re.sub(r"\\(?:cite|ref|label)\{[^}]*\}", " ", text)
    text = re.sub(r"^\s{0,3}(?:#{1,6}|[-*+]\s+|\d+[.)]\s+)", "", text, flags=re.MULTILINE)
    return text


def split_sentences(text: str) -> list[str]:
    compact = re.sub(r"\s+", " ", text).strip()
    if not compact:
        return []
    parts = [s.strip() for s in SENTENCE_RE.split(compact) if s.strip()]
    return parts or [compact]


def split_paragraphs(text: str) -> list[str]:
    return [re.sub(r"\s+", " ", p).strip() for p in re.split(r"\n\s*\n", text) if p.strip()]


def words(text: str) -> list[str]:
    return WORD_RE.findall(text)


def snippet(text: str, start: int, width: int = 150) -> str:
    left = max(0, start - 45)
    right = min(len(text), start + width)
    value = re.sub(r"\s+", " ", text[left:right]).strip()
    if left:
        value = "…" + value
    if right < len(text):
        value += "…"
    return value


def phrase_hits(text: str, phrases: tuple[str, ...]) -> list[dict[str, Any]]:
    lower = text.lower()
    hits: list[dict[str, Any]] = []
    for phrase in phrases:
        for match in re.finditer(r"\b" + re.escape(phrase) + r"\b", lower):
            hits.append({"phrase": phrase, "snippet": snippet(text, match.start())})
    return hits


def passive_hits(sentences: list[str]) -> list[dict[str, Any]]:
    hits: list[dict[str, Any]] = []
    for index, sentence in enumerate(sentences, 1):
        forms = sorted({m.group(0) for m in PASSIVE_RE.finditer(sentence)})
        if forms:
            hits.append(
                {
                    "sentence": index,
                    "forms": forms,
                    "snippet": sentence[:220] + ("…" if len(sentence) > 220 else ""),
                }
            )
    return hits


def nominalization_hits(tokens: list[str]) -> list[dict[str, Any]]:
    counts: Counter[str] = Counter()
    for token in tokens:
        term = token.lower().strip("-'’")
        if (
            len(term) > 7
            and term not in NOMINALIZATION_EXCEPTIONS
            and re.search(r"(?:tion|sion|ment|ance|ence|ity|ization)$", term)
        ):
            counts[term] += 1
    return [{"term": term, "count": count} for term, count in counts.most_common(20)]


def acronym_report(text: str) -> dict[str, Any]:
    acronyms = Counter(ACRONYM_RE.findall(text))
    defined = set(DEFINED_ACRONYM_RE.findall(text))
    ignored = {"I", "A", "AN", "THE", "AND", "OR", "BUT", "US", "CI", "SD"}
    acronyms = Counter({k: v for k, v in acronyms.items() if k not in ignored})
    undefined = [a for a in acronyms if a not in defined and acronyms[a] > 0]
    return {
        "unique": len(acronyms),
        "total_uses": sum(acronyms.values()),
        "defined_in_parentheses": sorted(defined),
        "possibly_undefined": sorted(undefined),
        "most_common": [{"term": k, "count": v} for k, v in acronyms.most_common(20)],
    }


def transition_report(sentences: list[str]) -> dict[str, Any]:
    starts: list[dict[str, Any]] = []
    sequence: list[tuple[int, str]] = []
    pattern = re.compile(r"^(?:[\"'“‘\(]*)(" + "|".join(TRANSITIONS) + r")\b", re.IGNORECASE)
    for index, sentence in enumerate(sentences, 1):
        match = pattern.search(sentence)
        if match:
            term = match.group(1).lower()
            starts.append({"sentence": index, "term": term, "snippet": sentence[:180]})
            sequence.append((index, term))
    runs: list[list[int]] = []
    current: list[int] = []
    for index, _ in sequence:
        if current and index == current[-1] + 1:
            current.append(index)
        else:
            if len(current) >= 2:
                runs.append(current)
            current = [index]
    if len(current) >= 2:
        runs.append(current)
    return {"sentence_starts": starts, "consecutive_runs": runs}


def risk_signal(text: str) -> dict[str, Any]:
    relative = bool(
        re.search(
            r"\b(?:relative risk|risk ratio|hazard ratio|odds ratio|"
            r"\d+(?:\.\d+)?%\s+(?:higher|lower|increase|decrease|reduction))\b",
            text,
            flags=re.IGNORECASE,
        )
    )
    absolute = bool(
        re.search(
            r"\b(?:absolute risk|risk difference|\d+\s+(?:in|out of|per)\s+[\d,]+|"
            r"from\s+\d+(?:\.\d+)?%?\s+to\s+\d+(?:\.\d+)?%?)\b",
            text,
            flags=re.IGNORECASE,
        )
    )
    return {
        "relative_risk_language_detected": relative,
        "absolute_risk_language_detected": absolute,
        "review_needed": relative and not absolute,
        "note": "If writing for non-specialists, pair relative effects with baseline and absolute risk when possible.",
    }


def analyze(text: str, long_sentence: int, long_paragraph: int) -> dict[str, Any]:
    clean = prose_only(text)
    sentence_list = split_sentences(clean)
    paragraph_list = split_paragraphs(clean)
    token_list = words(clean)
    sentence_lengths = [len(words(s)) for s in sentence_list]
    paragraph_lengths = [len(words(p)) for p in paragraph_list]

    long_sentences = [
        {
            "sentence": i,
            "words": length,
            "snippet": sentence_list[i - 1][:240] + ("…" if len(sentence_list[i - 1]) > 240 else ""),
        }
        for i, length in enumerate(sentence_lengths, 1)
        if length > long_sentence
    ]
    long_paragraphs = [
        {
            "paragraph": i,
            "words": length,
            "snippet": paragraph_list[i - 1][:240] + ("…" if len(paragraph_list[i - 1]) > 240 else ""),
        }
        for i, length in enumerate(paragraph_lengths, 1)
        if length > long_paragraph
    ]

    return {
        "notice": "Diagnostic signals require human judgment; they are not errors or proof of AI authorship.",
        "metrics": {
            "words": len(token_list),
            "sentences": len(sentence_list),
            "paragraphs": len(paragraph_list),
            "mean_sentence_words": round(statistics.mean(sentence_lengths), 1) if sentence_lengths else 0,
            "median_sentence_words": round(statistics.median(sentence_lengths), 1) if sentence_lengths else 0,
            "max_sentence_words": max(sentence_lengths, default=0),
            "mean_paragraph_words": round(statistics.mean(paragraph_lengths), 1) if paragraph_lengths else 0,
            "em_dashes": text.count("—"),
            "en_dashes": text.count("–"),
            "numbers_detected": len(NUMBER_RE.findall(clean)),
        },
        "long_sentences": long_sentences,
        "long_paragraphs": long_paragraphs,
        "possible_passives": passive_hits(sentence_list),
        "possible_nominalizations": nominalization_hits(token_list),
        "clutter_phrases": phrase_hits(clean, CLUTTER_PHRASES),
        "ai_coded_phrases": phrase_hits(clean, AI_CODED_PHRASES),
        "transition_starts": transition_report(sentence_list),
        "acronyms": acronym_report(clean),
        "risk_reporting": risk_signal(clean),
        "number_inventory": sorted(set(NUMBER_RE.findall(clean))),
    }


def render_text(report: dict[str, Any]) -> str:
    metrics = report["metrics"]
    lines = [
        "SciHumanizer diagnostic scan",
        report["notice"],
        "",
        (
            f"Words: {metrics['words']} | Sentences: {metrics['sentences']} | "
            f"Paragraphs: {metrics['paragraphs']} | Mean sentence: "
            f"{metrics['mean_sentence_words']} words"
        ),
        (
            f"Long sentences: {len(report['long_sentences'])} | Long paragraphs: "
            f"{len(report['long_paragraphs'])} | Possible passives: "
            f"{len(report['possible_passives'])}"
        ),
        (
            f"Clutter hits: {len(report['clutter_phrases'])} | AI-coded phrase hits: "
            f"{len(report['ai_coded_phrases'])} | Unique acronyms: "
            f"{report['acronyms']['unique']}"
        ),
        "",
    ]

    sections = (
        ("Long sentences", report["long_sentences"]),
        ("Long paragraphs", report["long_paragraphs"]),
        ("Possible passive constructions", report["possible_passives"]),
        ("Clutter phrases", report["clutter_phrases"]),
        ("AI-coded phrases", report["ai_coded_phrases"]),
        ("Possible nominalizations", report["possible_nominalizations"]),
    )
    for title, items in sections:
        lines.append(title + ":")
        if not items:
            lines.append("  None detected.")
        else:
            for item in items[:20]:
                detail = item.get("snippet") or f"{item.get('term')}: {item.get('count')}"
                lines.append("  - " + str(detail))
        lines.append("")

    undefined = report["acronyms"]["possibly_undefined"]
    lines.append("Possibly undefined acronyms:")
    lines.append("  " + (", ".join(undefined) if undefined else "None detected."))
    lines.append("")
    if report["risk_reporting"]["review_needed"]:
        lines.append("Risk reporting review: relative language appears without an obvious absolute-risk expression.")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", help="UTF-8 plain text/Markdown/LaTeX file, or - for stdin")
    parser.add_argument("--json", action="store_true", help="emit structured JSON")
    parser.add_argument("--long-sentence", type=int, default=35, help="diagnostic word threshold (default: 35)")
    parser.add_argument("--long-paragraph", type=int, default=180, help="diagnostic word threshold (default: 180)")
    args = parser.parse_args()

    try:
        text = read_text(args.file)
    except (OSError, UnicodeError) as exc:
        parser.error(str(exc))

    report = analyze(text, args.long_sentence, args.long_paragraph)
    if args.json:
        json.dump(report, sys.stdout, indent=2, ensure_ascii=False)
        sys.stdout.write("\n")
    else:
        sys.stdout.write(render_text(report))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
