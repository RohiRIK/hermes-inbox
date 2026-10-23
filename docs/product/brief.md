# Product brief — Hermes Fleet Inbox

## Purpose

A fleet-aware work-and-attention inbox, derived from Nous Research's Inbox plugin. Inbox observes work; Bob and the owning agents still coordinate it.

## Repository boundary

This fork contains Inbox only. Telegram Business, Workflow Record, their tests, documentation and artwork are excluded from the current tree. Upstream history, root/Inbox license text and attribution remain intact. No runtime data or private coordination files belong in the published repository.

## Implemented development slice

- The original process, delegation, cron, session and Kanban snapshot remains.
- `--fleet` explicitly opts into same-host native profile-ledger discovery.
- Herald configuration selects the ledger; the supplied profile home controls identity and `${HERMES_HOME}` expansion, not another ambient profile.
- Unknown identity fails closed. Missing, unreadable and truncated sources are disclosed. Other hosts and inaccessible origins remain unknown.
- Safe trace/parent IDs and observation provenance are retained. Prompt text, instructions, reasoning and result previews are not collected.

## Core implementation and release boundary

The candidate implements exact-ID work threads, persistent observations and
independent consumer cursors, occurrence-scoped acknowledge/snooze, and
owner/action/wait/done/unknown lanes. Missing action/approval/acceptance facts stay
unknown. Source tests do not establish independent review, installed-artifact or
live-pilot acceptance; these remain separate release gates.

## Live-pilot release gate

The live-pilot gate is documented in [live-pilot.md](live-pilot.md). It requires:
1. Frozen artifact review (no code changes after freeze)
2. Installed artifact test on the default profile under controlled lifecycle
3. Restart/cursor/ack/snooze/new-failure/isolation/coverage/truncation verification
4. Normal work shadow observation
5. The discovered profile roster verified sequentially, including custom configuration cases
6. Marketplace listing only after verified pilot and catalog eligibility — not promised

No automatic new cron, model changes, or destructive production tests. Stage window proposed 24–48h is a proposal, not started, and not scheduled.

## Non-goals and activation boundaries

No extra coordinator, autonomous task retries, provider changes, service restarts, automatic sends, task closures or upstream status rewrites. Proposed status-refresh, existing-result retrieval and snooze-expiry automation is not activated. A source reference is not verified evidence; a completed process is not an accepted outcome or proof of delivery.

The fork currently shares the `inbox` plugin identifier and `hermes inbox` command with upstream, so installation is an exclusive replacement, not proof of coexistence. The upstream catalog entry still installs upstream. A separate catalog listing requires material differentiation and maintainer acceptance; branding alone does not qualify.

Powered by caffeine and questionable life choices.