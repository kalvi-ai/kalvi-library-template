# Ruler: multi-agent strategy (Gemini, Cursor, Zed, Claude, Trae, Codex, Warp)

Deep research on [Ruler](https://github.com/intellectronica/ruler) (intellectronica/ruler) and a concrete strategy to keep **Gemini CLI, Cursor, Zed, Claude Code, Trae AI, OpenAI Codex, and Warp** in sync for rules, MCP, and skills.

---

## 1. What Ruler does

- **Single source of truth**: You keep all agent instructions in a **`.ruler/`** directory (Markdown files). Ruler concatenates them in a defined order and writes the result to each agent’s expected config file(s).
- **One MCP config**: Define MCP servers once in **`.ruler/ruler.toml`**; Ruler propagates to Cursor (`.cursor/mcp.json`), Zed (`.zed/settings.json`), Codex (`.codex/config.toml`), Claude (`.mcp.json`), Gemini (`.gemini/settings.json`), etc.
- **One skills tree**: Put skills in **`.ruler/skills/<name>/SKILL.md`**; Ruler copies them into each agent’s native skills dir (e.g. `.cursor/skills/`, `.claude/skills/`, `.gemini/skills/`, `.codex/skills/`). Trae, Zed, Warp have no “skills” in Ruler’s model; they only get the rules file.
- **Nested rules**: Optional **nested** `.ruler/` dirs (e.g. per package in a monorepo) with `ruler apply --nested` or `nested = true` in `ruler.toml`.
- **CLI**: `ruler init` (scaffold `.ruler/`), `ruler apply` (distribute), `ruler revert` (undo). Agent selection via `--agents` or `default_agents` in `ruler.toml`.

References: [Ruler README](https://github.com/intellectronica/ruler), [NPM @intellectronica/ruler](https://www.npmjs.com/package/@intellectronica/ruler).

---

## 2. How Ruler maps to your seven agents

| Agent        | Rules output                    | MCP output                 | Skills output      |
| ------------ | ------------------------------- | -------------------------- | ------------------- |
| **Gemini CLI** | `AGENTS.md`                     | `.gemini/settings.json`    | `.gemini/skills/`   |
| **Cursor**   | `AGENTS.md`                     | `.cursor/mcp.json`         | `.cursor/skills/`   |
| **Zed**      | `AGENTS.md`                     | `.zed/settings.json`       | –                   |
| **Claude Code** | `CLAUDE.md`                   | `.mcp.json` (root)         | `.claude/skills/`   |
| **Trae AI**  | `.trae/rules/project_rules.md` | –                          | –                   |
| **Codex**    | `AGENTS.md`                     | `.codex/config.toml`       | `.codex/skills/`    |
| **Warp**     | `WARP.md` (default)             | –                          | –                   |

- **Rule content**: Ruler builds one concatenated body from `.ruler/` (root `AGENTS.md` if present, then `.ruler/AGENTS.md`, then other `.ruler/*.md` in order) and writes it to each agent’s rules path. So one edit in `.ruler/` updates AGENTS.md, CLAUDE.md, .trae/rules/project_rules.md, and WARP.md (same text, different filenames/locations).
- **MCP**: Defined under `[mcp_servers.*]` in `ruler.toml`. Ruler merges (or overwrites) into each tool’s MCP config. Zed gets `context_servers` in `.zed/settings.json` (project root only).
- **Skills**: Only Cursor, Claude, Gemini, and Codex get skills from Ruler in your set. Trae, Zed, Warp do not have a “skills” target in Ruler.

---

## 3. Recommended strategy for your stack

### 3.1 Single source: `.ruler/` and Ruler as the publisher

- **Canonical instructions**: In **`.ruler/AGENTS.md`** (and optionally more `.ruler/*.md`, e.g. `coding_style.md`, `testing.md`). Do **not** maintain separate AGENTS.md, CLAUDE.md, etc. by hand; Ruler generates them from `.ruler/`.
- **Canonical MCP**: In **`.ruler/ruler.toml`** under `[mcp_servers.*]`. Migrate your current `.cursor/mcp.json` (and any other tool MCP) into `ruler.toml` so Ruler can propagate to Cursor, Zed, Codex, Claude, Gemini.
- **Canonical skills**: In **`.ruler/skills/<name>/SKILL.md`**. Ruler will copy them to `.cursor/skills/`, `.claude/skills/`, `.gemini/skills/`, `.codex/skills/`. Your existing `.cursor/skills/` (commit, release, research, etc.) can be moved into `.ruler/skills/` and then removed from version control as generated (or keep committing generated dirs; see below).

### 3.2 Enable only your seven agents

In **`.ruler/ruler.toml`**:

```toml
# Only these agents; case-insensitive substring match
default_agents = ["gemini-cli", "cursor", "zed", "claude", "trae", "codex", "warp"]
```

Or run with an explicit list:

```bash
ruler apply --agents gemini-cli,cursor,zed,claude,trae,codex,warp
```

Optional: make Warp use the same root file as everyone else (no separate WARP.md):

```toml
[agents.warp]
enabled = true
output_path = "AGENTS.md"
```

Then Warp reads `AGENTS.md` like Zed/Codex/Gemini/Cursor; you can delete or ignore `WARP.md`.

### 3.3 Sync and “instructions always in sync”

- **Option A – Commit generated files (recommended for “clone and go”)**
  Run `ruler apply --no-gitignore`. Commit the generated files (AGENTS.md, CLAUDE.md, .cursor/mcp.json, .zed/settings.json, .trae/rules/project_rules.md, .codex/config.toml, .gemini/settings.json, and optionally .cursor/skills/, .claude/skills/, .gemini/skills/, .codex/skills/). Anyone who clones the repo gets the same instructions and MCP without running Ruler. “Sync” = run `ruler apply` when you change `.ruler/` or `ruler.toml`, then commit the diff.
- **Option B – Generated files not committed**
  Keep Ruler’s default `--gitignore` so it adds generated paths to `.gitignore`. Only people who run `ruler apply` (or a post-clone script) get updated rules/MCP/skills. Document: “After clone, run `ruler apply`.”

Recommendation: **Option A** so every agent (Gemini, Cursor, Zed, Claude, Trae, Codex, Warp) works immediately after clone, and instructions stay in sync via git.

### 3.4 Cursor rules (`.cursor/rules/*.mdc`)

Ruler does **not** generate `.cursor/rules/*.mdc`. Cursor uses those for activation and globs. Keep a small set of **hand-maintained** `.cursor/rules/*.mdc` that **point to** the generated AGENTS.md, e.g. “Project context and commands: see [AGENTS.md](AGENTS.md).” So: **content** lives in `.ruler/` and is distributed by Ruler; **Cursor-specific activation** stays in `.cursor/rules/` and stays thin/referential.

### 3.5 Codex and CODEX_HOME

Codex reads MCP from its “home” config. Ruler writes to **`.codex/config.toml`** in the project. So use a project-local Codex home:

```bash
export CODEX_HOME="$(pwd)/.codex"
```

Document this in AGENTS.md (or `.ruler/AGENTS.md`) and in README/setup docs so Codex users get MCP and overrides from the repo.

### 3.6 Skills: one tree in `.ruler/skills/`

- Move (or copy) existing **`.cursor/skills/`** content into **`.ruler/skills/`** with the same structure: e.g. `.ruler/skills/commit/SKILL.md`, `.ruler/skills/release/SKILL.md`, `.ruler/skills/research/SKILL.md`.
- Run `ruler apply` (with `--skills`, which is default). Ruler will populate:
  - `.cursor/skills/`
  - `.claude/skills/`
  - `.gemini/skills/`
  - `.codex/skills/`
- If you use **Option A** (commit generated files), you can either:
  - Let Ruler add `.cursor/skills/`, `.claude/skills/`, etc. to `.gitignore` and **not** commit them (everyone runs `ruler apply` to get skills), or
  - Run `ruler apply --no-gitignore` and **commit** those dirs so they’re in the repo and no one needs to run Ruler for skills.

For maximum “all agents work well” without a post-clone step, committing the generated skill dirs (and using `--no-gitignore` for those paths or overall) is consistent with Option A.

---

## 4. Step-by-step adoption (for this template)

1. **Install Ruler**
   `npm install -g @intellectronica/ruler` (or use `npx @intellectronica/ruler`).

2. **Bootstrap**
   From repo root: `ruler init`. This creates `.ruler/`, `.ruler/AGENTS.md`, `.ruler/ruler.toml`.

3. **Move content into `.ruler/`**
   - Copy or move the current **AGENTS.md** content into **`.ruler/AGENTS.md`** (and split into more `.ruler/*.md` files if you like).
   - Move **MCP** from `.cursor/mcp.json` into **`.ruler/ruler.toml`** as `[mcp_servers.github]`, `[mcp_servers.exa]`, `[mcp_servers.context7]` (and any env/headers). Use Ruler’s TOML format (see Ruler README).
   - Move **skills** from `.cursor/skills/` to **`.ruler/skills/`** (e.g. `commit`, `release`, `research`, … each with `SKILL.md`).

4. **Configure only your seven agents**
   In `.ruler/ruler.toml`: set `default_agents = ["gemini-cli", "cursor", "zed", "claude", "trae", "codex", "warp"]`. Optionally set `[agents.warp] output_path = "AGENTS.md"`.

5. **Apply and commit**
   Run:

   ```bash
   ruler apply --no-gitignore --agents gemini-cli,cursor,zed,claude,trae,codex,warp
   ```

   Commit the generated files (AGENTS.md, CLAUDE.md, .cursor/mcp.json, .zed/settings.json, .trae/rules/project_rules.md, .codex/, .gemini/, and skill dirs if you want them in git). Add a note in README/CONTRIBUTING: “Agent instructions and MCP live in `.ruler/`. After editing them, run `ruler apply --no-gitignore` and commit the changes.”

6. **Keep Cursor rules thin**
   Keep `.cursor/rules/always.mdc` (and others) as short “see AGENTS.md” pointers; do not duplicate long text from `.ruler/`.

7. **Document Codex**
   In `.ruler/AGENTS.md` (or setup docs): set `CODEX_HOME` to the project’s `.codex` so Codex uses the repo’s MCP and config.

---

## 5. Pre-commit and CI

### 5.1 Why add Ruler to pre-commit

- **Sync guarantee**: If you commit generated files (Option A), any commit that touches `.ruler/` should also include the updated AGENTS.md, CLAUDE.md, MCP, and skills. Otherwise the repo is inconsistent (e.g. AGENTS.md out of date with `.ruler/AGENTS.md`).
- **Pre-commit** can run `ruler apply` and then either **check** that generated files are staged, or **apply and stage** them automatically.

### 5.2 Two modes

| Mode | Behavior | Use when |
|------|----------|----------|
| **Check (default)** | Run `ruler apply`; if any generated file is modified or untracked, **fail** and ask the user to stage and commit again. | You want explicit control: developer runs ruler apply, stages, then commits. No automatic staging. |
| **Apply + stage** | Run `ruler apply`, then **stage** all generated paths so the next commit includes them. | You want one-commit workflow: edit `.ruler/`, commit; pre-commit updates and stages generated files. |

This template uses **check mode** by default so the staging area is not changed automatically. To use apply+stage, run `scripts/ruler-pre-commit.sh --stage` before committing (or add a separate hook that calls the script with `--stage`).

### 5.3 What’s in this repo

- **Script**: [scripts/ruler-pre-commit.sh](../../scripts/ruler-pre-commit.sh)
  - Exits 0 if `.ruler/ruler.toml` is missing (repos that don’t use Ruler are unaffected).
  - Runs `npx @intellectronica/ruler apply --no-gitignore --no-backup`.
  - **Check mode**: Fails if any generated path (AGENTS.md, CLAUDE.md, .cursor/mcp.json, .zed/, .trae/, .codex/, .gemini/, .mcp.json, .cursor/skills/, .claude/skills/) is modified or untracked.
  - **Stage mode** (`--stage`): Stages those paths after apply so the next commit includes them.

- **Pre-commit hook**: In [.pre-commit-config.yaml](../../.pre-commit-config.yaml), hook `ruler-apply` runs `bash scripts/ruler-pre-commit.sh` (check mode). No Node/ruler dependency until you create `.ruler/`; then you need `npx` (or global `ruler`) so the hook can run.

### 5.4 CI

In CI, run the same check so that “generated files must match `.ruler/`” is enforced:

```yaml
# Example: add a step when .ruler/ exists
- name: Ruler sync check
  run: |
    if [[ -f .ruler/ruler.toml ]]; then
      npx -y @intellectronica/ruler apply --no-gitignore --no-backup
      git diff --exit-code -- AGENTS.md CLAUDE.md WARP.md .cursor .zed .trae .codex .gemini .mcp.json .claude/skills || (echo "Generated agent files are out of sync with .ruler/. Run ruler apply and commit." && exit 1)
    fi
```

Or run the pre-commit hook (which does the same thing in check mode):

```yaml
- name: Pre-commit (includes ruler check when .ruler/ present)
  run: uv run pre-commit run --all-files
```

### 5.5 Requirements

- **Node.js and npx** (or global `ruler`) are required only when `.ruler/` exists. Document in README/CONTRIBUTING: “If you use Ruler (`.ruler/`), install Node and run `npm install -g @intellectronica/ruler` or rely on `npx` for the pre-commit hook.”

---

## 6. Summary

| Goal                    | Approach                                                                 |
| ------------------------ | ----------------------------------------------------------------------- |
| One place for instructions | **`.ruler/`** (AGENTS.md + any other .md). Ruler writes AGENTS.md, CLAUDE.md, .trae/rules/project_rules.md, WARP.md (or Warp → AGENTS.md). |
| One place for MCP        | **`.ruler/ruler.toml`** `[mcp_servers.*]`. Ruler propagates to Cursor, Zed, Claude, Codex, Gemini. |
| One place for skills     | **`.ruler/skills/`**. Ruler propagates to Cursor, Claude, Gemini, Codex. |
| Only your seven agents   | `default_agents` or `--agents gemini-cli,cursor,zed,claude,trae,codex,warp`. |
| Instructions in sync     | Run `ruler apply` when `.ruler/` or ruler.toml changes; commit generated files (Option A) so clone = ready. |
| Cursor behavior          | Keep `.cursor/rules/*.mdc` as thin pointers to AGENTS.md; Ruler does not generate them. |
| Codex MCP                | Set `CODEX_HOME` to project’s `.codex` and document it.                  |
| Pre-commit / CI          | Use `scripts/ruler-pre-commit.sh` (check mode) in pre-commit; optional CI step to enforce sync. |

This gives you a single source of truth (`.ruler/` + ruler.toml), one command to sync (ruler apply), and consistent rules, MCP, and skills across Gemini, Cursor, Zed, Claude, Trae, Codex, and Warp.

---

## 7. References

- [Ruler – GitHub (intellectronica/ruler)](https://github.com/intellectronica/ruler)
- [Ruler – NPM (@intellectronica/ruler)](https://www.npmjs.com/package/@intellectronica/ruler)
- [Generic agent rules (Cursor, Zed, Warp, Codex, Claude)](generic-agent-rules-cursor-zed.md) – how each tool reads rules without Ruler
