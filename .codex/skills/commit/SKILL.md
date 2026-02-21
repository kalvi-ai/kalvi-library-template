---
name: commit
description: Proposes a Conventional Commit message, then runs git commit after explicit user approval. Use when the user asks to commit, suggest a commit message, or "commit with approval".
---

# Commit (with manual approval)

Use when the user asks to **commit** (e.g. "commit", "suggest a commit message", "commit message for this"). Propose a message first; run `git commit` **only after** the user explicitly approves.

## Input

- Staged diff (preferred), or unstaged/diff the user describes or shares.
- Optionally: issue number (e.g. "for #12") to add "Fixes #12" in the body.
- If the user says "suggest only" or "just the message", stay advisory: output the message only and do not run any git commands.

## Process

### 1. Propose message

1. Summarize what the diff does (files changed, main behavior change).
2. Choose **type**: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`, or `ci`.
3. Write a **subject** line: imperative, lowercase after type, ~50 chars (e.g. `feat: add validation for email input`).
4. If useful, add a **body**: brief explanation and/or "Fixes #N" when there’s an issue to close.
5. Remind: run `uv run pre-commit run --all-files` before committing (and use the commit-msg hook if enabled).

Output the proposed message in Conventional Commits form, then:

**Ask for approval:** "Reply **yes**, **commit**, or **approve** to run `git commit` with this message (only currently staged files). Reply **suggest only** if you only want the message."

### 2. After approval

- If the user replies **yes** / **commit** / **approve** (or equivalent): run `git commit` with the approved message. Use the exact subject and body you proposed (e.g. `git commit -m "subject" -m "body"`). Commit **only** what is already staged; do not run `git add` unless the user explicitly asked to add and commit.
- If there is **nothing staged**: do not run `git commit`. Tell the user: "Nothing staged. Stage files (e.g. `git add <files>`) then ask to commit again."
- If the user does **not** approve: do nothing further; they can copy the message and commit themselves.

## Boundaries

- Do not run `git add` unless the user explicitly asked to "add all and commit" or similar.
- Do not run `git commit` without explicit approval in this flow.
- If the user only wanted a suggestion, they can say "suggest only" and you output the message only.
