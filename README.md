# mcp-tenki
[![smithery badge](https://smithery.ai/badge/mcp-tenki)](https://smithery.ai/server/mcp-tenki)

A MCP server with weather of Japan

<a href="https://glama.ai/mcp/servers/jbl3sfsi9r"><img width="380" height="200" src="https://glama.ai/mcp/servers/jbl3sfsi9r/badge" alt="Tenki MCP server" /></a>

# Setup
### Installing via Smithery

To install MCP Tenki for Claude Desktop automatically via [Smithery](https://smithery.ai/server/mcp-tenki):

```bash
npx -y @smithery/cli install mcp-tenki --client claude
```

```
$ uv sync
```

# Running Server 


Run without clone

```json: {{.HOME}}/Library/Application\ Support/Claude/claude_desktop_config.json
{
    "mcpServers": {
        "tenki": {
            "command": "uvx",
            "args": ["--from", "git+https://github.com/acxelerator/mcp-tenki.git", "mcp-tenki"]
        }
    }
}
```

Run with clone

```json: {{.HOME}}/Library/Application\ Support/Claude/claude_desktop_config.json
{
    "mcpServers": {
        "tenki": {
            "command": "uv",
            "args": ["--directory", "/PATH/TO/REPOSITORY/mcp-tenki/mcp_tenki", "run", "main.py"]
        }
    }
}
```
