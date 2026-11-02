---
title: "How to read a backtest: trading strategy backtesting pitfalls"
description: "A short sanity check for any trading strategy backtest: costs, sample size, luck, drawdown, and in-sample versus out-of-sample results, with a real gold example."
---

# How to read a backtest: trading strategy backtesting pitfalls

A backtest shows what some rules would have done on past data. It does not show what they will do next. Here are six questions to ask before you trust one, using our [London breakout gold backtest](https://github.com/TradingTPSL/Trading-Strategies-TPSL.si/blob/main/strategies/london-breakout-classic.md) as the example.

> Hypothetical backtest examples. Past results do not predict future results. Not financial advice.

## 1. Are costs included, and what happens if they double?

Spread, commission and slippage take money on every trade, so a strategy with many small wins can lose everything to them. Check which costs were assumed, then double them.

If a good result dies at double costs, it was never robust. If it survives, as ours does (profit factor 1.35 to 1.33), that is still not proof. It may only mean that the stops are wide compared with the costs. Costs are also worst when markets move fast, which is when breakouts fill.

## 2. How many trades are there?

Few trades can produce any result by chance. As a rough rule, under 30 trades tells you very little, and even 200 leaves a wide range. Our 239 trades give a profit factor of 1.35, but the 90% range runs from 1.04 to 1.72. Always ask for the range, not only the number.

## 3. Could it be luck?

Keep the same entries and draw the direction at random, many times. If random directions often do as well, the rules probably add nothing. Ours beat all 200 random runs, but that only tests the direction choice on this data. It does not promise the pattern will continue.

## 4. How bad was the drawdown?

Drawdown is the worst drop from a peak. Compare it with the profit: ours fell $638 against a total of $1,004 per 1 oz. Then ask how long it lasted. Ours lost for four months in a row, and most people stop trading a strategy long before that. A result you could not sit through is not one you would really get.

Look at every month, not only the total. A nice total can hide a result that came from a few good months.

## 5. In-sample or out-of-sample?

In-sample data is what the rules were built on, so it always flatters them. Out-of-sample data was kept apart, which makes it the more honest test. Run the same rules, unchanged, on other years. Ours made a profit factor of 1.37 and 1.20 on the two older years, lower than or close to the main period, and that is normal.

Be careful: if you look at the older years and then change the rules, those years stop being out-of-sample.

## 6. How many ideas were tried?

Test enough variations and one will look great by accident. This is overfitting, and picking the best result is selection bias. Ask how many versions were tried. Then change each setting a little: a real effect should survive small changes, while a lucky setting will collapse.

## A quick backtest sanity check

Before you trust any result, whether from a Python script or a screenshot, check that:

- costs are included, and the result survives double costs
- there are enough trades, and you can see the range of the result
- every month is shown, including the losing ones
- the worst drawdown is one you could actually live through
- it also works on data that was not used to build it
- small changes to the settings do not destroy it
- you know how many ideas were tried before this one
- it can be followed live on paper before any real money is involved

Passing all of this still does not mean a strategy will make money. It only means the strategy is worth following on paper.

---

You can run these checks on your own rules with [TPSL](https://tpsl.si/?utm_source=github&utm_medium=guide), without writing code. You can run 5 strategy tests for free. Results are hypothetical and TPSL never places orders.
