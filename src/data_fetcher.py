import yfinance as yf

def get_stock_data(ticker: str):
    dados = yf.Ticker(ticker)
    return dados.history(period="1y")

def get_stock_info(ticker: str):
    dados = yf.Ticker(ticker)
    return dados.info
