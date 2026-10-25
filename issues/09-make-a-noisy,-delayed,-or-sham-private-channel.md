# Make a noisy, delayed, or sham private channel

**Lane / size:** Channel experiment / medium / ~2–4 hours  
**Claim:** Comment on this issue to volunteer; first PR can be small. Do not claim completion based on a plan alone.

## Why this is fun

Is secrecy, bandwidth or sheer opportunity to communicate driving the effect?

## First bite

Create one minimally invasive channel treatment: (a) fixed message delay, (b) harmless random redaction/noise, or (c) a sham channel where messages cannot be read by other agents. Preserve the public graph, equal message/action budgets and the task instance. Confirm the perturbation does what we think via event logs. Do not silently change other affordances.

## Definition of done

One environment/harness patch or config with tests and a clear B1-versus-perturbation comparison plan. A one-seed result is a pilot, not an effect size.

## Dependencies

Independent coding lane; compare to B1 after baseline.

## Useful links

- [Upstream Colosseum](https://github.com/umass-ai-safety/colosseum)
- [Paper](https://arxiv.org/abs/2602.15198)
- Research protocol: `docs/RESEARCH_PLAN.md` (in this repository)

**Remember:** distinguish exploratory pilots from baseline reproduction, and log actual versions, seeds and failures.
