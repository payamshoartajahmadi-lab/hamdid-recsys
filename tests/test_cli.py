"""Exercise the installed module from outside the repository."""

import os
import subprocess
import sys
from importlib.metadata import version
from pathlib import Path


def run_cli(cwd: Path, *arguments: str) -> subprocess.CompletedProcess[str]:
    """Use the active environment without inheriting a source-path override."""
    repository = Path(__file__).resolve().parents[1]
    assert not cwd.resolve().is_relative_to(repository)
    environment = os.environ.copy()
    environment.pop("PYTHONPATH", None)
    return subprocess.run(
        [sys.executable, "-m", "hamdid", *arguments],
        cwd=cwd,
        env=environment,
        capture_output=True,
        text=True,
        encoding="utf-8",
        timeout=10,
        check=False,
    )


def test_version_matches_installed_metadata(tmp_path: Path) -> None:
    result = run_cli(tmp_path, "--version")

    assert result.returncode == 0, result.stderr
    assert result.stdout == f"{version('hamdid-recsys')}\n"
    assert result.stderr == ""


def test_help_exits_successfully(tmp_path: Path) -> None:
    result = run_cli(tmp_path, "--help")

    assert result.returncode == 0, result.stderr
    assert "usage: hamdid" in result.stdout
    assert "--help" in result.stdout
    assert "--version" in result.stdout
    assert result.stderr == ""


def test_invalid_argument_is_rejected(tmp_path: Path) -> None:
    result = run_cli(tmp_path, "--invalid-option")

    assert result.returncode == 2
    assert result.stdout == ""
    assert "unrecognized arguments: --invalid-option" in result.stderr
