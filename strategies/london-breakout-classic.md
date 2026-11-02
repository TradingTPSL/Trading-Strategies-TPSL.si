# London breakout (classic): rules, backtest results and drawdown (gold, XAUUSD)

A simple gold breakout strategy with exact rules, tested with costs. It made money over the 13 months tested, and it also lost for four months in a row. Both are shown here.

> **Hypothetical backtest. Past results do not predict future results. Not financial advice. No funding guaranteed.**

## Gold breakout strategy rules

| Rule | Value |
|---|---|
| Market | Gold (XAUUSD), 1-minute candles |
| Days | Monday to Friday |
| Clock | Broker time (Athens). 08:00 Athens is 06:00 in London |
| Range | High and low from 03:00 to 08:00 |
| Skip the day | Range under 0.3% or over 1.6% of price |
| Entry | At 08:00, a buy stop above the range high and a sell stop below the range low, each 0.2 beyond the level. The first fill cancels the other |
| Stop | The other side of the range, 0.6% of price at most |
| Target | 2.5R (R is the stop distance) |
| Break-even | Stop moves to the entry price once the trade is +1.5R |
| Time exit | Close at 21:00, and cancel unfilled orders |
| Limit | One trade a day |

The same rules are in [london-breakout-classic.json](london-breakout-classic.json). The idea comes from a public MQL5 blog post.

## Assumed costs

Spread from each candle, commission 0.07 per trade, slippage 0.05 on entry and 0.10 on stops, all three times higher near news. These are assumptions, not real fills. Results are per 1 oz of gold.

## Backtest results

1 Oct 2025 to 27 Oct 2026. [See the report](https://tpsl.si/s/Dog2RsZHIt).

| | |
|---|---|
| Trades | 239 |
| Winning trades | 42.3% |
| Profit factor | 1.35 (90% range 1.04 to 1.72) |
| Net result | +$1,004.36 per 1 oz |
| Worst drop from a peak | -$637.56 per 1 oz |
| Average per trade | 0.16R |

### Month by month (net per 1 oz)

| Month | Trades | Net |
|---|---|---|
| Oct 2025 | 20 | +174 |
| Nov 2025 | 18 | -46 |
| Dec 2025 | 21 | -169 |
| Jan 2026 | 17 | -131 |
| Feb 2026 | 13 | -185 |
| Mar 2026 | 14 | +3 |
| Apr 2026 | 20 | +352 |
| May 2026 | 20 | +385 |
| Jun 2026 | 17 | +122 |
| Jul 2026 | 22 | +82 |
| Aug 2026 | 18 | +197 |
| Sep 2026 | 21 | +251 |
| Oct 2026 (to the 27th) | 18 | -29 |

### Older years, same rules

| Period | Trades | Winning | Profit factor | Net per 1 oz | Worst drop |
|---|---|---|---|---|---|
| Oct 2023 to Sep 2024 | 181 | 44.8% | 1.37 | +305 | -68 |
| Oct 2024 to Sep 2025 | 225 | 43.6% | 1.20 | +315 | -264 |

### Other checks

- **Double costs:** profit factor 1.33, net +$964. The average stop is wide compared with the costs, so this test barely moves the result. Costs in a fast market can be much worse than double.
- **Luck test:** the same entries with the direction drawn at random, 200 times. None did as well. The median random run had a profit factor of 0.99. This test says nothing about whether the pattern will continue.
- **Sells and buys:** sells made +$720, buys made +$285. Most of the profit came from one side.

## The weak spots

- **Four losing months in a row.** November 2025 to February 2026 lost about $531 per 1 oz. February had 13 trades, and only about 1 in 13 won. Five of the 13 months lost money.
- **The profit came from one stretch.** April to September 2026 made about $1,388, more than the whole 13-month total. The worst drop (-$638) is about 63% of the total profit.
- **Most trades do not reach the target.** In the closely matching 238-trade run behind the challenge test below, 34 trades hit the target, 101 hit the stop, 89 closed at 21:00 and 14 closed at break-even.
- **Selection bias.** This is one of the better rule sets from our own testing. Picking a good one from many makes it look better than it will likely be.
- **The data has seams.** Candles come from a broker's MT5 history until 19 Oct 2026, and from other feeds after that. There is no walk-forward test.

## Prop firm challenge strategy backtest

We replayed the trades through generic 3-step challenge rules: $100k balance, 5% target on each phase, 5% daily loss limit, 10% max loss, 0.5% risk per trade, no time limit. You can run the same test on your own trades with the [simulator](../tools/prop_challenge_sim.py). This used a 238-trade run from a day earlier than the report above. The trade list is not published here.

| Start month | Result | Days in phase 1, 2, 3 |
|---|---|---|
| Oct 2025 | Passed | 238, 46, 48 |
| Nov 2025 | **Failed**, 10% max loss on 23 Feb 2026 | |
| Dec 2025 | Passed | 205, 43, 24 |
| Jan 2026 | Passed | 138, 42, 46 |
| Feb 2026 | Passed | 86, 25, 66 |
| Mar 2026 | Passed | 57, 20, 40 |
| Apr 2026 | Passed | 27, 20, 40 |
| May 2026 | Passed | 26, 46, 48 |
| Jun to Oct 2026 | Unfinished, trades ran out | |

So 6 of the 7 starts from October to April passed, and the May start passed too. The daily limit was never hit, and the worst day was about -1R.

Why this is weaker than it looks:

- **Trading with no edge also passes often when there is no time limit.** Ignoring costs, a coin flip with a +5% target and a -10% limit passes one phase about 2 times in 3, so all three phases about 30% of the time.
- **The starts overlap.** Most of them finished thanks to the same good months, so they are not 7 separate tests.
- **Phase 1 took from about 1 to 8 months.** That is 27 to 238 days, with a median of about 112 days for the six October to April passes. Many real challenges have time limits, and some of these runs would fail them.
- **Only closed trades count here.** Real challenges also count open losses.
- These are generic rules, not those of any specific firm.

## Test your own version

You can copy these rules from the [report](https://tpsl.si/s/Dog2RsZHIt) into [TPSL](https://tpsl.si/?utm_source=github&utm_medium=strategy) and change the hours, the stop or the target, without writing code. You can run 5 strategy tests for free.

Next: [how to read a backtest](../docs/how-to-read-a-backtest.md) and [the best time to trade gold](../docs/best-time-to-trade-gold.md).
