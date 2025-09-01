import yfinance as yf
import pandas as pd

# List of stock symbols
symbols = [
    'TCS.NS','INFY.NS','HDFCBANK.NS','BAJAJ-AUTO.NS','ADANIGREEN.NS',
    'TATASTEEL.NS','ITC.NS','SBILIFE.NS','HDFCLIFE.NS',
    'TATAPOWER.NS','ICICIBANK.NS','YESBANK.NS','KOTAKBANK.NS',
    'AXISBANK.NS','INDUSINDBK.NS','SBIN.NS'
]

all_data = []

for symbol in symbols:
    # Download last 6 months daily data
    df = yf.download(symbol, period="6mo", interval="1d", auto_adjust=False)
    df.reset_index(inplace=True)            # Make Date a column
    df = df[['Date', 'Close']]             # Keep only Date and Close
    df['Symbol'] = symbol                  # Add Symbol column
    df = df[['Date', 'Symbol', 'Close']]   # Reorder columns
    all_data.append(df)

# Combine all dataframes into long format
final_df = pd.concat(all_data, ignore_index=True)

# Save to CSV
final_df.to_csv("all_stocks_close_long.csv", index=False)

