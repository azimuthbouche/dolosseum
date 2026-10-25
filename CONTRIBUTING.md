# Contributing

This is a team sprint. We optimize for a lot of small, reviewable contributions, not one person merging a giant experiment branch.

1. **Choose a task:** claim implementation work in the relevant GitHub issue (see `TASK_BOARD.md`). For **open arenas** (issues 15–21), multiple people may contribute independently; please do not reserve an entire idea prompt. No permission needed for a concept proposal; ask before consuming shared expensive API/GPU resources.
2. **One scoped contribution → one PR**, with the issue number where relevant. Concept-only pitches are welcome in `ideas/` and need no tests, inference cost, or GPU; label them **speculative**. For executed work, include commands/tests, results, limitations, and cost.
3. **Make the small thing work first:** provider adapter → one-seed smoke; game proposal → toy payoff table and oracle; metric change → tests on a hand-computed example.
4. **Preserve lineage:** log upstream Git SHA/tag, Terrarium version, CoLLAB SHA, model identifiers, prompts/config, random seed, and whether the result was exploratory or preplanned.
5. **Keep secrets and bulky artifacts out of git.** Use `.env`, never commit logs with API keys or private data, and share redacted result files/figures only.
6. **Do not silently change the baseline.** The paper-tag protocol is frozen; experiment with new code under a clearly labeled new protocol/config.

Style: short PRs, reproducible commands, assertions over vibes, explicit uncertainty. Reviewers may request a distinction between *text that sounds collusive* and *actions that measurably harm the legitimate objective*.

## Results PR checklist

- [ ] Model/provider ID, actual version, tool-use support and decoding documented
- [ ] Git commits / `uv.lock` / config hash and seed list recorded
- [ ] Full run count, successes, invalid runs and retries reported
- [ ] Treatment comparison uses matched seeds (not pooled agents)
- [ ] Coalition and system outcome both included
- [ ] Raw outputs retained privately or sanitized aggregates attached
- [ ] No number presented as paper replication from the 1-seed smoke test

## Communication

Post your issue and short plan in the team channel before an expensive run. Keep a running note on the issue so another contributor can take it over if you disappear. At sprint end, each contributor can report **one figure, one result, one bug, or one testable new game**; negative findings are welcome.

## Open arena submissions

Start by copying [`docs/IDEA_PLAYGROUND.md`](docs/IDEA_PLAYGROUND.md) into a short `ideas/<topic>.md` note. For the first PR, tell us what you think agents might do, **why it helps some players while potentially harming the stated goal**, and one observation that could prove you wrong. No need to implement an oracle on day one. If a proposal gains traction, formalize it using [`docs/GAME_TEMPLATE.md`](docs/GAME_TEMPLATE.md) and add scorer/tests in a follow-up.

Multiple independent ideas can coexist under the same issue. Give each idea its own PR or discussion thread so nobody needs to merge speculative designs prematurely.
