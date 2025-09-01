import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

# 🔹 Date range
start_date = '2024-01-01'
end_date = (datetime.today() - timedelta(days=1)).strftime('%Y-%m-%d')  # kal tak

# 🔹 List of symbols
symbols = [
    'TCS.NS', 'INFY.NS', 'HDFCBANK.NS', 'BAJAJ-AUTO.NS', 'ADANIGREEN.NS',
    'TATASTEEL.NS', 'ITC.NS', 'SBILIFE.NS', 'HDFCLIFE.NS', 'TATAPOWER.NS',
    'ICICIBANK.NS', 'YESBANK.NS', 'KOTAKBANK.NS', 'AXISBANK.NS', 'INDUSINDBK.NS',
    'SBIN.NS'
]

# 🔹 Empty dataframe to store all corporate actions
all_corporate_actions = pd.DataFrame()

for symbol in symbols:
    stock = yf.Ticker(symbol)
    
    actions = stock.actions.reset_index()
    if actions.empty:
        print(f"No corporate actions found for {symbol}")
        continue
    
    # Filter actions by date
    actions = actions[(actions['Date'] >= start_date) & (actions['Date'] <= end_date)]
    if actions.empty:
        continue
    
    structured_rows = []
    for idx, row in actions.iterrows():
        # Dividend
        if row.get('Dividends', 0) != 0:
            structured_rows.append({
                'Date': row['Date'],
                'Symbol': symbol,
                'CorporateAction': 'Dividend',
                'Value': row['Dividends'],
                'MarketCap': stock.info.get('marketCap', None)
            })
        
        # Split / Bonus
        if row.get('Stock Splits', 0) != 0:
            action_type = 'Bonus' if row['Stock Splits'] > 1 else 'Split'
            structured_rows.append({
                'Date': row['Date'],
                'Symbol': symbol,
                'CorporateAction': action_type,
                'Value': row['Stock Splits'],
                'MarketCap': stock.info.get('marketCap', None)
            })
    df_structured = pd.DataFrame(structured_rows)
    all_corporate_actions = pd.concat([all_corporate_actions, df_structured], ignore_index=True)

# 🔹 Save to CSV
all_corporate_actions.to_csv('All_Corporate_Actions_01Jan2024_Onwards.csv', index=False)

print("All corporate actions from 01/01/2024 to yesterday saved in 'Corporate_Actions_01Jan2024_Onwards.csv'")