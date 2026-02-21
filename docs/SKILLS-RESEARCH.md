# Skills research: review, commit, and related

Short research summary on adding **review** and **commit** (and similar) skills to the agent.

---

## Review skill

### Why the review skill helps

- Best practice is to treat agent output like a PR: review the diff before committing ([Cursor agent best practices](https://cursor.com/blog/agent-best-practices)).
- Review in a **fresh context** (e.g. separate chat or “review this diff”) reduces confirmation bias ([Agentic Coding – Reviewing code](https://agenticoding.ai/docs/practical-techniques/lesson-9-reviewing-code)).
- Structured checklists (architecture, code quality, maintainability, tests, docs) improve consistency and catch issues before commit.

**What a “review” skill can do**

- **Input**: Staged changes, or “review my changes for issue #N”, or “review the last implementation”.
- **Process**: Compare diff to issue (scope, acceptance criteria), then run through a short checklist: architecture/design, style/conventions, tests, docs, and any project-specific rules.
- **Output**: Short pass/fail + list of concerns and concrete suggestions (no need to run tools; the agent can read the diff and code).
- **Boundary**: Review only; no edits. User (or a follow-up “implement”) applies fixes.

**Recommendation**: Add a **review** skill so the agent has a single, repeatable procedure for “review before commit” or “review this diff”.

---

## Commit skill

### Why the commit skill helps

- Conventional Commits are already required (commitizen); generating a good first draft from the diff saves time and keeps messages consistent.
- Many tools (e.g. [Commit](https://commit.dev), [Git AI](https://github.com/dracondev/git-ai-committer)) generate commit messages from staged diff; a skill encodes the same workflow for the in-IDE agent.
- Including “Fixes #N” in the body closes issues and keeps traceability.

**What a “commit” skill can do**

- **Input**: Staged (or unstaged) diff; optionally issue number.
- **Process**: Summarize changes, pick type (feat/fix/docs/chore/etc.), write a short subject and optional body with “Fixes #N” if applicable.
- **Output**: Suggested Conventional Commit message only. Remind user to run `uv run pre-commit run --all-files` (or pre-commit install) before committing.
- **Boundary**: **Suggest only**; do not run `git add` or `git commit` for the user (avoids accidental commits and keeps control with the user).

**Recommendation**: Add a **commit** skill that suggests a commit message and pre-commit reminder; user copies and runs git themselves.

---

## Other skills considered

- **refactor** – Could be “refactor for clarity/style” with a small checklist. Partially covered by **plan** + **implement-from-issue**; add later if you want a dedicated refactor flow.
- **docs** – “Update docs for this change” (README, docstrings, CHANGELOG). Could be a separate skill or folded into **implement-from-issue** (e.g. “and update docs if needed”). Optional.
- **test** – “Add or extend tests for X.” Largely covered by **implement-from-issue** (acceptance criteria → tests). Optional unless you want a “tests only” workflow.

---

## Summary

| Skill        | Purpose                                        | Status      |
| ------------ | ----------------------------------------------- | ----------- |
| **review**   | Structured review of changes before commit      | Implemented |
| **commit**   | Suggest Conventional Commit message from diff   | Implemented |
| **refactor** | Refactor for clarity/style, no behavior change | Implemented |
| **docs**     | Update README, docstrings, CHANGELOG           | Implemented |
| **test**     | Add or extend tests only (no new features)      | Implemented |

References: [Agentic Coding – Reviewing code](https://agenticoding.ai/docs/practical-techniques/lesson-9-reviewing-code), [Cursor – Best practices for coding with agents](https://cursor.com/blog/agent-best-practices), [Commit – Usage](https://comit.dev/docs/usage), [Pre-commit and code review prep checklist](https://craftautomata.com/2025/05/22/my-pre-commit-and-code-review-prep-checklist/).
