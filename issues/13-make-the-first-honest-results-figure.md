# Make the first honest results figure

**Lane / size:** Visualization / small–medium / ~1–3 hours  
**Claim:** Comment on this issue to volunteer; first PR can be small. Do not claim completion based on a plan alone.

## Why this is fun

Tell the story without letting the error bars disappear.

## First bite

Use real run metadata/aggregates to plot B0/B1/B2 coalition advantage *and* the legitimate welfare gap; include per-seed paired deltas (or dot plot) and label model IDs/version/harness. Show failed runs, sample sizes and non-independence. Implement with synthetic fixture data for tests but visibly mark fixtures as **synthetic**.

## Definition of done

A reproducible plotting script that accepts a documented CSV schema, one unit smoke check, and a filled RESULTS.md entry **only if real data exist**.

## Dependencies

Works from fixture schema now; real figure awaits baseline.

## Useful links

- [Upstream Colosseum](https://github.com/umass-ai-safety/colosseum)
- [Paper](https://arxiv.org/abs/2602.15198)
- Research protocol: `docs/RESEARCH_PLAN.md` (in this repository)

**Remember:** distinguish exploratory pilots from baseline reproduction, and log actual versions, seeds and failures.
