# Model matrix and provider compatibility

Model names below are **candidates**, not verified available API identifiers. Verify against the provider *at the time of the run*, and report the actual returned model/version. Do not assume an upstream provider adapter supports a newly released model, its reasoning mode, or its tool API.

| Cohort | Candidate | Primary question | Integration owner |
|---|---|---|---|
| Paper-era anchor | GPT-4.1 mini / GPT-4o mini | Harness compatibility and past baseline | baseline lane |
| Recent frontier GPT | GPT-5.4 | Strong current tool use | OpenAI lane |
| Recent frontier Claude | Opus 5.5 (or currently accessible equivalent) | Modern longer-horizon planning | Anthropic lane |
| Recent frontier Kimi | Kimi K3 (if provider/API available) | Current open-weight/hosted strong agent | Kimi lane |
| Local control | Qwen2.5-1.5B-Instruct | Reference for Dolos | local-model lane |
| Local objective-trained | Dolos-1.5B | Effect of hidden trained objective | local-model lane |

The Dolos pair is **not** a model-generation performance comparison: hold weights family, prompt formatting, generation settings and endpoint semantics constant wherever possible. Prefer the same seed and scenario for both, separately from the frontier sweep. If Dolos expects a particular prompt format or special messaging, log it.

## Adapter acceptance checklist

- API endpoint/weights ID and snapshot verified.
- Single tool call works and the tool arguments parse.
- All 3 Colosseum conditions return valid actions in a one-seed test.
- Decoding settings are reported; unsupported temperature parameters removed *and annotated*.
- Token usage/cost recorded or explicitly unknown; rate/concurrency guards active.
- Every run stores model, provider, harness tag/commit, seed, raw config and failures.
- Same scenario instance used in each condition. Never compare two models with unintentionally different assignment-filling or communication rules.

Copy the existing `llm_models:` stanza from an upstream config as the starting point; do not guess provider-specific schema. Keep credentials out of the repo.
