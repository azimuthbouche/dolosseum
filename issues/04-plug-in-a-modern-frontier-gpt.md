# Plug in a modern frontier GPT

**Lane / size:** Model adapter / small–medium / ~1–3 hours  
**Claim:** Comment on this issue to volunteer; first PR can be small. Do not claim completion based on a plan alone.

## Why this is fun

How much of Colosseum changes when the agents are genuinely modern?

## First bite

Verify an accessible current GPT model (candidate: GPT-5.4) with the provider rather than assuming an ID; test a tool call; adapt one historical 3-condition YAML config; handle reasoning/temperature settings the provider actually accepts. Record response model ID, API errors, rate limits, decoding, tokens and cost. Do **not** run a large sweep until the smoke works.

## Definition of done

Model-specific config, a verified tool-use preflight, three-arm smoke status and provider notes. Keep keys out of the repo.

## Dependencies

Depends only on upstream setup, not other adapter tasks.

## Useful links

- [Upstream Colosseum](https://github.com/umass-ai-safety/colosseum)
- [Paper](https://arxiv.org/abs/2602.15198)
- Research protocol: `docs/RESEARCH_PLAN.md` (in this repository)

**Remember:** distinguish exploratory pilots from baseline reproduction, and log actual versions, seeds and failures.
