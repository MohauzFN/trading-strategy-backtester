# Algorithmic Trading Strategy Backtester

A modular Python framework designed to backtest quantitative trading strategies using historical market data. This project allows users to evaluate the historical performance of algorithmic strategies before deploying capital in a practical environment.

## Features & Roadmap
- [x] **Moving Average Crossover:** Backtest SMA/EMA strategies with customizable short/long windows.
- [x] **Relative Strength Index (RSI) Filter:**
Incorporating momentum metrics to reduce false signals.


## Tech Stack
- **Language:** Python 3
- **Libraries:** Pandas, NumPy, Matplotlib, yfinance

## How It Works (Example: Moving Average Crossover)
The backtester processes historical daily closing prices. When the short-term moving average crosses above the long-term moving average, a **Buy** signal is triggered. A **Sell** signal is triggered on the reverse cross.

## How It Works (Example: Relative Strength Index)
The backtester processes historical daily closing prices. When the RSI surpasses the low relative strength index threshold, a **Buy** signal is triggered; a **Sell** signal is triggered when the RSI surpasses the high relative strength index threshold.
## Notes
- The **'FIX'** tag identifies sections optimized or debugged using AI.
