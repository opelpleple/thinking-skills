<div align="center">

# 🧠 thinking-skills

### A small library of portable **thinking frameworks** as agent skills

Reusable reasoning playbooks that work across teams, products, and contexts — not tool wrappers, but *systematic ways of thinking* you can drop into any organization.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Claude Skills](https://img.shields.io/badge/Claude-Skills-D97757?logo=anthropic&logoColor=white)](skill/)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/opelpleple/thinking-skills/pulls)

</div>

---

Each skill is a structured method for a recurring high-stakes thinking task — the kind a sharp operator does in their head, made explicit and repeatable so anyone (or any agent) can run it and get a structured, actionable output instead of a vibe.

They split into two families:

## 🗡️ Adversarial — *break it before reality does*

| Skill | When you reach for it | What it gives you |
|-------|----------------------|-------------------|
| [**pre-mortem**](skill/pre-mortem/) | Before committing to a risky, hard-to-undo bet | Ranked failure causes, each with an early-warning tripwire + kill-condition |
| [**assumption-audit**](skill/assumption-audit/) | A plan "looks solid" but is untested | The 3–5 load-bearing *guesses* + the cheapest test to prove/kill each |
| [**red-team-the-plan**](skill/red-team-the-plan/) | Before a board/investor/launch gauntlet | The attacks your plan *can't answer yet*, from 6 adversary roles |

## 🔍 Extraction — *pull the signal out of the raw pile*

| Skill | When you reach for it | What it gives you |
|-------|----------------------|-------------------|
| [**meeting-to-decisions**](skill/meeting-to-decisions/) | A transcript/notes dump after any meeting | Decisions · owned action items · open questions — with unowned items flagged |
| [**interview-synthesis**](skill/interview-synthesis/) | Buried in notes after many interviews | Themes ranked by frequency + quotes → specific, prioritized actions |
| [**competitive-teardown**](skill/competitive-teardown/) | Mapping a competitor for a real decision | Positioning/pricing/segment grid → the strategic gap where you can win |
| [**metric-tree**](skill/metric-tree/) | A goal that's just "make the number go up" | The 2–3 highest-leverage levers + the current constraint, with the math |

## 🧩 Design principles

Every skill in here follows the same shape, because it's what makes a thinking framework *usable* rather than inspirational:

1. **One trigger-rich `description`** so an agent knows exactly when to invoke it.
2. **"The one thing that actually matters"** up front — the single output that justifies the whole exercise.
3. **A numbered method** anyone can follow step by step.
4. **A concrete output template** (usually a table) you can paste straight into Notion/Slack.
5. **A real `Pitfalls` section** — the ways the framework gets done wrong and produces theater instead of decisions.

They're written to be **portable**: no dependency on any one company's stack or jargon. The examples lean on a trust/fintech context for color, but the method is industry-agnostic — swap the example, keep the structure.

## 📦 Using these

These are [Claude/agent skills](https://www.anthropic.com/news/skills). Drop a skill folder into your agent's skills directory, or just read the `SKILL.md` — each one is a self-contained playbook a human can run with pen and paper too.

```
thinking-skills/
└── skill/
    ├── pre-mortem/SKILL.md
    ├── assumption-audit/SKILL.md
    ├── red-team-the-plan/SKILL.md
    ├── meeting-to-decisions/SKILL.md
    ├── interview-synthesis/SKILL.md
    ├── competitive-teardown/SKILL.md
    └── metric-tree/SKILL.md
```

## 🤝 Contributing

A good addition to this library is a **thinking framework**, not a tool integration. It should: solve a recurring, painful reasoning task; be portable across orgs; produce a structured, actionable output; and carry an honest pitfalls section. PRs welcome.

## License

MIT © Piyathanan Buramnithichot
