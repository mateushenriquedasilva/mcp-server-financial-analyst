from fastmcp import FastMCP
from fastmcp.prompts import Message
import yfinance as yf

mcp = FastMCP("Financial Analyst")

@mcp.tool()
def get_stock_price(ticker: str) -> float:
    """"Fetches the current stock price for a given ticker symbol using yfinance."""

    try: 
        stock = yf.Ticker(ticker)
        price = stock.info.get("currentPrice")
        if price is None:
            raise ValueError(f"Could not fetch price for ticker: {ticker}")
        return price
    except Exception as e:
        raise ValueError(f"Error fetching stock price for {ticker}: {e}")