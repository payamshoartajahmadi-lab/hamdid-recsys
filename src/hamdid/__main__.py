"""Minimal package entry point for foundation verification."""

import argparse

from hamdid import __version__


def main() -> None:
    """Parse the foundation CLI's help and version options."""
    parser = argparse.ArgumentParser(
        prog="hamdid",
        description="Hamdid package foundation; no recommendation commands yet.",
    )
    parser.add_argument("--version", action="version", version=__version__)
    parser.parse_args()


if __name__ == "__main__":
    main()
