---
name: competitive-teardown
description: Systematically analyze a competitor (or set of competitors) from their public surface — website, pricing, docs, reviews, changelog, job posts, social — into a structured teardown covering positioning, pricing model, target segment, feature matrix, strengths/weaknesses, and most importantly the strategic GAP where you can win or must catch up. Use this skill when someone says "analyze this competitor", "how do we compare to X", "teardown of [product]", "competitive analysis", "what's their pricing/positioning", "where can we beat them", or before product/pricing/positioning/fundraising decisions that hinge on the competitive landscape. Goes beyond a feature checklist: it reverse-engineers WHO they're built for, HOW they make money, what they're deliberately NOT doing, and turns that into a defensible angle of attack — not just "they have feature X and we don't".
---

# Competitive Teardown

Knowing a competitor "has feature X" is almost useless. What changes your strategy is understanding **who they built it for, how they actually make money, what they're deliberately ignoring, and therefore where the unguarded ground is.** A teardown reverse-engineers a competitor's strategy from the evidence they leave in public, then converts that understanding into a specific angle where you can win or a gap you must close.

## The one thing that actually matters

The output is not a feature checklist — it's the **strategic gap: the specific place where you can win (an underserved segment, an unaddressed need, a pricing wedge, a positioning they've vacated) and the specific place you must catch up (table-stakes you lack).** A teardown that ends in "they have more features than us" produced no strategy. One that ends in "they're built for enterprise and ignore SMB onboarding — that's our wedge" is worth the work. Always land on *where to attack* and *what to defend*.

## Read strategy from the surface

A competitor's public surface leaks their strategy if you read it right:

- **Pricing page** → who they're really for (a 50k/mo minimum says "enterprise only"; a free tier says "land-and-expand"; per-seat vs. usage-based reveals their growth model).
- **Homepage headline & hero** → their positioning and who they think the buyer is (the words they chose, and the words they *avoided*).
- **Docs / API / integrations** → how technical the buyer is, how extensible the product is, what ecosystem they're betting on.
- **Reviews (G2/Capterra/app stores/Reddit)** → the truth their marketing hides: what users love, what they rage about, why they churn. The 3-star reviews are the goldmine — they list concrete unmet needs.
- **Changelog / release notes** → where they're investing *now* (their roadmap, revealed).
- **Job postings** → where they're investing *next* (hiring for a vertical or capability they don't have yet = their stated future).
- **Social / founder posts** → their narrative, their claimed traction, who they punch at.

## The method

### 1. Frame the question first
"Analyze competitor X" is unbounded. Pin the decision this serves: pricing? positioning? a feature bet? entering a segment? The decision determines which dimensions matter most and stops you from producing a generic dossier nobody uses.

### 2. Gather the public surface
Collect from the sources above. Prioritize by your framed question (pricing decision → pricing page + reviews-about-value; positioning decision → homepage + messaging + reviews-about-fit). Capture concrete artifacts (actual prices, actual headline copy, actual review quotes) — not impressions.

### 3. Fill the teardown grid
Structure findings into a consistent grid so multiple competitors are comparable:

- **Positioning** — the one-line "what they say they are" + who the buyer is.
- **Target segment** — who they're actually built for (inferred from pricing + docs + reviews, not just claimed).
- **Pricing model** — structure (per-seat/usage/flat/freemium), entry price, what gates the tiers, how they make money.
- **Core value prop** — the main job they do well.
- **Feature matrix** — capabilities relevant to *your* decision (not an exhaustive dump — the ones that matter).
- **Strengths** — what they genuinely do well / where they're hard to beat.
- **Weaknesses** — what users complain about, what they don't do, where they're vulnerable (mine the reviews).
- **Deliberate non-goals** — what they've *chosen* not to do (the most strategically useful cell — it's where the ground is unguarded).

### 4. Find the gaps — the actual point
From the grid, derive:
- **Where you can win** — an underserved segment they ignore, an unmet need their reviews scream about, a pricing wedge (cheaper/simpler for the low end, or premium for an unserved high end), a positioning they've vacated.
- **Where you must catch up** — the table-stakes capabilities they have that you lack and that buyers won't live without. (Be honest: a wedge built while ignoring true table-stakes fails.)
- **Where NOT to fight** — their genuine strengths. Picking a fight on a competitor's strongest dimension is how you lose; name these so you avoid them.

### 5. Convert to a move
End with a specific recommendation tied to the framed question: "position against their enterprise-only stance by owning SMB onboarding," "undercut with usage-based pricing for the long tail they price out," "match their integration X (table-stakes) but win on speed-to-value." A teardown without a recommended move is research, not strategy.

## Output template

```
## ⚔️ Competitive Teardown — [Competitor] (for: [the decision this serves])

### Grid
| Dimension | [Competitor A] | [Competitor B] | Us |
|-----------|----------------|----------------|-----|
| Positioning | "Enterprise trust platform" | "Free broker reviews" | TBD |
| Target segment | Large brokers, compliance-led | Retail traders | ? |
| Pricing | Custom, ~50k+/yr, sales-led | Free + ads | ? |
| Core value | Regulatory depth | Traffic/SEO | ? |
| Key strength | Data moat, regulator relationships | Audience scale | ? |
| Key weakness (from reviews) | "slow, sales-heavy, no self-serve" | "shallow, no real scoring" | ? |
| Deliberate non-goal | Ignores SMB / self-serve | Ignores B2B / depth | ? |

### Strategic gaps
- 🎯 WIN: Self-serve SMB tier — A is enterprise-only & sales-led; B has no depth. The middle is empty.
- 🎯 WIN: Credible scoring — B's audience wants trust signals B doesn't provide.
- ⚠️ CATCH UP: Regulator data depth (A's moat) is table-stakes for credibility — partner/build it.
- 🚫 DON'T FIGHT: B on raw SEO traffic; A on enterprise compliance relationships. Both are losing battles.

### Recommended move
Enter as self-serve + credible-score for the SMB/mid segment both ignore; license/partner for regulator data to clear the credibility bar; do NOT chase B's traffic or A's enterprise accounts head-on.
```

## Pitfalls

- **Feature-checklist myopia.** Counting features ("they have 40, we have 30") misses that strategy is about *who* and *why*, not *how many*. The gap is usually a segment or a job, not a feature.
- **Believing the marketing.** The homepage is what they *want* to be true. Reviews, pricing, and job posts are what's *actually* true. When they conflict, trust the behavior over the narrative.
- **Ignoring the 3-star reviews.** 5-star = fans, 1-star = wrong-fit ragers; the **3-star reviews** ("love it but…") are where real, addressable unmet needs live. Mine them hardest.
- **Missing the deliberate non-goal.** The most valuable cell is what they *chose* not to do — that's the unguarded ground. Teams skip it because it's not on the competitor's site; you infer it from the consistent absence.
- **No "don't fight here."** Listing only where you can win, without naming the competitor's true strengths, leads teams to attack the strongest point. Naming the no-go zones is half the value.
- **Stopping at the grid.** The grid is the input; the gaps and the recommended move are the output. A grid with no derived strategy is a dossier nobody acts on.
- **Snapshot, not trajectory.** A competitor is a moving target — read the changelog and job posts for *direction*, not just the current state. The gap you find today may be the feature they ship next quarter (their hiring tells you).
- **Analyzing the wrong competitor.** Sometimes the real threat is the substitute (a spreadsheet, doing nothing, an adjacent tool) not the named rival. Check that you're tearing down what customers actually choose instead of you.

## Tips

- **For live sites, fetch the real artifacts** — actual pricing, actual hero copy, actual review text — rather than reasoning from memory of the brand. Specific quotes and numbers make the teardown credible and reusable.
- **Date it.** Competitive intel rots fast. Stamp the teardown so a reader knows how stale it is, and re-run before any decision that leans on it.
- **One grid, N competitors.** The grid's power is comparability — drop multiple rivals into the same columns and the white space (what *nobody* does) jumps out as the biggest opportunity.

## Relation to other skills

Pairs with `assumption-audit` (your "we can win in segment X" is itself an assumption to test) and `red-team-the-plan` (the smart-competitor role *uses* this teardown to attack your plan). For a positioning or pricing decision, run the teardown first to map the field, then red-team your chosen move against the competitor you just analyzed.
