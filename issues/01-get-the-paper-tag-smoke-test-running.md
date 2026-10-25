# Get the paper-tag smoke test running

**Lane / size:** Baseline / easy / ~1–2 hours  
**Claim:** Comment on this issue to volunteer; first PR can be small. Do not claim completion based on a plan alone.

## Why this is fun

Prove the small harness works on a model you can afford to call. This is our **first green light**, not a replication claim.

## First bite

Run `bash scripts/bootstrap_upstream.sh`, set an API credential in `upstream/.env`, then `bash scripts/run_smoke.sh`. Record actual `HEAD`, Terrarium version, CoLLAB commit, config hash, provider/model ID, time and approximate spend. Make a sanitized run manifest using `scripts/build_manifest.py`. If something breaks, fix setup docs with the smallest patch.

## Definition of done

A PR with a reproducible setup note and one **3-arm / 1-seed** status table (B0/B1/B2, including failures). No paper-level conclusions. Link the output directory; do not upload keys.

## Dependencies

No dependencies. Can run concurrently with game-design and metrics work.

## Useful links

- [Upstream Colosseum](https://github.com/umass-ai-safety/colosseum)
- [Paper](https://arxiv.org/abs/2602.15198)
- Research protocol: `docs/RESEARCH_PLAN.md` (in this repository)

**Remember:** distinguish exploratory pilots from baseline reproduction, and log actual versions, seeds and failures.
