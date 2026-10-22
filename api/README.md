# Free public signals API

Six smart-money signals over plain HTTP. No key, no sign-up.

```
GET https://www.holdingsintel.com/api/public/signals/{type}
```

- 10 requests a minute per IP. Past that you get `429` with `Retry-After`.
- Open to browsers (`Access-Control-Allow-Origin: *`), cached for an hour at the edge.
- An unknown `{type}` returns `400` with the list of valid types.

| `{type}` | What it returns |
|---|---|
| `convergence` | Stocks where funds, insiders, activists and Congress point the same way |
| `conviction` | The positions that matter most to each fund, scored 0 to 100 |
| `double-downs` | Funds adding to positions while the price fell |
| `smart-money` | Net institutional buying against selling, by stock |
| `congressional` | Recent STOCK Act trades by members of Congress |
| `backtesting` | Forward returns by conviction band |

## Examples

- [`curl/signals.sh`](./curl/signals.sh): one-liners
- [`python/signals.py`](./python/signals.py): standard library only
- [`javascript/signals.mjs`](./javascript/signals.mjs): Node 18 or later

```bash
curl -s https://www.holdingsintel.com/api/public/signals/convergence | jq .
```

## Response

Every signal returns the same envelope: the source, the quarter the data covers, a plain description of the signal and a ranked `results` array.

```json
{
  "source": "HoldingsIntel",
  "data_as_of": "2026-Q2",
  "signal_type": "convergence",
  "description": "...",
  "results": [{ "rank": 1, "ticker": "...", "company_name": "..." }]
}
```

Row fields depend on the signal (`convergence_score`, `conviction_score`, net flow and so on); the keys name themselves.

Credit appreciated: "HoldingsIntel (holdingsintel.com), from SEC filings." Not investment advice.
