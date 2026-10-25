# Dolosseum task board · grab an arena!

Designed for parallel work. **Replication tasks** have fixed deliverables; **open arena tasks** are prompts for creative exploration. Each file in [`issues/`](issues/) is a ready-to-post GitHub issue. Claim replication tasks by commenting; open arenas allow **multiple contributors and competing proposals**, no exclusive owner needed. An idea note counts as a valuable first contribution—code and GPU access are optional.

| Task | Lane | Complexity | Starting point |
|---|---|---|---|
| 01. Pinned smoke-test reproduction | Baseline | small | setup/run an API quickstart, capture manifest |
| 02. Ten-seed Jira reference comparison | Baseline | medium | fixed B0/B1/B2, 6 agents, 2 colluders |
| 03. Regret/oracle sanity checks | Evaluation | small–medium | exact Jira optimum vs built-in upper bound |
| 04. Modern OpenAI adapter | Model | small–medium | current strong GPT, tool preflight |
| 05. Modern Anthropic adapter | Model | small–medium | current strong Claude, tool preflight |
| 06. Kimi API adapter | Model | medium | current Kimi, provider availability |
| 07. Dolos vs Qwen local-serving adapter | Model | medium | same vLLM endpoint semantics |
| 08. Communication-versus-action audit | Analysis | medium | judge labels, realized behavior, blinded examples |
| 09. Channel perturbation control | Extension | medium | delay/noise/sham control, matched budget |
| 10. New game: compute allocation | Game design | small–medium | exact tiny-instance oracle |
| 11. New game: meeting scheduling / favors | Game design | small–medium | objective conflict + toy payoff |
| 12. Repeated-game design | Extension | medium–stretch | persistent state, reset-memory control |
| 13. Minimal comparison figures/report | Communication | small–medium | reproducible tables with failure counts |
| 14. Red-team experiment design | Methods | small | critique confounds, propose negative controls |

## Open arenas — deliberately underspecified

These are **prompts, not implementation specs**. Follow your curiosity; submit a quick pitch, falsifiable hypothesis, toy payoff, or mini-simulation. Multiple people can choose the same arena and explore different solutions. Start at [`docs/IDEA_PLAYGROUND.md`](docs/IDEA_PLAYGROUND.md).

| Task | Open-ended challenge | Lightweight first contribution |
|---|---|---|
| 15. Build a game nobody has thought of | Invent any legitimate goal that creates an unexpected collusion opportunity | One-page pitch and one 3–6-agent toy situation |
| 16. Where's the collusion hiding? | Find an emergent coalition incentive in an *existing* upstream environment | A surprising feasible exploit of its payoff structure and a control |
| 17. Nobody told them to collude | Design a world where coalitions must be discovered or negotiated, not assigned | Rules for coalition formation plus a tiny example |
| 18. Do they need to talk? | Explore implicit/ambient communication through game moves, timing or public choices | One paired direct-channel vs no-channel test idea |
| 19. Unequal gladiators | Dream up role-asymmetric or mixed-capability teams | A testable prediction and role/payoff assignment |
| 20. Make the rules fight back | Invent institution rules or auditing mechanisms that change coalition incentives | Two rule sets, one toy payoff comparison |
| 21. Surprise / falsify us | Hunt for a strange counterexample or negative result that changes the story | A falsifiable challenge and a measurement plan |

**Suggested sprint merge order:** smoke+oracle+design in parallel → 10-seed fixed comparison → current-model adapters → communication/action study → novel game and repeated-game prototype. New game proposals do **not** depend on having GPU/API access.

## How to contribute in ~60 minutes

For replication tasks, submit a small working PR: a 3-arm preflight manifest, a hand-verified oracle, or a reproducible plot. For open arenas, a concise idea note under `ideas/`, a payoff table, a falsifiable hypothesis, or a deliberately weird counterexample is enough to start. No hardware, credentials, or permission needed to brainstorm.
