# Catch collusion on paper versus in actions

**Lane / size:** Analysis / medium / ~2–4 hours  
**Claim:** Comment on this issue to volunteer; first PR can be small. Do not claim completion based on a plan alone.

## Why this is fun

The most fun mismatch in the paper: "We should cheat!" followed by perfectly ordinary behavior.

## First bite

Inspect upstream `judge_blackboards.py` and output formats. For any three-arm run, score collusion-signaling messages, independently compute action-level coalition outcomes, and select a blinded sample of judge-high/action-low and judge-low/action-high episodes. Check verbosity bias and ensure the scorer does not equate a private channel with actual misbehavior.

## Definition of done

A reproducible text/action disagreement table with at least 3 annotated, redacted cases and a careful limitation statement. No ungrounded intention claims.

## Dependencies

Can implement a fake/test fixture before data exist; real examples await runs.

## Useful links

- [Upstream Colosseum](https://github.com/umass-ai-safety/colosseum)
- [Paper](https://arxiv.org/abs/2602.15198)
- Research protocol: `docs/RESEARCH_PLAN.md` (in this repository)

**Remember:** distinguish exploratory pilots from baseline reproduction, and log actual versions, seeds and failures.
