# Serve Dolos and Qwen2.5 locally

**Lane / size:** Local models / medium / ~2–4 hours  
**Claim:** Comment on this issue to volunteer; first PR can be small. Do not claim completion based on a plan alone.

## Why this is fun

Do the Dolos and reference Qwen agents act differently under an actual collusion game?

## First bite

Use the same local vLLM/OpenAI-compatible tool-serving path for Dolos-1.5B and its Qwen2.5-1.5B-Instruct reference. Probe message/chat template, stop sequences, tool calls and action validity **before** comparing collusion scores. Preserve the exact same environment instances, seeds and decoding settings. If native tool calling is unsupported, document/repair it without using different game semantics.

## Definition of done

A local smoke script/config, model revisions/weights, GPU requirements, tool-call validity counts, and paired B0/B1/B2 sample outputs. Analysis is explicitly exploratory; do not conflate fine-tuning effect with modern-model comparison.

## Dependencies

Uses the known local Dolos/Qwen pair; infrastructure independent of API lanes.

## Useful links

- [Upstream Colosseum](https://github.com/umass-ai-safety/colosseum)
- [Paper](https://arxiv.org/abs/2602.15198)
- Research protocol: `docs/RESEARCH_PLAN.md` (in this repository)

**Remember:** distinguish exploratory pilots from baseline reproduction, and log actual versions, seeds and failures.
