---
name: plan
description: Produces a short implementation plan (scope, steps, validation) without editing code. Use when the user asks to plan, design, or break down an issue or feature.
---

# Plan (no code changes)

Use this when the user wants a **plan only**—no implementation yet.

## Input

- A GitHub issue (by number or link), or
- A short description of the feature/fix.

## Output

Write a concise plan with:

1. **Scope**
   - What will be changed (files, modules, behavior).
   - What will **not** be changed.

2. **Steps** (2–6 steps)
   - Each step: what to do and where (e.g. “Add `validate_email()` in `src/.../validation.py`, unit tests in `tests/test_validation.py`”).

3. **Validation**
   - How to verify: which tests, which acceptance criteria, any manual checks.

4. **Risks or unknowns** (if any)
   - Ambiguities, dependencies, or decisions that need clarification.

Keep it short (one screen). The user or the agent can then implement using the **implement-from-issue** skill.
