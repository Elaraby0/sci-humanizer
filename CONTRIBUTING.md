# Contributing

Contributions are welcome when they improve scientific clarity without
weakening evidence fidelity.

Before opening a pull request:

1. Keep `SKILL.md` focused on operational instructions; place detailed guidance
   in the relevant file under `references/`.
2. Do not add copyrighted course transcripts, slides, images, or extended
   quotations.
3. Do not add rules that encourage invented facts, citations, statistics, or
   stronger causal language than the evidence supports.
4. Add or update a behavioral case in `tests/evals.json` and, when trigger
   behavior changes, `tests/trigger-evals.json`.
5. Run the local discovery check:

   ```bash
   npx skills add . --list
   ```

Please explain the problem, the proposed behavior, and any scientific-writing
standard that motivates the change.
