# Coding agents for cumulative science

We want to do the best and biggest science we can, including science that would not be possible without coding agents.

That ambition asks for more than getting additional output from a model. It asks us to build scientific systems in which longer, larger, and more parallel work becomes cumulative rather than disposable. Earlier work should leave a better starting point for the next researcher, agent, experiment, or project.

We call this **cumulative science**. It compounds two things together:

- our ability to do better scientific work
- the strength and reach of what we understand

Coding agents can expand a researcher's ambition and agency. They make more scientific activity possible at lower cost and greater parallelism. Our direction is to scale the transitions between scientific activities without losing the evolving, provisional state of understanding carried through them.

Scale is useful only when the work remains inspectable and reusable. Another person or agent should be able to understand what was attempted, examine the evidence, question the interpretation, and carry the work forward.

## Why agent scale needs scientific structure

More activity does not automatically produce more science.

Agents work within bounded contexts. They can continue after a task has grown beyond what they can reliably track. Small errors can pass into later steps, acquire the appearance of certainty, and compound as agents reuse one another's output. Without enough structure, scaling activity can scale confusion and slop.

Coding agents are collaborators in scientific work, but they do not supply the scientific structure themselves. That structure comes from the questions we ask, the disciplines we practice, and the ways we preserve the changing state of the research.

## A working view of scientific activity

We currently use eight activities to locate where scientific work happens:

1. Decide:
    1. Orient
    2. Frame
2. Design
3. Implement
    1. Prototype
    2. Build
4. Run
5. Analyze/Interpret
6. Communicate

This is a lens, loosely modeled after [O*NET](https://epoch.ai/gradient-updates/toward-an-onet-for-ai-rnd) and [OpenAI research intern discussion](https://openai.com/index/research-acceleration-view-inside-openai/). Real research moves backward, forward, and across these activities.

At each activity, we ask four questions:

1. What does good work here contribute to cumulative science?
2. What can agents now make possible at a larger scale?
3. What agent limitations or compounding failures appear here?
4. What artifacts, controls, and practices make the work dependable?

## Disciplines for dependable work

Several disciplines recur across scientific activities:

- **Epistemic discipline:** connect claims to evidence, expose assumptions, represent uncertainty, and consider alternatives.
- **Artifact discipline:** preserve provenance, versions, data lineage, tests, and executable state.
- **Context discipline:** separate current state, history, and references; maintain vocabulary and instructions.
- **Coordination discipline:** divide work, manage agents, review outputs, and leave reliable handoffs.
- **Resource discipline:** manage compute, time, cost, access, and scarce experimental opportunities.

These are working concepts, still

## Epistemic status

Science rarely moves cleanly from unknown to known. We work with provisional understanding, graded evidence, uncertainty, and live alternatives.

Epistemic status is the current standing of that understanding. It includes:

- current claims and their confidence
- evidence for and against them
- assumptions and alternative explanations
- negative and inconclusive results
- unresolved questions
- decisions and what justified them

As scientific activity expands, this changing picture must remain visible. A new observation, failed assumption, or competing explanation may affect more than the immediate task. Cumulative science requires us to understand how far that change reaches through the surrounding work.

We have not yet decided how a scientific system should represent or propagate these updates. The principle comes first: provisional understanding must not silently harden into fact as work passes among people and agents.

## Where this stands

This overview is a first orientation, not a curriculum outline. Concrete research harnesses already show useful examples of inspectability, provenance, explicit uncertainty, preserved failures, validation, and reliable handoff. Those examples support the direction, but they do not yet define a universal mechanism set.

The detailed research lifecycle, course sequence, lesson boundaries, recipes, case studies, and implementation practices remain open. We will let further research and prototypes earn that structure.

# A first attempt at a course
In progress...