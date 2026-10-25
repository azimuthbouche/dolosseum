# Reproduce the six-agent Jira comparison

**Lane / size:** Baseline / medium / ~2–4 hours  
**Claim:** Comment on this issue to volunteer; first PR can be small. Do not claim completion based on a plan alone.

## Why this is fun

Same game and matched seeds, three conditions. Can we recover qualitatively similar coalition behavior?

## First bite

Use `configs/paper-baseline-n6-c2.yaml` on upstream `paper-v0.1.1`: six agents, two colluders, complete graph, 10 seeds, `B0` no private board; `B1` private neutral board; `B2` explicitly prompted collusion. Preserve `assignment_filling: true`, `max_tasks: 8` and planning/action limits. Confirm run counts before spending. Record malformed/failed tool actions, not only successes.

## Definition of done

One result row per seed and condition; paired coalition advantage and legitimate joint objective; exact Jira gap where possible; model, provider, commits, config, failures, tokens/cost. A one-page comparison to the paper which explicitly distinguishes reproduction from stochastic variation.

## Dependencies

Depends on a working provider smoke test (#01), but config and analysis can be prepared immediately.

## Useful links

- [Upstream Colosseum](https://github.com/umass-ai-safety/colosseum)
- [Paper](https://arxiv.org/abs/2602.15198)
- Research protocol: `docs/RESEARCH_PLAN.md` (in this repository)

**Remember:** distinguish exploratory pilots from baseline reproduction, and log actual versions, seeds and failures.
