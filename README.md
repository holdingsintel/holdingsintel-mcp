# HoldingsIntel MCP Server

Ask your AI assistant what hedge funds, company insiders, activist investors and members of Congress are trading, and get answers built from their SEC filings and official disclosures, with filing dates and links back to the source.

[www.holdingsintel.com](https://www.holdingsintel.com) · [Setup guide](https://www.holdingsintel.com/mcp) · [Developers](https://www.holdingsintel.com/developers)

## Connect

One URL works in every client. The server speaks Streamable HTTP:

```
https://mcp.holdingsintel.com/sse
```

No account needed to start. For your plan's full limits and history, sign in at [holdingsintel.com](https://www.holdingsintel.com), open **Settings > API Keys > Create Key**, and your client config comes back with the key filled in.

| Client | Steps |
|---|---|
| Claude Desktop | **Settings > Connectors > Add custom connector**. Name it HoldingsIntel and paste the URL. |
| Claude Code | `claude mcp add --transport http holdingsintel https://mcp.holdingsintel.com/sse` |
| ChatGPT | Turn on **Developer mode**, open **Apps > Create**, name it HoldingsIntel and paste the URL (Streamable HTTP). |
| Cursor | **Settings > MCP > Add new MCP server**, or [`examples/cursor-mcp.json`](./examples/cursor-mcp.json) in `~/.cursor/mcp.json`. |

With a key, send it as a header:

```json
{
  "mcpServers": {
    "holdingsintel": {
      "url": "https://mcp.holdingsintel.com/sse",
      "headers": { "Authorization": "Bearer hi_live_YOUR_KEY_HERE" }
    }
  }
}
```

## Tools (24)

Research (15):

| Tool | What it answers |
|---|---|
| `analyze_stock` | The Smart Money Verdict for one stock: funds, insiders, activists and Congress in one read |
| `analyze_fund` | A fund's profile: rating, Fund DNA and how its holdings are doing |
| `find_signals` | Lists of stocks and fund moves by signal: sources agreeing, conviction buys, funds buying weakness, new positions, first movers |
| `compare_funds` | Two or three funds side by side on the same quarter: overlap, style, ratings and shared holdings |
| `clone_fund` | A backtest of copying a fund's disclosed portfolio, using only what was public at each filing date |
| `get_fund_holdings` | A fund's full 13F portfolio for a quarter |
| `get_stock_holders` | Every 13F holder of a stock for a quarter |
| `get_13f_activity` | What a fund bought, added to, trimmed or exited in a quarter, or which funds changed a stock |
| `get_insider_trades` | Company insider buys and sells from Form 4 |
| `get_activist_stakes` | Activist and large-holder stakes above 5% from Schedules 13D and 13G |
| `get_congress_trades` | Trades disclosed by members of Congress and executive-branch officials |
| `analyze_politician` | One politician's trading record and performance |
| `search_filers` | Find a fund by name |
| `search_securities` | Find a stock by ticker or company name |
| `list_quarters` | The quarters on file and which ones your access covers |

Saved lists (8, with an API key):

| Tool | What it does |
|---|---|
| `list_saved_lists` | Your Watchlist and named lists |
| `get_saved_list` | One list with its stocks, funds, politicians or insiders |
| `create_saved_list` | Start a named list |
| `rename_saved_list` | Rename a list |
| `delete_saved_list` | Delete a named list |
| `add_saved_list_item` | Add a stock, fund, politician or insider to a list |
| `update_saved_list_item_notes` | Edit the note on a list item |
| `remove_saved_list_item` | Remove an item from a list |

Account (1):

| Tool | What it answers |
|---|---|
| `get_my_mcp_status` | Your plan, daily quota and usage so far today |

Every tool carries a title and a read-only or destructive annotation. The server also ships one prompt, `verdict-quick`, for a short Verdict on any ticker. Ideas to try: [`examples/prompts.md`](./examples/prompts.md).

## Prefer plain HTTP?

The free public signals API needs no key: [`api/`](./api/) has curl, Python and JavaScript examples.

## About the data

The funds that hold 89% of US 13F-disclosed capital ($70.7T, Q2 2026), with filings back to 2014. Form 4 insider trades, Schedule 13D and 13G activist stakes, and STOCK Act disclosures from the House and Senate. Funds file 13F holdings up to 45 days after each quarter ends; insider, activist and Congress filings are checked every 10 to 15 minutes. Not investment advice.

## License

MIT for this repository: docs, manifest and example configs. The HoldingsIntel platform and its analytics are proprietary.
