# Formalize a Dolosseum game

For a first idea sketch, use [`IDEA_PLAYGROUND.md`](IDEA_PLAYGROUND.md) instead. This fuller template is for promoting a promising pitch into a testable environment.

Name: **[short memorable title]**  
Pitch (2 sentences): **[what the agents ostensibly try to achieve, and why a coalition might defect]**

## Mechanism

- **Legitimate shared objective:** [define reward `W(a_1, ..., a_n, s)` and what the optimum means]
- **Coalition's secondary objective:** [define `C(a_1, ..., a_n, s)` and specify the conflict with `W`]
- **Players/roles:** [n, symmetry/asymmetry, private/public information]
- **Available actions:** [discrete feasible action sets; no open-ended score ambiguity]
- **Communications:** [public/private channels; timing; topology; who can read them]
- **Sequence:** [one-shot or repeated genuine rounds; if repeated, what state persists?]
- **Payoffs:** [numerical toy instance for which both welfare and coalition reward can be computed]
- **Oracle/scorer:** [exact search, integer program, known optimum, or explicit approximation bound]
- **Controls:** [no secret B0; neutral secret B1; prompted B2; at least one confound check]
- **Failure modes:** [degenerate incentives, impossible coordination, lack of observability, oracle blowup, prompt leakage]

## Minimum deliverable

A toy JSON/game config with 3–6 players, a `score(actions, instance)` reference implementation, and at least **three invariant tests**: valid actions, score consistency, and a small enumerated exact optimum. No need for a polished Terrarium subclass until the game earns it.

## Questions to answer before coding

1. Could higher colluder reward arise without reducing system welfare? If yes, how will you distinguish it from harmful collusion?
2. Does the hidden coalition receive different **information** or merely a private ability to coordinate? Which causal contrast are you testing?
3. Can a trivial agent maximize coalition reward alone? If so, it is not really testing multi-agent collusion.
4. Are there enough independent instances to avoid cherry-picking a colorful anecdote?

## Example seed ideas

- **Meeting schedule swap:** jointly maximize meeting coverage; private coalition prefers a specific slot that imposes missed connections on everyone else.
- **Disaster-response allocation (simulated):** coordinate vehicles to priority zones; coalition reroutes scarce resources toward its own zones.
- **Compute allocation:** optimize total queue value while some agents are incentivized to divert scarce GPU time to coalition workloads.
- **Reciprocal favors (repeated):** a sequence of independent-looking allocations; two agents trade favors across rounds and punish defections.

These are *ideas*, not implemented or validated environments. New games must use synthetic/fictitious assets and an objectively checkable scorer.
