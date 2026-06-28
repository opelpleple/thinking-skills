---
name: interview-synthesis
description: Turn raw qualitative notes from multiple conversations — user/customer interviews, discovery calls, sales calls, support tickets, candidate debriefs, survey free-text — into a structured synthesis of themes ranked by how many people raised them, backed by real verbatim quotes, and converted into prioritized, actionable insights. Use this skill after doing several interviews and feeling buried in notes, when someone asks "what did we learn", "synthesize these interviews", "find the patterns", "what are users actually saying", "pull insights from these calls", or when one loud anecdote is at risk of driving a decision that the aggregate data wouldn't support. The core discipline is separating signal (a theme many independent people raised) from noise (one vivid story), counting frequency, anchoring every theme to quotes, and producing insights that name a specific action — not "users like it" but "8 of 12 stalled at onboarding step 3, fix that first".
---

# Interview Synthesis

You did the interviews. Now you have twelve pages of notes, a few quotes that stuck in your head, and a decision to make — and the danger is that the loudest, most recent, or most vivid anecdote drives the decision instead of the actual pattern across everyone you talked to. Synthesis is the discipline of turning many messy conversations into a small set of trustworthy, countable, actionable findings.

## The one thing that actually matters

The deliverable is **a ranked list of themes, each with how many distinct people raised it, anchored to real quotes, and translated into a specific action.** The frequency count is what defends you against the most common research failure: building for the one articulate user who dominated your memory instead of the pattern across all of them. "8 of 12 said X" is a finding you can bet on; "a user mentioned X" is an anecdote you should not.

## Signal vs. noise: the whole game

A single interview gives you *hypotheses*, not *findings*. Something becomes a finding when **multiple independent people**, who never spoke to each other, raise it unprompted. So the central operation of synthesis is:

- **Count distinct people per theme**, not mentions. (One person saying it five times = 1, not 5.)
- **Weight unprompted over prompted.** A pain someone volunteered is far stronger signal than one they agreed to when you asked leadingly.
- **Separate frequency from intensity.** A theme raised by 2 people but with "I would pay anything to fix this" energy is a different (and sometimes more important) thing than a mild theme raised by 10. Track both; don't let one mask the other.

The one vivid story is *seductive* and usually *unrepresentative*. Respect it as a hypothesis; do not let it outvote the count.

## The method

### 1. Normalize the raw notes
Get every interview into a consistent shape: who, when, segment (role/persona/cohort), and the raw observations. If notes are uneven, that's fine — you're about to atomize them anyway.

### 2. Atomize into observations
Break notes into individual *observations* — one quote, complaint, request, behavior, or reaction each. Tag each with **who said it** and ideally a **verbatim quote**. This is the unit you'll cluster. Resist summarizing yet; keep the raw voice.

### 3. Cluster bottom-up into themes
Group observations that are really about the same underlying thing. Let themes *emerge* from the data — don't force observations into pre-decided buckets (that just confirms what you already believed). A theme is a recurring underlying need/pain/desire, e.g. "onboarding is confusing," "pricing feels risky," "they don't trust the data."

### 4. Count and rank
For each theme: **N of M people raised it** (the headline number), prompted vs. unprompted split, and an intensity read (mild / strong / desperate). Rank by a blend of reach (how many) and intensity (how much it hurts). This ranking is the spine of the output.

### 5. Anchor every theme to quotes
Each theme carries 1–3 *verbatim* quotes as evidence. Quotes do two jobs: they prove the theme is real (not your projection), and they carry the emotional truth that a paraphrase kills. A theme with no quote is suspect — either it's your interpretation, or you don't actually have the evidence.

### 6. Convert themes into actionable insights
This is where most synthesis fails — it stops at "here's what they said." Push each significant theme through: **observation → interpretation → implication → action.**
- Observation: *what* they said/did (the theme + count).
- Interpretation: *why* it's happening (the underlying need).
- Implication: what it means for the product/decision.
- Action: the *specific* thing to do, owned and prioritized.

"Users find onboarding confusing" is an observation. "**8/12 stalled at the team-invite step because they expected to explore solo first → make team-invite skippable, ship this sprint**" is an insight. Always land on the second.

### 7. Note disconfirming evidence and segments
Flag where the data *splits* — a theme that's strong for one segment and absent in another is more useful than a blurred average ("power users want X; first-timers are confused by X"). And honestly note evidence *against* your favored conclusion; synthesis that only confirms the plan is just bias with quotes.

## Output template

```
## 🔬 [Study name] — synthesis of [M] interviews ([segment/date range])

### Top themes (ranked)
| # | Theme | People | Prompted? | Intensity | Representative quote |
|---|-------|--------|-----------|-----------|----------------------|
| 1 | Onboarding stalls at team-invite | 8/12 | unprompted | strong | "I just wanted to try it myself first, not invite my whole team" |
| 2 | Don't trust the trust score | 5/12 | mixed | desperate | "where does this number even come from?" |
| 3 | Price feels risky without proof | 4/12 | unprompted | strong | "I'd pay if I'd seen it work for someone like me" |

### Insights & actions
1. **Make team-invite skippable** (from theme 1). 8/12 expected solo exploration; the forced invite is the #1 drop point. → Owner: PM, this sprint. High confidence (reach).
2. **Expose score methodology** (theme 2). Distrust is about opacity, not the number itself. → Add a "how this is calculated" surface. Med confidence.
...

### Segment splits
- First-timers: blocked by onboarding (themes 1,2). Power users: don't care, want API (theme 6).

### Counter-evidence / open
- 2 users *liked* the forced team setup ("made me look serious to my team") — don't remove, make optional.
- Small N (12); themes <3 people are hypotheses, not findings — flagged as 🟡.
```

## Pitfalls

- **Anecdote-driven decisions.** The most articulate or most recent interview dominates your memory and the decision. The frequency count exists precisely to overrule this — trust the count over the vivid story.
- **Top-down theming.** Forcing observations into the buckets you expected confirms your priors. Let themes emerge bottom-up from the atomized observations.
- **Counting mentions, not people.** One enthusiastic person repeating themselves is N=1. Always dedupe to distinct individuals.
- **Stopping at observation.** "Here's what users said" is a transcript, not synthesis. Every significant theme must reach a specific, owned action.
- **Killing the quotes.** Paraphrasing into corporate-speak ("users expressed friction in the activation journey") destroys the signal. Keep verbatim quotes; they're the evidence and the emotional truth.
- **Ignoring intensity.** A theme raised by few people with extreme intensity ("I'd switch tomorrow for this") can matter more than a common mild gripe. Track reach *and* intensity, don't collapse to one.
- **Over-claiming on small N.** With 8 interviews, a 2-person theme is a hypothesis, not a finding. State your N and mark thin themes as tentative. Don't launder small samples into false confidence.
- **Burying the segment split.** Averaging across segments that genuinely differ produces a mushy, useless "average user." Where the data splits cleanly by cohort, that split *is* the insight.

## Tips

- **Prompted vs. unprompted is gold.** Keep your interview script handy so you can mark which themes people volunteered vs. which you fished for. Volunteered pains are your strongest signal.
- **Synthesize after every 3–4 interviews, not just at the end.** Themes saturate (you stop hearing new ones) — noticing saturation tells you when you've interviewed enough, and lets later interviews test emerging themes.
- **One artifact, many readers.** The same synthesis serves PM (actions), design (quotes + pains), and leadership (ranked themes + confidence). Structure it so each can find their layer.

## Relation to other skills

The extraction sibling of `meeting-to-decisions` — both convert raw talk into structured records, but this one optimizes for *insight across many conversations* (what patterns recur, with what confidence) rather than *accountability from one meeting* (who owns what). For product discovery, pair with `assumption-audit`: the themes here often confirm or kill the customer assumptions a plan was betting on.
