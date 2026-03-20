#!/usr/bin/env python3
"""Legacy Beast dashboard shim.

Kept for backward compatibility; delegates to the unified CLI.
"""

import argparse
import sys


def main() -> None:
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--summary", action="store_true")
    parser.add_argument("--export", action="store_true")
    parser.add_argument("--filename", type=str)
    args, _unknown = parser.parse_known_args()

    from cli import main as cli_main

    sys.argv = [sys.argv[0], "dashboard", "--type", "beast"]
    if args.summary:
        sys.argv.append("--summary")
    if args.export:
        sys.argv.append("--export")
    if args.filename:
        sys.argv.extend(["--filename", args.filename])

    print("⚠️  Deprecated entrypoint: use `python cli.py dashboard ...` instead.")
    cli_main()


if __name__ == "__main__":
    main()
