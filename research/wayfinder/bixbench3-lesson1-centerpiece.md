# BixBench3 and a second centerpiece for Lesson 1

Date: 2026-09-08

Ticket: [EqualAPriori/codingagents4science#9](https://github.com/EqualAPriori/codingagents4science/issues/9)
Branch: `research/bixbench3-lesson1-centerpiece`

## Question and scope

What can BixBench3 and *AI scientists produce results without reasoning scientifically*
teach the first lesson's central question: **Think Big—and where are the failure modes
today?** This note is a source review for the Lesson 1 prototype, not a proposal to
redesign the course map.

I used the two papers, their author-provided code/data artifacts, and this repository's
`README.md`, `CONTEXT.md`, and issue-tracker guidance. Paper claims, course
interpretations, and proposed coding-agent tasks are kept separate below. The papers
are preprints; numerical and methodological claims should be rechecked against later
versions before a benchmark is treated as a stable reference.

## Short finding

The papers support a useful two-part Lesson 1 thesis:

1. Coding agents can already be assigned work at the scale of a complete computational
   study, but current success is partial, expensive, sensitive to data size and chain
   depth, and dependent on a prescribed method and exact artifact contract.
2. Producing a plausible or even correct result does not show that the agent used
   evidence scientifically. In the second paper, evidence uptake, testing, belief
   revision, and convergent evidence are measured directly and are often absent.

Together, the papers motivate a prototype that makes both output quality and the path
to the output inspectable. Neither paper by itself establishes that a particular
course scaffold will solve these failures, that agents can choose important research
questions, or that a successful reproduction is a new scientific discovery.

## 1. Paper claims: BixBench3

### Scientific task and setup

BixBench3 asks an agent to reconstruct the analysis of a published computational-biology
study from raw data. The scientist supplies a biological objective and methodological
guidance; the agent is responsible for implementing the analysis and writing structured
artifacts. The benchmark contains 20 studies across 17 assay types and 9 scientific
domains, with 138 graded artifacts. The artifacts form a dependency graph from raw
data through downstream analyses, so the task is longer-horizon than an isolated
biology question or one analysis command. [BixBench3 paper](https://arxiv.org/html/2608.25286v1#S1)

The benchmark runtime used a 32-vCPU, 128-GB-memory Google Cloud VM, a 500-GB boot
disk, no GPU, Docker, a 24-hour wall-clock limit, and no fixed token limit. Agents had
five tools in an Inspect AI ReAct loop: a persistent shell, Python, text editing,
web-access requests, and submission. Network access was mediated by an allowlist and
an adjudicated request path intended to prevent access to answers such as the original
paper and processed data. [BixBench3 methods](https://arxiv.org/html/2608.25286v1#S4.SS2)

### Evaluation

Each requested artifact is compared with the corresponding published artifact. The
grader uses row/column F1, Lin's concordance correlation coefficient, macro F1 for
categorical labels, and genomic-interval overlap F1 as appropriate. The metrics are
multiplied into one artifact score; an artifact passes at 0.80 or above, a threshold
calibrated against expert ratings of 25 artifacts. A task score is the proportion of
its artifacts that pass. Separately, an LLM process judge reads the prompt, the agent's
`METHODS.md`, a compacted trace, grading summaries, and artifact previews to attach
evidence-backed run-level failure-mode tags. [BixBench3 grading and process judge](https://arxiv.org/html/2608.25286v1#S4.SS4)

### Results reported by the paper

- Thirteen frontier models were evaluated over 260 completed runs and 1,794
  model-artifact evaluations. The highest mean task score was 0.48, meaning that
  approximately 48% of requested artifacts retained the original artifact's main
  biological meaning under the paper's pass criterion.
- Mean binary artifact pass rates were 0.30 for depth-1 artifacts, 0.44 for depth-2
  artifacts, and 0.24 for depth-3-or-more artifacts. For raw-input size, the paper
  reports an average score of 0.10 on tasks above 100 GB, compared with 0.36 below
  100 GB in the abstract and more detailed size bins in the results.
- An average attempt used 102 million tokens, 6.8 hours, and $43. The most expensive
  or longest attempts reached 1.07 billion tokens, 24 hours, and $525. Higher score
  did not require maximum cost; the paper describes a cost-performance Pareto frontier.
- Premature termination and repetitive retry loops were enriched in the lowest-score
  quantile. Environment setup failures, incomplete data, and synthetic or placeholder
  outputs were also enriched there.

These results measure reproduction of specified artifacts, not autonomous question
selection. The authors explicitly say that task prompts prescribe the analyses and
that a scientifically valid alternative can score poorly if it differs from the
published artifact in format, scale, or other details. The benchmark also inherits
possible errors or under-specification from its source papers. [BixBench3 results and limitations](https://arxiv.org/html/2608.25286v1#S3.SS1)

### Linked artifacts and what they make inspectable

The authors provide a [public runner and deterministic grader](https://github.com/EdisonScientific/BixBench3), a [Hugging Face dataset card and task index](https://huggingface.co/datasets/EdisonScientific/BixBench3), and a benchmark page with links to the paper, code, and dataset. The repository documents prompts and output contracts in the dataset, raw inputs and metadata in GCS, and separate ground-truth artifacts and grading specifications. Access to the dataset files requires accepting a contact-information condition, and the raw scientific data retain upstream terms. This is useful provenance, but it means “publicly described” and “locally reproducible without credentials, cloud resources, or licensed software” are not the same claim. [BixBench3 repository README](https://github.com/EdisonScientific/BixBench3#readme)

## 2. Paper claims: AI scientists produce results without reasoning scientifically

### Scientific task and setup

The second paper asks whether LLM-based scientific agents exhibit epistemic patterns
that make scientific inquiry self-correcting. It reports more than 25,000 runs across
eight scientific domains, 15+ environment scopes, and 90+ tools. The environments span
workflow execution, strategic search, and hypothesis-driven inquiry. Within domains,
scope is varied from smaller to larger search spaces and tasks are decomposed into
subtasks for retrieval, execution, reasoning, and validation. [Paper abstract and benchmark design](https://arxiv.org/html/2604.18805v1#S1)

The main experiments compare three models (GPT-4o, Claude Sonnet 4.5, and GPT-OSS-120B)
and two scaffolds (ReAct and structured tool calling). Main scores use temperature 0;
tool-description verbosity is varied in a controlled way. The authors analyze both
performance and traces. For epistemological graphs, traces are annotated into
hypothesis, test, evidence, judgment, update, and commitment nodes, with edges such as
testing, observing, contradicting, competing, and updating. The paper reports automated
checks that quotes occur in cited messages, expert-guided annotation design, and
substantial agreement on a representative sample of 25 traces. [Methods for agents and trace annotation](https://arxiv.org/html/2604.18805v1#S4.SS3)

### Results reported by the paper

- In the paper's latent-factor decomposition, reasoning ability explains 41.4% of
  explained variance, environment scope 30.1%, scaffold 1.5%, and tool-description
  verbosity 0.1%. The authors' conclusion is that the base model was the primary
  determinant in these experiments.
- Untested claims occurred in 53% of traces overall and 63% in hypothesis-driven
  domains. Evidence non-uptake occurred in 68%; beliefs were never updated in 71%;
  refutation-driven belief revision appeared in 26%; and convergent multi-test
  evidence appeared in 7%.
- The paper reports little adaptation of reasoning topology to epistemic demand.
  Evidence non-uptake was 82% in workflow domains, 66% in strategic reasoning, and
  60% in hypothesis-driven domains. The authors interpret the common topology as a
  single reasoning mode that may be adequate for procedural work but is not enough for
  disciplined inquiry under uncertainty.
- Injecting one or two successful early steps helped workflow tasks, while
  hypothesis-driven and strategic tasks required near-complete successful traces to
  show gains. In those harder groups, the probability that all repeated trials
  succeeded fell below 0.05 by roughly 4–6 trials under baseline conditions.

The paper's claim is about measured behavior in these environments and configurations.
It does not show that every coding agent has the same epistemic profile, that no
scaffold can ever help, or that process annotations are a complete measure of
scientific reasoning. Its graph analysis uses ReAct traces, its annotation is partly
LLM-mediated, and its main model comparison is only three models. [Results and limitations in the paper](https://arxiv.org/html/2604.18805v1#S2)

### Linked artifacts

The authors publish the [Corral framework](https://github.com/lamalab-org/corral), a
[Hugging Face collection of environments, traces, reports, annotations, and
log-probabilities](https://huggingface.co/collections/jablonkagroup/corral), and a
Zenodo archive linked from the paper. The framework's README describes standardized
tools, environments, agents, multiple trials, and pass@k-style metrics; these are
implementation artifacts that make the paper's evaluation approach more inspectable,
not independent evidence for every result in the paper. [Corral README](https://github.com/lamalab-org/corral#readme)

## 3. Course interpretation

This section applies the repository's vocabulary; the mappings are interpretations of
the sources, not claims made by the papers.

### What “Think Big” can mean here

The current `README.md` frames the course around **cumulative science**: more ambition,
scale, and parallelism are valuable only when work remains inspectable and reusable.
`CONTEXT.md` defines the **research activity map**, **prototype**, **research artifact**,
and **reliable handoff**, but the current files do not define the issue's “Horizon” or
“Compass” terms. That is a live vocabulary question for Lesson 1.

BixBench3 gives “big” a concrete operational meaning: raw data, long dependency chains,
many artifacts, substantial compute, and a handoff from a scientist's objective to an
agent's implementation. The second paper adds a different scale axis: increasing
epistemic demand and scope. The course should not collapse these into one number. A
large workflow can be procedurally difficult but epistemically prescribed; a smaller
task can be scientifically demanding if it requires competing hypotheses, discriminating
tests, and belief revision.

### Map to the README concepts

| Course concept | Evidence-bearing case | Interpretation for Lesson 1 |
|---|---|---|
| Scientific ambition and agency | BixBench3 delegates a complete analysis implementation from a high-level objective; Corral spans workflow to hypothesis-driven environments. | Thinking big includes asking what work can be delegated at study scale, but also choosing a scale of question and evidence that remains governable. |
| Bounded context and compounding errors | BixBench3 reports lower scores for deeper artifact dependencies and possible accumulation of early errors; the second paper reports repeated-trial unreliability and poor evidence uptake. | The prototype should make intermediate state and error propagation visible, rather than showing only a final answer. |
| Decide: orient and frame | In BixBench3, the scientist supplies objective and method; in the second paper, some environments require the agent to form hypotheses. | Separate delegation of a framed question from agent ability to frame or select a good question. |
| Design | BixBench3 supplies parameters, contrasts, filters, and output contracts; hypothesis-driven Corral tasks require discriminating tests. | A Lesson 1 task should expose what is fixed by the human and what the agent must design. |
| Implement and run | BixBench3 directly evaluates a multi-step pipeline from raw data to artifacts. | This is the strongest direct bridge from the papers to coding-agent work. |
| Analyze/Interpret | BixBench3 grades artifacts against published outputs; the second paper inspects evidence, judgments, updates, and commitments. | Output similarity and scientific interpretation are different evidence layers and should be graded separately. |
| Communicate and reliable handoff | BixBench3 requires exact output paths/formats and `METHODS.md`; Corral preserves traces and reports. | A handoff should include artifacts, methods, evidence links, failures, uncertainty, and rerun information, not just a score. |
| Epistemic discipline | The second paper directly measures untested claims, evidence non-uptake, belief updates, and convergent evidence. | Require explicit hypotheses, tests, observations, updates, and unresolved contradictions in the prototype. |
| Artifact discipline | BixBench3 uses dependency graphs, output contracts, deterministic grading, and retained run artifacts. | Freeze inputs and contracts; preserve raw outputs, derived outputs, and provenance. |
| Inspectability | Both projects expose structured artifacts; Corral also exposes trace annotations and graphs. | Build a purpose-made view of what happened at each seam. Inspectability is not the same as correctness. |
| Reproducibility | Both projects publish code and data artifacts, but BixBench3 still depends on cloud storage, credentials, and some licensed software. | Distinguish reproducible protocol, reproducible computation, and accessible rerun in the lesson. |
| Coordination and resource discipline | BixBench3 shows 24-hour/500-GB/compute limits and large token/cost variation; its harness and process judge coordinate the run. | Include a budget, stopping rule, and explicit human/agent handoff. The papers do not test course-style multi-agent coordination directly. |

### What the papers support about current failure modes

They support a bounded claim that current agents can execute long prescribed analyses
with partial success while failing under larger data, deeper dependencies, and some
recovery situations; and that process traces can reveal failures invisible to a final
answer score. They do not support the stronger claim that agents cannot do science at
all, that benchmark reproduction equals discovery, or that prompt/scaffold changes are
universally ineffective. The second paper finds scaffolds explained little variance in
its decomposition, but its own environments and models define the scope of that result.

The course's central failure is therefore not simply “the model made a mistake.” It is
that a plausible output can hide an untested premise, ignored evidence, missing
provenance, an invisible retry loop, an incomplete denominator, or a failure to tell the
next researcher what remains unknown. This is a course interpretation grounded by the
two papers and aligned with the `README.md` emphasis on epistemic status, inspectability,
and reusable artifacts.

## 4. Proposed coding-agent tasks

These are proposals for a Lesson 1 prototype, not paper results.

### Task A: miniature study-scale reconstruction

Give the agent a small, fixed, openly licensed dataset, a research objective, method
guidance, and a three-artifact output contract. Put inputs under read-only `data/`,
require all derived files under `outputs/`, and cap the run at 30–45 minutes. Require:

- a raw-to-derived dependency manifest with input hashes and tool versions;
- two intermediate artifacts and one downstream result, each with a deterministic
  schema and a small reference output;
- `METHODS.md` that records commands, parameters, deviations, failures, and stopping
  decisions; and
- a handoff that separates observed results, interpretation, uncertainty, and next
  checks.

Grade artifact structure and values with deterministic checks, then separately review
whether the run preserved provenance, exposed failures, and completed the denominator.
Run the same task once with a short horizon and once with a larger artifact chain. This
is a small, affordable analogue of BixBench3, not a claim that its score predicts
performance on the full benchmark.

### Task B: evidence-update loop

Give the agent a deterministic toy scientific environment with two competing hypotheses,
several tests of unequal cost, noisy observations, and one deliberately ambiguous or
contradictory result. Ask it to choose tests under a fixed budget, record a hypothesis
before each test, state what observation would discriminate the hypotheses, update its
belief after each result, and finish with a bounded conclusion or abstention.

Grade the final decision separately from the trace structure: hypotheses must be
testable, selected tests must connect to the stated uncertainty, observations must be
quoted or linked, contradictions must be acknowledged, and the final belief must
change when the prespecified evidence warrants it. Compare a one-shot answer with a
version that has to maintain an evidence journal. This is a course prototype inspired
by Corral's epistemological graph formalism, not a replication of the second paper's
eight-domain evaluation.

The two tasks can be combined later, but Lesson 1 should first decide whether it wants
to teach study-scale execution, evidence-sensitive inquiry, or the seam between them.

## 5. Open questions for the Lesson 1 prototype

1. What exactly does “Think Big” mean in the lesson: larger datasets and longer
   horizons, a more ambitious scientific question, parallel delegation, cumulative
   artifacts, or all four?
2. What are “Horizon” and “Compass” in the course vocabulary? They are referenced by
   the ticket but are not defined in the current `README.md` or `CONTEXT.md`.
3. Is the first prototype meant to be a local, low-cost teaching exercise or a faithful
   miniature of a cloud benchmark? The BixBench3 resource profile makes a full
   reproduction unsuitable as the default lesson exercise.
4. Which boundary should the human set: question, method, data, evaluation contract,
   stopping rule, or all of them? What should the coding agent be allowed to decide?
5. Should success require both a correct artifact and a defensible evidence record?
   If so, which process properties are mandatory, and how will they be scored without
   treating an LLM judge as ground truth?
6. How should the prototype represent unknown, incomplete, failed, and intentionally
   stopped work? A binary “pass/fail” would hide the failure modes the course wants
   students to notice.
7. What is the comparison baseline: one long agent run, checkpointed execution,
   multiple independent trials, a human-only run, or different scaffolds around one
   model?
8. How much coordination is in scope for Lesson 1? The papers provide useful harness,
   trace, and artifact patterns, but they do not establish the best way to divide work
   among multiple agents or create a reliable human-agent handoff.
9. Which dataset and software license permit students to rerun the exercise locally,
   and what resource budget is acceptable for a course cohort?
10. What lesson artifact should persist after the prototype: a report, evidence journal,
    run manifest, inspectable trace, reusable task harness, or a compact combination?

## Sources

- Koch et al., “BixBench3: Benchmarking AI agents on research-study-scale computational biology tasks,” [arXiv:2608.25286](https://arxiv.org/abs/2608.25286) and [HTML full text](https://arxiv.org/html/2608.25286v1).
- Edison Scientific, [BixBench3 runner and deterministic grader](https://github.com/EdisonScientific/BixBench3), [dataset card](https://huggingface.co/datasets/EdisonScientific/BixBench3), and [benchmark results page](https://advances.edisonscientific.com/benchmarks/bixbench3/).
- Ríos-García et al., “AI scientists produce results without reasoning scientifically,” [arXiv:2604.18805](https://arxiv.org/abs/2604.18805) and [HTML full text](https://arxiv.org/html/2604.18805v1).
- Jablonka group, [Corral framework](https://github.com/lamalab-org/corral) and [published artifact collection](https://huggingface.co/collections/jablonkagroup/corral).
- This repository's [README.md](../../README.md) and [CONTEXT.md](../../CONTEXT.md).
