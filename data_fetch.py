import yfinance as yf
import pandas as pd
import os

def fetch_and_save_data(ticker, start_date, end_date):
    filename = f"{ticker}_data.csv"
    
    if os.path.exists(filename):
        print(f"Loading {ticker} data from localized CSV...")
        df = pd.read_csv(filename, index_col=0, parse_dates=True)
        
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)
            
        # If the CSV is in an old broken format — delete it and re-download cleanly
        if len(df) > 0 and df.iloc[0].astype(str).str.contains(ticker).any():
            print("Detected old broken CSV format. Re-downloading fresh data...")
            # FIX: delete the bad file so we don't load it again
            
            os.remove(filename)
            df = yf.download(ticker, start=start_date, end=end_date)
            
            if isinstance(df.columns, pd.MultiIndex):
                df.columns = df.columns.get_level_values(0)
                
            df.to_csv(filename)
            print(f"Saved fresh {ticker} data to {filename}")
    else:
        print(f"Downloading {ticker} from Yahoo Finance...")
        df = yf.download(ticker, start=start_date, end=end_date)
        
        # FIX:Flatten yfinance's MultiIndex columns down to a single level
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)
            
        df.to_csv(filename)
        print(f"Saved {ticker} data to {filename}")        
        
    # Cast financial columns to numeric types to prevent object/string type mismatches
    for col in ['Open', 'High', 'Low', 'Close', 'Volume']:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
            
    # Drop rows that don't have valid price data
    df = df.dropna(subset=['Close'])
    
    return df