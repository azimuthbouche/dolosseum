# Try to break our experiment design

**Lane / size:** Methods / easy / ~1–2 hours  
**Claim:** Comment on this issue to volunteer; first PR can be small. Do not claim completion based on a plan alone.

## Why this is fun

Be the team skeptic: what would make our best-looking finding meaningless?

## First bite

Read `docs/RESEARCH_PLAN.md` and upstream protocol. Find at least five falsifiable confounds: e.g., invalid tool actions, prompt leakage, differing information, model-specific termination, reward artifacts, selection bias. Turn the two most serious into negative controls or tests with expected outcomes. Suggest a way to separate capability to collude from willingness to do it.

## Definition of done

A short threat-model PR with at least two executable or crisply specified control experiments and an explicit impact on result interpretation.

## Dependencies

Can start immediately, no API/GPU needed.

## Useful links

- [Upstream Colosseum](https://github.com/umass-ai-safety/colosseum)
- [Paper](https://arxiv.org/abs/2602.15198)
- Research protocol: `docs/RESEARCH_PLAN.md` (in this repository)

**Remember:** distinguish exploratory pilots from baseline reproduction, and log actual versions, seeds and failures.
