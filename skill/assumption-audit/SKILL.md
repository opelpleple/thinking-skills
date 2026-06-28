---
name: assumption-audit
description: Surface, classify, and prioritize the hidden assumptions buried inside a plan, strategy, business case, spec, forecast, or investment thesis — then identify the cheapest tests that would prove or kill the riskiest ones before you bet on them. Use this skill whenever a plan "looks solid" but hasn't been pressure-tested, when a forecast or business case rests on numbers nobody has validated, when estimating, when writing or reviewing a strategy doc or PRD, or when someone says "this should work", "assuming X", "we expect", "obviously", "the model says", "de-risk this", or "what are we taking for granted". Distinct from a risk list (which asks what bad thing could happen) — an assumption audit asks what we are silently treating as TRUE that, if false, breaks everything, and then ranks those beliefs by how load-bearing and how unverified they are.
---

# Assumption Audit

Every plan is a stack of beliefs wearing a trenchcoat. Some are verified. Most are guesses no one labeled as guesses. The dangerous ones are the beliefs that are **simultaneously load-bearing and unverified** — if they're wrong, the whole plan collapses, and nobody actually checked.

An assumption audit drags those beliefs into the open, tags each one, and tells you the cheapest experiment that would turn the scariest guess into knowledge before you've committed real money or time.

## The one thing that actually matters

The deliverable is a short list: **the 3–5 assumptions that are both most load-bearing and most unverified, each paired with the cheapest test that would settle it.** Everything else — the full ledger, the tags — is scaffolding to produce that list. A plan rarely dies from a known risk; it dies from a guess everyone treated as a fact. Your job is to find which guess that is *before* it's expensive, and to design a cheap probe for it *this week*.

## The core distinction: load-bearing vs. unverified

Two independent axes. Plot every assumption on both:

- **Load-bearing** — if this is false, how much of the plan breaks? (a little / a feature / the whole thing)
- **Verified** — how do we actually know it's true? (proven with evidence / inferred / pure guess)

The matrix tells you where to spend:

```
                  UNVERIFIED  ───────────────►  VERIFIED
   LOAD-BEARING    🔴 TEST THIS WEEK            🟢 fine, but re-check if it drifts
        │          (a guess your plan
        │           depends on — the
        │           killer lives here)
        ▼
   NOT LOAD-       🟡 note it, cheap to         ⚪ ignore
   BEARING         be wrong, monitor
```

The 🔴 quadrant — **load-bearing AND unverified** — is the only thing that should keep you up at night. A verified load-bearing assumption is fine. An unverified trivial one doesn't matter. The audit exists to isolate the red quadrant and shrink it.

## The method

### 1. Extract every assumption — read the plan like a prosecutor

Go through the plan/doc/model sentence by sentence and pull out every claim that is being *treated as true without proof*. Hunt specifically for the linguistic tells of a buried assumption:

- **Hedge words doing heavy lifting:** "should," "expect," "likely," "assuming," "once we," "by then."
- **Confident adverbs hiding a guess:** "obviously," "clearly," "of course," "naturally."
- **Numbers with no cited source:** conversion rates, CAC, adoption %, timelines, "the model says," "industry standard."
- **Passive constructions that hide an actor:** "it will be integrated," "users will be migrated" — by whom, when, with whose buy-in?
- **Causal leaps:** "we'll launch, *so* revenue will grow" — every "so"/"therefore" is an assumption that the cause produces the effect.
- **Inherited givens:** things copied from a previous plan or a competitor that were never true for *you*.

Don't judge yet. Just list them. Aim for completeness — 15–40 raw assumptions is normal for a real plan.

### 2. Tag each assumption

For every item, assign:

- **Type:** Market / Customer / Technical / Financial / Operational / Team / External-dependency / Regulatory.
- **Load-bearing:** Low / Medium / High (how much breaks if false).
- **Verification status:** ✅ Proven (cite the evidence) / 🟨 Inferred (reasonable but not checked) / 🟥 Guess (we made it up).
- **Falsifiability:** can you even state what evidence would prove it false? An assumption you can't falsify is one you can't test — flag it; vague beliefs hide here.

### 3. Rank by the red quadrant

Sort to the top everything tagged **High load-bearing + 🟥 Guess** (and then High + 🟨 Inferred). These are your kill-risks. Usually 3–6 of them carry the whole plan.

A sharp framing for each: *"This plan is a bet that ___ is true. If it's not, ___ happens."* If you can't fill that in for your top assumptions, you don't yet understand what you're betting on.

### 4. Design the cheapest disproof for each top assumption

For each red-quadrant assumption, ask: **what is the smallest, fastest, cheapest thing that would tell me this is wrong?** Bias hard toward cheap disconfirmation, not expensive confirmation. Examples by type:

- **Customer/demand:** 10 problem-interviews; a fake-door / landing-page smoke test; pre-sell to 3 design partners; a single cold-outreach batch.
- **Willingness-to-pay:** put a real price on a real page and count clicks-to-checkout; ask for an LOI, not an opinion.
- **Technical feasibility:** a one-day spike on the *hardest* unknown part only (not the easy 80%).
- **Adoption/behavior-change:** watch 5 real users try the current workaround; a Wizard-of-Oz manual version before building.
- **Financial:** rebuild the key number from independent bottom-up inputs and see if it survives; sensitivity-test it (at what value does the plan stop working?).
- **Dependency/team:** literally ask the owning person/team "are you committed to X by date Y?" and get a yes in writing.

The test should be runnable in **days, not quarters**, and should be designed to *fail loudly* if the assumption is false. A test that can only confirm is worthless — design for disproof.

### 5. Sequence the plan around the tests

Reorder the actual work so the riskiest assumption gets tested *first and cheapest*, before the expensive build that depends on it. The highest-leverage move an audit produces is often "don't build the thing yet — spend three days proving the one belief the whole thing rests on."

## What good output looks like

| # | Assumption | Type | Load | Status | The bet | Cheapest disproof | When |
|---|---|---|---|---|---|---|---|
| 1 | Brokers will pay 200k+/yr for a TrustScore | Financial | High | 🟥 Guess | "If they won't, there is no business." | Put pricing on a real page + 20 sales calls to pricing | This week |
| 2 | We can match entities to brands well enough to score | Technical | High | 🟨 Inferred | "If match rate <10%, scores aren't credible." | 1-day spike on the match pipeline only | This week |
| 3 | "เอส" can own SEO + Fake-Detect + 100Media at once | Team | High | 🟥 Guess | "If not, 3 KRs slip together." | Ask him + map his real weekly capacity | Today |
| 4 | News audience will tolerate the pause | Customer | Med | 🟨 Inferred | "If they churn, relaunch is harder." | Watch traffic/retention over pause window | Ongoing |

Four rows of "here's the bet, here's the cheap disproof" is worth more than a 40-line strategy memo.

## Pitfalls

- **Auditing only the assumptions you can answer.** People surface the comfortable, verifiable assumptions and skip the terrifying unfalsifiable one at the core. The scariest assumption is usually the one you most want to skip.
- **Designing tests that can only confirm.** "Let's build it and see if people like it" is not a test of "people want it." Design for disproof — what result would make you abandon the plan?
- **Treating inherited numbers as proven.** A conversion rate copied from a deck, a CAC from a blog post, "industry standard" anything — these are 🟥 guesses until *you* verified them for *your* context. Pasted ≠ proven.
- **Confusing load-bearing with scary.** A vivid risk that breaks one feature matters less than a boring assumption that the whole revenue model rests on. Rank by load-bearing × unverified, not by how dramatic it feels.
- **One pass and done.** Assumptions drift as you learn. Re-run the audit at each major milestone; a green assumption can go red when conditions change.
- **No date on the test.** "We should validate that" with no owner and no date never happens. Every red-quadrant assumption gets a test, an owner, and a this-week-ish date, or the audit changed nothing.

## Relation to other skills

- Run **before** committing real resources; pairs naturally with `pre-mortem` (pre-mortem finds *failure modes*, assumption-audit finds the *false beliefs* underneath them — a pre-mortem cause is often just an assumption that turned out 🟥).
- The cheap-disproof tests are mini-experiments; if one is "build a tiny thing to learn," that's a spike.
- For business cases and forecasts, the financial assumptions especially deserve the rebuild-from-independent-inputs treatment in step 4.
