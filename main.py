from data_fetch import fetch_and_save_data
from strategies import moving_average_crossover, rsi
from backtester import run_backtest
import matplotlib.pyplot as plt
from datetime import date

def main():
    # Fetch data
    ticker = "NVDA"
    initial_capital = 10000.0
    start_date = "2023-01-01"
    end_date = str(date.today())
    df = fetch_and_save_data(ticker, start_date, end_date)
    sp500_df = fetch_and_save_data("^GSPC", start_date, end_date)

    # Apply strategy signals
    df_ma = moving_average_crossover(df)
    performance_ma = run_backtest(df_ma, initial_capital=initial_capital)
    df_rsi = rsi(df)
    performance_rsi = run_backtest(df_rsi, initial_capital=initial_capital)
    # Baseline 1: Buy-and-Hold Target Ticker
 
    # FIX: Ensure that the backtest dates are aligned between the two strategies and the benchmarks dataframes. This prevents misalignment issues when plotting or comparing results, as trades are able to be generated at different times
    backtest_dates = performance_ma.index.intersection(performance_rsi.index)

    asset_closes = df.loc[backtest_dates, 'Close']
    asset_initial_price = asset_closes.iloc[0]
    buy_and_hold_ticker = initial_capital * (asset_closes / asset_initial_price)
    
    # Baseline 2: Buy-and-Hold S&P 500 Index

    sp500_closes = sp500_df.loc[backtest_dates, 'Close']
    sp500_initial_price = sp500_closes.iloc[0]
    buy_and_hold_sp500 = initial_capital * (sp500_closes / sp500_initial_price)

    # Print baseline results

    final_strategy_val = performance_ma['Portfolio_Value'].iloc[-1]
    final_asset_val = buy_and_hold_ticker.iloc[-1]
    final_sp500_val = buy_and_hold_sp500.iloc[-1]
    print(f"\n--- Final Results Comparison ({ticker} vs Benchmark) ---")
    print(f"MA Crossover Strategy ({ticker}):  ${final_strategy_val:,.2f}")
    print(f"{ticker} Buy & Hold:               ${final_asset_val:,.2f}")
    print(f"S&P 500 Benchmark (^GSPC):    ${final_sp500_val:,.2f}")
    print(f"RSI Strategy ({ticker}):        ${performance_rsi['Portfolio_Value'].iloc[-1]:,.2f}")
    
    # Plot the graph
    plt.figure(figsize=(12, 6))
    plt.plot(backtest_dates, performance_ma.loc[backtest_dates, 'Portfolio_Value'], label="MA Crossover Strategy", color="blue", linewidth=1.5)
    plt.plot(backtest_dates, performance_rsi.loc[backtest_dates, 'Portfolio_Value'], label="RSI Strategy", color="purple", linewidth=1.5)
    plt.plot(backtest_dates, buy_and_hold_ticker, label=f"Hold {ticker}", color="orange", linewidth="1.5")
    plt.plot(backtest_dates, buy_and_hold_sp500, label="S&P 500 Index", color="green", linewidth="1.5")
    plt.title(f"Portfolio Growth Comparison ($10k Initial Capital, Starting: {backtest_dates[0].strftime('%Y-%m-%d')} , Ending: {end_date})")
    plt.xlabel("Date")
    plt.ylabel("Portfolio Value ($)")
    plt.legend()
    plt.grid(True)
    plt.show()
    plt.ion()

if __name__ == "__main__":
    main()
