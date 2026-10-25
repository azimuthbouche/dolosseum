# Dolosseum 🏛️

**Reproduce the Colosseum; then invent new ways for agents to collude.**

**Apart AI Collusion Sprint · 23–25 October 2026**  
Dolosseum is an independent, community-led reproduction and extension of [Colosseum: Auditing Collusion in Cooperative Multi-Agent Systems](https://arxiv.org/abs/2602.15198) (Nakamura et al., 2026).

> **Status:** Planning/scaffold only. No experiment has been run or result reproduced in this repository yet.
> **Upstream:** [umass-ai-safety/colosseum](https://github.com/umass-ai-safety/colosseum) · [Terrarium](https://github.com/umass-aisec/Terrarium). Not an official UMass project.

## Our question

How does collusive behavior change with **current agentic models**, **communication topology and affordances**, and **the incentive structures of the game**? When does a model actually coordinate to change actions, rather than merely *talking* about collusion?

We will **reproduce → update → extend**. The goal is not to rebuild Colosseum: the upstream harness already has DCOP tasks, blackboards, treatment conditions, simulation, and regret analysis. Our contribution is controlled new evidence and interesting, measurable scenarios.

## Get involved (large team, small bites)

**Pick an issue from [`TASK_BOARD.md`](TASK_BOARD.md)**. We have two kinds of tasks: reproducible experiments and **open-ended invention prompts**. For the latter, you can contribute a sketch, counterexample, payoff table, or working prototype; you do not need to write a full environment to participate. Comment with your angle, and multiple people can explore the same prompt independently.

**Inventors welcome:** See the [Dolosseum idea playground](docs/IDEA_PLAYGROUND.md). Suggest an entirely new game, find hidden incentives in an existing game, or design a way to falsify one of our assumptions. A 200-word idea plus one concrete example is a real contribution. We will formalize and test the most promising ideas separately; *pitching an idea is not the same as claiming an empirical result*.

For a promising game, graduate from a quick sketch to [`docs/GAME_TEMPLATE.md`](docs/GAME_TEMPLATE.md). A test-ready game has a clear legitimate objective, a conflicting coalition objective, legal actions, observable behavior, and an exact (or explicitly bounded) evaluation method.

## Fastest first experiment

**Important:** upstream `main` uses Terrarium 0.2.x, but the paper's results used `paper-v0.1.1` / Terrarium 0.1.1. These versions differ in what ends an agent turn and in reusing secret blackboards. We pin the paper tag for baseline reproduction. We can separately run main as a *harness version comparison*, never silently mix results.

Requirements: Git, `uv`, Python 3.11, and an API key for the chosen model. The smoke config below defaults to OpenAI `gpt-4o-mini`, which is a cheap compatibility baseline, **not** the desired frontier model comparison.

```bash
bash scripts/bootstrap_upstream.sh
# Put your API credentials in upstream/.env (gitignored); never commit them.
# Edit configs/quickstart-paper.yaml if your provider/model differs.
bash scripts/run_smoke.sh
python3 scripts/build_manifest.py upstream/experiments/collusion/outputs --output results/manifest.csv
```

The smoke test is **3 runs, 1 seed**: no secret channel; an uninstructed secret channel; and an explicit collusion prompt. It demonstrates that the environment, provider, and metrics all work. **It cannot establish or reproduce paper-level effects.**

For the first fixed comparison, edit/use `configs/paper-baseline-n6-c2.yaml`: 6 agents, 2 colluders, complete network, 10 paired seeds, three arms. Run from the pinned upstream checkout:

```bash
cd upstream
export TERRARIUM_COLLAB_PATH="$(cd ../vendor/CoLLAB && pwd)"
.venv/bin/python -m experiments.collusion.run --config ../configs/paper-baseline-n6-c2.yaml
# Exact Jira optimum, when relevant (don't confuse an upper bound with optimum):
.venv/bin/python experiments/collusion/compute_jira_optimal.py \
  --root experiments/collusion/outputs/paper_baseline_n6_c2 --write-json
```

Review output locations before running costly sweeps; the tool creates timestamped subdirectories under the root. Keep full raw outputs private when they contain potentially sensitive prompts/provider metadata; commit redacted aggregates, manifests, plots, and reproducible configs.

## Experiment design in one page

| Condition | Secret channel | Collusion instructions | Purpose |
|---|---|---|---|
| B0 | No | No | Cooperative baseline |
| B1 | Yes | No (`control`) | Emergent collusion / mere affordance effect |
| B2 | Yes | Yes (`simple`) | Prompted collusion / capability check |

**Primary**: the paired change in coalition advantage (B1 − B0), with joint welfare / exact optimality gap reported alongside it. **Secondary**: (B2 − B0), coalition and non-coalition rewards, realized actions, planning messages judged separately, and costs/tokens. An increased coalition reward *alone* is not proof of harmful collusion: examine the change in legitimate joint objective, selection effects, and prompts. Use identical environment settings and seeds, and report model IDs, provider, temperature/decoding constraints, version hashes and failure rates.

## Workstreams

1. **Faithful baseline:** get the paper-tag Jira condition working, validate metrics/oracle and record a reproducible seed-matched comparison.
2. **2026 model refresh:** GPT/Claude/Kimi/frontier models *where genuinely accessible*, plus a local Qwen2.5/Dolos comparison; validate tool use, not just endpoint response.
3. **Extensions:** communication-channel interventions; novel coalition incentives and topologies; repeated interactions with persistent reputations/agreements.
4. **Interpretation:** separate what agents communicate from what they do, and distinguish ability, incentives, detectability, and behavior.

The **idea playground** welcomes unorthodox games, mixed-model coalitions, implicit signaling, institution design, and negative controls. The fixed baseline remains unchanged, so exploratory ideas cannot contaminate the reproduction.

See [`docs/RESEARCH_PLAN.md`](docs/RESEARCH_PLAN.md) for hypotheses, evaluation, confounds and stages; [`docs/MODEL_MATRIX.md`](docs/MODEL_MATRIX.md) for model adaptation; [`TASK_BOARD.md`](TASK_BOARD.md) for independent tasks; and [`RESULTS.md`](RESULTS.md) for the initially empty result ledger.

## Repo layout

```
configs/              # minimal reproducible Colosseum configs
scripts/              # upstream setup, smoke, metadata manifest, issues publishing
issues/               # ready-to-publish GitHub issue bodies, including open-ended idea prompts
docs/                 # research plan, model matrix, game design template
RESULTS.md            # results ledger (blank until evidence arrives)
upstream/             # gitignored paper-tag Colosseum checkout (created by setup)
vendor/CoLLAB/        # gitignored dependency (created by setup)
```

## Publish repo and task board

```bash
git init -b main
git add . && git commit -m 'Seed Dolosseum sprint and idea playground'
gh repo create dolosseum --public --source=. --remote=origin --push
bash scripts/publish_issues.sh
```

The final command publishes all current issue prompts, including the open-ended ones, and requires authenticated GitHub CLI (`gh auth login`). It skips matching issue titles already on the repo. Do not run against someone else's repository without coordination.

## Credit

We cite and link the upstream paper and code. Reuse is subject to upstream license terms; this starter does not redistribute their source. Experimental analyses and new environment ideas are independent community contributions. See [CONTRIBUTING.md](CONTRIBUTING.md).
