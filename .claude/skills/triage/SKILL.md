---
name: triage
description: Triages a GitHub issue: classify, check completeness, suggest labels and next steps. Use when the user asks to triage, review, or assess an issue (or open issues).
---

# Triage issue

Use when the user asks to **triage** an issue (or “review this issue,” “assess open issues”). Triage = classify, check if ready for implementation, and suggest labels or follow-up.

**Note**: GitHub offers an [AI-powered issue intake](https://docs.github.com/en/issues/tracking-your-work-with-issues/administering-issues/triaging-an-issue-with-ai) (triggered by label `request ai review`). This skill is for **agent-driven triage** in Cursor (e.g. “triage #5” or “which issues are ready to implement?”).

## Steps

1. **Get the issue(s)**
   From the user (number, link) or via MCP/list — e.g. “triage #12” or “triage open issues.”

2. **Classify**
   - **Task** – feature, improvement, refactor. Has or can have summary + acceptance criteria.
   - **Bug** – something broken. Has or can have description + steps to reproduce.
   - **Question** – clarification, discussion, or “how do I…?” (not yet actionable as task/bug).
   - **Other** – duplicate, invalid, wontfix, or out of scope. Say why.

3. **Check completeness**
   - **Task**: Summary clear? Acceptance criteria present and testable? If vague, mark “needs clarification” and suggest concrete criteria.
   - **Bug**: Description (expected vs actual)? Steps to reproduce? Environment/version useful? If missing, mark “needs more info” and list what’s needed.

4. **Suggest labels** (if the repo uses them)
   Template defaults: `task`, `bug`. Optional labels to suggest when useful:
   - `needs-triage` – not yet triaged (remove after triage).
   - `question` – needs discussion or clarification.
   - `good first issue` – only if well-scoped and documented.
   - `help wanted` – open for contributors.
   - `duplicate` / `wontfix` / `invalid` – with brief reason.

5. **Recommend next step**
   - **Ready for implement** – scope and acceptance criteria clear; can use **implement-from-issue**.
   - **Needs clarification** – list what to ask the author.
   - **Needs more info** (bugs) – list missing repro/environment details.
   - **Close** – duplicate, invalid, or wontfix; state reason.

## Output

Summarize in a short reply: **Type** | **Completeness** (ready / needs clarification / needs more info) | **Suggested labels** | **Next step**. If the user wants, you can draft a comment for the issue (e.g. “Could you add acceptance criteria?” or “Looks like #7, possible duplicate?”).

## Optional: GitHub AI intake

For automation, the repo can enable GitHub’s “AI assessment comment labeler” and use the label `request ai review` on issues. That runs in GitHub Actions; this skill is for on-demand triage in the IDE.
