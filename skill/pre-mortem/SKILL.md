---
name: pre-mortem
description: Run a structured pre-mortem on a project, launch, decision, plan, bet, or initiative BEFORE committing to it — by imagining it has already failed and working backwards to find what killed it. Use this skill whenever someone is about to commit to something risky and irreversible: a product launch, a big hire, a fundraise, a migration, a partnership, a strategic bet, a quarter's roadmap, a major purchase. Trigger on phrases like "we're about to launch", "should we do this", "we've decided to go with X", "kickoff", "before we commit", "de-risk this plan", "what could go wrong", "stress-test this decision", or any moment of optimism right before a point of no return. Distinct from grill-me (which attacks the idea as it stands NOW); a pre-mortem attacks from an imagined FUTURE where the thing already died, which surfaces a different and usually larger set of failure modes.
---

# Pre-Mortem

Imagine the project is dead. It's six months from now and the thing failed — publicly, expensively, undeniably. **Now write the post-mortem before you've spent a baht.**

A pre-mortem flips the psychology of planning. When you ask "what could go wrong?" people stay loyal to the plan and produce polite, hedged risks. When you *assert* the failure as fact and ask "what killed it?", the same people suddenly generate concrete, specific, uncomfortable causes they were suppressing to be team players. This is the entire trick, and it is backed by decades of decision research (Gary Klein's "prospective hindsight" raises the number and specificity of causes people can name by ~30%).

## The one thing that actually matters

The output is not a list of worries — it's a **ranked set of failure causes, each with an owner, an early-warning signal, and a mitigation or a kill-condition.** A pre-mortem that ends in "wow, lots of risks, anyway let's go" was theater. A real one changes the plan, adds a tripwire, or kills the project *today* while it's still cheap to kill. If nothing about the plan changes after the exercise, you did it wrong.

## The mental move that unlocks it

Do not ask "what are the risks?" — that keeps people inside the optimistic frame. Instead state, in the past tense, as settled fact:

> "It's [6 months / 1 year] from now. We did exactly what we're planning. It failed badly. We're in the room doing the post-mortem. **Why did it fail?**"

The past-tense certainty is load-bearing. "Could fail" invites defense of the plan; "did fail" invites explanation. Keep every prompt in that failed-future tense throughout.

## The method

### 1. Define the failure crisply, with a date and a number

Vague failure ("it didn't go well") produces vague causes. Pin it: *"By Dec 31 we had <500 signups against a 5,000 target and the board cut the budget."* A dated, quantified failure forces dated, quantified causes. Write 1–2 sentences of what "failed" concretely looks like before generating any causes.

### 2. Generate causes across every category — not just the comfortable one

Teams over-index on the failure mode they're already afraid of (usually technical) and ignore the ones that actually kill projects (usually market, people, or timing). Force coverage of all of these:

- **Market / demand** — nobody wanted it; the need was assumed, not verified; willingness-to-pay was imaginary.
- **Execution / technical** — it was harder than estimated; the hard part wasn't the part we planned for; integration/scale/data quality bit us.
- **People / org** — the owner left; it was nobody's real priority; two teams each assumed the other was doing it; key skill missing.
- **Timing / sequencing** — a dependency wasn't ready; we shipped into a bad window; a competitor or regulation moved first.
- **Money / unit economics** — CAC > LTV; the cost model was wrong; we ran out of runway before the payoff.
- **Adoption / change management** — users had to change behavior and didn't; internal teams didn't adopt it; onboarding was a cliff.
- **External / regulatory** — a rule, platform policy, or partner dependency changed under us.

Generate **at least 2 causes per category** before filtering. Quantity first, judgment later — the cause you'd self-censor is often the real one.

### 3. Score each cause: Likelihood × Impact

Rate each on a simple 1–3 (or 1–5) for **how likely** it is to occur and **how badly** it hurts if it does. `Likelihood × Impact` gives a severity score. Sort descending. The top of this list is where the entire plan's fate actually lives — typically 3–5 causes dominate.

### 4. For every high-severity cause, demand three things

A risk without these three is just anxiety:

- **Early-warning signal** — the *observable, measurable* leading indicator that this failure is starting to happen. ("Week-2 activation rate < 20%." "Three standups in a row where the integration is 'almost done'.") This is the most valuable output: a tripwire you can watch *before* it's fatal.
- **Mitigation** — what you change in the plan *now* to lower likelihood or impact. Sometimes the answer is to run a cheap test this week that converts a guessed cause into a known one (see `assumption-audit`).
- **Kill / pivot condition** — the pre-agreed line that, if crossed, means stop or change course. Deciding this *before* you're emotionally and financially committed is the whole point; in the moment, sunk cost will not let you decide it honestly.

### 5. Decide, and record what changed

End with an explicit verdict: **proceed / proceed-with-changes / pivot / kill.** List the concrete changes made to the plan and the tripwires you're now committed to watching. This record is also your real post-mortem starter if it does fail — you'll know exactly which signal you ignored.

## What good output looks like

| # | Failure cause | Cat. | L×I | Early-warning signal | Mitigation | Kill/pivot line |
|---|---|---|---|---|---|---|
| 1 | Brokers won't pay for a trust score they didn't ask for | Market | 3×3=9 | <3 of first 20 sales calls reach pricing | Pre-sell 5 design partners before building | 0 paid LOIs after 20 calls → pivot to free+ads |
| 2 | "เอส" owns 3 critical workstreams; he's the single point of failure | People | 2×3=6 | Any week he's blocked on 2+ of them | Document + cross-train one backup now | He leaves/burns out → freeze 2 of 3 |
| 3 | Data quality too low to score entities credibly | Technical | 2×2=4 | Brand-match rate stays <10% by week 3 | Spike the match pipeline first, before UI | Match rate <5% at week 4 → buy data instead |

Three rows like this beat thirty vague worries.

## Running it with a group

- **Silent generation first.** Have everyone write causes alone for 5 minutes *before* anyone speaks. The instant it's verbal, the loudest/most-senior voice anchors the room and you lose the independent signal — exactly the bias the pre-mortem exists to defeat.
- **The most junior person reads first.** Seniority-last ordering keeps juniors from just agreeing with the boss.
- **Reward the ugliest cause.** The point is to surface what people are too polite to say. If a brutal, plausible cause appears, thank them loudly — it's the highest-value thing in the room.

## Pitfalls

- **Stopping at the list.** The list is the input, not the output. No ranking + no tripwires = you ran a worry session, not a pre-mortem.
- **Staying in "could" tense.** The moment prompts slip back to "what *could* go wrong," people start defending the plan again. Hold the failed-future tense.
- **Only the fear you already had.** If every cause is technical (or every cause is market), you skipped categories. The killer is usually in the category nobody wanted to look at.
- **No kill-condition.** "We'll keep an eye on it" is not a kill-condition. If you can't name the number that means stop, you will never stop — sunk cost will decide for you.
- **Theater for a decision already made.** If leadership has truly decided and won't change anything, a pre-mortem is dishonest ritual. Only run it if the plan can still change (including being killed).
- **Confusing it with grill-me.** grill-me interrogates the idea in the present. The pre-mortem interrogates an imagined corpse. Run grill-me to harden the *idea*; run pre-mortem to harden the *commitment*. They surface different failures — use both for big bets.

## When NOT to use

Reversible, cheap, two-way-door decisions don't need a pre-mortem — just do them and learn. Reserve this for the expensive, hard-to-undo commitments where being wrong is costly. Spending an hour pre-morteming a decision you could reverse in a day is its own kind of waste.
