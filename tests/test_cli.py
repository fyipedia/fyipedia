"""Tests for the fyipedia unified CLI."""

from typer.testing import CliRunner

from fyipedia.cli import _PLUGINS, app

runner = CliRunner()


def test_help() -> None:
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "FYIPedia" in result.output


def test_version_command() -> None:
    result = runner.invoke(app, ["version"])
    assert result.exit_code == 0
    assert "fyipedia" in result.output
    assert "Installed Plugins" in result.output


def test_no_args_shows_version() -> None:
    """No args invokes the callback which shows version info."""
    result = runner.invoke(app, [])
    assert result.exit_code == 0
    assert "fyipedia" in result.output


def test_plugins_list_has_10_entries() -> None:
    assert len(_PLUGINS) == 10
