"""Behavioral checks for the read-only scientific prose scanner."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills" / "sci-humanizer" / "scripts" / "diagnose.py"
SPEC = importlib.util.spec_from_file_location("diagnose", SCRIPT)
diagnose = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(diagnose)


class DiagnoseTests(unittest.TestCase):
    def scan(self, text: str) -> dict:
        return diagnose.analyze(text, long_sentence=35, long_paragraph=180)

    def test_staged_openers_and_closers_with_typographic_apostrophes(self):
        text = "Here’s the thing. Let’s dive in. The estimate was 1.20. Let that sink in."
        report = self.scan(text)
        phrases = {hit["phrase"] for hit in report["ai_coded_phrases"]}
        self.assertEqual(phrases, {"here's the thing", "let's dive in", "let that sink in"})
        opener = next(hit for hit in report["ai_coded_phrases"] if hit["phrase"] == "here's the thing")
        self.assertIn("Here’s the thing", opener["snippet"])
        self.assertIn("1.20", " ".join(report["number_inventory"]))

    def test_scientific_associations_and_hedges_are_not_phrase_errors(self):
        text = (
            "Exposure was associated with fatigue. Residual confounding may explain "
            "the finding. The adjusted model used robust regression. Perhaps the "
            "association differs by age; the available evidence is uncertain."
        )
        report = self.scan(text)
        self.assertEqual(report["ai_coded_phrases"], [])
        self.assertIn("human judgment", report["notice"])
        self.assertNotIn("ai_probability", report)

    def test_code_and_link_targets_do_not_create_phrase_hits(self):
        text = (
            "The command is `let that sink in`.\n\n"
            "```text\nHere’s the thing.\nLet’s dive in.\n```\n\n"
            "Read the [protocol](https://example.org/let-that-sink-in)."
        )
        self.assertEqual(self.scan(text)["ai_coded_phrases"], [])

    def test_phrase_boundaries_do_not_match_inside_longer_words(self):
        self.assertEqual(
            diagnose.phrase_hits("pseudopivotal unpivotality", ("pivotal",)), []
        )

    def test_json_cli_reads_current_file_without_modifying_it(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "manuscript.md"
            source.write_text("Let that sink in. The estimate was 1.20.\n", encoding="utf-8")
            before = source.read_bytes()
            result = subprocess.run(
                [sys.executable, str(SCRIPT), str(source), "--json"],
                capture_output=True, text=True, check=True,
            )
            report = json.loads(result.stdout)
            self.assertEqual(source.read_bytes(), before)
            self.assertEqual(report["ai_coded_phrases"][0]["phrase"], "let that sink in")
            self.assertIn("number_inventory", report)
            self.assertIn("risk_reporting", report)
            self.assertIn("possible_passives", report)

    def test_stdin_text_mode_keeps_diagnostic_notice(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "-"], input="The estimate may differ by age.",
            capture_output=True, text=True, check=True,
        )
        self.assertIn("Diagnostic signals require human judgment", result.stdout)
        self.assertIn("not errors or proof of AI authorship", result.stdout)

    def test_evaluation_fixture_paths_exist(self):
        cases = json.loads((ROOT / "tests" / "evals.json").read_text())
        for case in cases["evals"]:
            for path in case["files"]:
                with self.subTest(case=case["id"], path=path):
                    self.assertTrue((ROOT / path).is_file())


if __name__ == "__main__":
    unittest.main()
