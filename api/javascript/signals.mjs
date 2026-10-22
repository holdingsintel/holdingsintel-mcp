#!/usr/bin/env node
// HoldingsIntel public signals API: JavaScript example (Node 18 or later, global fetch).
//
// Usage:
//   node signals.mjs                # fetches 'convergence'
//   node signals.mjs conviction     # any of the 6 signal types

const BASE = "https://www.holdingsintel.com/api/public/signals";
const VALID = [
  "convergence", "conviction", "double-downs",
  "smart-money", "congressional", "backtesting",
];

/** Fetch and parse a signal. Throws on non-2xx (429 over the limit, 400 unknown type). */
export async function fetchSignal(type) {
  if (!VALID.includes(type)) {
    throw new Error(`Unknown type '${type}'. Valid: ${VALID.join(", ")}`);
  }
  const res = await fetch(`${BASE}/${type}`, {
    headers: { Accept: "application/json" },
  });
  if (!res.ok) {
    throw new Error(`HTTP ${res.status}: ${await res.text()}`);
  }
  return res.json();
}

const type = process.argv[2] ?? "convergence";
try {
  const data = await fetchSignal(type);
  console.log(JSON.stringify(data, null, 2).slice(0, 4000));
} catch (err) {
  console.error(err.message);
  process.exit(1);
}
