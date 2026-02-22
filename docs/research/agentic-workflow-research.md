# Agentic workflow: research and recommendations

**Background only.** For the canonical loop and skill chain, use [Agentic workflow (finalized flow)](../agentic-workflow.md). This doc summarizes approaches, compares them, and explains when to adopt heavier options.

---

## 1. Main approaches in the wild

### A. Issues as source of truth (what this template does)

- **Idea**: GitHub Issues hold scope, acceptance criteria, and "why." Agents (and humans) get constraints from issues; no separate spec doc.
- **Pros**: Single place for work items, traceability, prevents "requirements quietly mutating mid-implementation," works with Cursor (and other issue-aware agents).
- **Cons**: Issue text is often informal; not executable; less structure than formal specs.
- **Best for**: Single/small teams, libraries, apps where one issue ≈ one deliverable and acceptance criteria are enough.

### B. Four-phase workflow (Research → Plan → Execute → Validate)

- **Source**: [Agentic Coding](https://agenticoding.ai/docs/methodology/lesson-3-high-level-methodology) and similar operator-minded guides.
- **Idea**: Shift from "craftsman" (reading every line) to "operator" (directing systems, validating architecture).
  - **Research**: Ground the agent in codebase + domain (e.g. code search, docs).
  - **Plan**: Choose "exploration" (solution unclear) vs "exact" (solution clear); write a short execution plan.
  - **Execute**: Supervised (watch and steer) or autonomous (fire-and-forget; real gain is parallel work, not per-task speed).
  - **Validate**: Run code, run tests, check against mental model; iterate or regenerate from better context.
- **Pros**: Reduces drift, scales to "many tasks in parallel," quality via architecture/patterns rather than line-by-line review.
- **Cons**: Needs discipline (planning step, mental model); overkill for trivial fixes.
- **Best for**: Non-trivial features, refactors, and when you want the agent to run with minimal babysitting.

### C. Spec-driven development (SDD)

- **Idea**: Executable specifications are the source of truth; AI generates code, tests, and docs from specs. Phases: Specify → Clarify → Plan → Tasks → Implement.
- **Maturity levels**: Spec-first (spec then discard), spec-anchored (spec maintained with code), spec-as-source (humans edit specs only; code generated).
- **Tooling**: [GitHub spec-kit](https://github.com/github/spec-kit) (`/speckit.constitution`, `/speckit.specify`, `/speckit.plan`, `/speckit.tasks`, `/speckit.implement`), Tessl's spec-driven tile, etc.
- **Pros**: Predictable delivery, less coordination overhead in large/enterprise teams, specs stay in sync (outdated spec → broken build), good for multi-service/API contracts.
- **Cons**: Heavier process; learning curve; more useful when many people/services need to align than for a single library.
- **Best for**: Multi-team or multi-service products, API/contract-first work, and when "executable blueprint" matters more than speed of small iterations.

### D. Context files (AGENTS.md, etc.)

- **Fact**: [Research (arXiv 2602.11988)](https://arxiv.org/html/2602.11988v1) shows repository-level context files (e.g. AGENTS.md) can **reduce** task success and **increase** inference cost when they're long or aspirational.
- **Recommendation from research**: Keep human-written context **minimal and actionable** (e.g. exact commands, real error patterns, production gotchas). Avoid long principle lists and vague "compliance checklist" content; ~200–300 lines of concrete guidance is a suggested ceiling before quality degrades.

### E. Skills and rules (Cursor)

- **Skills**: Encapsulate repeatable workflows (e.g. "run quality checks," "release").
  - **implement-from-issue**: Implement in `src/`, add/update tests; use the issue's "Reference" section (if present) where applicable.
- **Rules**: Project/convention guidance (e.g. Python style, paths).
- **Observation**: In studies, skills/subagents are still used in a "shallow" way (few artifacts per repo); but for a template, a small set of skills (quality checks, release) and rules (layout, commands) is practical and tool-agnostic.

### F. Tooling and simplicity (Ronacher-style)

- **Ideas**: Prefer simple, fast tools (scripts, Makefile) over complex MCP when possible; tools must be robust to misuse; observability (e.g. logs) so the agent can debug; stable ecosystems and simple code so the agent doesn't get lost.
- **Fits**: Any agentic flow; especially important when the agent runs autonomously.

---

## 2. Recommended option for this template

**Best fit: issues-as-source-of-truth + lightweight four-phase + minimal AGENTS.md + skills.**

- **Keep**: GitHub Issues as the single source of scope and acceptance criteria (already in this template). No change of paradigm.
- **Add lightly**:
  - **Plan-before-execute** for non-trivial work: for larger or ambiguous tasks, have the agent (or you) state a short plan (scope, steps, validation) before editing. This can be one paragraph in the issue or a short planning reply; no new tooling required.
  - **Validate**: After implementation, run tests and lint (your existing skills/tasks) and check behavior against the issue's acceptance criteria.
- **AGENTS.md**: Keep it short and actionable (paths, commands, "get scope from the issue," "run checks before done"). Avoid long philosophical or aspirational sections.
- **Skills**: Keep "run-quality-checks" and "release"; they encode your workflow and are the main "skill workflow" the agent should use.

This gives you:

- A single source of truth (issues).
- A light operator loop (plan when it matters → execute → validate with existing commands).
- Evidence-based context (minimal, actionable AGENTS.md).
- Repeatable workflows via skills and tasks, without adopting full SDD or heavy tooling.

---

## 3. When to consider spec-driven development

Consider SDD (and tooling like spec-kit or Tessl) when:

- You have **multiple teams or services** that must share contracts/APIs and you want one executable spec per surface.
- You care about **predictable sprint outcomes** and **onboarding** via specs rather than reverse-engineering from code.
- You're building **product/API-first** and are willing to maintain specs as first-class artifacts.

For a single Python library or a small app, **issues + acceptance criteria + plan-then-execute** is usually enough; you can introduce a "spec-lite" (e.g. one markdown spec per feature with acceptance criteria and API notes) later without full SDD tooling.

---

## 4. Issue triage

**Recommendation: include a triage skill for the agent; optionally use GitHub's AI intake for automation.**

- **Triage** = classify (task / bug / question), check completeness (summary + acceptance criteria or repro steps), suggest labels, and recommend next step (ready for implement / needs clarification / needs more info). Standard practice (e.g. [Kubernetes issue triage](https://kubernetes.dev/docs/guide/issue-triage)) is to do this so issues are actionable before implementation.
- **Agent triage skill**: When the user says "triage #12" or "which issues are ready?", the agent reads the issue(s), classifies, checks completeness, and suggests labels and next step. Fits "issues as source of truth"—triage keeps the backlog ready for **implement-from-issue**.
- **GitHub's AI-powered issue intake**: [AI assessment comment labeler](https://docs.github.com/en/issues/tracking-your-work-with-issues/administering-issues/triaging-an-issue-with-ai) runs in Actions when the label `request ai review` is applied. Use it for automation; use the **triage** skill for on-demand triage in the IDE.

---

## 5. Summary table

| Approach              | Best for                          | Use in this template        |
|-----------------------|------------------------------------|-----------------------------|
| Issues as source of truth | Libraries, small teams, traceability | **Yes – keep as is**        |
| Four-phase (R→P→E→V)  | Non-trivial features, autonomy     | **Yes – lightweight** (plan then execute when non-trivial) |
| Spec-driven (SDD)     | Multi-team, APIs, enterprise       | **Optional** – adopt when scaling |
| Minimal AGENTS.md     | All                                | **Yes** – short, actionable only |
| Skills / rules        | Repeatable workflows, conventions  | **Yes** – already in place  |
| Simple, fast tools    | Any                                | **Yes** – uv, Ruff, pytest, etc. |
| Issue triage          | Backlog clarity, ready-to-implement | **Yes** – triage skill; optional GitHub AI intake |

---

## 6. References

- [Agentic Coding – Four-phase methodology](https://agenticoding.ai/docs/methodology/lesson-3-high-level-methodology)
- [Armin Ronacher – Agentic coding recommendations](https://lucumr.pocoo.org/2025/6/12/agentic-coding/)
- [Evaluating AGENTS.md (arXiv 2602.11988)](https://arxiv.org/html/2602.11988v1)
- [Spec-driven development & AI agents (Augment)](https://www.augmentcode.com/guides/spec-driven-development-ai-agents-explained)
- [GitHub spec-kit](https://github.com/github/spec-kit)
- [Martin Fowler – Spec-driven development tools (Kiro, spec-kit, Tessl)](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html)
