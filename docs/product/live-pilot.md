# Live-pilot release gate

**Purpose:** prove the installed build against real Hermes activity before asking
for marketplace distribution. Source tests, an installation receipt and a healthy
snapshot are three different pieces of evidence, not interchangeable success.

This is an operator-run checklist, not an automatic monitoring service. A fresh
snapshot reads durable source records; it is not a remote worker heartbeat.

## 1. Freeze, review and prepare rollback

- Record the immutable Git commit, plugin version, source-tree digest and Hermes
  runtime revision. Run the full native-schema test suite and plugin validator.
- Obtain an independent code/security review. Resolve material findings and rerun
  the affected gates before installing revised bytes.
- Back up the existing plugin, installation provenance, enablement settings and
  existing Inbox-owned state. Keep backups private; never publish runtime data.
- Pass only with an accepted, reproducible artifact and a usable rollback path.

## 2. Exercise a native installation

- Install the exact commit through `hermes plugins install`, including the nested
  `inbox` directory. Verify the installed manifest, recorded source/revision and
  code digest, not just the source checkout.
- In a fresh CLI process run default view, `--json`, `--fleet --json` and `--help`.
  Parse JSON and check coverage, truncation, lanes and local-state availability.
- First verify an isolated profile and then the default profile. Do not assume a
  long-running gateway reloaded code simply because a fresh CLI sees it.
- Missing sources must be named; they must not produce a global all-clear.

## 3. Controlled real lifecycle on the default profile

- Commission one harmless, explicitly identified read-only fleet task. Record its
  exact dispatch/trace IDs; never use a similar title to correlate work.
- Capture a snapshot while it is dispatched/running and another after it settles.
  Compare Inbox with the native dispatch receipt and persisted ledger. Record any
  delay between task completion, ledger update and Inbox observation.
- Run `observe --fleet`; confirm `changes --consumer pilot` includes the exact
  observed item and changes. Repeating the same unchanged snapshot must not create
  another event for that item. Other real concurrent changes may create events.
- A completed task with no accepted-outcome receipt must remain outcome-unknown.
  Callback mode alone must not become proof of delivery to the human owner.
- Use only this commissioned item's occurrences for local acknowledgment/snooze
  exercises. Do not hide unrelated production failures just to satisfy a test.

## 4. Persistence, isolation and adversarial cases

- In separate fresh CLI processes, verify observation/cursor/attention persistence.
  A process restart is not a service restart; no infrastructure restart is needed.
- Mark a specific observed sequence seen for `pilot`; confirm another consumer's
  cursor is unchanged. Plain viewing and `changes` must not advance either one.
- Acknowledge one occurrence: its local attention hides, but raw source execution,
  failure, outcome and delivery remain unchanged. A new changed failure resurfaces.
- Snooze a separate occurrence for a short explicit duration; it hides before the
  deadline and reappears on the next view after expiry. No cron is required.
- Use isolated native-schema fixtures, not destructive production edits, to test
  repeated failures, locked/corrupt/absent sources, ambiguous parent links, cycles,
  invalid arguments, bounded-result overflow and profile/consumer separation.
- Compare source database contents and JSON-store hashes in controlled fixtures
  before/after all local attention actions. SQLite reader sidecars are not source
  task updates. Never assert byte stability of concurrently active production DBs.

## 5. Observe normal work

- Run the accepted candidate alongside ordinary work and save redacted snapshots
  with timestamps, exact source coverage and matching native receipts.
- Look for missing tasks, duplicate threads, misleading ownership, stale state,
  leaked prompts/results, incorrect suppression and unexpected local writes.
- Record command latency, actual coverage limits and unresolved unknowns. No issue
  may be silently treated as success simply because a command exited zero.
- A 24–48-hour observation window is recommended before public distribution. That
  elapsed-time gate cannot be replaced by fast fixtures or claimed in advance.
  This document creates no schedule and does not itself start that window.

## 6. Sequential profile qualification

- After the default-profile gate passes, qualify the remaining discovered native
  profiles, including Felix. Record the actual roster rather than a hard-coded
  number as a universal product property.
- Per profile verify native install/provenance/digest, fresh CLI snapshots and a
  dedicated pilot consumer. Verify isolated attention state with isolated fixtures
  or a profile-owned harmless pilot occurrence; never acknowledge another task.
- On a failure stop that rollout lane, preserve evidence and restore the previous
  plugin with the native installer. Do not delete user state or keep propagating a
  failed artifact. Fix, refreeze and rerun the affected gates.

## 7. Marketplace readiness is a separate decision

Required evidence: accepted independent review; green source and installed-artifact
checks; controlled live lifecycle; persistence/isolation/failure checks; completed
normal-work observation; a qualified profile roster; truthful docs and our own
verified artwork; no private data; preserved licenses; catalog-policy eligibility.

Passing these gates makes the candidate eligible for a release/submission decision.
It does **not** create a listing, replace the upstream catalog plugin, establish
maintainer acceptance or authorize a public marketplace submission automatically.
External publication follows the owner's release approval.

Automatic status polling, result retrieval and automatic repairs remain outside
this candidate. The operator executes this checklist; the owner does not need to
manually run every test or approve each routine test command again.
