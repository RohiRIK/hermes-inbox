# Inbox — Hermes Fleet Inbox development plugin

A read-only snapshot of work in flight, with an opt-in view of locally observed
Herald dispatches. This is the plugin directory of an Inbox-only fork; see the
[root README](../README.md) for development status and the remaining roadmap.

The original Inbox came from Nous Research's Hermes Agent PR #81507 and
[hermes-labs-plugins](https://github.com/NousResearch/hermes-labs-plugins).
Its [MIT license](LICENSE) and upstream history are retained. This fork is
independently developed, not an officially supported Nous Research product.

## Installation status

`hermes plugins install inbox` selects the **upstream catalog entry**, not this
fork. No reviewed release pin for this development branch has been published.
Installation will be qualified against the actual nested repository layout and
immutable source revision before rollout. The shared plugin ID means replacement,
not side-by-side installation with upstream.

## Implemented candidate commands

```text
hermes inbox                  active-profile snapshot
hermes inbox --json           structured snapshot
hermes inbox --fleet           opt-in same-host Herald ledger view
hermes inbox --fleet --json    structured fleet observations and coverage
hermes -p work inbox           selected profile; plugin must be installed there
```

The default snapshot includes processes, native asynchronous delegations, cron,
open chat surfaces and the shared Kanban board. `--fleet` adds local Herald
records; it does not create dispatches, contact remote peers, poll automatically
or grant permission to act. There are no `--herald-fleet` or `--label` flags.

## Herald configuration and coverage

The adapter reads `hermes_herald.origin_name` and `hermes_herald.ledger_file` from
each supplied profile home's `config.yaml`. A falsy ledger path uses that home's
`hermes-herald.db`. Tilde expands normally; `$HERMES_HOME` and `${HERMES_HOME}`
expand to the **supplied profile home**, not another ambient profile. Unresolved
other variables fail closed rather than querying a credential store. Relative
paths retain Herald's current-working-directory semantics.

An explicit nonblank origin name takes precedence over the native profile ID.
Unknown identities cannot trigger unrestricted ledger reads. Fleet discovery is
limited to the native default home and identifiable same-host profiles; arbitrary
supplied directories do not cause discovery of the real user's profiles. At most
33 profile homes are considered, with explicit truncation disclosure.

`herald_meta` reports source availability, observation coverage and truncation.
Each source and the combined result are bounded (20 edges by default, maximum
500 for direct adapter calls). Shared-ledger observations are deduplicated and
conflicting observations are marked. Unreadable origins and other hosts remain
unknown; an empty local ledger does not prove the absence of incoming work.

Only safe identity/status/linkage metadata is collected. Full prompts,
instructions, reasoning and result previews are excluded. Work completion does
not imply an accepted outcome, independently verified evidence or user delivery.
Herald delivery modes (`callback`, `none`, `sync`) are not delivery receipts.

## Source boundary

JSON stores are read as files and SQLite is opened with `mode=ro`; Inbox never
repairs, prunes, migrates or rewrites native task stores. SQLite itself may create
WAL/SHM reader sidecars. Missing or unreadable sources are disclosed in text and
JSON, not treated as verified all-clear. Kanban remains a shared upstream store.
In-memory approvals and clarify prompts have no durable cross-process source;
answer them in the conversation that asked.

Persistent observations, consumer cursors, acknowledge/snooze and attention lanes
remain subsequent core stages. They will use plugin-owned state, not write native
truth. Proposed automatic hooks remain unactivated.

## Development

Tests run against Hermes core and isolated temporary stores, using native writer
fixtures for its databases. The compatibility workflow validates the manifest and
runs the Inbox suite on Linux, macOS and Windows. A passing source suite does not
establish installed-artifact or fleet acceptance.

Powered by caffeine and questionable life choices.
