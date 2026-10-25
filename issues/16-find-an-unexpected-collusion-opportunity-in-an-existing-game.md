# Find an unexpected collusion opportunity in an existing game

**Lane:** Opportunity hunting / open arena  
**Status:** Open to multiple independent contributors; please do not reserve this whole arena.

## Your challenge

Maybe the interesting collusion experiments are already latent in Colosseum's environments. Inspect an existing game's rules and find a surprising coalition incentive the original sweep didn't isolate.

## First bite — no GPU required

Choose any existing upstream game, identify a possible joint deviation or non-obvious information asymmetry, and give a toy action/payoff example. Say what legitimate cooperation would do instead.

## Good enough for a first PR

A concrete hypothesis grounded in one existing environment, plus a control that would distinguish the effect from ordinary efficiency or randomness. No API run required.

## Stretch ideas

Formalize the game or mechanism using `docs/GAME_TEMPLATE.md`; implement a tiny scorer/oracle, isolate a negative control, or run a carefully labeled exploratory pilot. These are **not** prerequisites to sharing a first idea.

## House rules

Keep scenarios synthetic and benign, describe the intended legitimate task, and distinguish coalition advantage from genuine harm to shared welfare. Cite any upstream code or prior work you reuse. New designs remain **exploratory** until separately preregistered; see `docs/IDEA_PLAYGROUND.md`.
