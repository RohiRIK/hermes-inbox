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
    parser.add_argument("action", nargs="?", default="view", choices=("view", "observe", "changes", "mark-seen", "ack", "snooze"))
    parser.add_argument("occurrence", nargs="?", type=int, help="Local observation occurrence for ack/snooze")
    parser.add_argument("--seconds", type=float, help="Explicit snooze duration, at most seven days")
    parser.add_argument("--consumer", default="owner", help="Independent observation consumer")
    parser.add_argument("--through", type=int, help="Explicit observed sequence to mark seen")
    parser.add_argument("--fleet", action="store_true",
                        help="Include Herald edges for the active profile (opt-in, disabled by default)")


def handle(args: argparse.Namespace) -> int:
    from .report import build_inbox, render_inbox

    action = getattr(args, "action", "view")
    if action != "view":
        from hermes_constants import get_hermes_home
        from .herald import profile_identity
        from .state import InboxState, InboxStateError
        from .observations import records
        import sqlite3
        try:
            home = get_hermes_home()
            state = InboxState(home, profile_identity(home))
            consumer = getattr(args, "consumer", "owner")
            if action == "observe":
                sequences = state.observe(records(build_inbox(home=home, fleet=bool(getattr(args, "fleet", False)))))
                result = {"created": len(sequences), "sequences": sequences}
            elif action == "changes":
                result = state.changes(consumer=consumer)
            elif action == "mark-seen":
                result = {"cursor": state.mark_seen(consumer=consumer, upto=getattr(args, "through", None))}
            elif action in ("ack", "snooze"):
                from .attention import AttentionState
                attention = AttentionState(state)
                occurrence = getattr(args, "occurrence", None)
                result = (attention.ack(occurrence) if action == "ack" else
                          attention.snooze(occurrence, getattr(args, "seconds", None)))
            else:
                raise ValueError("unknown action")
            print(json.dumps(result, indent=2))
            return 0
        except (InboxStateError, ValueError, OSError, sqlite3.Error):
            print(json.dumps({"error": "Local Inbox state unavailable or invalid action input"}))
            return 2
    data = build_inbox(fleet=bool(getattr(args, "fleet", False)))
    print(json.dumps(data, indent=2, default=str) if args.json else render_inbox(data))
    return 0