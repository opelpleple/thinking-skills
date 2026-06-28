# Stack variants

The escalation pattern is identical everywhere: cheap attempt → validate → retry → escalate, feeding failure context forward. Only the plumbing changes.

## Plain Python

Use `scripts/escalating_agent.py` directly. It is provider-agnostic in shape; swap the `_call` method to target a different SDK. Keep the `Tier` enum as the one place model IDs live.

## n8n

Map the loop onto nodes:

1. **Cheap model node** — an AI/LLM node configured with the cheap model.
2. **Validation node** — a Function (Code) node implementing your validator; it sets `valid = true/false` and a `reason` on the item.
3. **IF node** — if `valid`, route to success. If not, increment a counter.
4. **Counter** — store attempt count in *workflow static data* (`$getWorkflowStaticData`) for a single run, or in a **Supabase** row keyed by job ID if the run spans executions / you want durable history and analytics.
5. **Switch node** — when `counter >= threshold`, route to a second AI node configured with the **pricier model**; otherwise loop back to the cheap node with the failure `reason` merged into the prompt.

Notes:
- n8n's built-in node retries are *exception* retries — they re-run on error, but they don't know about *validation* failure or which model to use. You need the explicit IF/Switch + counter to get escalation, not just retry.
- Persisting the counter and the winning tier to Supabase gives you the escalation-rate metric for free, which is how you tell whether the cheap tier is pulling its weight.

## Claude Code sub-agents

Orchestrate via the Task tool. The pattern shifts from a loop in one process to an orchestrator coordinating sub-agents:

1. Orchestrator spawns a **cheap sub-agent** (Task tool, cheap model) with the task.
2. Orchestrator **validates** the returned result itself (structural/executable check, or a judge sub-agent).
3. On failure, the orchestrator spawns the sub-agent again with the failure reason appended — up to N times.
4. After N failures, the orchestrator spawns a **stronger sub-agent** (more capable model), carrying all failure reasons forward in the task brief.
5. Orchestrator returns the first result that passes validation.

The difference from the single-process version: the orchestrator owns the validator and the failure log, and "spawn a stronger model" literally means launching a new sub-agent with a different model rather than calling a different model ID in a loop. The decision logic — count failures, feed reasons forward, escalate the tier — is exactly the same.

## Generic / other frameworks (LangGraph, custom)

Model it as a state machine:
- **State:** `{ task, tier_index, attempt_in_tier, failure_log }`.
- **Node "attempt":** call the current tier with `task + failure_log`, run the validator.
- **Edge on pass →** done.
- **Edge on fail →** increment `attempt_in_tier`; if it is below N, loop back to "attempt"; if it has hit N, increment `tier_index` (escalate) and reset `attempt_in_tier`.
- **Terminal:** `tier_index` past the last tier → return the failure log.

Whatever the framework, the three invariants are the same: validate every output, feed failure reasons forward, and only escalate after a tier has genuinely used up its attempts.
