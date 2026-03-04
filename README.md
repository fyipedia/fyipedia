# fyipedia

Unified CLI for [FYIPedia](https://github.com/fyipedia) developer tools.

## Install

```bash
pip install "fyipedia[all]"     # All 10 tools
pip install "fyipedia[color,distance]"  # Just color + distance
```

## Usage

```bash
fyi color FF5733               # Color info
fyi distance calc --lat1 37.57 --lon1 126.98 --lat2 35.68 --lon2 139.65
fyi unit convert 100 celsius fahrenheit
fyi time now America/New_York
fyi emoji search fire
fyi holiday upcoming US
fyi name romanize 김민준
fyi version                    # Show installed plugins
```

## Available Plugins

| Plugin | Package | Description |
|--------|---------|-------------|
| `color` | colorfyi | Color conversions, harmonies, WCAG contrast |
| `emoji` | emojifyi | Emoji lookup, search, encoding |
| `symbol` | symbolfyi | Symbol encoding, Unicode properties |
| `unicode` | unicodefyi | Unicode character info, encoding |
| `font` | fontfyi | Google Fonts metadata, CSS, pairing |
| `distance` | distancefyi | Distance, bearing, midpoint calculations |
| `time` | timefyi | Timezone operations, time differences |
| `name` | namefyi | Korean romanization, Five Elements |
| `unit` | unitfyi | Unit conversion — 220 units, 20 categories |
| `holiday` | holidayfyi | Holiday dates, Easter, upcoming holidays |

## License

MIT
