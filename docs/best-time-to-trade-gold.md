---
title: "Best time to trade gold: XAUUSD sessions compared"
description: "How much gold (XAUUSD) moves in each hour and trading session, measured on one year of 1-minute candles, and why the busiest hours are not automatically the best."
---

# Best time to trade gold: XAUUSD sessions compared

Gold moves most when London and New York are both open, and least late in the US evening. That does not make the busiest hours the best ones to trade. It only tells you when there is the most movement.

> Measured on past data. Past results do not predict future results. Not financial advice.

## Gold sessions compared

Median range of a one-hour candle, as a percent of price. Weekdays, 1 Oct 2025 to 19 Oct 2026, from a broker's 1-minute candles. Times are UTC. Session names are approximate, because they shift with summer time.

| Session (UTC) | Median hourly range | Compared with all hours (0.38%) |
|---|---|---|
| Asia, 00:00 to 07:00 | 0.38% | About the same |
| London morning, 07:00 to 12:00 | 0.34% | Lower |
| **London and New York overlap, 12:00 to 16:00** | **0.55%** | **About 45% higher** |
| New York afternoon, 16:00 to 20:00 | 0.35% | Lower |
| Evening, 20:00 to 24:00 | 0.27% | About 30% lower |

## Hour by hour

| Hour (UTC) | Median range | Hour (UTC) | Median range |
|---|---|---|---|
| 00 | 0.41% | 12 | 0.47% |
| 01 | 0.54% | **13** | **0.60%** |
| 02 | 0.41% | **14** | **0.58%** |
| 03 | 0.32% | 15 | 0.54% |
| 04 | 0.26% | 16 | 0.41% |
| 05 | 0.42% | 17 | 0.35% |
| 06 | 0.37% | 18 | 0.35% |
| 07 | 0.35% | 19 | 0.32% |
| 08 | 0.36% | 20 | 0.25% |
| 09 | 0.32% | 21 | 0.25% |
| 10 | 0.31% | 22 | 0.26% |
| 11 | 0.34% | 23 | 0.31% |

Hours 21 and 22 have fewer samples, because the market closes for part of them.

## What this does and does not tell you

- **Movement is not profit.** A wide candle can hit your stop just as easily as your target.
- **The result depends on the strategy.** A breakout, a reversal and a trend rule can each need different hours. Test the hours with your own rules rather than copying a table.
- **Costs change through the day.** Spreads are often wider in thin hours and around news.
- **This is one year of data.** Gold's behaviour changes, so the pattern may not hold.

## Example: the London breakout

Our [London breakout strategy](https://github.com/TradingTPSL/Trading-Strategies-TPSL.si/blob/main/strategies/london-breakout-classic.md) places its orders at 06:00 London time, before the busy hours in the table. It closes any open trade at 21:00 broker time. Its full results, including four losing months in a row, are on its page.

## Test the hours on your own rules

[TPSL](https://tpsl.si/?utm_source=github&utm_medium=hours) lets you limit a gold strategy to the hours you actually trade and compare the backtest with and without that limit. You can run 5 strategy tests for free. Results are hypothetical and TPSL never places orders.
