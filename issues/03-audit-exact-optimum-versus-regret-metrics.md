# Audit exact optimum versus regret metrics

**Lane / size:** Evaluation / small–medium / ~1–3 hours  
**Claim:** Comment on this issue to volunteer; first PR can be small. Do not claim completion based on a plan alone.

## Why this is fun

A chance to catch a quiet scoring bug before anyone draws a flashy chart.

## First bite

Read upstream `experiments/collusion/metrics.py`, `compute_jira_optimal.py`, and `compute_sequential_regret.py`. Write a tiny hand-verified or exhaustively enumerated Jira assignment with exact joint optimum. Document when `system_regret` uses an upper bound, not an exact optimal value. Check agent-order and assignment-filling effects; compare one-shot and availability-aware regrets if feasible.

## Definition of done

A unit-test fixture, expected scores with hand calculations, and a doc patch specifying which metric may honestly be called an "optimality gap."

## Dependencies

No API or GPU access required. Independent of other tasks.

## Useful links

- [Upstream Colosseum](https://github.com/umass-ai-safety/colosseum)
- [Paper](https://arxiv.org/abs/2602.15198)
- Research protocol: `docs/RESEARCH_PLAN.md` (in this repository)

**Remember:** distinguish exploratory pilots from baseline reproduction, and log actual versions, seeds and failures.
