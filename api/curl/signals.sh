#!/usr/bin/env bash
# HoldingsIntel public signals API: curl examples. No key required.
set -euo pipefail

BASE="https://www.holdingsintel.com/api/public/signals"

# Stocks where funds, insiders, activists and Congress point the same way
curl -s "$BASE/convergence" | jq .

# The positions that matter most to each fund
curl -s "$BASE/conviction" | jq .

# Recent STOCK Act trades by members of Congress
curl -s "$BASE/congressional" | jq .

# How many results each signal returns (6 calls, within the 10-a-minute limit)
for t in convergence conviction double-downs smart-money congressional backtesting; do
  echo "== $t =="
  curl -s "$BASE/$t" | jq '.results | length'
done
