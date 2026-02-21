# MCP setup

This project uses [Model Context Protocol](https://cursor.com/docs/context/mcp) (MCP) for agent tools. Config: [.cursor/mcp.json](../.cursor/mcp.json) (or global `~/.cursor/mcp.json`).

## Required

- **GitHub** – Issues as source of truth. Set `GITHUB_TOKEN` in your environment or Cursor MCP settings.

## Optional (research)

- **Exa** – Web and code search. URL: `https://mcp.exa.ai/mcp`. For higher rate limits, set `EXA_API_KEY` (see [Exa MCP](https://docs.exa.ai/reference/exa-mcp)).
- **Context7** – Up-to-date library documentation. URL: `https://mcp.context7.com/mcp`. Set `CONTEXT7_API_KEY` in env or Cursor MCP settings so the server can authenticate.

Do not commit API keys; use environment variables or Cursor’s MCP settings.
