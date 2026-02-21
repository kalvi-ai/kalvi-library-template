#!/usr/bin/env bash
# Ruler pre-commit: run ruler apply when .ruler/ exists, then either check sync or apply+stage.
#
# Usage:
#   scripts/ruler-pre-commit.sh           # check mode: fail if generated files are out of sync
#   scripts/ruler-pre-commit.sh --stage    # apply+stage: run ruler apply and stage generated files
#
# Requires: npx (Node) and @intellectronica/ruler. Skip if .ruler/ruler.toml is missing.
set -e

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

if [[ ! -f .ruler/ruler.toml ]]; then
  exit 0
fi

STAGE_MODE=false
if [[ "${1:-}" == "--stage" ]]; then
  STAGE_MODE=true
fi

# Run ruler apply so generated files are up to date. Use --no-gitignore so we don't modify .gitignore;
# use --no-backup to avoid .bak files in the tree.
npx -y @intellectronica/ruler apply --no-gitignore --no-backup --agents gemini-cli,cursor,zed,claude,trae,codex,warp

# Paths that Ruler may write (for the seven agents: gemini-cli, cursor, zed, claude, trae, codex, warp).
# Used to detect unstaged changes (check mode) or to stage (stage mode).
GENERATED_PATTERN='^(AGENTS\.md|CLAUDE\.md|WARP\.md|\.cursor/mcp\.json|\.cursor/skills/|\.zed/|\.trae/|\.codex/|\.gemini/|\.mcp\.json|\.claude/skills/)'

if [[ "$STAGE_MODE" == true ]]; then
  # Stage generated files that exist and have changes.
  CHANGED=$(git diff --name-only | grep -E "$GENERATED_PATTERN" || true)
  if [[ -n "$CHANGED" ]]; then
    echo "$CHANGED" | xargs git add --
  fi
  # Also stage any new generated files that are untracked.
  UNTRACKED=$(git ls-files --others --exclude-standard | grep -E "$GENERATED_PATTERN" || true)
  if [[ -n "$UNTRACKED" ]]; then
    echo "$UNTRACKED" | xargs git add --
  fi
  exit 0
fi

# Check mode: fail if any generated file is modified or untracked (out of sync with .ruler/).
MODIFIED=$(git diff --name-only | grep -E "$GENERATED_PATTERN" || true)
UNTRACKED=$(git ls-files --others --exclude-standard | grep -E "$GENERATED_PATTERN" || true)

if [[ -n "$MODIFIED" || -n "$UNTRACKED" ]]; then
  echo "Ruler: generated agent files are out of sync with .ruler/." >&2
  echo "Run: npx @intellectronica/ruler apply --no-gitignore" >&2
  echo "Then stage the updated files and commit again." >&2
  if [[ -n "$MODIFIED" ]]; then
    echo "Modified: $MODIFIED" >&2
  fi
  if [[ -n "$UNTRACKED" ]]; then
    echo "Untracked: $UNTRACKED" >&2
  fi
  exit 1
fi

exit 0
