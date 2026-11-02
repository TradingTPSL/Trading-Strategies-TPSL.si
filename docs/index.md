---
title: "Gold (XAUUSD) trading strategy backtests with costs"
description: "A London breakout strategy for gold with exact rules and honest backtest results, a free prop challenge simulator in Python, and a guide to backtesting pitfalls."
---

# Gold (XAUUSD) trading strategies, backtested with costs

One gold trading strategy with exact rules and full results, including the losing months, plus free tools for checking your own backtests.

> Hypothetical backtest. Past results do not predict future results. Not financial advice. No funding guaranteed.

## London breakout strategy for gold

Mark the range from 03:00 to 08:00 broker time. At 08:00, place a stop order on each side. The stop goes on the other side of the range and the target is 2.5R, with one trade a day.

From 1 Oct 2025 to 27 Oct 2026, with assumed costs: 239 trades, 42.3% winners, profit factor 1.35 (90% range 1.04 to 1.72), +$1,004 per 1 oz, worst drop -$638, and four losing months in a row.

[Read the full rules and results](https://github.com/TradingTPSL/Trading-Strategies-TPSL.si/blob/main/strategies/london-breakout-classic.md)

## Guides

- [How to read a backtest](how-to-read-a-backtest.md): costs, sample size, luck, drawdown, and in-sample versus out-of-sample
- [Best time to trade gold](best-time-to-trade-gold.md): how much XAUUSD moves in each hour and session

## Free prop challenge simulator

[A small Python script](https://github.com/TradingTPSL/Trading-Strategies-TPSL.si/blob/main/tools/prop_challenge_sim.py) that replays your own closed trades through multi-step prop challenge rules, one attempt per start month.

## Test your own rules

These results come from [TPSL (Take Profit, Stop Loss)](https://tpsl.si/?utm_source=github&utm_medium=pages), a web app where you can chart gold, write your own trading rules and backtest them with costs, without writing code. You can run 5 strategy tests for free. Results are hypothetical and TPSL never places orders.

[View this project on GitHub](https://github.com/TradingTPSL/Trading-Strategies-TPSL.si)
