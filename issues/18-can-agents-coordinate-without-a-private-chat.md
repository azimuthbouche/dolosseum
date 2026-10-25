# Can agents coordinate without a private chat?

**Lane:** Communication affordances / open arena  
**Status:** Open to multiple independent contributors; please do not reserve this whole arena.

## Your challenge

Invent an environment where bids, timing, public votes, action order, or other legitimate outputs could let agents coordinate without a secret blackboard. Does the channel even matter?

## First bite — no GPU required

Propose one toy signaling mechanism and a paired intervention where the apparent signal is scrambled, delayed, or made uninformative without changing feasible rewards.

## Good enough for a first PR

A concrete measurement plan comparing action-level coordination with and without the possible indirect signal. Use only synthetic game interactions.

## Stretch ideas

Formalize the game or mechanism using `docs/GAME_TEMPLATE.md`; implement a tiny scorer/oracle, isolate a negative control, or run a carefully labeled exploratory pilot. These are **not** prerequisites to sharing a first idea.

## House rules

Keep scenarios synthetic and benign, describe the intended legitimate task, and distinguish coalition advantage from genuine harm to shared welfare. Cite any upstream code or prior work you reuse. New designs remain **exploratory** until separately preregistered; see `docs/IDEA_PLAYGROUND.md`.
