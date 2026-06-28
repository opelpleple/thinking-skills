---
name: model-escalation
description: Implement cost-aware model escalation (tiered agent fallback) — a cheap model attempts a task, and if it fails a configurable number of times, the work escalates to a more capable, more expensive model, with failure context fed forward. Use this skill whenever the user wants to make an agent cheaper or more token/cost-efficient, mentions model fallback, retry logic, escalation, tiered models, routing between cheap and expensive LLMs, "use Haiku first then Opus", "spawn a bigger model if the small one fails", failure handling for agents, output validation for LLMs, or any setup where a small model should do the easy work and a big model is only paid for when actually needed. Also trigger for designing agent reliability, building validators that check LLM output quality, or reducing inference cost on agentic/automation workflows (Python, n8n, Claude Code sub-agents).
---

# Model Escalation (Tiered Agent Fallback)

Make agents **cheap by default and expensive only when they have to be**. A low-cost model attempts the task; if it fails repeatedly, the work escalates up a ladder of more capable, more expensive models. Failure reasons from each attempt are passed forward, so the next model starts ahead instead of from scratch.

This is the pattern behind "run Haiku, and only pay for Opus when Haiku can't cut it."

## The one thing that actually matters

The escalation loop is the easy 20%. The hard 80% is **detecting failure** — deciding whether an output is good enough to accept or bad enough to retry/escalate. An escalation system is only as good as its validator: if you can't reliably tell that the cheap model produced garbage, escalation does nothing. Spend your design effort here.

For how to build good validators (structural, executable, and LLM-as-judge), read `references/validators.md`.

## The second trap: escalating blind

If you bump from a cheap model to an expensive one **without telling it what the cheap one got wrong**, you pay more and start over from zero — you wasted the escalation. Always append each failure reason to the prompt for the next attempt. This is what makes escalation worth paying for, and it frequently lets the *cheap* model self-correct on attempt 2 so you never escalate at all.

## The algorithm

Order models cheapest → most expensive, then:

1. For each tier, attempt the task up to **N** times (default N = 2).
2. After each attempt, run the validator. If it passes → **return immediately**.
3. If it fails, record the failure reason and append it to the prompt for the next attempt.
4. If a tier uses up its N attempts, **escalate to the next tier** — carrying *all* accumulated failure reasons forward.
5. If every tier fails, return the full failure log so the caller can decide what to do (alert a human, fall back to a default, etc.).

The whole thing is a nested loop plus a counter. Runnable reference implementation with two example validators: `scripts/escalating_agent.py`. Run it directly to see escalation and token accounting in action.

## Choosing N (attempts per tier)

N = 2 is a sane default, but it is not sacred:

- **Deterministic failures** (the model genuinely can't do the task) recur on retry — retrying the same tier just burns tokens. Escalate sooner, sometimes after a single failure.
- **Stochastic failures** (temperature noise, occasionally-malformed JSON) are worth retrying at the same tier before escalating, because the next sample often succeeds for free.

Where you can cheaply tell the two apart, do. Otherwise default to 2 and tune from logs.

## Skip the ladder when you already know

Escalation is for tasks that are "probably right, but not sure." If a task is **known-hard up front** (multi-step reasoning, ambiguous extraction, long-context synthesis), classify it and route straight to the strong model. Paying for two doomed cheap attempts before escalating is pure tax. A single cheap classifier call at the top of the pipeline usually pays for itself many times over.

## Defining the model tiers

Use the cheapest model that *can* pass for the easy majority of inputs, and reserve the strong model for the hard tail. For Claude, a common ladder is **Haiku → Sonnet → Opus**.

Model IDs change over time — always confirm the current strings before shipping rather than hardcoding from memory. The reference implementation isolates them in a single `Tier` enum so there is exactly one place to update.

## Measuring whether it actually saved money

The entire point is cost. Instrument it:
- Log which tier ultimately succeeded, per task.
- Track tokens (in/out) per attempt; the reference impl already accumulates these.
- Watch the **escalation rate**: if almost everything escalates, your cheap tier is mis-chosen (drop it or move work up). If almost nothing does, you may be able to push more work down to an even cheaper tier.

## Stack variants

The pattern is identical everywhere — only the plumbing differs. See `references/stack-variants.md` for concrete mappings:
- **Plain Python** — the reference implementation.
- **n8n** — error branch + a counter in workflow static data or a Supabase row, routing to a node configured with the pricier model once the counter crosses the threshold.
- **Claude Code sub-agents** — orchestrate via the Task tool: a cheap sub-agent attempts the work, the orchestrator validates, and spawns a stronger sub-agent on repeated failure.
