# Algorithmic Trading Strategy Backtester

A modular Python framework designed to backtest quantitative trading strategies using historical market data. This project allows users to evaluate the historical performance of algorithmic strategies before deploying capital in a practical environment.

## Features & Roadmap
- [x] **Moving Average Crossover:** Backtest SMA/EMA strategies with customizable short/long windows.
- [ ] **Correlated Pairs Trading (In Progress):** Statistical arbitrage logic using cointegration.
- [ ] **Relative Strength Index (RSI) Filter (In Progress):** Incorporating momentum metrics to reduce false signals.
- [ ] **Performance Analytics:** Tracks cumulative returns, Sharpe ratio, and maximum drawdown.

## Tech Stack
- **Language:** Python 3
- **Libraries:** Pandas, NumPy, Matplotlib

## How It Works (Example: Moving Average Crossover)
The backtester processes historical daily closing prices. When the short-term moving average crosses above the long-term moving average, a **Buy** signal is triggered. A **Sell** signal is triggered on the reverse cross.

## How It Works (Example: Correlated Pairs Trading)

## How It Works (Example: Relative Strength Index)

## Notes
- The **'FIX'** tag identifies sections optimized or debugged using AI.
