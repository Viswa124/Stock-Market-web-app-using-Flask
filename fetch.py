import yfinance as yf


def company_info(ticker):
    ticker = yf.Ticker(ticker)
    return ticker.info
