# Generic agent rules: Cursor, Zed, Warp, Codex, Claude, and portable instructions

Research on making project rules work across Cursor, Zed, OpenAI Codex, Claude Code, Gemini CLI, and other coding agents without maintaining duplicate instruction sets. Includes how to keep “skills” and modular rules clean per tool.

---

## 1. How each tool reads rules

### Cursor

- **Location**: `.cursor/rules/*.mdc` (YAML frontmatter + Markdown body).
- **Format**: Cursor-specific: `description`, `globs`, `alwaysApply`, `tags`, etc. Rules are injected into model context; activation can be automatic or by glob.
- **Skills**: `.cursor/skills/*/SKILL.md` — workflow procedures (implement-from-issue, commit, release, etc.). Cursor-only.
- **Other**: Cursor can use project docs; AGENTS.md is often linked from README or rules but is not automatically the single source of truth for Cursor’s rule engine.

### Zed

- **Location**: One **project-level rules file** at the repo root. Zed **auto-includes** the first file it finds from a fixed priority list.
- **Priority order** (first match wins):
  `GEMINI.md` → `CLAUDE.md` → **`AGENTS.md`** → `AGENT.md` → `.github/copilot-instructions.md` → `.clinerules` → `.windsurfrules` → `.cursorrules` → `.rules`.
- **Format**: Plain text/Markdown. No required schema. Content is included in every Agent Panel interaction.
- **Implication**: If you have **AGENTS.md** at the root, Zed uses it (unless GEMINI.md or CLAUDE.md exist). Zed does **not** read `.cursor/rules/*.mdc` or `.cursor/skills/`.

### OpenAI Codex

- **Location**: `AGENTS.md` at repo root (and optionally `AGENTS.override.md` in nested dirs). Global: `~/.codex/AGENTS.md` (or `CODEX_HOME`).
- **Format**: Plain Markdown. Codex concatenates from root down; closer directories override. Size limit ~32 KiB by default (`project_doc_max_bytes`). Fallback filenames configurable via `project_doc_fallback_filenames` (e.g. add `CLAUDE.md`).
- **Skills**: No separate “skills” — everything is in the AGENTS.md chain.

### Claude Code

- **Location**: **`CLAUDE.md`** at project root (case-sensitive). Also: `.claude/rules/*.md` (modular rules), `CLAUDE.local.md` (gitignored), `~/.claude/CLAUDE.md` (global).
- **Format**: Plain Markdown. Claude does **not** yet support `AGENTS.md` natively (feature request exists); it looks for `CLAUDE.md`.
- **Skills / modular rules**: **`.claude/rules/*.md`** — separate files, auto-loaded. Optional YAML frontmatter with `paths: "src/**/*.py"` for path-specific rules. Keeps context focused and scalable.

### Gemini CLI

- **Location**: Default **`GEMINI.md`**; configurable via `.gemini/settings.json`: `"context": { "fileName": ["AGENTS.md", "GEMINI.md"] }`.
- **Format**: Plain Markdown. Can reference other files with `@file.md` in context.
- **Skills**: No separate skills; single context file (or list).

### Aider

- **Location**: Any file you pass with `--read` or in `.aider.conf.yml` (e.g. `read: AGENTS.md`).
- **Format**: Plain Markdown. No required filename; AGENTS.md is the common choice.

### Warp (warp.dev)

- **Location**: **`AGENTS.md`** at repo root (or **`WARP.md`** for backwards compatibility). Filename must be **all caps** (`AGENTS.md`, not `agents.md`) for Warp to recognize it. Can also place `AGENTS.md` in subdirectories for monorepo-specific guidance.
- **Format**: Plain Markdown. Warp prepends project rules to every prompt. No required schema.
- **Precedence**: Global Rules (Warp Drive) → root `AGENTS.md` → current subdirectory `AGENTS.md`. When editing files in another subdirectory, Warp makes a best-effort attempt to include that subdirectory’s rules file.
- **Other**: Warp can link existing rule files to `AGENTS.md`; it also recognizes `CLAUDE.md`, `.cursorrules`, `AGENT.md`, `GEMINI.md`, `.clinerules`, `.windsurfrules`, `.github/copilot-instructions.md` for migration or compatibility. Default and recommended is `AGENTS.md`.
- **Implication**: A single **AGENTS.md** at root works for Warp with no extra file. Same canonical file as Codex, Aider, Zed (when no CLAUDE/GEMINI).

### AGENTS.md (open format)

- **Steward**: [agents.md](https://agents.md/), Agentic AI Foundation (Linux Foundation). Used by Cursor, Zed, Aider, Windsurf, Copilot, Codex, Jules, and others.
- **Format**: **Plain Markdown** at repo root. Conventional sections (no rigid schema): Build & Test, Code style, Project overview, PR/commit guidelines, Security, Dev environment tips, etc.
- **Monorepos**: Nested `AGENTS.md` per package; “nearest file wins.”
- **Benefits**: One file, human-readable, parseable by many agents, no tool-specific syntax.

---

## 2. Best practices for portable rules

### Use AGENTS.md as the canonical instruction set

- Put **all** agent-relevant content (commands, paths, workflow, conventions, links to principles/decisions/specs) in **AGENTS.md** at the project root.
- Use **conventional section headings** (e.g. “## Build & Test”, “## Code style”, “## Key paths”) so different agents can find the same information.
- Keep it **concise and actionable** (e.g. under ~150 lines if possible); link to `docs/` for long content.

### Keep Cursor rules thin and referential

- **Do not duplicate** the same instructions in both AGENTS.md and `.cursor/rules/*.mdc`; duplication drifts.
- Use **.mdc for Cursor-only behavior**: activation (`alwaysApply`), `globs`, and a **short pointer** to AGENTS.md (e.g. “Project context and commands: see [AGENTS.md](AGENTS.md). Summary: …” with 1–3 bullets).
- Optionally keep a **minimal summary** in the rule so Cursor still gets quick context without re-reading AGENTS.md every time; the source of truth remains AGENTS.md.

### One canonical file, multiple filenames (symlinks)

- **Codex, Aider, Gemini (when configured), Zed** (if no CLAUDE/GEMINI) use **AGENTS.md**.
- **Claude Code** only looks for **CLAUDE.md** (no native AGENTS.md yet).
- **Zed** checks **GEMINI.md** and **CLAUDE.md** before AGENTS.md; **Gemini CLI** defaults to **GEMINI.md**.
- **Clean approach**: Keep **AGENTS.md** as the only file you edit. Add **CLAUDE.md** and optionally **GEMINI.md** as **symlinks** to AGENTS.md: `ln -sf AGENTS.md CLAUDE.md` and `ln -sf AGENTS.md GEMINI.md`. Then every tool gets the same content; no duplication. Commit the symlinks (Git stores them; Windows may need developer mode or a note in README). If symlinks are awkward (e.g. Windows without symlink support), document “Claude users: copy AGENTS.md to CLAUDE.md” or provide a small script.

### Skills and modular rules: keep tool-specific, document the map

- **Cursor**: `.cursor/skills/` (workflow procedures: implement-from-issue, commit, release, etc.) and `.cursor/rules/*.mdc` (activation, globs). No standard way to express “skills” in a portable file; Cursor skills are Cursor-specific.
- **Claude Code**: `.claude/rules/*.md` — modular, optional `paths:` in frontmatter for path-specific rules. Content can **point to AGENTS.md** (“Implementation: get scope from issue; run tests before done. Full commands and paths: see [AGENTS.md](../AGENTS.md).”) so you don’t duplicate the full instruction set. Add one or two small rules (e.g. `implementation.md`, `testing.md`) that summarize workflow and link to AGENTS.md.
- **Codex / Gemini / Aider**: No separate “skills”; they only have the main context file (AGENTS.md or CLAUDE.md / GEMINI.md). Workflow is described inside that file.
- **Clean approach**: (1) Put **workflow and commands** in **AGENTS.md** so every agent gets them. (2) **Cursor**: keep `.cursor/skills/` and `.cursor/rules/` as today; document in AGENTS.md. (3) **Claude**: optionally add `.claude/rules/` with thin, referential `.md` files (e.g. “Before done: run tests. See AGENTS.md for commands.”) so Claude users get path-specific or modular rules without duplicating AGENTS.md. (4) Don’t try to unify Cursor skills and Claude rules into one format — document in AGENTS.md where each tool’s extra behavior lives.

### Tool-specific add-ons and filenames

- **AGENTS.md** at root = canonical. **CLAUDE.md** and **GEMINI.md** as symlinks to AGENTS.md give Claude and Gemini users the same content without maintaining three files. Zed works with any of the three; Codex and Aider use AGENTS.md (Aider via config).
- **Cursor**: `.cursor/rules/`, `.cursor/skills/`, `.cursor/mcp.json`. Document in AGENTS.md: “Cursor users: see .cursor/rules/ and .cursor/skills/ for Cursor-specific workflows.”
- **Claude**: `.claude/rules/`, `CLAUDE.local.md`. Document: “Claude Code: .claude/rules/ for modular rules; CLAUDE.md at root (or symlink to AGENTS.md).”
- **Codex**: `~/.codex/AGENTS.md`, `project_doc_fallback_filenames` if you use another name.
- **Gemini**: `.gemini/settings.json` with `context.fileName` if you want AGENTS.md.
- **Zed**: Single project rules file (AGENTS.md, CLAUDE.md, or GEMINI.md); Rules Library is local/UI. No extra project files needed.
- **Warp**: **AGENTS.md** at root (all caps); optional per-subdirectory AGENTS.md for monorepos. Global Rules in Warp Drive. No symlink needed for Warp — it uses AGENTS.md natively.
- **MCP, API keys**: Document in AGENTS.md or docs/setup-mcp.md; no need to duplicate in every tool’s config.

---

## 3. Summary

| Goal                         | Practice                                                                 |
| ---------------------------- | ------------------------------------------------------------------------- |
| One instruction set          | Put content in **AGENTS.md**; use conventional Markdown sections.        |
| Codex, Aider, Zed, Warp      | Use **AGENTS.md** at root (Warp requires all-caps filename).              |
| Claude Code                  | **CLAUDE.md** at root (symlink to AGENTS.md so one source of truth).      |
| Gemini / Zed (Gemini first)  | **GEMINI.md** optional symlink to AGENTS.md.                             |
| Cursor                       | **.cursor/rules/*.mdc** for activation/globs only; point to AGENTS.md.     |
| Skills / modular             | **Cursor**: .cursor/skills/; **Claude**: .claude/rules/*.md (thin, link to AGENTS.md). Document in AGENTS.md. |
| Avoid drift                  | Do not duplicate full instructions; symlink or reference AGENTS.md.       |

---

## 4. References

- [Zed – AI Rules (.rules, .cursorrules, AGENTS.md)](https://zed.dev/docs/ai/rules.html)
- [AGENTS.md – open format for AI coding agents](https://agents.md/)
- [Cursor – Rules (context)](https://cursor.com/docs/context/rules)
- [OpenAI Codex – Custom instructions with AGENTS.md](https://developers.openai.com/codex/guides/agents-md/)
- [Claude Code – CLAUDE.md and .claude/rules](https://code.claude.com/docs/) (memory/settings)
- [Gemini CLI – Context with GEMINI.md / AGENTS.md](https://geminicli.com/docs/cli/gemini-md)
- [Aider – Conventions (e.g. read: AGENTS.md)](https://aider.chat/docs/usage/conventions.html)
- [Claude Code issue: Support AGENTS.md](https://github.com/anthropics/claude-code/issues/6235)
- [Warp – Rules (Project Rules in AGENTS.md)](https://docs.warp.dev/agent-platform/capabilities/rules)
