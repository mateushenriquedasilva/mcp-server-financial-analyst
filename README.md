# MCP Server Financial Analyst

A FastMCP server for financial analysis using Yahoo Finance data.

## Overview

This project implements an MCP-compatible server that exposes financial analysis capabilities to MCP clients. It uses Python and integrates with Yahoo Finance for market data retrieval.

## Features

- MCP server implementation with FastMCP
- Financial data lookup and analysis tools
- Lightweight Python setup
- Easy integration with MCP-capable clients/editors

## Tech Stack

- Python
- FastMCP
- yfinance

## Project Structure

- `main.py`: MCP server entry point and tool definitions
- `requirements.txt`: Python dependencies
- `README.md`: setup and usage documentation

## Prerequisites

- Python 3.10+
- pip

## Getting Started

1. Clone the repository:

```bash
git clone https://github.com/mateushenriquedasilva/mcp-server-financial-analyst.git
cd mcp-server-financial-analyst
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the MCP server:

```bash
python main.py
```

## Example Use Cases

- Fetch current stock prices by ticker
- Build higher-level financial assistant workflows
- Integrate portfolio insights into MCP clients

## Next Steps

- Add more financial indicators and analytics tools
- Add caching/rate-limit handling
- Add automated tests for tool behavior

## License

This project is available under the repository license terms.
