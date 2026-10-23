# Hermes Fleet Inbox

A work-and-attention inbox for Hermes agents, derived from Nous Research's Inbox plugin.

**Development preview — not a released or fleet-accepted build.** The upstream
catalog command `hermes plugins install inbox` still installs the upstream plugin,
not this fork. Development code is not automatically installed on any profile.

## What this repository contains

This is an **Inbox-only fork**. The unrelated Telegram Business and Workflow Record
plugins, their tests, documentation and artwork have been removed from the current
tree. Upstream Git history, attribution and the MIT license are preserved.

- `inbox/`: plugin implementation and tests.
- `docs/product/`: product scope and boundaries.
- `.github/workflows/`: Inbox validation and compatibility tests.

## What works in the development candidate

The original read-only snapshot covers background processes, native async
delegations, scheduled jobs, open sessions and the shared Kanban board.

The first Herald integration adds `--fleet` and reads locally available dispatch
records without exposing full prompts or result previews. **This is a partial
implementation, not proof of complete fleet coverage.** Ledger configuration,
profile isolation and coverage disclosure are being qualified before acceptance.
Missing or inaccessible sources must remain explicitly unavailable, not all-clear.

```text
hermes inbox                 active-profile snapshot
hermes inbox --json          machine-readable snapshot
hermes inbox --fleet --json  candidate Herald view; requires this fork installed
```

## Remaining development stages

1. Qualify the Herald adapter and explicit fleet coverage.
2. Link work threads using exact native trace and parent IDs, never titles.
3. Persist observations and per-consumer "new since last check" cursors.
4. Add local acknowledge/snooze state with new-failure and expiry resurfacing.
5. Present owner/action/wait/done/unknown lanes with evidence provenance.
6. Review a frozen artifact, verify an installed build on one profile, then
   qualify the remaining profiles before claiming fleet readiness.

These stages are **planned, not shipped** unless explicitly described otherwise
above. A passing adapter test suite is not completion of the product plan.

## Safety boundary

- Native task, session, cron and dispatch stores are read-only sources.
- Future Inbox-owned state may record observations, cursors and attention only.
  It cannot turn a native failure into success or close the source task.
- Execution, accepted outcome, evidence, result delivery and acknowledgment are
  different facts; one does not prove another.
- "Agent can act" is a classification, not execution permission.
- Automatic status refresh, existing-result retrieval and snooze-expiry hooks
  are plans only. They are not activated by installing this development candidate.
- No task reruns, model/provider changes, service restarts, external sends or
  autonomous repairs are enabled by this repository.
- Private ledgers, runtime databases, prompts, coordination plans and credentials
  are not repository content.

## Development and installation status

The plugin retains the nested `inbox/` layout. Compatibility tests run against
Hermes core and seed isolated temporary data. A release will include the exact
repository/subdirectory and immutable commit to install; there is no accepted
release pin yet. Do not manually overwrite a running plugin or edit profile
configuration to infer that this candidate is installed.

Catalog eligibility is a separate maintainer-controlled process. This fork does
not replace the upstream catalog listing and is not an officially supported Nous
Research product.

## Origin and license

Derived from the Inbox plugin in
[NousResearch/hermes-labs-plugins](https://github.com/NousResearch/hermes-labs-plugins).
Upstream copyright notices and the [MIT license](LICENSE) are retained.

Powered by caffeine and questionable life choices.
