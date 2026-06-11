# ML Stock Market Predictor & Backtester

## Description
This project implements a complete Machine Learning pipeline designed to predict the directional movements of a financial asset (up or down) and simulate the financial viability of these predictions using a custom backtesting engine.

## Project Architecture
The codebase is structured in a modular way:
- **fetcher.py**: Historical market data retrieval via the Yahoo Finance API (`yfinance`).
- **engineering.py**: Feature engineering based on technical analysis indicators (using the `ta` library).
- **trainer.py**: Data splitting, training, and evaluation of the artificial intelligence model.
- **backtester.py** (or **strategy.py**): Financial simulation engine. It calculates the cumulative returns of the strategy and compares them to a passive investment approach.
- **main.py**: Entry point orchestrating the entire pipeline.

## Features & Technical Indicators
The model relies on several technical indicators to analyze market trends and volatility:
- Daily returns (Returns)
- Simple Moving Averages (SMA 20, SMA 50) and their crossover (MA_cross)
- RSI (Relative Strength Index) and its past values (Lags)
- MACD (Moving Average Convergence Divergence)
- Relative distance between the closing price and the 20-day moving average

## Model Used
The primary algorithm is an **XGBoost Classifier**. The model performs binary classification based on the following rules:
- `1` (Up/Bullish): Buy or hold the position in the market.
- `0` (Down/Bearish): Sell and hold the portfolio in cash (liquidity).

## Backtest Results (Case Study: AAPL)
The strategy was tested on Apple stock (AAPL) over a 5-year historical period, using a chronological data split (80% for training, 20% for testing).

**Performance over the test period (excluding transaction fees):**
- **ML Strategy Return:** ~ +20%
- **Market Return (Buy & Hold):** ~ +45%

**Analysis of Results:**
The backtest successfully validates the technical functionality of the pipeline. The strategy proves to be profitable (no capital loss) and successfully avoids certain downtrends by exiting the market. However, it underperforms the benchmark index. Graphical analysis reveals that the model behaves too cautiously: false negative signals trigger market exits during strong bullish phases
