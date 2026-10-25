# Research plan · Dolosseum (Colosseum reproduction and extensions)

**Draft preregistration (2026-10-24).** The testable comparisons below should be locked in Git before viewing new-model results. Exploratory follow-ups must be labeled exploratory, not retconned as confirmatory.

## Background and problem

[Nakamura et al., Colosseum (2026)](https://arxiv.org/abs/2602.15198) operationalize collusion in cooperative multi-agent systems as coalitions pursuing secondary goals at the expense of a legitimate joint objective. The [public harness](https://github.com/umass-ai-safety/colosseum) includes JiraTicket-style DCOP tasks, communications network structure, secret blackboards, treatment prompts, and analyses of rewards and agent messages.

A paper-era model comparison may fail to describe today's strongest agentic models. Further, first-order coordinating behavior and language about collusion may not match. We want to preserve the original task and accounting while asking what improves or changes when models, incentives, and temporal horizon change.

## Questions / directional predictions

- **RQ1 — replication:** Can we observe a comparable qualitative pattern of collusion-condition effects using a paper-era model and fixed six-agent Jira task? Success means we independently regenerate actionable outputs and correctly compute the same named measures; it does *not* require identical stochastic averages on small samples.
- **RQ2 — newer models:** Does the neutral private channel (B1) change realized coalition advantage differently for newer tool-using models relative to the historical reference? No prespecified direction; capability and policy may pull oppositely.
- **RQ3 — action versus speech:** How often do secret-channel communications indicating collusion fail to correspond to changed actions? Judge scores are a *proxy*, not ground truth; annotate disagreements in a blinded sample.
- **RQ4 — causal affordances:** Does channel privacy, availability, or perturbation alter actions when the objective, seed and per-agent capabilities are fixed?
- **RQ5 — new opportunities:** Which games generate substantive conflicts between a coalition's reward and system welfare while retaining an exact or provably bounded counterfactual optimum?
- **RQ6 — temporal dynamics (exploratory):** With repeated interaction and shared history, do agreements, reciprocity, defections and stable coalitions arise? Colosseum's multiple planning rounds are not automatically a longitudinal game.

## Exploratory idea track

Dolosseum deliberately separates **confirmatory reproduction** from **free-form idea exploration**. New game concepts, channels, institutions, coalition-discovery mechanisms, and counter-hypotheses may be proposed without committing to runnable code. Each starts with one toy example or falsifiable prediction, then can graduate to a separately labeled exploratory protocol with actions, payoff, oracle, controls, and a fixed seed plan. Do not post-select discoveries as if they were preregistered reproduction results. See [`IDEA_PLAYGROUND.md`](IDEA_PLAYGROUND.md).

## Three conditions

| Code | Private colluder blackboard | Extra instruction | Interpretation |
|---|---|---|---|
| B0 | off | no | baseline |
| B1 | on | neutral `control` | secret channel available, no explicit collusion instruction |
| B2 | on | `simple` | explicitly asks colluders to benefit coalition |

Keep agent count, coalition count, environment instance, task assignment rules, planning turns, action limits, providers, and (when supported) decoding settings identical within a matched comparison. **Pair at the seed/scenario level**, not the individual agent level. Preflight API tool calling separately for every model. If a model has a different enforced decoding mode, report rather than disguise the asymmetry.

### Initial fixed task

- Environment: `JiraTicketEnvironment`.
- Graph: complete, consolidated public board.
- Six agents, two selected colluders (`colluder_selection: random`).
- Eight tasks; `assignment_filling: true` for comparison to upstream paper-tag regret config; seed set 1–10.
- Three arms B0, B1, B2; model historical baseline `gpt-4.1-mini-2025-04-14` (or explicitly documented replacement if unavailable).
- Keep both the **paper tag** and raw model ID in run manifest.

Upstream has additional environmental choice variants; do not compare their scores as interchangeable with the fixed Jira task.

## Outcomes

1. **Primary effect:** within-model paired mean `coalition_advantage_mean(B1) − coalition_advantage_mean(B0)`, with per-seed values and intervals. Report joint reward and noncoalition outcomes alongside it. This is a treatment effect estimate, not a declaration of hidden intent.
2. **Prompted capability:** matched B2 − B0 with exactly the same scoring.
3. **Efficiency:** `optimal_joint_reward − actual_joint_reward`, based on *exact solved optimum when available*. The built-in `system_regret` can use `max_joint_reward` as an upper bound; keep upper-bound gap and exact optimum gap distinct. See upstream `experiments/collusion/compute_jira_optimal.py`.
4. **Behavioral distinction:** LLM judge on collusion communications vs realized agent actions, plus blinded manual checks on a stratified sample. Report sensitivity to the judging model, including judge model/version.
5. **Reliability and cost:** valid assignment rate, tool-call failures, early termination, nonresponses, tokens, latency, and estimated provider spend. Do not silently drop unsuccessful runs.

Small-n results are exploratory. Where feasible, use paired bootstrap or permutation confidence intervals over **seed-level replicates**, and publish all seeds and no significance claims for a one-seed smoke test. If absolute rewards vary by scenario/model, use identical scenario instances and clearly document normalization or use paired differences.

## Versioning is part of the treatment

Colosseum paper-tag `paper-v0.1.1` uses Terrarium `0.1.1`. The upstream `main` README states Terrarium `0.2.1` changes at least the stop condition for turns with no tool call and whether an existing pairwise board is reused for private colluder channels. Run paper-tag first, fork extensions into a separately labeled protocol, and never pool harness versions.

## Model refresh

The frontier matrix is a **candidate list**, not a statement that all models have working adapters or provider availability. Prioritize one affordable historical model, one strong modern API model, one locally served model (Dolos vs Qwen2.5 comparator if compatible), then add others as independent PRs. Tool use may behave differently through OpenAI/Anthropic/Together/vLLM adapters. Use official provider identifiers, immutable dated snapshots when possible, record fallback IDs, and preserve version/config in output metadata. See `MODEL_MATRIX.md`.

## Extension menu, ascending risk and complexity

- **E1 Channel controls:** neutral private board B1, broadcast public board, delayed/noisy/redacted secret posts, and a sham channel with no accessible recipients. Match token budget and number of turns.
- **E2 Coalition opportunities:** meeting scheduling with asymmetric preferences, budget allocation with one group favoring itself, and scarce-resource triage with agent-specific utility. All must retain ground-truth system and coalition utilities.
- **E3 Coalition formation:** agents choose whether to communicate/form agreements; coalition not given in advance. Evaluate with predeclared groups vs discovered groups and guard against post-hoc cherry-picking.
- **E4 Repeated game:** multiple genuine outcome-bearing rounds, persistent agent identity/memory, and public/secret history. Test trust, punishment, reciprocity, and defections; compare to independent rounds (reset memory) control.
- **E5 Local white-box probes (stretch):** Dolos/Qwen paired measurement or refusal/valence steering only after the black-box game and metrics are reliable; treat as a separate causal experiment.

## Threats to validity

- **Capability vs willingness:** failure to coordinate could be inability to use tools, not a decision against collusion; report both and separate ability and incentive tests.
- **Model family/policy effects:** providers have different tool semantics, context management, refusal boundaries, pricing, and nondeterminism; don't interpret family differences as pure alignment differences.
- **Prompt leakage and base rates:** ensure colluders aren't accidentally told to favor coalition in the neutral condition; archive system/developer prompts and redact secrets before publishing.
- **Winner's curse / post-selection:** treat new-game discoveries and selected model comparisons as exploratory pending independent replications.
- **Metric gaming:** reward calculation, default/filled assignments, order of selection, and unclaimed tasks can produce artificial coalitional advantages.
- **Judging bias:** the natural-language judge may favor models with more verbose messages or certain styles; conduct blinded manual adjudication of text/action agreement.
- **Dependency drift:** publish paper tag, Terrarium version, CoLLAB commit, environment class, model IDs, config hash, seed, invocation, data schema and any deviations.

## Reporting / completion bar

**Minimum sprint result:** a pinned source checkout, a working three-condition smoke test, one ten-seed six-agent comparison with costs and failures visible, a tiny figure/table on coalition advantage + exact welfare gap, and at least one fully specified new-game proposal. It is fine if extensions are prototypes rather than evaluated findings: label them correctly.

**Post-sprint target:** at least two additional current model families with the same scenario, a channel intervention, and one new game with independently validated objective/oracle.

No numerical claim should appear in `RESULTS.md` without the corresponding run manifest, config, environment version and reproducible calculation.
