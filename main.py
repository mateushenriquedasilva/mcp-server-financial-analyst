from fastmcp import FastMCP
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
    
@mcp.prompt()
def financial_report(ticker: str) -> str:
    """Generate a financial report for a given stock ticker."""
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        report = f"Financial Report for {ticker}:\n"
        report += f"Company Name: {info.get('longName')}\n"
        report += f"Sector: {info.get('sector')}\n"
        report += f"Industry: {info.get('industry')}\n"
        report += f"Current Price: {info.get('currentPrice')}\n"
        return report
    except Exception as e:
        raise ValueError(f"Error generating financial report for {ticker}: {e}")