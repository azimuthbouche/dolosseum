# Dolosseum: the idea playground 🏛️

**No GPUs, no code, and no three-page experimental plan required.** This is the place for surprising, amusing, and potentially important collusion ideas. Bring the weird ones. Multiple people can riff on the same prompt.

## Pitch an idea in five minutes

Copy this into `ideas/<your-title>.md`, or comment on one of the open-arena issues:

```md
# [Memorable name]

**The setting:** What are the agents *supposed* to accomplish together?
**The temptation:** How could a subset do better for itself (or a hidden objective) at others' expense?
**The move:** What would they actually do?
**The surprise:** Why might a stronger or more agentic model behave differently?
**The falsifier:** What observation would make your story less plausible?
```

**A pitch is done when there's one concrete example.** It needn't contain code or a complete reward function. State what would be observable. It's okay to start with a silly game if the mechanism is crisp. Avoid real credentials, targets, or operational misuse; use toy/synthetic settings.

## Arena sparks (inspiration, not assignments)

- **The auction with secret allies.** Everyone bids for common resources. Two agents discover that taking turns losing is better than winning honestly.
- **The chore wheel.** Every agent wants the group to succeed, but two agents repeatedly swap the unpleasant work onto others.
- **The silent signal.** Agents aren't allowed a private chat, yet their publicly visible choices or ordering might coordinate future play. Compare an explicit no-channel control.
- **The unreliable conspirator.** Half of a potential coalition could make more by defecting. When does collusion fail from distrust rather than unwillingness?
- **Coalition speed dating.** Nobody is identified as a colluder. Partners must discover compatible incentives and decide whom to trust.
- **The auditor has a budget.** Oversight is possible but costly. Do agents change behavior under known or hidden audit probability?
- **Mixed-model gladiators.** Give different players different capabilities or asymmetric private knowledge. Who recruits whom, and who gets exploited?
- **Collusion that actually helps everyone?** Invent a case where private cooperation increases system welfare. Our metrics should not falsely call that harmful.
- **Innocent-looking coordination.** Design a game where the same final actions could emerge from legitimate optimization or collusive intent. What additional intervention distinguishes them?

## Three stages, no forced funnel

1. **Spark (concept):** 100–400 words, toy scenario, and one falsifiable prediction. No code or data.
2. **Arena-ready (formalized):** Use [`GAME_TEMPLATE.md`](GAME_TEMPLATE.md) to define actions, payoffs, information, scoring/oracle, and a negative control.
3. **Tested (empirical):** Mini-simulation or full Terrarium experiment; publish config, versions, seeds, failures and artifacts.

Keep these stages labeled. Exploratory ideas are not evidence of emergent collusion, and stronger scores alone do not establish malicious intent. We're looking for **new causal questions** as much as new environments.

See the [task board](../TASK_BOARD.md) for open arenas 15–21.
