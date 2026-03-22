# TON Tolk Compiler MCP Server

A professional Model Context Protocol (MCP) server for the **Tolk compiler**, designed to empower AI coding assistants (like Claude Desktop, Cursor, or Windsurf) to seamlessly work with TON smart contracts.

## Features

- **`compile_tolk`**: Compiles `.tolk` source files into TON bytecode JSON using the official `@ton/tolk-js`.
- **`convert_func_to_tolk`**: Automates migration from legacy FunC contracts to the modern Tolk format.
- **`get_tolk_version`**: Verifies the current environment's Tolk compiler version.

## Prerequisites

- **Python 3.10+**
- **Node.js 18+** (for `npx` access to official compilers)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/tolk-mcp-server.git
   cd tolk-mcp-server
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

## Configuration for Claude Desktop

Add the following to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "tolk-compiler": {
      "command": "python3",
      "args": ["/absolute/path/to/tolk-mcp-server/tolk_server.py"]
    }
  }
}
```

## License
MIT
