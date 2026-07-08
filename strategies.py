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

def rsi(df, window = 14, oversold = 30, overbought = 70):
    df = df.copy()

    #RSI Calculation
    delta = df['Close'].diff()
    gain = delta.where(delta > 0, 0).rolling(window=window).mean()
    loss = -delta.where(delta < 0, 0).rolling(window=window).mean()
    rs = gain / loss
    df['RSI'] = 100 - (100 / (1 + rs))

    df['Signal'] = None
    df.loc[df['RSI'] < oversold, 'Signal'] = 1
    df.loc[df['RSI'] > overbought, 'Signal'] = -1
    
    # Holds the position until an opposite signal occurs
    # (Replacing 0s with previous positions, ignoring the initial warm-up)
    df['Signal'] = df['Signal'].ffill().fillna(0)
    return df
