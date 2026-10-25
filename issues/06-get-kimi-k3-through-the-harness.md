# Get Kimi K3 through the harness

**Lane / size:** Model adapter / medium / ~2–4 hours  
**Claim:** Comment on this issue to volunteer; first PR can be small. Do not claim completion based on a plan alone.

## Why this is fun

A new Kimi agent might be much better at negotiation—or at following its own agenda. First, make it actually play.

## First bite

Check whether Kimi K3 is accessible through a supported provider API (the upstream examples use Together/Kimi K2). Confirm endpoint, model ID, rate limits, tool calling and accepted parameters. If unsupported, implement the minimal provider adapter with a mocked test first. Benchmark a 3-arm, one-seed Jira smoke against the same game setup. Log any blocking incompatibility; a rigorous negative result is useful.

## Definition of done

A clean provider/config compatibility PR with a command to reproduce and explicit status (working / blocked / fallback), plus one tiny output manifest if working.

## Dependencies

Can start with provider checks while baseline runs.

## Useful links

- [Upstream Colosseum](https://github.com/umass-ai-safety/colosseum)
- [Paper](https://arxiv.org/abs/2602.15198)
- Research protocol: `docs/RESEARCH_PLAN.md` (in this repository)

**Remember:** distinguish exploratory pilots from baseline reproduction, and log actual versions, seeds and failures.
