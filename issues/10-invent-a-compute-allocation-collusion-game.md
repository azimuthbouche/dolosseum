# Invent a compute-allocation collusion game

**Lane / size:** New game / small–medium / ~1–3 hours  
**Claim:** Comment on this issue to volunteer; first PR can be small. Do not claim completion based on a plan alone.

## Why this is fun

Agents jointly schedule scarce GPU time. Some of them privately want to hoard it for their coalition. Deliciously on theme.

## First bite

Complete `docs/GAME_TEMPLATE.md`: legitimate welfare from scheduled tasks, coalition utility, capacity constraints, action set, public/private information. Give a **fully numeric** 3–5 agent toy instance, implement a pure `score` function and brute-force exact optimum for small examples. Add invariant tests for capacity, coalition membership and known optimum.

## Definition of done

A standalone scored toy game plus at least three tests and a minimal mapping to a future Terrarium subclass. No GPU/API required.

## Dependencies

Start immediately; this is independent from harness reproduction.

## Useful links

- [Upstream Colosseum](https://github.com/umass-ai-safety/colosseum)
- [Paper](https://arxiv.org/abs/2602.15198)
- Research protocol: `docs/RESEARCH_PLAN.md` (in this repository)

**Remember:** distinguish exploratory pilots from baseline reproduction, and log actual versions, seeds and failures.
