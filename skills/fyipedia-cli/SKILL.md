---
name: fyipedia-cli
description: Unified CLI for 10 FYI developer tools -- color conversion, emoji lookup, symbol encoding, Unicode search, Google Fonts, distance calculation, timezone operations, Korean romanization, unit conversion, and holiday dates. Use when you need terminal access to any FYI tool via the `fyi` command.
license: MIT
metadata:
  author: fyipedia
  version: "0.1.1"
  homepage: "https://fyipedia.com/"
---

# FYIPedia CLI -- Unified Developer Tools

One command (`fyi`) gives you instant access to 10 specialized developer tools. Install once, use everything. Each plugin is loaded lazily -- only installed packages are registered.

**Install**: `pip install "fyipedia[all]"` · **PyPI**: [fyipedia](https://pypi.org/project/fyipedia/) · **MCP**: [fyipedia-mcp](https://pypi.org/project/fyipedia-mcp/)

## When to Use

- User needs to convert colors, check WCAG contrast, or generate palettes from the terminal
- User wants to look up emoji metadata, Unicode characters, or encode symbols
- User needs to calculate distances, convert timezones, or find business hours overlap
- User wants to convert units, check holiday dates, or romanize Korean text
- User needs quick access to Google Fonts metadata or font pairings
- User wants one CLI instead of 10 separate tools

## Install

```bash
pip install "fyipedia[all]"              # All 10 tools
pip install "fyipedia[color,distance]"   # Just color + distance
pip install "fyipedia[color,emoji,font]" # Pick any combination
pip install fyipedia                     # Core only (no plugins)
```

Requires Python 3.10+.

## Commands

### `fyi color` -- Color Tools (colorfyi)

| Command | Description | Example |
|---------|-------------|---------|
| `info <hex>` | Full color info in 7 color spaces (RGB, HSL, HSV, CMYK, Lab, OKLCH) | `fyi color info FF6B35` |
| `contrast <fg> <bg>` | WCAG 2.1 contrast ratio + AA/AAA checks | `fyi color contrast 000000 FFFFFF` |
| `harmonies <hex>` | 5 harmony types (complementary, analogous, triadic, split-comp, tetradic) | `fyi color harmonies FF6B35` |
| `shades <hex>` | Tailwind-style 50-950 shade palette | `fyi color shades 3B82F6` |
| `blindness <hex>` | Color blindness simulation (4 types) | `fyi color blindness FF5733` |
| `mix <hex1> <hex2>` | Mix two colors in perceptual Lab space | `fyi color mix FF0000 0000FF` |
| `compare <hex1> <hex2>` | Delta E comparison + gradient | `fyi color compare FF6B35 3498DB` |
| `gradient <hex1> <hex2>` | Smooth perceptual gradient steps | `fyi color gradient FF0000 0000FF` |

### `fyi emoji` -- Emoji Tools (emojifyi)

| Command | Description | Example |
|---------|-------------|---------|
| `lookup <slug>` | Emoji metadata (char, codepoint, category, version) | `fyi emoji lookup fire` |
| `search <query>` | Search 3,953 emojis by keyword | `fyi emoji search heart` |
| `encode <char>` | 8 encodings (UTF-8, HTML, CSS, JS, Python, Java) | `fyi emoji encode "🔥"` |

### `fyi symbol` -- Symbol Encoding (symbolfyi)

| Command | Description | Example |
|---------|-------------|---------|
| `info <char>` | Unicode properties + 11 encodings | `fyi symbol info "@"` |
| `encode <char>` | 11 encoding formats (HTML, CSS, URL, UTF-8, etc.) | `fyi symbol encode "->"` |

### `fyi unicode` -- Unicode Characters (unicodefyi)

| Command | Description | Example |
|---------|-------------|---------|
| `info <codepoint>` | Full Unicode info (accepts U+hex, char, or hex) | `fyi unicode info U+2764` |
| `encode <codepoint>` | 17 encodings (HTML, CSS, JS, Python, Go, Rust, etc.) | `fyi unicode encode U+00E9` |
| `search <query>` | Search characters by name | `fyi unicode search heart` |

### `fyi font` -- Google Fonts (fontfyi)

| Command | Description | Example |
|---------|-------------|---------|
| `info <slug>` | Font metadata (family, weights, subsets, designer) | `fyi font info inter` |
| `css <slug>` | CSS import snippet + font-family declaration | `fyi font css roboto` |
| `pairings <slug>` | Font pairing recommendations | `fyi font pairings inter` |
| `search <query>` | Search Google Fonts by name | `fyi font search mono` |

### `fyi distance` -- Distance Calculation (distancefyi)

| Command | Description | Example |
|---------|-------------|---------|
| `calc` | Distance, bearing, midpoint, travel times | `fyi distance calc --lat1 37.57 --lon1 126.98 --lat2 35.68 --lon2 139.65` |
| `bearing` | Compass bearing between two points | `fyi distance bearing --lat1 40.7 --lon1 -74.0 --lat2 51.5 --lon2 -0.1` |
| `midpoint` | Geographic midpoint | `fyi distance midpoint --lat1 40.7 --lon1 -74.0 --lat2 51.5 --lon2 -0.1` |

### `fyi time` -- Timezone Operations (timefyi)

| Command | Description | Example |
|---------|-------------|---------|
| `now <tz>` | Current time in IANA timezone | `fyi time now America/New_York` |
| `diff <tz1> <tz2>` | Time difference between timezones | `fyi time diff Asia/Seoul America/New_York` |
| `convert <time> <from> <to>` | Convert time across timezones | `fyi time convert "2026-03-05 09:00" Asia/Seoul America/New_York` |

### `fyi unit` -- Unit Conversion (unitfyi)

| Command | Description | Example |
|---------|-------------|---------|
| `convert <value> <from> <to>` | Convert between 220 units in 20 categories | `fyi unit convert 100 celsius fahrenheit` |
| `categories` | List all measurement categories | `fyi unit categories` |
| `list <category>` | List units in a category | `fyi unit list temperature` |

### `fyi name` -- Name Tools (namefyi)

| Command | Description | Example |
|---------|-------------|---------|
| `romanize <text>` | Korean Revised Romanization | `fyi name romanize 김민준` |
| `elements <strokes>` | Five Elements for CJK stroke count | `fyi name elements 12` |

### `fyi holiday` -- Holiday Dates (holidayfyi)

| Command | Description | Example |
|---------|-------------|---------|
| `upcoming <country>` | Next N public holidays (ISO country code) | `fyi holiday upcoming US` |
| `easter <year>` | Western or Orthodox Easter date | `fyi holiday easter 2026` |
| `check <date> <countries>` | Check holidays on a specific date | `fyi holiday check 2026-12-25 US,KR,JP` |

### `fyi version` -- Plugin Status

Shows installed plugins and their versions.

```bash
fyi version
```

## Plugin Architecture

FYIPedia uses lazy-loading plugin discovery. Each tool is an independent PyPI package with its own CLI module. Only installed packages are registered -- missing packages are silently skipped.

```
fyipedia (hub)
├── fyi color    → colorfyi     (if installed)
├── fyi emoji    → emojifyi     (if installed)
├── fyi symbol   → symbolfyi    (if installed)
├── fyi unicode  → unicodefyi   (if installed)
├── fyi font     → fontfyi      (if installed)
├── fyi distance → distancefyi  (if installed)
├── fyi time     → timefyi      (if installed)
├── fyi name     → namefyi      (if installed)
├── fyi unit     → unitfyi      (if installed)
└── fyi holiday  → holidayfyi   (if installed)
```

## Available FYI Packages

| Plugin | Package | Description |
|--------|---------|-------------|
| `color` | [colorfyi](https://pypi.org/project/colorfyi/) | Color conversion (7 spaces), WCAG contrast, harmonies, shades, color blindness |
| `emoji` | [emojifyi](https://pypi.org/project/emojifyi/) | 3,953 emoji metadata, search, 8 encoding formats |
| `symbol` | [symbolfyi](https://pypi.org/project/symbolfyi/) | Symbol encoding (11 formats), Unicode properties |
| `unicode` | [unicodefyi](https://pypi.org/project/unicodefyi/) | Unicode character info, 17 encodings, 90 HTML entities |
| `font` | [fontfyi](https://pypi.org/project/fontfyi/) | 50 Google Fonts metadata, CSS snippets, font pairings |
| `distance` | [distancefyi](https://pypi.org/project/distancefyi/) | Haversine distance, bearing, midpoint, travel times |
| `time` | [timefyi](https://pypi.org/project/timefyi/) | Timezone operations, time differences, sunrise/sunset |
| `name` | [namefyi](https://pypi.org/project/namefyi/) | Korean romanization, Five Elements, CJK stroke count |
| `unit` | [unitfyi](https://pypi.org/project/unitfyi/) | 220 units across 20 categories, Decimal precision |
| `holiday` | [holidayfyi](https://pypi.org/project/holidayfyi/) | Holiday dates for 100+ countries, Easter calculation |

## Demo

![FYIPedia CLI demo](https://raw.githubusercontent.com/fyipedia/fyipedia/main/demo.gif)

## FYIPedia Ecosystem

Part of the [FYIPedia](https://fyipedia.com) open-source developer tools ecosystem. Also available as an [MCP server](https://pypi.org/project/fyipedia-mcp/) for AI assistants (Claude, Cursor, Windsurf).
