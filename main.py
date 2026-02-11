"""Command-line entrypoint for the project."""

from __future__ import annotations

import sys

from app import completion_message


def main(argv: list[str] | None = None) -> int:
    """Run the CLI app and print a completion message."""
    args = argv if argv is not None else sys.argv[1:]
    project_name = " ".join(args)
    print(completion_message(project_name))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
