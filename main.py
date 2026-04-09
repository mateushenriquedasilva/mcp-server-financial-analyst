from fastmcp import FastMCP
from fastmcp.prompts import Message
import json
import yfinance as yf

mcp = FastMCP("Financial Analyst")

@mcp.tool()
def get_stock_price(ticker: str) -> float:
    """Fetches the current stock price for a given ticker symbol using yfinance."""

    try: 
        stock = yf.Ticker(ticker)
        price = stock.info.get("currentPrice")
        if price is None:
            raise ValueError(f"Could not fetch price for ticker: {ticker}")
        return price
    except Exception as e:
        raise ValueError(f"Error fetching stock price for {ticker}: {e}")
    
@mcp.resource("stock://{ticker}")
def get_stock_resource(ticker: str) -> str:
    """Return basic information about a stock."""
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        payload = {
            "ticker": ticker,
            "currentPrice": info.get("currentPrice"),
            "previousClose": info.get("previousClose"),
            "open": info.get("open"),
            "dayHigh": info.get("dayHigh"),
            "dayLow": info.get("dayLow"),
        }
        return json.dumps(payload, ensure_ascii=False)
    except Exception as e:
        raise ValueError(f"Error fetching stock resource for {ticker}: {e}")