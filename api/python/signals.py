#!/usr/bin/env python3
"""HoldingsIntel public signals API: Python example (standard library only).

Usage:
    python signals.py                # fetches 'convergence'
    python signals.py conviction     # any of the 6 signal types
"""
import json
import sys
import urllib.error
import urllib.request

BASE = "https://www.holdingsintel.com/api/public/signals"
VALID = ["convergence", "conviction", "double-downs", "smart-money",
         "congressional", "backtesting"]


def fetch_signal(signal_type: str):
    """Return the parsed JSON for a signal type. Raises on HTTP/URL errors."""
    if signal_type not in VALID:
        raise ValueError(f"Unknown type '{signal_type}'. Valid: {', '.join(VALID)}")
    req = urllib.request.Request(
        f"{BASE}/{signal_type}", headers={"Accept": "application/json"}
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def main() -> int:
    signal_type = sys.argv[1] if len(sys.argv) > 1 else "convergence"
    try:
        data = fetch_signal(signal_type)
    except urllib.error.HTTPError as e:
        # 429 = over 10 requests a minute; 400 = unknown type.
        print(f"HTTP {e.code}: {e.read().decode(errors='replace')}", file=sys.stderr)
        return 1
    except (urllib.error.URLError, ValueError) as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    print(json.dumps(data, indent=2)[:4000])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
