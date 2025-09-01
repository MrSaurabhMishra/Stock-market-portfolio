import yfinance as yf
import pandas as pd

# 🔹 List of symbols
symbols = [
    'TCS.NS', 'INFY.NS', 'HDFCBANK.NS', 'BAJAJ-AUTO.NS', 'ADANIGREEN.NS',
    'TATASTEEL.NS', 'ITC.NS', 'SBILIFE.NS', 'HDFCLIFE.NS', 'TATAPOWER.NS',
    'ICICIBANK.NS', 'YESBANK.NS', 'KOTAKBANK.NS', 'AXISBANK.NS', 'INDUSINDBK.NS',
    'SBIN.NS', '^NSEI', '^BSESN'
]

market_caps = []

for symbol in symbols:
    stock = yf.Ticker(symbol)
    info = stock.info
    market_cap = info.get('marketCap', None)  # Latest market cap
    market_caps.append({
        'Symbol': symbol,
        'MarketCap': market_cap
    })

# 🔹 Convert to DataFrame
df_market_cap = pd.DataFrame(market_caps)

# 🔹 Save to CSV
df_market_cap.to_csv('Stocks_MarketCap.csv', index=False)

print("Market cap for all symbols saved in 'Stocks_MarketCap.csv'")
