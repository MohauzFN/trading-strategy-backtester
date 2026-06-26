import pandas as pd

def run_backtest(df, initial_capital=10000.0, commission=0.001, slippage=0.0005):
    """Simulates trading based on signals while applying realistic market constraints."""
    cash = initial_capital
    shares = 0
    portfolio_values = []
    
    for i in range(1, len(df)):
        prev_day_signal = df['Signal'].iloc[i-1]
        current_open = df['Open'].iloc[i]
        current_close = df['Close'].iloc[i]

        # Skip rows where the signal is still 0 (the warm-up period)
        if prev_day_signal == 0:
            portfolio_values.append(cash + shares * current_close)
            continue

        # BUY: Signal was 1 yesterday and we don't already own shares
        if prev_day_signal == 1 and shares == 0:
            # Apply slippage penalty to the execution price
            buy_price = current_open * (1 + slippage)
            shares = int(cash // buy_price)
            
            trade_cost = shares * buy_price
            fee = trade_cost * commission
            cash -= (trade_cost + fee)

        # FIX: SELL signal is now -1 (was 0, which incorrectly triggered during
        # the warm-up period and tried to sell shares that were never bought)
        elif prev_day_signal == -1 and shares > 0:
            sell_price = current_open * (1 - slippage)
            trade_value = shares * sell_price
            fee = trade_value * commission
            cash += (trade_value - fee)
            shares = 0
            
        # Track total value of the portfolio at the end of each day
        daily_portfolio_value = cash + (shares * current_close)
        portfolio_values.append(daily_portfolio_value)
        
    # Create a clean DataFrame tracking performance
    results_df = pd.DataFrame(index=df.index[1:])
    results_df['Portfolio_Value'] = portfolio_values
    return results_df