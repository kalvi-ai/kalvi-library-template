---
name: debug
description: Reproduce, isolate, and fix failures (tests, runtime errors, CI). Use when the user reports failing tests, an error, or "why does X happen?"
---

# Debug / investigate

Use when the user says **tests are failing**, **this errors**, **why does X happen?**, or **reproduce this bug**. Follow a structured loop: reproduce → isolate → hypothesize → verify.

## Input

- **Symptom**: Failing test name, error message, traceback, or short description (e.g. "import fails after adding Y").
- **Context** (if any): What changed recently, branch, or how to run the failing case.

## Steps

1. **Reproduce**
   - Run the failing command (e.g. `uv run pytest`, or the exact test path/user flow).
   - Capture the full error output (traceback, assertion message, exit code). If the user already pasted it, use that and optionally re-run to confirm.

2. **Isolate**
   - Identify the minimal failing case: one test, one function, or one code path.
   - If the failure is broad, narrow it (e.g. run a single test with `-k`, or comment out code to find the minimal repro). Check recent diffs or recent commits if "it worked before."

3. **Hypothesize**
   - From the traceback or failure message, identify the likely cause (wrong type, missing import, bad state, env difference, dependency version, etc.).
   - Inspect the relevant code (and tests) at the failure point.

4. **Fix and verify**
   - Propose or apply a fix (code or test or config). Re-run the failing command to confirm it passes.
   - Run **run-quality-checks** (or at least `uv run pytest` and `uv run ruff check src tests scripts`) so the fix doesn’t break anything else.

## Output

- State what was wrong and what changed.
- If the fix is non-obvious, add a one-line comment or doc note where it helps.

## Boundaries

- Do not change behavior beyond what’s needed to fix the failure unless the user asks.
- If the failure is flaky or environment-specific, say so and suggest how to make it reproducible (e.g. pin a version, add a test).
