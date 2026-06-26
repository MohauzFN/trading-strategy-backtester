import pandas as pd

def moving_average_crossover(df, short_window=50, long_window=200):
    # Work on an isolated copy to prevent altering a dataframe slice
    df = df.copy()
    
    # Calculate moving averages
    df["Short_MA"] = df["Close"].rolling(window=short_window).mean()
    df["Long_MA"] = df["Close"].rolling(window=long_window).mean()
    
    # Initialize all signals to 0 (no position / neutral)
    df['Signal'] = 0

    # FIX: Use -1 as an explicit SELL signal (was 0 before, which caused
    # the backtester to try selling shares never bought during warm-up)
    df.loc[df['Short_MA'] > df['Long_MA'], 'Signal'] = 1    # BUY signal
    df.loc[df['Short_MA'] <= df['Long_MA'], 'Signal'] = -1  # SELL signal

    return df