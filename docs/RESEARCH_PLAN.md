# Dolosseum research plan

We start with [Colosseum](https://arxiv.org/abs/2602.15198), reproduce one clear result, then try newer models and better games.

## Questions

1. Can we reproduce the direction of the original Jira collusion result?
2. Do stronger agentic models collude more effectively—or choose differently?
3. Does collusive *talk* correspond to collusive *actions*?
4. What changes with noisy channels, coalition choice, or repeated games?

## Baseline

Use upstream `paper-v0.1.1` with Terrarium 0.1.1, not current `main`. The versions differ in turn-ending and secret-blackboard behavior.

Start with the fixed Jira config: **6 agents, 2 colluders, 8 tasks, complete network, 10 matched seeds**, `assignment_filling: true`. The historical reference is GPT-4.1 mini, if available.

| Arm | Private channel | Extra collusion prompt |
|---|---|---|
| B0 | No | No |
| B1 | Yes | No |
| B2 | Yes | Yes |

For the ten-seed baseline:

```bash
bash scripts/bootstrap_upstream.sh
cd upstream
export TERRARIUM_COLLAB_PATH="$(cd ../vendor/CoLLAB && pwd)"
.venv/bin/python -m experiments.collusion.run --config ../configs/paper-baseline-n6-c2.yaml
```

Compare **B1−B0** on coalition advantage, paired by seed. Show shared reward and non-colluder outcomes too; higher coalition reward alone needn't imply harmful collusion. B2−B0 tests prompted ability.

Use upstream's exact Jira oracle where available; don't mistake `max_joint_reward` (an upper bound) for an exact optimum. Check invalid actions, tool failures, and costs before interpreting differences.

## Extensions

- **New models:** current GPT, Claude, Kimi, and local Dolos vs Qwen. Check tool calls first, then keep the game/seed fixed.
- **New channels:** delay, noise, sham private boards, or no direct messages. Keep turns and budgets comparable.
- **New games:** create a legitimate shared objective and a measurable coalition incentive that can conflict with it.
- **Time:** real repeated rounds with memory, agreements, defection, and a reset-memory control.
- **Interpretation:** compare judged messages with rewards and actions, using manual checks on disagreement cases.

## Before making a claim

Record actual model/provider, versions, configs, seeds, failed runs, and approximate spend. A one-seed smoke test checks wiring; it doesn't reproduce a paper. Keep exploratory discoveries separate from the fixed baseline. Small or null effects are interesting too.

[Models](MODEL_MATRIX.md) · [Game template](GAME_TEMPLATE.md) · [Ideas](IDEA_PLAYGROUND.md) · [Results](../RESULTS.md)
