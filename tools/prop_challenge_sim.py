#!/usr/bin/env python3
"""Replay a list of closed trades through generic multi-step prop challenge rules.

The script tries one attempt per start month, so you can see how much the result
depends on when you began. It needs Python 3.9+ and nothing else.

Input CSV, with a header row:
    date,r       one trade per row, result in R (multiples of the amount risked)
    date,pnl     or the result in money, used as it is

Dates must look like 2026-01-31 (a time after the date is allowed).

Limits of this model:
- It only sees closed trades. A real challenge also counts open losses, so a real
  account can fail where this replay passes.
- It does not know a firm's real rules. Set the numbers to match the one you check.
- A trade list that was fitted to past data will look better here than it will live.
"""
from __future__ import annotations

import argparse
import csv
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path


@dataclass(frozen=True)
class Trade:
    day: date
    r: float | None = None
    pnl: float | None = None


@dataclass(frozen=True)
class Rules:
    balance: float = 100_000
    risk_pct: float = 0.5
    targets_pct: tuple[float, ...] = (5, 5, 5)
    daily_loss_pct: float = 5
    max_loss_pct: float = 10


@dataclass(frozen=True)
class Attempt:
    start: date
    status: str  # "passed", "failed" or "unfinished"
    reason: str
    phase: int  # the last phase reached, counted from 1
    phase_days: tuple[int, ...]  # calendar days taken by each completed phase
    worst_day_pct: float  # worst daily result, in percent of the starting balance


def load_trades(path: Path) -> list[Trade]:
    with path.open(newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        columns = {(c or "").strip().lower() for c in reader.fieldnames or []}
        if "date" not in columns or not columns & {"r", "pnl"}:
            raise ValueError("the CSV needs a 'date' column and an 'r' or 'pnl' column")
        trades = []
        for line, raw in enumerate(reader, start=2):
            row = {(k or "").strip().lower(): (v or "").strip() for k, v in raw.items()}
            try:
                day = date.fromisoformat(row["date"][:10])
                r = float(row["r"]) if row.get("r") else None
                pnl = float(row["pnl"]) if row.get("pnl") else None
            except ValueError as e:
                raise ValueError(f"line {line}: {e}") from e
            if r is None and pnl is None:
                raise ValueError(f"line {line}: no result")
            trades.append(Trade(day, r, pnl))
    # sorted() is stable, so trades on the same day keep their order in the file.
    return sorted(trades, key=lambda t: t.day)


def trade_money(trade: Trade, rules: Rules) -> float:
    if trade.pnl is not None:
        return trade.pnl
    return trade.r * rules.balance * rules.risk_pct / 100


def simulate(trades: list[Trade], start: date, rules: Rules) -> Attempt:
    """Run one attempt, using the trades dated on or after `start`.

    Each phase restarts at the starting balance. The daily limit is measured from
    the balance at the start of that day, and the max loss from the starting balance.
    """
    daily_limit = rules.balance * rules.daily_loss_pct / 100
    max_limit = rules.balance * rules.max_loss_pct / 100

    phase = 0
    equity = rules.balance
    phase_start = None
    phase_days: list[int] = []
    current_day = None
    day_open = equity
    worst_day = 0.0

    def attempt(status: str, reason: str) -> Attempt:
        return Attempt(start, status, reason, phase + 1, tuple(phase_days),
                       worst_day / rules.balance * 100)

    for trade in trades:
        if trade.day < start:
            continue
        if trade.day != current_day:
            current_day, day_open = trade.day, equity
        if phase_start is None:
            phase_start = trade.day

        equity += trade_money(trade, rules)
        day_result = equity - day_open
        worst_day = min(worst_day, day_result)

        if day_result <= -daily_limit:
            return attempt("failed", f"daily loss limit on {trade.day}")
        if equity <= rules.balance - max_limit:
            return attempt("failed", f"max loss limit on {trade.day}")

        target = rules.balance * rules.targets_pct[phase] / 100
        if equity >= rules.balance + target:
            phase_days.append((trade.day - phase_start).days)
            if phase + 1 == len(rules.targets_pct):
                return attempt("passed", f"finished on {trade.day}")
            phase += 1
            # A new phase starts from the next trade, on a fresh balance.
            equity = rules.balance
            phase_start = None
            current_day = None

    return attempt("unfinished", "ran out of trades")


def month_starts(trades: list[Trade]) -> list[date]:
    months = sorted({t.day.replace(day=1) for t in trades})
    return months


def report(attempts: list[Attempt]) -> str:
    lines = ["start        result      phase  phase days        worst day  note"]
    for a in attempts:
        days = ",".join(str(d) for d in a.phase_days) or "-"
        lines.append(
            f"{a.start}   {a.status:<10}  {a.phase:<5}  {days:<16}  "
            f"{a.worst_day_pct:>7.2f}%  {a.reason}"
        )
    passed = sum(a.status == "passed" for a in attempts)
    failed = sum(a.status == "failed" for a in attempts)
    unfinished = len(attempts) - passed - failed
    lines += ["", f"{passed} passed, {failed} failed, {unfinished} unfinished, "
                  f"out of {len(attempts)} start months."]
    return "\n".join(lines)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Replay closed trades through prop challenge rules.")
    p.add_argument("csv", type=Path, help="CSV with date,r or date,pnl columns")
    p.add_argument("--balance", type=float, default=100_000, help="starting balance")
    p.add_argument("--risk", type=float, default=0.5, help="percent risked per trade, for R results")
    p.add_argument("--targets", default="5,5,5", help="profit target of each phase, in percent")
    p.add_argument("--daily-loss", type=float, default=5, help="daily loss limit, in percent")
    p.add_argument("--max-loss", type=float, default=10, help="max loss limit, in percent")
    return p.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        trades = load_trades(args.csv)
        targets = tuple(float(x) for x in args.targets.split(","))
    except (OSError, ValueError) as e:
        print(f"error: {e}", file=sys.stderr)
        return 2
    if not trades:
        print("error: the CSV has no trades", file=sys.stderr)
        return 2
    rules = Rules(args.balance, args.risk, targets, args.daily_loss, args.max_loss)
    print(report([simulate(trades, s, rules) for s in month_starts(trades)]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
