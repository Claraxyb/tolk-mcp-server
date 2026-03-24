# 🏺 TON Tolk Compiler MCP Server
**ID:** FOOTSTEP-CLARA-001 | **Status:** Production-Ready

A professional **Model Context Protocol (MCP)** server for the **Tolk compiler**, designed to bridge the gap between AI coding assistants (Claude, Cursor, Windsurf) and the modern TON smart contract ecosystem.

## 🏛️ Vision
To accelerate TON development, AI agents must have native, real-time access to official compilers. This server provides a seamless interface for AI to compile, convert, and verify Tolk contracts without manual terminal intervention.

## 🛠️ Integrated Tools

- **`compile_tolk`**: Compiles `.tolk` source files directly into TON bytecode JSON using the official `@ton/tolk-js` WASM compiler.
- **`convert_func_to_tolk`**: Automates the evolution from legacy FunC contracts to the modern Tolk architecture.
- **`get_tolk_version`**: Ensures the environment is always aligned with the latest official compiler release via `npx`.

## ⚙️ Prerequisites

- **Python 3.10+** (Core server logic)
- **Node.js 18+** (Required for `@ton/tolk-js` and `@ton/convert-func-to-tolk` via `npx`)

## 🚀 Installation & Setup

1. **Clone the Nexus Repository:**
   ```bash
   git clone https://github.com/Claraxyb/tolk-mcp-server.git
   cd tolk-mcp-server
   ```

2. **Initialize the Environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Claude Desktop Integration:**
   Add this entry to your `claude_desktop_config.json`:
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

## 📜 Technical Philosophy
This server is built on the principle of **Hermetic Precision**—ensuring that every compilation is deterministic and every conversion is transparent. It utilizes the official `@ton` NPM packages to guarantee compatibility with the TON blockchain's core standards.

---
*Architected by Clara Sophia - Dedicated to the growth of the Open Network.*
*,License: MIT*
