"""Unified CLI for FYIPedia developer tools.

Lazily registers sub-commands for installed packages only.

Usage::

    fyi color FF5733
    fyi distance calc --lat1 37.57 --lon1 126.98 --lat2 35.68 --lon2 139.65
    fyi unit convert 100 celsius fahrenheit
    fyi time now America/New_York
    fyi emoji search fire
    fyi holiday upcoming US
    fyi name romanize 김민준
"""

from __future__ import annotations

from importlib import import_module

import typer

app = typer.Typer(
    name="fyi",
    help="FYIPedia — unified developer tools CLI.",
    invoke_without_command=True,
)

# Each entry: (sub-command name, module path to Typer app, help text)
_PLUGINS: list[tuple[str, str, str]] = [
    ("color", "colorfyi.cli", "Color conversions, harmonies, WCAG contrast"),
    ("emoji", "emojifyi.cli", "Emoji lookup, search, encoding"),
    ("symbol", "symbolfyi.cli", "Symbol encoding, Unicode properties"),
    ("unicode", "unicodefyi.cli", "Unicode character info, encoding"),
    ("font", "fontfyi.cli", "Google Fonts metadata, CSS, pairing"),
    ("distance", "distancefyi.cli", "Distance, bearing, midpoint calculations"),
    ("time", "timefyi.cli", "Timezone operations, time differences"),
    ("name", "namefyi.cli", "Korean romanization, Five Elements"),
    ("unit", "unitfyi.cli", "Unit conversion — 220 units, 20 categories"),
    ("holiday", "holidayfyi.cli", "Holiday dates, Easter, upcoming holidays"),
]


def _register_plugins() -> None:
    """Lazily discover and register installed FYIPedia package CLIs."""
    for cmd_name, module_path, help_text in _PLUGINS:
        try:
            mod = import_module(module_path)
            sub_app: typer.Typer = mod.app
            app.add_typer(sub_app, name=cmd_name, help=help_text)
        except (ImportError, AttributeError):
            # Package not installed — skip silently
            pass


_register_plugins()


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context) -> None:
    """FYIPedia — unified developer tools CLI."""
    if ctx.invoked_subcommand is None:
        _show_version()


@app.command()
def version() -> None:
    """Show fyipedia version and installed plugins."""
    _show_version()


def _show_version() -> None:
    from rich.console import Console
    from rich.table import Table

    from fyipedia import __version__

    console = Console()
    console.print(f"[bold]fyipedia[/bold] v{__version__}\n")

    table = Table(title="Installed Plugins")
    table.add_column("Plugin", style="cyan")
    table.add_column("Version", style="green")
    table.add_column("Status", style="yellow")

    for cmd_name, module_path, _ in _PLUGINS:
        pkg_name = module_path.split(".")[0]
        try:
            mod = import_module(pkg_name)
            ver = getattr(mod, "__version__", "?")
            table.add_row(cmd_name, ver, "installed")
        except ImportError:
            table.add_row(cmd_name, "-", "not installed")

    console.print(table)
