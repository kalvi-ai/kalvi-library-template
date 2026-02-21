# Project grounding: constitution, architecture, patterns, conventions, ADRs

Deep research on **project-level documentation** that humans and agents can refer to: constitution/principles, architecture, design patterns, conventions, and Architecture Decision Records (ADRs). Focus is on structure, single source of truth, and how to make it referable.

---

## 1. Project constitution and principles

### What it is

A **project constitution** (or **engineering principles**) is a small set of high-level rules that govern how the project is built and maintained: quality bar, testing, structure, and "how we work." It answers "what must always be true" rather than implementation details.

### Formats and sources

**Principles.dev format** ([principles.dev/documentation](https://principles.dev/documentation/)):

- **Required**: Principle name, What it is, Why you should use it.
- **Optional**: How to implement, When to use it, Definitions, Exceptions, References.
- Stored as Markdown with optional TOML frontmatter (summary, tags, authors, license). Suited to human-readable docs that agents can parse.

**GitHub Spec-Kit constitution** ([github/spec-kit](https://github.com/github/spec-kit)):

- Created via `/speckit.constitution`; defines governing principles for spec-driven development.
- **Boundary**: Constitution = high-level principles and rules (WHAT/MUST). Specifications = detailed contracts and implementation (HOW).
- Example: "Modules MUST have clear I/O contracts" belongs in constitution; concrete schemas belong in specs.

**John Lewis Partnership, Sourcegraph, Microsoft**:

- Principles live in handbooks or dedicated sites, often grouped by: architecture/design, operations, team/process, software practices.
- Microsoft's Engineering Playbook recommends: repository-specific docs (contributing, design decision log) plus shared project docs (team agreements, definition of done/ready).

### Best practices for referability

- **Short and scannable**: Name + what + why in the first few paragraphs.
- **One principle per concept**: Easier to link and reference.
- **Stable paths**: e.g. `docs/principles.md` or `docs/constitution.md` so agents and links don't break.
- **Avoid vague or aspirational lists**: Prefer "Run tests before commit" over "We value quality."

---

## 2. Architecture documentation

### Frameworks

**arc42** ([arc42.org](https://arc42.org/)):

- Template with 12 sections: Introduction and goals, Constraints, Context and scope, Solution strategy, Building block view, Runtime view, Deployment view, Crosscutting concepts, **Architectural decisions**, Quality requirements, Risks and technical debt, Glossary.
- Fits agile iteration; technology-agnostic. "Crosscutting concepts" and "Architectural decisions" are the main places for patterns and ADRs.

**C4 model** (Context, Containers, Components, Code):

- Hierarchical diagrams; often used **inside** arc42's building block view.
- Complements arc42 for "where things live" and boundaries.

**Single source of truth** (Google, AWS, Azure guidance):

- ADRs are the **decision log**; they are the single source of truth for *why* the architecture looks the way it does.
- Store ADRs with the codebase or in a unified docs repo; treat as append-only (supersede with new ADRs rather than editing old ones).

### What to document for agent referability

- **Context and scope**: System boundaries, main components, entry points ("see `src/...` for X").
- **Solution strategy**: Key tech choices (language, framework, layout).
- **Crosscutting concepts**: Naming, error handling, logging, patterns that apply everywhere.
- **Pointers**: "Auth lives in `src/auth/`," "API contract in `docs/api/`." Concrete paths help both humans and agents.

---

## 3. Architecture Decision Records (ADRs)

### Purpose

ADRs capture **architecturally significant decisions**: structure, patterns, non-functional requirements, dependencies, interfaces, tooling. They record **what** was decided and **why**, not step-by-step implementation.

### Templates

**MADR (Markdown Architectural Decision Records)** ([adr.github.io/madr](https://adr.github.io/madr/)):

- Lightweight Markdown template. Sections: Context and problem statement, Decision drivers, Considered options, **Decision outcome** (chosen option + justification), Consequences, optional Pros/cons per option, More information.
- Filenames: `NNNN-title-with-dashes.md` (e.g. `0001-use-src-layout.md`). Place under `docs/decisions/` (or `docs/adr/`).
- MADR 4.x focuses on architectural decisions but can still be used for any important decision.

**Y-statement** (compact):

- One-sentence form: "In the context of [context], facing [problem], we decided for [option] and neglected [alternative], to achieve [goal], accepting [consequence], because [rationale]."
- Good for a short summary; often paired with a longer MADR or free-form section.

**Full ADR (AWS/Google/Microsoft style)**:

- Status (Proposed, Accepted, Deprecated, Superseded by ADR-XXX), Date, Context, Decision, Alternatives considered, Consequences, Related decisions, References.

### Lifecycle and storage

- **Append-only**: Once accepted, an ADR is immutable. To change direction, add a new ADR that supersedes the old one; mark the old one "Superseded by ADR-0123."
- **Store in repo**: `docs/decisions/` or `docs/adr/`; link from README or main architecture doc.
- **Index**: Keep an index or TOC (e.g. `docs/decisions/README.md`) listing ADRs by number and title so agents and humans can discover them.
- **Categories** (optional): For large repos, subfolders by area (e.g. `docs/decisions/backend/`, `docs/decisions/ui/`) or by theme; numbers can be per-category.

### Making ADRs agent-referable

- **Stable paths**: e.g. `docs/decisions/0001-use-src-layout.md`.
- **Structured headings**: Context, Decision, Consequences; agents can pull sections by heading.
- **Link from AGENTS.md or rules**: "Architectural decisions: see `docs/decisions/`" so the agent knows where to look.

---

## 4. Conventions and patterns

### Style and coding conventions

- **Single source of truth**: Project-specific style wins over generic (e.g. PEP 8). Consistency inside the project matters most.
- **Document in one place**: e.g. "Code style: see `docs/STYLE.md`" or "Ruff + pyproject.toml; see `.cursor/rules/python.mdc`."
- **Enforce where possible**: Linters, formatters, pre-commit so the doc and the tools stay aligned.

### Project structure and patterns

- **"See X for Y"**: e.g. "Routes in `App.tsx`," "Design tokens in `app/lib/theme/tokens.ts`," "Tests next to code in `tests/`."
- **Good/bad examples**: "Prefer pattern in `components/Foo.tsx`; avoid legacy in `LegacyBar.tsx`." Point to real files.
- **API and contracts**: "API docs in `docs/api/`"; "Use client in `app/api/client.ts`." Reduces guesswork for agents and new contributors.

### What to put where

| Content              | Suggested location        | Referable by |
| -------------------- | ------------------------- | ------------ |
| Principles/constitution | `docs/principles.md` or `docs/constitution.md` | Humans, agents |
| Architecture overview | `docs/architecture.md` or arc42 in `docs/`      | Humans, agents |
| ADRs                 | `docs/decisions/` (MADR or similar)            | Humans, agents |
| Coding/style conventions | `docs/STYLE.md` or CONTRIBUTING + linter config | Humans, agents |
| API/contracts        | `docs/api/` or OpenAPI spec                     | Humans, agents |
| How to contribute    | CONTRIBUTING.md                                | Humans, agents |

---

## 5. Documentation hierarchy (standard layout)

Common pattern:

- **README.md**: Purpose, quick start, links to rest. Entry point for humans and often for agents.
- **CONTRIBUTING.md**: How to contribute, branches, PRs, code of conduct. Linked by GitHub on PR/issue.
- **docs/**:
  - **architecture.md** (or arc42 sections): Context, building blocks, deployment.
  - **decisions/** or **adr/**: ADRs (e.g. MADR).
  - **principles.md** or **constitution.md**: Project principles.
  - **api/**, **recipes/**, **reference/**: As needed.
- **ADR index**: `docs/decisions/README.md` with list of ADRs for discovery.

Avoid duplicating the same rule in many files; link to a single source of truth.

---

## 6. Making it referable for agents

### Principles (from research and practice)

1. **Single source of truth**: Each piece of knowledge lives in one place; other docs link to it.
2. **Stable paths**: Fixed locations (e.g. `docs/decisions/`, `docs/architecture.md`) so references and tools don't break.
3. **Structured Markdown**: Clear headings (Context, Decision, Consequences, etc.); agents can retrieve by section.
4. **Minimal and concrete**: Prefer "Run `uv run pytest` before commit" over "We value testing." Reduces noise and improves agent behavior (see arXiv 2602.11988).
5. **Pointers over prose**: "See X for Y" and "Use Z for W" beat long narrative when the goal is lookup.
6. **Index or TOC**: An index (e.g. `docs/decisions/README.md`, or a "Documentation" section in README) helps agents and humans discover what exists.

### What to avoid

- Long, aspirational principle lists that duplicate the same idea in many ways.
- Scattered conventions (style in README, in CONTRIBUTING, and in a doc); consolidate and link.
- Editing old ADRs instead of superseding with new ones (breaks history and traceability).

---

## 7. Summary: options for this template

| Need                    | Lightweight (this template)     | Heavier (when scaling)                |
| ----------------------- | ------------------------------- | -------------------------------------- |
| Constitution/principles | Short list in `docs/principles.md` or a section in README | Full principles.dev-style or spec-kit constitution |
| Architecture            | README "Layout" + AGENTS.md "Key paths" | arc42 + C4 in `docs/architecture.md`   |
| Decisions              | Optional `docs/decisions/` with MADR; start when first non-obvious decision appears | Full ADR process + index + categories |
| Conventions             | CONTRIBUTING + Ruff/editorconfig + `.cursor/rules` | Dedicated `docs/STYLE.md` + linters    |
| Agent referability      | AGENTS.md points to "Key paths"; rules point to commands and layout | Explicit "Documentation" section linking docs/, decisions/, principles |

For a small library template, **lightweight** is enough: principles in a short doc or README, architecture as "Key paths" + layout, ADRs only when you have meaningful decisions to record. Add structure (arc42, full ADR index, separate constitution file) when the project or team grows.

---

## 8. References

- [MADR – Markdown Architectural Decision Records](https://adr.github.io/madr/)
- [ADR GitHub org (templates, practices)](https://adr.github.io/)
- [Principles.dev – How to write a principle](https://principles.dev/documentation/)
- [GitHub Spec-Kit](https://github.com/github/spec-kit) (constitution vs specification)
- [arc42 – Architecture documentation template](https://arc42.org/)
- [Google Cloud – Architecture decision records](https://docs.cloud.google.com/architecture/architecture-decision-records)
- [AWS – ADR best practices](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/best-practices.html)
- [Microsoft – Maintain an ADR](https://learn.microsoft.com/en-us/azure/well-architected/architect-role/architecture-decision-record)
- [Microsoft Engineering Playbook – Projects and repositories](https://microsoft.github.io/code-with-engineering-playbook/documentation/guidance/project-and-repositories/)
- [Continue – Codebase context for agents](https://docs.continue.dev/customize/context/codebase)
- arXiv 2602.11988 – Evaluating AGENTS.md (minimal, actionable context)
