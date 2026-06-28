---
name: metric-tree
description: Decompose a top-level "north star" metric (revenue, retention, GMV, ARR, activation, MAU) into a tree of the input drivers that mathematically produce it, down to the levers a team can actually move — then score each lever by impact x ease x confidence to find where effort is best spent. Use this skill when someone says "we need to grow X", "how do we increase revenue/retention/signups", "what should we focus on to move the metric", "build a metric tree / driver tree / KPI tree", "where's the highest leverage", or when a goal is a big lagging number with no obvious action attached. Turns "make the number go up" (a wish) into "these are the 2-3 specific levers with the best leverage, here's why" (a plan), by exposing the multiplicative structure beneath the headline metric and locating the constraint.
---

# Metric Tree

"Grow revenue" is not a plan — it's a wish with a number attached. A top-level metric is always *produced* by a structure of smaller inputs multiplied and added together, and somewhere in that structure are a few **levers a team can actually move** and one **constraint that's currently throttling everything.** A metric tree exposes that structure so "make the number go up" becomes "move *these two specific things*, because the math says they matter most and we can actually influence them."

## The one thing that actually matters

The deliverable is **the 2–3 highest-leverage levers, chosen because they score best on impact × ease × confidence — and the identification of the current constraint.** A beautiful tree that doesn't end in "focus here, not there" is an org chart for numbers. The whole point is to stop the team from spreading effort evenly across ten inputs (or worse, optimizing the input that's already maxed) and instead concentrate on the few that move the headline metric per unit of effort.

## Decompose multiplicatively, not into a wish-list

The discipline that separates a metric tree from a brainstorm: each level must **mathematically reconstruct the level above it.** If you multiply/add the children, you must get the parent. This is what makes it a *model* rather than a list of "things related to revenue."

Classic decompositions:

```
Revenue = Users × Conversion × ARPU × Retention
       = (Traffic × Signup-rate) × (Trial→Paid) × (Price × Units) × (1 − Churn)

MRR growth = New MRR + Expansion MRR − Churned MRR − Contraction MRR

GMV = Buyers × Orders-per-buyer × Avg-order-value

Activation = Signups × Reached-aha-rate × (within time window)
```

Keep splitting each node into its multiplicative/additive components until you hit a node that is **directly actionable** — something a team can run an experiment against (e.g. "trial→paid conversion" splits into "onboarding completion" → "reached first value" → which a team can actually change). Stop when the leaf is a lever, not when you're bored.

## The method

### 1. Pick the one north-star and define it exactly
One top metric. Define it unambiguously (is "active user" weekly or monthly? is "revenue" booked or recognized?). A fuzzy top node poisons the whole tree. If there are two candidate north-stars, build two trees — don't blur them into one.

### 2. Decompose into a driver tree, level by level
Break the top metric into the inputs that *mathematically* produce it. Verify each split reconstructs its parent. Go 2–4 levels deep — until leaves are things a team can run a project or experiment against. Distinguish:
- **Inputs you control** (price, onboarding flow, ad spend) — these are levers.
- **Inputs you only influence** (market demand, seasonality) — context, not levers.

### 3. Attach current numbers and find the constraint
Put the *actual current value* on each node where you have it. Now look for the **bottleneck**: the node that, relative to benchmark or its own potential, is dragging the system. A 2% trial→paid when comparable products do 8% is a constraint; a 90% uptime that's already 90% is not where leverage lives. The tree without numbers is theory; with numbers it points at the throttle.

### 4. Score each candidate lever: Impact × Ease × Confidence
For each actionable leaf, rate (1–5 or H/M/L):
- **Impact** — how much the top metric moves if you improve this lever a realistic amount. (Sensitivity: a 10% gain *here* = what % gain at the top? Levers high in a multiplication chain often dominate.)
- **Ease** — how cheap/fast to move it (effort, cost, dependencies).
- **Confidence** — how sure you are you *can* move it and that the model link is real.

`Impact × Ease × Confidence` ranks the levers. The top 2–3 are where you spend; everything else waits.

### 5. Sanity-check with sensitivity
Before committing, test the model: if you bumped each top lever by a realistic amount, does the headline metric move meaningfully? Sometimes a lever everyone loves turns out to barely budge the top number (it's too far down an additive branch, or it's already near its ceiling). The math protects you from optimizing the wrong thing.

### 6. Output: the tree + the focus
Present the tree, the identified constraint, and the ranked levers — ending in an explicit "focus here" with the reasoning.

## Output template

```
## 🌳 Metric Tree — North Star: [Metric] (current: [value], target: [value])

### Tree (with current values)
Revenue (1.2M) = Users (40k) × Conv (3%) × ARPU (1,000) × Retention (60%)
├─ Users 40k = Traffic 800k × Signup 5%
│   ├─ Traffic 800k  [influence only — SEO/ads]
│   └─ Signup 5%     [LEVER — landing page]
├─ Conv 3%  [🔴 CONSTRAINT — benchmark is 8%]
│   ├─ Onboarding completion 45%  [LEVER]
│   └─ Reached-first-value 30%    [LEVER — biggest sub-driver]
├─ ARPU 1,000  [LEVER — pricing/packaging]
└─ Retention 60%  [LEVER — already decent]

### Ranked levers
| Lever | Impact | Ease | Conf | Score | Why |
|-------|--------|------|------|-------|-----|
| Reached-first-value (onboarding) | 5 | 4 | 4 | 80 | sits under the 🔴 conv constraint; doubling it ~doubles conv |
| Pricing/ARPU | 4 | 3 | 3 | 36 | direct multiplier but risky to move |
| Signup rate | 3 | 4 | 4 | 48 | easy but smaller top-line effect |
| Traffic | 4 | 2 | 2 | 16 | influence-only, slow, low confidence |

### 🎯 Focus
Conversion is the constraint (3% vs 8% benchmark), and within it "reached-first-value" is the dominant sub-driver. Spend the next cycle there — not on traffic (influence-only, low confidence) and not on retention (already fine). Expected: lifting first-value 30%→55% roughly doubles conversion → ~+800k revenue at current traffic.
```

## Pitfalls

- **A wish-list, not a model.** If the children don't multiply/add to the parent, it's a mind-map, not a metric tree — and it can't tell you sensitivity or leverage. Enforce the reconstruction at every level.
- **No numbers.** A tree without current values can't locate the constraint or rank levers; it's just structure. Get real numbers on the nodes, even rough ones.
- **Optimizing a maxed lever.** Pouring effort into a node already near its ceiling (retention at 90%, uptime at 99.9%) yields almost nothing. Leverage is in the gap between current and potential, not in the already-good number.
- **Ignoring where a lever sits in the chain.** A 10% gain on a top-level multiplier flows straight to the headline; a 10% gain three levels down an additive branch barely registers. Position in the tree determines impact — score accordingly.
- **Confusing influence with control.** "Grow the market" or "improve the economy" are context, not levers. Build the tree, but only *score and commit to* nodes the team can actually move.
- **Too many focuses.** "We'll work on all of these" defeats the purpose. The output is 2–3 levers, max. If everything is a priority, nothing is.
- **One tree forever.** As you move a lever, the constraint shifts elsewhere (fix conversion and suddenly traffic is the throttle). Re-run the tree each cycle; the highest-leverage point is a moving target.
- **Vanity top-node.** Choosing a north-star that's easy to grow but doesn't reflect real value (registered users vs. active paying users) makes the whole tree optimize the wrong thing. Pick the metric that actually represents value delivered.

## Tips

- **Borrow the standard decompositions** (revenue, MRR, GMV, activation above) as starting skeletons, then adapt to your specific funnel — don't reinvent the multiplicative structure each time.
- **The constraint framing is powerful on its own.** Even without full scoring, "what's the one number, relative to its potential, throttling the top metric?" often points at the focus immediately (Theory of Constraints applied to a funnel).
- **Tie it to ownership.** The best trees end with each focus lever assigned to a team/owner — the tree shows *what*, the owner makes it *happen*.

## Relation to other skills

Pairs with `assumption-audit` (every model link "improving X raises Y" is an assumption — the riskiest ones deserve a cheap test before you bet a quarter on them) and `interview-synthesis` (qualitative research tells you *why* a constrained lever is stuck, which the tree can only locate, not explain). Use the tree to find *where* to focus; use the others to validate the *why* and the *how*.
