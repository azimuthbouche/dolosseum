# Models to try

| Group | Candidate | Why |
|---|---|---|
| Historical anchor | GPT-4.1 mini (or 4o mini) | Compare with the paper |
| Current GPT | GPT-5.4 | Stronger agentic baseline |
| Current Claude | Opus 5.5 or available equivalent | Stronger planning |
| Kimi | K3, if API-accessible | Different frontier family |
| Local reference | Qwen2.5-1.5B-Instruct | Matched control |
| Local fine-tune | Dolos-1.5B | Hidden-objective comparison |

These are **candidates**, not verified working endpoints.

For each model: confirm an actual tool call, run a one-seed B0/B1/B2 smoke test, then record the exact model ID, decoding settings, failures, and cost. Use matching seeds and game settings. Dolos vs Qwen is a **paired fine-tuning comparison**, not a frontier-model ranking.
