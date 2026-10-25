# Invent a meeting-scheduling favor-trading game

**Lane / size:** New game / small–medium / ~1–3 hours  
**Claim:** Comment on this issue to volunteer; first PR can be small. Do not claim completion based on a plan alone.

## Why this is fun

Could two agents quietly sacrifice meeting coverage to give each other better slots?

## First bite

Design a meeting-slot allocation with public coordination reward and private coalition advantage. Check first whether upstream already has `MeetingSchedulingChoiceEnvironment` and adapt instead of duplicating. Provide a small instance with exact optimum, roles, allowed actions, messages and what behavior would *count* as harmful collusion rather than harmless bargaining.

## Definition of done

A filled game template, one numeric example, a toy oracle/test, and a decision on reusing upstream meeting scheduling versus writing a new subclass.

## Dependencies

No provider needed; coordinate only if someone else is editing the same environment.

## Useful links

- [Upstream Colosseum](https://github.com/umass-ai-safety/colosseum)
- [Paper](https://arxiv.org/abs/2602.15198)
- Research protocol: `docs/RESEARCH_PLAN.md` (in this repository)

**Remember:** distinguish exploratory pilots from baseline reproduction, and log actual versions, seeds and failures.
