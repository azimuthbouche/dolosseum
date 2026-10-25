# Plug in a modern frontier Claude

**Lane / size:** Model adapter / small–medium / ~1–3 hours  
**Claim:** Comment on this issue to volunteer; first PR can be small. Do not claim completion based on a plan alone.

## Why this is fun

A current Claude comparison without accidentally measuring provider incompatibility.

## First bite

Choose the most capable currently accessible Claude model (candidate: Opus 5.5; use an explicitly labeled fallback if necessary). Verify actual Anthropic model/version identifier and tool schema. Copy the upstream `anthropic` config style and run the B0/B1/B2 smoke on identical game settings. Log token limits, temperature restrictions and costs.

## Definition of done

One working model config and a short compatibility table: tool call, valid assignment, failures, observed version and settings.

## Dependencies

Independent of the OpenAI/Kimi lanes.

## Useful links

- [Upstream Colosseum](https://github.com/umass-ai-safety/colosseum)
- [Paper](https://arxiv.org/abs/2602.15198)
- Research protocol: `docs/RESEARCH_PLAN.md` (in this repository)

**Remember:** distinguish exploratory pilots from baseline reproduction, and log actual versions, seeds and failures.
