from data_fetch import fetch_and_save_data
from strategies import moving_average_crossover
from backtester import run_backtest
import matplotlib.pyplot as plt
from datetime import date

def main():
    # Fetch data
    ticker = "NVDA"
    today = str(date.today())
    df = fetch_and_save_data(ticker, "2020-01-01", today)
    
    # Apply strategy signals
    df_with_signals = moving_average_crossover(df)
    
    # Run simulation
    performance = run_backtest(df_with_signals, initial_capital=10000)
    
    # Print baseline results
    final_val = performance['Portfolio_Value'].iloc[-1]
    print(f"\n--- Final Results for {ticker} ---")
    print(f"Ending Portfolio Value: ${final_val:,.2f}")
    
    # Plot the graph
    performance['Portfolio_Value'].plot(title="Portfolio Growth Over Time")
    plt.ylabel("Portfolio Value ($)")
    plt.grid(True)
    plt.show()
    plt.ion()

if __name__ == "__main__":
    main()