"""``hermes inbox`` argparse wiring."""

from __future__ import annotations

import argparse
import json

HELP = "Show everything in flight: background work, results, cron, sessions, kanban"
DESCRIPTION = (
    "A read-only view of Hermes activity for the active profile: what needs your attention "
    "(stalled or dropped delegations, failed cron runs, orphaned background processes, blocked "
    "kanban tasks), what is in progress, finished delegation results not yet delivered, upcoming "
    "cron jobs and open chat surfaces. Nothing is changed."
)


def setup_parser(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--json", action="store_true", help="Print the snapshot as JSON")
    parser.add_argument("--fleet", action="store_true",
                        help="Include Herald edges for the active profile (opt-in, disabled by default)")


def handle(args: argparse.Namespace) -> int:
    from .report import build_inbox, render_inbox

    data = build_inbox(fleet=bool(getattr(args, "fleet", False)))
    print(json.dumps(data, indent=2, default=str) if args.json else render_inbox(data))
    return 0