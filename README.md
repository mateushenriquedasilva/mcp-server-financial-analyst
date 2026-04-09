# MCP Server - Financial Analyst

Servidor MCP (Model Context Protocol) construído com FastMCP para consultas financeiras usando Yahoo Finance (`yfinance`).

## Visao Geral

Este projeto expoe capacidades financeiras via MCP:

- Tool: `get_stock_price(ticker)`
- Resource: `stock://{ticker}`
- Prompt: `financial_report(ticker)`

Com isso, um cliente MCP pode consultar preco de acao em tempo real, ler um recurso estruturado com dados basicos e gerar um pequeno relatorio financeiro.

## Estrutura

```text
mcp_server/
  main.py
  requirements.txt
  utils/
    mcp_utils.py
```

## Requisitos

- Python 3.10+
- Dependencias em `requirements.txt`

## Instalacao

1. Crie e ative um ambiente virtual:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Instale as dependencias:

```powershell
pip install -r requirements.txt
```

## Execucao

Com o ambiente ativo:

```powershell
fastmcp run main.py
```

Se o comando `fastmcp` nao estiver no PATH, use:

```powershell
python -m fastmcp run main.py
```

## API MCP Disponivel

### Tool

- Nome: `get_stock_price`
- Entrada: `ticker: str`
- Saida: `float`

Exemplo de ticker: `AAPL`, `MSFT`, `PETR4.SA`.

### Resource

- URI template: `stock://{ticker}`
- Retorna JSON com campos como:
  - `ticker`
  - `currentPrice`
  - `previousClose`
  - `open`
  - `dayHigh`
  - `dayLow`

### Prompt

- Nome: `financial_report`
- Entrada: `ticker: str`
- Retorna texto curto com nome da empresa, setor, industria e preco atual.

## Arquivo Utilitario

`utils/mcp_utils.py` contem uma classe utilitaria para inicializar sessao MCP via SSE e interagir com tools/resources/prompts do servidor.

## Observacoes

- Os dados dependem da disponibilidade da API do Yahoo Finance.
- Alguns tickers podem nao retornar `currentPrice` dependendo do mercado e horario.
