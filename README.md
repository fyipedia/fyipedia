# fyipedia

[![PyPI](https://img.shields.io/pypi/v/fyipedia)](https://pypi.org/project/fyipedia/)
[![Python](https://img.shields.io/pypi/pyversions/fyipedia)](https://pypi.org/project/fyipedia/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

Unified CLI for the [FYIPedia](https://github.com/fyipedia) developer tools ecosystem. One command (`fyi`) gives you instant access to 10 specialized tools -- [color conversion](https://colorfyi.com/), [emoji lookup](https://emojifyi.com/), [symbol encoding](https://symbolfyi.com/), [Unicode search](https://unicodefyi.com/), [Google Fonts metadata](https://fontfyi.com/), [distance calculation](https://distancefyi.com/), [timezone operations](https://timefyi.com/), [Korean romanization](https://namefyi.com/), [unit conversion](https://unitfyi.com/), and [holiday dates](https://holidayfyi.com/) -- all from your terminal.

> **Install once, use everything.** Each plugin is loaded lazily -- only installed packages are registered. Install all 10 tools or pick just the ones you need.

## Install

```bash
pip install "fyipedia[all]"              # All 10 tools
pip install "fyipedia[color,distance]"   # Just color + distance
pip install "fyipedia[color,emoji,font]" # Pick any combination
pip install fyipedia                     # Core only (no plugins)
```

Requires Python 3.10+. Each plugin is an optional dependency -- install only what you need.

## Quick Start

```bash
# Convert a hex color to 7 color spaces (RGB, HSL, HSV, CMYK, Lab, OKLCH)
fyi color info FF6B35

# Check WCAG contrast between two colors
fyi color contrast 000000 FFFFFF

# Generate Tailwind-style shade palette
fyi color shades 3B82F6

# Simulate color blindness (protanopia, deuteranopia, tritanopia)
fyi color blindness FF5733
```

```bash
# Calculate distance between Seoul and Tokyo
fyi distance calc --lat1 37.57 --lon1 126.98 --lat2 35.68 --lon2 139.65

# Convert temperature
fyi unit convert 100 celsius fahrenheit

# Convert weight
fyi unit convert 70 kilogram pound
```

```bash
# Look up current time in a timezone
fyi time now America/New_York

# Search for emojis by keyword
fyi emoji search fire

# Look up an emoji by slug
fyi emoji lookup fire
```

```bash
# Find upcoming holidays in the US
fyi holiday upcoming US

# Calculate Easter date for any year
fyi holiday easter 2026

# Romanize Korean text (Revised Romanization)
fyi name romanize 김민준

# Look up a Unicode character
fyi unicode info U+2764

# Encode a symbol in 11 formats
fyi symbol info "@"
```

```bash
# Get Google Fonts metadata and CSS
fyi font info inter

# Find font pairings
fyi font pairings inter

# Show installed plugins and versions
fyi version
```

## Complete Command Reference

### `fyi color` -- Color Tools

| Command | Description | Example |
|---------|-------------|---------|
| `info <hex>` | Full color info in 7 color spaces | `fyi color info FF6B35` |
| `contrast <fg> <bg>` | WCAG 2.1 contrast ratio + AA/AAA checks | `fyi color contrast 000000 FFFFFF` |
| `harmonies <hex>` | 5 harmony types (complementary, analogous, triadic, etc.) | `fyi color harmonies FF6B35` |
| `shades <hex>` | Tailwind-style 50-950 shade palette | `fyi color shades 3B82F6` |
| `blindness <hex>` | Color blindness simulation (4 types) | `fyi color blindness FF5733` |
| `mix <hex1> <hex2>` | Mix two colors in perceptual Lab space | `fyi color mix FF0000 0000FF` |
| `compare <hex1> <hex2>` | Delta E comparison + gradient | `fyi color compare FF6B35 3498DB` |
| `gradient <hex1> <hex2>` | Smooth gradient steps | `fyi color gradient FF0000 0000FF` |

### `fyi emoji` -- Emoji Tools

| Command | Description | Example |
|---------|-------------|---------|
| `lookup <slug>` | Emoji metadata (char, codepoint, category, version) | `fyi emoji lookup fire` |
| `search <query>` | Search 3,953 emojis by keyword | `fyi emoji search heart` |
| `encode <char>` | 8 encodings (UTF-8, HTML, CSS, JS, Python, Java) | `fyi emoji encode "🔥"` |

### `fyi symbol` -- Symbol Encoding

| Command | Description | Example |
|---------|-------------|---------|
| `info <char>` | Unicode properties + 11 encodings | `fyi symbol info "@"` |
| `encode <char>` | 11 encoding formats (HTML, CSS, URL, UTF-8, etc.) | `fyi symbol encode "->"` |

### `fyi unicode` -- Unicode Characters

| Command | Description | Example |
|---------|-------------|---------|
| `info <codepoint>` | Full Unicode info (accepts U+hex, char, or hex) | `fyi unicode info U+2764` |
| `encode <codepoint>` | 17 encodings (HTML, CSS, JS, Python, Go, Rust, etc.) | `fyi unicode encode U+00E9` |
| `search <query>` | Search characters by name | `fyi unicode search heart` |

### `fyi font` -- Google Fonts

| Command | Description | Example |
|---------|-------------|---------|
| `info <slug>` | Font metadata (family, weights, subsets, designer) | `fyi font info inter` |
| `css <slug>` | CSS import snippet + font-family declaration | `fyi font css roboto` |
| `pairings <slug>` | Font pairing recommendations | `fyi font pairings inter` |
| `search <query>` | Search Google Fonts by name | `fyi font search mono` |

### `fyi distance` -- Distance Calculation

| Command | Description | Example |
|---------|-------------|---------|
| `calc` | Distance, bearing, midpoint, travel times | `fyi distance calc --lat1 37.57 --lon1 126.98 --lat2 35.68 --lon2 139.65` |
| `bearing` | Compass bearing between two points | `fyi distance bearing --lat1 40.7 --lon1 -74.0 --lat2 51.5 --lon2 -0.1` |
| `midpoint` | Geographic midpoint | `fyi distance midpoint --lat1 40.7 --lon1 -74.0 --lat2 51.5 --lon2 -0.1` |

### `fyi time` -- Timezone Operations

| Command | Description | Example |
|---------|-------------|---------|
| `now <tz>` | Current time in IANA timezone | `fyi time now America/New_York` |
| `diff <tz1> <tz2>` | Time difference between timezones | `fyi time diff Asia/Seoul America/New_York` |
| `convert <time> <from> <to>` | Convert time across timezones | `fyi time convert "2026-03-05 09:00" Asia/Seoul America/New_York` |

### `fyi unit` -- Unit Conversion

| Command | Description | Example |
|---------|-------------|---------|
| `convert <value> <from> <to>` | Convert between 220 units in 20 categories | `fyi unit convert 100 celsius fahrenheit` |
| `categories` | List all measurement categories | `fyi unit categories` |
| `list <category>` | List units in a category | `fyi unit list temperature` |

### `fyi name` -- Name Tools

| Command | Description | Example |
|---------|-------------|---------|
| `romanize <text>` | Korean Revised Romanization | `fyi name romanize 김민준` |
| `elements <strokes>` | Five Elements for CJK stroke count | `fyi name elements 12` |

### `fyi holiday` -- Holiday Dates

| Command | Description | Example |
|---------|-------------|---------|
| `upcoming <country>` | Next N public holidays (ISO country code) | `fyi holiday upcoming US` |
| `easter <year>` | Western or Orthodox Easter date | `fyi holiday easter 2026` |
| `check <date> <countries>` | Check holidays on a specific date | `fyi holiday check 2026-12-25 US,KR,JP` |

### `fyi version` -- Plugin Status

```bash
$ fyi version
                 FYIPedia v0.1.0
┌────────────┬─────────┬───────────┐
│ Plugin     │ Version │ Status    │
├────────────┼─────────┼───────────┤
│ colorfyi   │ 0.2.0   │ installed │
│ emojifyi   │ 0.2.0   │ installed │
│ symbolfyi  │ 0.2.0   │ installed │
│ unicodefyi │ 0.2.0   │ installed │
│ fontfyi    │ 0.2.0   │ installed │
│ distancefyi│ 0.1.0   │ installed │
│ timefyi    │ 0.1.0   │ installed │
│ namefyi    │ 0.1.0   │ installed │
│ unitfyi    │ 0.1.0   │ installed │
│ holidayfyi │ 0.1.0   │ installed │
└────────────┴─────────┴───────────┘
```

## Plugin Architecture

FYIPedia uses a **lazy-loading plugin system**. Each tool is an independent Python package with its own CLI module. FYIPedia discovers and registers them at startup:

```
fyipedia (hub)
├── fyi color    → colorfyi.cli.app    (if installed)
├── fyi emoji    → emojifyi.cli.app    (if installed)
├── fyi symbol   → symbolfyi.cli.app   (if installed)
├── fyi unicode  → unicodefyi.cli.app  (if installed)
├── fyi font     → fontfyi.cli.app     (if installed)
├── fyi distance → distancefyi.cli.app (if installed)
├── fyi time     → timefyi.cli.app     (if installed)
├── fyi name     → namefyi.cli.app     (if installed)
├── fyi unit     → unitfyi.cli.app     (if installed)
└── fyi holiday  → holidayfyi.cli.app  (if installed)
```

**How it works:**

1. Plugin registry defines 10 entries as `(command_name, module_path, help_text)` tuples
2. At startup, `importlib.import_module()` attempts to load each plugin's CLI module
3. Successfully loaded plugins are registered as Typer sub-commands
4. Missing packages are silently skipped -- no errors, graceful degradation
5. `fyi version` shows which plugins are installed and their versions

**Creating a plugin** -- any package that exports a `typer.Typer` app can integrate:

```python
# mypackage/cli.py
import typer
app = typer.Typer(help="My custom tool")

@app.command()
def hello(name: str) -> None:
    typer.echo(f"Hello, {name}!")
```

## Available Plugins

| Plugin | Package | PyPI | Description |
|--------|---------|------|-------------|
| `color` | [colorfyi](https://github.com/fyipedia/colorfyi) | [![PyPI](https://img.shields.io/pypi/v/colorfyi)](https://pypi.org/project/colorfyi/) | Color conversion (7 spaces), WCAG contrast, harmonies, shades, color blindness simulation |
| `emoji` | [emojifyi](https://github.com/fyipedia/emojifyi) | [![PyPI](https://img.shields.io/pypi/v/emojifyi)](https://pypi.org/project/emojifyi/) | 3,953 emoji metadata, search, 8 encoding formats |
| `symbol` | [symbolfyi](https://github.com/fyipedia/symbolfyi) | [![PyPI](https://img.shields.io/pypi/v/symbolfyi)](https://pypi.org/project/symbolfyi/) | Symbol encoding (11 formats), Unicode properties |
| `unicode` | [unicodefyi](https://github.com/fyipedia/unicodefyi) | [![PyPI](https://img.shields.io/pypi/v/unicodefyi)](https://pypi.org/project/unicodefyi/) | Unicode character info, 17 encodings, 90 HTML entities |
| `font` | [fontfyi](https://github.com/fyipedia/fontfyi) | [![PyPI](https://img.shields.io/pypi/v/fontfyi)](https://pypi.org/project/fontfyi/) | 50 Google Fonts metadata, CSS snippets, font pairings |
| `distance` | [distancefyi](https://github.com/fyipedia/distancefyi) | [![PyPI](https://img.shields.io/pypi/v/distancefyi)](https://pypi.org/project/distancefyi/) | Haversine distance, bearing, midpoint, travel times |
| `time` | [timefyi](https://github.com/fyipedia/timefyi) | [![PyPI](https://img.shields.io/pypi/v/timefyi)](https://pypi.org/project/timefyi/) | Timezone operations, time differences, sunrise/sunset |
| `name` | [namefyi](https://github.com/fyipedia/namefyi) | [![PyPI](https://img.shields.io/pypi/v/namefyi)](https://pypi.org/project/namefyi/) | Korean romanization, Five Elements, CJK stroke count |
| `unit` | [unitfyi](https://github.com/fyipedia/unitfyi) | [![PyPI](https://img.shields.io/pypi/v/unitfyi)](https://pypi.org/project/unitfyi/) | 220 units across 20 categories, Decimal precision |
| `holiday` | [holidayfyi](https://github.com/fyipedia/holidayfyi) | [![PyPI](https://img.shields.io/pypi/v/holidayfyi)](https://pypi.org/project/holidayfyi/) | Holiday dates for 100+ countries, Easter calculation |

## Features

- **10 tools in one CLI**: Color, emoji, symbol, Unicode, font, distance, time, name, unit, holiday
- **Lazy plugin loading**: Only installed packages are registered -- no startup penalty
- **Flexible installation**: Install all tools or pick specific ones via optional dependency groups
- **Graceful degradation**: Missing plugins are silently skipped, no import errors
- **Rich terminal output**: Formatted tables and colors via Rich
- **Type-safe**: Full type annotations, strict mypy, PEP 561 compliant
- **Zero lock-in**: Each plugin works standalone (`colorfyi info FF6B35`) or through the hub (`fyi color info FF6B35`)

## Also Available as MCP Server

Use all 10 tools from AI assistants (Claude, Cursor, Windsurf) via the [MCP hub server](https://github.com/fyipedia/fyipedia-mcp):

```bash
pip install "fyipedia-mcp[all]"
```

See the [fyipedia-mcp README](https://github.com/fyipedia/fyipedia-mcp) for integration guides.

## FYIPedia Developer Tools

Part of the [FYIPedia](https://github.com/fyipedia) open-source developer tools ecosystem:

| Package | PyPI | npm | Description |
|---------|------|-----|-------------|
| [colorfyi](https://colorfyi.com/) | [`colorfyi`](https://pypi.org/project/colorfyi/) | [`colorfyi`](https://www.npmjs.com/package/colorfyi) | Color conversion, WCAG contrast, harmonies, 809 named colors |
| [emojifyi](https://emojifyi.com/) | [`emojifyi`](https://pypi.org/project/emojifyi/) | [`emojifyi`](https://www.npmjs.com/package/emojifyi) | Emoji encoding & metadata for 3,953 Unicode emojis |
| [symbolfyi](https://symbolfyi.com/) | [`symbolfyi`](https://pypi.org/project/symbolfyi/) | [`symbolfyi`](https://www.npmjs.com/package/symbolfyi) | Symbol encoding in 11 formats + Unicode properties |
| [unicodefyi](https://unicodefyi.com/) | [`unicodefyi`](https://pypi.org/project/unicodefyi/) | [`unicodefyi`](https://www.npmjs.com/package/unicodefyi) | Unicode character lookup, 17 encodings + search |
| [fontfyi](https://fontfyi.com/) | [`fontfyi`](https://pypi.org/project/fontfyi/) | [`fontfyi`](https://www.npmjs.com/package/fontfyi) | Google Fonts metadata, CSS helpers, font pairings |
| [distancefyi](https://distancefyi.com/) | [`distancefyi`](https://pypi.org/project/distancefyi/) | [`distancefyi`](https://www.npmjs.com/package/distancefyi) | Haversine distance, bearing, travel times |
| [timefyi](https://timefyi.com/) | [`timefyi`](https://pypi.org/project/timefyi/) | [`timefyi`](https://www.npmjs.com/package/timefyi) | Timezone operations, time differences, sunrise/sunset |
| [namefyi](https://namefyi.com/) | [`namefyi`](https://pypi.org/project/namefyi/) | [`namefyi`](https://www.npmjs.com/package/namefyi) | Korean romanization, Five Elements, CJK stroke count |
| [unitfyi](https://unitfyi.com/) | [`unitfyi`](https://pypi.org/project/unitfyi/) | [`unitfyi`](https://www.npmjs.com/package/unitfyi) | Unit conversion, 220 units, 20 categories |
| [holidayfyi](https://holidayfyi.com/) | [`holidayfyi`](https://pypi.org/project/holidayfyi/) | [`holidayfyi`](https://www.npmjs.com/package/holidayfyi) | Holiday dates, Easter calculation, 100+ countries |
| **fyipedia** | [`fyipedia`](https://pypi.org/project/fyipedia/) | -- | Unified CLI (`fyi` command) for all 10 tools |
| [fyipedia-mcp](https://github.com/fyipedia/fyipedia-mcp) | [`fyipedia-mcp`](https://pypi.org/project/fyipedia-mcp/) | -- | Unified MCP server for AI assistants |

## Links

- [FYIPedia GitHub Organization](https://github.com/fyipedia) -- All repositories
- [fyipedia-mcp](https://github.com/fyipedia/fyipedia-mcp) -- MCP server for AI assistants
- [awesome-fyi](https://github.com/fyipedia/awesome-fyi) -- Curated list of FYIPedia resources
- [Source Code](https://github.com/fyipedia/fyipedia) -- MIT licensed

## License

MIT
