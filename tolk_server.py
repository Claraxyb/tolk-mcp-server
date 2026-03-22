# tolk_mcp_server/tolk_server.py
"""
TON TOLK COMPILER MCP SERVER
----------------------------
Detta är en officiell MCP-server för Tolk-kompilatorn på TON.
Byggd för att underlätta för AI-assistenter att arbeta med TON smarta kontrakt.
"""

from fastmcp import FastMCP
import subprocess
import os
import sys
import json

# Initialize the MCP server
mcp = FastMCP("TON Tolk Compiler Server")

@mcp.tool()
def compile_tolk(file_path: str) -> str:
    """
    Kompilerar en Tolk-fil (.tolk) till TON smart contract bytecode (JSON-format).
    Kräver att filen existerar lokalt.
    """
    if not os.path.exists(file_path):
        return f"FEL: Filen {file_path} hittades inte."

    try:
        # Vi använder npx för att hämta och köra den officiella tolk-js kompilatorn
        print(f"  [TOLK-MCP] Compiling {file_path}...", file=sys.stderr)
        
        # Kommandot npx @ton/tolk-js laddar ner och kör den officiella WASM-kompilatorn
        result = subprocess.run(
            ["npx", "-y", "@ton/tolk-js", "--output-json", "output.json", file_path],
            capture_output=True,
            text=True,
            check=True
        )
        
        # Läs resultatet om det finns
        if os.path.exists("output.json"):
            with open("output.json", "r") as f:
                compilation_data = json.load(f)
            return f"KOMPILERING LYCKADES: Resultat sparat i output.json. (Storlek: {len(str(compilation_data))} bytes)"
        
        return "KOMPILERING LYCKADES: Men ingen output.json hittades."

    except subprocess.CalledProcessError as e:
        error_msg = e.stderr or e.stdout
        return f"KOMPILERING MISSLYCKADES:\n{error_msg}"
    except Exception as e:
        return f"OVÄNTAT FEL: {str(e)}"

@mcp.tool()
def convert_func_to_tolk(input_path: str) -> str:
    """
    Konverterar befintliga FunC-kontrakt eller mappar till det nya Tolk-formatet.
    """
    try:
        print(f"  [TOLK-MCP] Converting {input_path} from FunC to Tolk...", file=sys.stderr)
        result = subprocess.run(
            ["npx", "-y", "@ton/convert-func-to-tolk", input_path],
            capture_output=True,
            text=True,
            check=True
        )
        return f"KONVERTERING SLUTFÖRD:\n{result.stdout}"
    except subprocess.CalledProcessError as e:
        return f"KONVERTERING MISSLYCKADES:\n{e.stderr}"

@mcp.tool()
def get_tolk_version() -> str:
    """
    Hämtar den nuvarande versionen av Tolk-kompilatorn.
    """
    try:
        result = subprocess.run(
            ["npx", "-y", "@ton/tolk-js", "--version"],
            capture_output=True,
            text=True,
            check=True
        )
        return f"TOLK VERSION: {result.stdout.strip()}"
    except Exception as e:
        return f"KUNDE INTE HÄMTA VERSION: {str(e)}"

if __name__ == "__main__":
    # Kör servern via stdio-transport för integration med Claude Desktop/Cursor
    mcp.run(transport="stdio")
