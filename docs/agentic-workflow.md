# Agentic workflow (finalized flow)

How the Cursor agent chooses and chains skills. **Source of truth:** GitHub issues; skills in `.cursor/skills/`. The template uses a lightweight **Research → Plan → Execute → Validate** loop; the flows below spell it out. For background and alternatives, see [Agentic workflow (research)](research/agentic-workflow-research.md).

---

## 1. Agent loop (each turn)

Each turn the agent: interprets the user's intent, selects a skill (or slash command), runs it, then either runs the next skill the workflow specifies or stops.

```mermaid
flowchart LR
  subgraph loop ["Agent loop"]
    A[User request] --> B[Interpret intent]
    B --> C[Select skill]
    C --> D[Execute skill]
    D --> E{Next?}
    E -->|next skill| C
    E -->|done| F[Stop]
  end
```

- **Select skill**: Match request to a skill (e.g. "implement #5" → implement-from-issue; "run tests" → run-quality-checks). Use the tables below.
- **Execute skill**: Follow that skill's steps (read issue, edit code, run commands, etc.).
- **Next?**: After the skill, either run the next skill the workflow specifies (see "Skill → next step") or stop.

---

## 2. Main flow: issue → implemented → committed

Full path from "implement this issue" to "commit with approval". Optional steps: triage, research, plan, review.

```mermaid
flowchart TD
  Start([Implement issue]) --> Triage[triage]
  Triage -->|not ready| Stop1([Stop: report])
  Triage -->|ready| Research[optional research]
  Research --> Plan[optional plan]
  Plan --> Implement[implement-from-issue]
  Implement --> Checks[run-quality-checks]
  Checks --> Pass{Pass?}
  Pass -->|no| Implement
  Pass -->|yes| Review[optional review]
  Review --> Commit[commit]
  Commit --> Stop2([Done])
```

- **triage**: Classify issue, check completeness; if not ready, stop and report.
- **(optional) research**: When the issue or approach depends on external APIs, standards, or current best practices.
- **(optional) plan**: Short plan (scope, steps, validation) before coding; use for non-trivial work.
- **implement-from-issue**: Implement in `src/`, add/update tests; use the issue's "Reference" section (if present) where applicable.
- **run-quality-checks**: pytest, Ruff check/format, optionally Pylint/mypy/pre-commit. If fail, fix and re-run checks.
- **(optional) review**: Review changes vs issue and standards; suggest only.
- **commit**: Propose Conventional Commit message; run `git commit` only after explicit user approval.

---

## 3. Plan-only flow

When the user wants a plan only (no code yet). Optional research when the plan depends on external or current knowledge.

```mermaid
flowchart TD
  Start([Plan only]) --> Research[optional research]
  Research --> Plan[plan]
  Plan --> Out([Output: scope, steps, validation])
  Out --> Later([Later: implement-from-issue to run-quality-checks to commit])
```

---

## 4. When to use which skill (and then what)

| User intent | Skill(s) | Then |
|-------------|----------|------|
| Do issue #N / Implement this | **implement-from-issue** | **run-quality-checks** |
| Break this down / Plan this | **plan** | (later) **implement-from-issue** |
| Which issues are ready? / Triage #N | **triage** | If ready → **implement-from-issue**, or optionally **research** → **plan** then **implement-from-issue**. If not → stop. |
| Review my changes / Review before commit | **review** | done, or **commit** if user wants to commit |
| Run tests / lint / verify green | **run-quality-checks** | done |
| Commit / suggest commit message | **commit** | done (after approval) |
| Something broke / tests failing | **debug** | **run-quality-checks** → done or **commit** |
| Update docs for this change | **docs** | done, or **run-quality-checks** then **commit** if code touched |
| Add tests for X | **test** | **run-quality-checks** → done or **commit** |
| Refactor X (no behavior change) | **refactor** | **run-quality-checks** → done or **commit** |
| Maintain library / keep things up to date | **maintain** | propose commit → **commit** if approved |
| Release / publish to PyPI | **release** | done |
| Upgrade dependency X | **dependency-update** | **run-quality-checks** → propose commit → **commit** if approved |
| How healthy is this project? | **project-review** | done (optional: **maintain** or **run-quality-checks** after) |
| Research X / write research doc | **research** | done |

---

## 5. Skill → next step

How to chain after each skill.

| Skill | Typical next step |
|-------|--------------------|
| **triage** | If ready → **implement-from-issue**, or optionally **research** → **plan** then **implement-from-issue**. If not ready → stop. |
| **research** | **plan** or **implement-from-issue** (or stop if standalone). |
| **plan** | (Later) **implement-from-issue**. |
| **implement-from-issue** | **run-quality-checks**. |
| **run-quality-checks** | If pass → **review** (optional) or **commit**. If fail → fix (e.g. **debug**) then **run-quality-checks** again. |
| **review** | **commit** if user wants to commit; else stop. |
| **commit** | Stop (commit runs once after approval). |
| **debug** | **run-quality-checks** then stop or **commit**. |
| **test**, **refactor** | **run-quality-checks** then stop or **commit**. |
| **docs** | If code touched → **run-quality-checks** then stop or **commit**. If docs only → stop. |
| **maintain** | Propose commit → **commit** if user approves. |
| **dependency-update** | **run-quality-checks** → propose commit → **commit** if approved. |
| **release** | Stop. |
| **project-review**, **research**, **bootstrap-from-template** | Stop (or user triggers another flow). |

---

## 6. Optional research

Use the **research** skill when a step depends on external or up-to-date information:

- **Before plan or implement**: Issue vague, or "best practice" / external API / library — run **research** then **plan** or **implement-from-issue**.
- **project-review**: Consult best practices (research + optional write to `docs/research/`).
- **maintain**: When validating docs/deps against current best practices.
- **dependency-update**: When upgrading a major version (changelog/migration).
- **docs**: When documenting an external API or standard.
- **debug**: When the failure is unknown or version-specific (search error message or library behavior).

Do not require research on every task; only when the workflow or issue clearly needs it.

---

## 7. Slash commands

- **`/code-review`**: Run **review** on selected or recent code (suggest only).
- **`/run-quality-checks`**: Run **run-quality-checks** and report pass/fail.

Same skills can be invoked by natural-language request. See [Cursor setup](cursor-setup.md) for more.

---

## 8. One-line summary

**Issue → triage (optional) → research/plan if needed → implement-from-issue → run-quality-checks → review (optional) → commit (with approval) → done.**

All paths and commands: **AGENTS.md** (repo root).
