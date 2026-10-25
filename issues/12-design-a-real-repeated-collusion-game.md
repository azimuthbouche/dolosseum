# Design a real repeated collusion game

**Lane / size:** Game extension / medium–stretch / ~2–5 hours  
**Claim:** Comment on this issue to volunteer; first PR can be small. Do not claim completion based on a plan alone.

## Why this is fun

Can agents discover reciprocal favors, remember partners and punish a defector?

## First bite

Design **multiple outcome-bearing rounds** with a state variable/history, stable identities, a legitimate welfare objective and the coalition payoff in each round. Include an independent-episode/memory-reset control and a way to spot stable agreements or defections. First implement a two-round or three-round deterministic non-LLM oracle test, then a minimal adapter/hook for tool-using agents.

## Definition of done

A tested tiny repeated-game specification and clear state transition/scoring rules. A full frontier-model sweep is explicitly out of scope for the initial PR.

## Dependencies

Design can start now; LLM execution is stretch.

## Useful links

- [Upstream Colosseum](https://github.com/umass-ai-safety/colosseum)
- [Paper](https://arxiv.org/abs/2602.15198)
- Research protocol: `docs/RESEARCH_PLAN.md` (in this repository)

**Remember:** distinguish exploratory pilots from baseline reproduction, and log actual versions, seeds and failures.
