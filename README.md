<p align="center"><img src="https://tpsl.si/icons/512" alt="TPSL logo" width="96" height="96"></p>

# Gold (XAUUSD) trading strategies, backtested with costs

One gold trading strategy with its exact rules and its full backtest results, including the losing months. Plus a free prop firm challenge simulator in Python and a guide to the most common backtesting pitfalls.

> **Hypothetical backtest. Past results do not predict future results. Not financial advice. No funding guaranteed.**

## What is in this repository

| Page | What you get |
|---|---|
| [London breakout strategy for gold](strategies/london-breakout-classic.md) | Exact rules, costs, results, drawdown and the weak spots |
| [The same rules as JSON](strategies/london-breakout-classic.json) | A plain description you can port to your own tools |
| [How to read a backtest](docs/how-to-read-a-backtest.md) | Costs, sample size, luck, drawdown, in-sample and out-of-sample |
| [Best time to trade gold](docs/best-time-to-trade-gold.md) | How much gold moves in each hour and session, measured |
| [Prop challenge simulator](tools/prop_challenge_sim.py) | Replays your own trades through 3-step challenge rules |

## London breakout strategy: the short version

Gold (XAUUSD), 1-minute candles, one trade a day. Mark the range from 03:00 to 08:00 broker time, then place a stop order on each side. Full rules are on the [strategy page](strategies/london-breakout-classic.md).

| 1 Oct 2025 to 27 Oct 2026, assumed costs included | |
|---|---|
| Trades | 239 |
| Winning trades | 42.3% |
| Profit factor | 1.35 (90% range 1.04 to 1.72) |
| Net result | +$1,004 per 1 oz |
| Worst drop from a peak | -$638 per 1 oz |
| Losing months | 5 of 13, including 4 in a row |

See the [full report for these rules](https://tpsl.si/s/Dog2RsZHIt). It is a saved snapshot of the backtest.

## Prop firm challenge simulator in Python

`tools/prop_challenge_sim.py` needs Python 3.9 or newer and nothing else. Give it a CSV of your closed trades, and it tries one attempt per start month, so you can see how much the result depends on when you began.

```bash
python tools/prop_challenge_sim.py tools/sample_trades.csv
```

The CSV has a `date` column and either `r` or `pnl`. Every setting can be changed:

```bash
python tools/prop_challenge_sim.py my_trades.csv --balance 100000 --risk 0.5 --targets 5,5,5 --daily-loss 5 --max-loss 10
```

`tools/sample_trades.csv` is invented, with one +2R winner for every two -1R losers, which adds up to zero. It only shows the format, and says nothing about any strategy.

The simulator only sees closed trades. A real challenge also counts open losses, and every firm has its own rules, so set the numbers to match the one you are checking.

## What is TPSL

These results come from [TPSL (Take Profit, Stop Loss)](https://tpsl.si/?utm_source=github&utm_medium=readme), a web app where you can chart gold, write your own trading rules and backtest them with costs, without writing code. You can run 5 strategy tests for free. Results are hypothetical, costs are assumed, and TPSL never places orders.

This repository does not contain the TPSL source code. The simulator was written separately for this repository.

## Licence

[MIT](LICENSE).
