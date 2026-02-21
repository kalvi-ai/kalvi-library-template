# MCP setup (Cursor)

This project uses [Model Context Protocol](https://cursor.com/docs/context/mcp) (MCP) for Cursor agent tools. Config: `.cursor/mcp.json` in the project root. For global config use `~/.cursor/mcp.json`.

## Required

- **GitHub** – Issues as source of truth. Set `GITHUB_TOKEN` in your environment or Cursor Settings → Tools → MCP.

## Optional

- **Exa** – Web and code search. URL: `https://mcp.exa.ai/mcp`. For higher rate limits, set `EXA_API_KEY` (see [Exa MCP](https://docs.exa.ai/reference/exa-mcp)).
- **Context7** – Up-to-date library documentation. URL: `https://mcp.context7.com/mcp`. Set `CONTEXT7_API_KEY` in env or Cursor MCP settings.

## Optimization

- **Single source**: Define servers only in project `.cursor/mcp.json` (or only in global) to avoid duplicates.
- **Disable duplicates**: In Cursor Settings → Tools, if the same server appears twice (e.g. from project + global), disable one to reduce token cost and clutter.
- **Few servers**: Keep only high-value servers; extra MCP servers add static context cost.

Do not commit API keys; use environment variables or Cursor’s MCP settings.
