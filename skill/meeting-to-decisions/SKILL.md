---
name: meeting-to-decisions
description: Convert a raw meeting transcript, recording notes, or messy minutes into a clean, structured record of what was actually decided, who owns what, by when, and what's still open — so the meeting produces accountability instead of evaporating. Use this skill whenever someone shares meeting notes/transcript and wants the takeaways, asks "what did we decide", "summarize this meeting", "pull out the action items", "who's doing what", "turn these notes into something useful", or after any standup/sync/planning/client call where decisions and owners need to be captured. The output separates Decisions (settled) from Action items (owner + deadline) from Open questions (unresolved) from FYI (context), discards chit-chat, and explicitly flags decisions or actions that have NO owner — because an unowned action is the one that silently doesn't happen.
---

# Meeting-to-Decisions

Most meetings produce a transcript and nothing else. A week later nobody remembers what was decided, who agreed to do what, or which questions were left hanging — so the same things get re-litigated in the next meeting. This skill turns the raw, rambling record of a conversation into the four things that actually carry value out of the room.

## The one thing that actually matters

The single highest-value output is **the action table with an owner and a date on every row — and a loud flag on every action or decision that has neither.** An unowned action item is not an action item; it's a wish that will not happen, and it's exactly the thing that falls through the cracks and resurfaces as "wait, I thought *you* were doing that." Finding the unowned commitments is worth more than the prettiest summary.

## The four buckets (and the trash)

Every meaningful line in a meeting sorts into exactly one of four buckets. Everything else is trash — discard it ruthlessly.

1. **Decisions** — things that were *settled*. "We're going with X." "We're killing Y." "Approved." A decision changes the state of the world going forward; capture *what* was decided and, briefly, *why* (the rationale prevents re-litigating it next month).
2. **Action items** — things someone committed to *do*, each with an **owner** and a **due date**. This is the accountability layer. "Owner: unassigned" or "Due: ?" is a defect to flag, not a row to quietly accept.
3. **Open questions** — things raised but *not resolved*: unanswered questions, unresolved disagreements, "we need to figure out…", parked items. These are the seeds of the next meeting; surfacing them prevents the false sense that everything got handled.
4. **FYI / context** — information shared that isn't a decision or action but matters for the record: status updates, data points, "heads up that…". Keep the load-bearing ones; drop the rest.

**Trash:** greetings, tangents, war stories, scheduling chatter, repeated points, thinking-out-loud that went nowhere. Cutting this is most of the value — a 60-minute transcript usually has ~10 lines that matter.

## The method

### 1. Read the whole thing once before extracting
Decisions often get *reversed* later in the same meeting ("actually, let's not…"). If you extract linearly you'll capture the abandoned version. Read end-to-end first so you record the *final* state of each thread, not an intermediate one.

### 2. Pass through and tag each meaningful line into a bucket
Go line by line, assigning D / A / O / FYI / trash. When in doubt between Decision and Action: a Decision is a *choice that was made*; an Action is *work someone will do*. They often pair ("Decided: launch in TH first [D]" → "Wat to prep the TH landing page by Fri [A]").

### 3. For every action, hunt down owner and date
This is the core work. For each committed action, find:
- **Owner** — a *named person*, not a team ("Ops will handle it" → who in Ops? flag if unresolvable).
- **Due date** — an actual date or a concrete relative one ("by next standup," "EOW"). "Soon"/"later" = 🔴 no date.
- If either is missing in the transcript, **keep the row and flag it** `⚠️ NO OWNER` / `⚠️ NO DATE`. Do not invent one — surface the gap so a human assigns it. Inventing owners is worse than flagging the hole.

### 4. Catch the implicit decisions
The most-missed decisions are never announced as decisions. They're buried in agreement: "yeah that makes sense, let's do that," or a question that everyone tacitly answered and moved past. Re-scan for *consensus that was reached without anyone saying "we decided."* Those count.

### 5. Flag conflicts and ambiguity
If two people seemed to agree to contradictory things, or a decision was made that contradicts an earlier one, flag it explicitly rather than smoothing it over. "Decided X at 0:12 but A and B may not share the same understanding of X" is a high-value catch.

### 6. Emit the structured record
Output in paste-ready form (so it drops straight into Notion/Slack/email). Lead with the action table — it's what people act on.

## Output template

```
## 📋 [Meeting name] — [date]
[1-line context: who, why]

### ✅ Decisions
1. **[What was decided]** — [1-line rationale if given]
2. ...

### ⚡ Action Items
| # | Action | Owner | Due | Notes |
|---|--------|-------|-----|-------|
| 1 | Prep TH landing page | Wat | Fri Jun 30 | blocks launch |
| 2 | Get 3 broker LOIs | ⚠️ NO OWNER | ⚠️ NO DATE | flagged — needs assignment |

### ❓ Open Questions
- [Unresolved question / disagreement] — raised by [who], needs [what] to close
- ...

### ℹ️ FYI / Context
- [Load-bearing info shared]

### 🚩 Flags
- 2 action items have no owner (rows #2, #5) — assign before this closes
- Possible conflict: decision #1 (TH-first) vs. action #4 (assumes global launch)
```

## Pitfalls

- **Capturing the reversed decision.** If you extract before reading the whole transcript, you'll record the version that got walked back. Read fully first, record final state.
- **Inventing owners to make it look complete.** A tidy table where you guessed the owners is a *liability* — people trust it and the wrong person gets "assigned." Flag the hole; never fabricate accountability.
- **Missing implicit decisions.** The decision that wasn't announced ("…yeah, let's just do that") is the one most often lost. Specifically re-scan for tacit consensus.
- **Keeping the chit-chat.** A "summary" that's 80% of the transcript reworded is not a summary. If trash isn't getting cut hard, you're transcribing, not extracting.
- **Vague dates surviving.** "Soon," "ASAP," "later" are not dates. Flag them — an action without a real date doesn't get scheduled and doesn't get done.
- **Smoothing over conflict.** When the meeting left two people with different understandings, the helpful-looking move is to write one clean version. Don't — flag the divergence; it's the thing most likely to blow up later.
- **Losing the "why."** A decision with no rationale gets re-opened the moment someone forgets the reasoning. One line of *why* per decision saves the re-litigation meeting.

## Tips for higher fidelity

- If the transcript has **timestamps or speaker labels**, keep them on decisions/actions as provenance — "who committed to this and when" settles future disputes.
- If you have the **agenda or goal** of the meeting, check the output against it: an agenda item with no decision and no open-question is a thread that got dropped — flag it.
- For **recurring meetings**, the Open Questions from last time are the implicit agenda for this time; carry them forward.
- Distinguish **"decided" from "discussed."** Lots of meetings discuss something thoroughly and decide nothing. If a big topic produced no decision and no action, that itself is the finding: "discussed at length, no decision reached → still open."

## Relation to other skills

This is the extraction sibling of `interview-synthesis` (which pulls themes from many conversations) — both turn raw talk into structured, actionable records, but meeting-to-decisions optimizes for *accountability* (who owns what), while interview-synthesis optimizes for *insight* (what patterns recur). Use this one for syncs, standups, planning, and client calls; use interview-synthesis for user research and discovery.
