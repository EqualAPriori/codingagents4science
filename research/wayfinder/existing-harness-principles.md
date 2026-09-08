# Principles already present in Learn_v2 and Elixir harnesses

Date: 2026-09-08

## Scope and method

This is a source audit, not a proposed curriculum. I treated these two projects as
the primary sources:

- `/Users/sesai/Documents/Code/Learn_v2`
- `/Users/sesai/Documents/Code/Elixir`

I weighted executable harness code, manifests, tests, runbooks, and post-run reports
more heavily than general aspiration. A principle is recurring when it is visible in
both projects or in a project rule plus a concrete implementation/report. Exact file
names, schemas, counts, and domain choices are project-specific unless the evidence
shows the same mechanism more than once.

## Short finding

Both projects make cumulative work depend on the same closed loop:

```text
define the question and evidence boundary
  -> freeze identities, inputs, and evaluation rules
  -> preflight the smallest risky dependency
  -> run an isolated logical unit
  -> persist successes, failures, gaps, and provenance
  -> validate completeness and comparison eligibility
  -> update the durable research state
```

The engineering principle is inspectability at each seam. The scientific principle is
that a result is reusable only when its population, metric, uncertainty, provenance,
and limits remain visible.

## Recurring principles

### 1. Separate operating rules, execution state, evidence, and synthesis

Neither project treats chat or memory as the research record. `Learn_v2` separates
repository rules, scientific purpose, current status, progress history, reports, and
source navigation; its research rules explicitly distinguish evidence from facts,
derivations, interpretation, and unresolved questions
(`/Users/sesai/Documents/Code/Learn_v2/research/README.md`, L16-L49;
`/Users/sesai/Documents/Code/Learn_v2/research/AGENTS.md`, L28-L52 and L77-L85).
`Elixir` uses the same separation between `STATUS.md`, `PROGRESS.md`, question-owned
reports, sources, and Git/issues
(`/Users/sesai/Documents/Code/Elixir/research/README.md`, L15-L45;
`/Users/sesai/Documents/Code/Elixir/research/README.md`, L54-L67).

The recurring mechanism is not the exact number of files. It is preserving three
different kinds of change: what the project promises, what was executed, and what the
evidence currently supports. This lets a later reader tell a changed belief from a
changed implementation or an unresolved gap.

### 2. Turn the scientific question into an explicit contract

The strongest harness work starts by specifying the observation unit, claim, positive,
negative, unknown, denominator, leakage boundary, abstention behavior, and decision
rule. Elixir's target contract separates structural validity, comparative site
ranking, condition/speciation compatibility, and absolute feasibility because they
require different observations and populations. It explicitly says that missing yield
and unrecorded alternatives are unknown, not failures, and requires reason codes for
synthetic negatives
(`/Users/sesai/Documents/Code/Elixir/research/reaction-viability/31-target-evaluation-contract/report.md`, L9-L22 and L40-L78).
The same report makes denominators and abstentions claim-specific and freezes the
benchmark, candidate generator, preprocessing, negative policy, and threshold
procedure before final evaluation (L80-L121).

`Learn_v2` makes scientific fidelity a completion gate: measure against the original
scientific contract, keep gaps visible, and do not redefine success around the easiest
implementation or available evidence
(`/Users/sesai/Documents/Code/Learn_v2/docs/agents/scientific-fidelity.md`, L87-L96 and L119-L137).

Recurring practice: make the intended claim executable before optimizing the pipeline.
Project-specific choices include reaction-site labels in Elixir and molecular-alert
or induction contracts in Learn_v2.

### 3. Freeze identity and inputs before the outcome can influence them

Both projects make a prepared unit carry identity and provenance. In `Learn_v2`, the
campaign evidence compiler groups planned cells by endpoint, evidence size, replicate,
and knowledge state, derives a requirement identity, and resolves only reviewed
freezes whose corpus, membership, and target identities match
(`/Users/sesai/Documents/Code/Learn_v2/src/rdkit-agent/src/rdkit_agent/campaign/evidence.py`, L39-L115 and L118-L168).
The preparation path checks freeze status, endpoint, and SHA-256 digests before
compilation
(`/Users/sesai/Documents/Code/Learn_v2/src/rdkit-agent/src/rdkit_agent/campaign/preparation.py`, L56-L114).
The registry rejects absolute or parent-traversing paths, validates repository and
protected-external artifact references, and checks supplied hashes against bytes
(`/Users/sesai/Documents/Code/Learn_v2/src/rdkit-agent/src/rdkit_agent/campaign/registry_contract.py`, L64-L120).

Elixir's ten-target prototype selects a deterministic source-order prefix before any
method probe, retains occurrence identity and source fields, preallocates the full
target × profile × attempt denominator, and records a terminal disposition for every
attempt
(`/Users/sesai/Documents/Code/Elixir/research/reaction-viability/36-complete-10-target-pipeline/report.md`, L24-L46;
`/Users/sesai/Documents/Code/Elixir/research/reaction-viability/36-complete-10-target-pipeline/README.md`, L6-L12).

Recurring practice: freeze the input population, configuration, and identity before
execution; hash the boundaries; reject mismatches. This is the foundation for both
engineering replay and scientific comparability.

### 4. Use cheap preflight gates to expose expensive blockers

`Learn_v2` requires import checks, dry runs, provider-readiness checks, and explicit
stop conditions before long or costly execution
(`/Users/sesai/Documents/Code/Learn_v2/AGENTS.md`, L35-L50 and L56-L67;
`/Users/sesai/Documents/Code/Learn_v2/docs/agents/provider-runs.md`, L1-L97).
Its campaign status path reports missing corpus identity, sampling contract,
membership, or target set instead of allowing an apparently ready campaign
(`/Users/sesai/Documents/Code/Learn_v2/src/rdkit-agent/src/rdkit_agent/campaign/evidence.py`, L171-L244).

Elixir uses the same gate for data and external assets. Its URSA smoke passed its
available tests, loaded the smallest route bundle, then stopped at a missing pinned
database; the report explicitly makes no production score claim
(`/Users/sesai/Documents/Code/Elixir/research/reaction-viability/33-ursa-smoke-visualization/report.md`, L7-L18 and L77-L98).
The ten-target pipeline retains no-go arms and condition gaps rather than replacing
them with fixtures
(`/Users/sesai/Documents/Code/Elixir/research/reaction-viability/36-complete-10-target-pipeline/report.md`, L48-L69).

Recurring practice: convert an assumption into the smallest executable question and
record the blocker in the result. The exact asset and environment checks are
project-specific.

### 5. Keep the harness generic; keep domain meaning in adapters and contracts

Elixir states the ownership boundary directly: the experiment harness owns
orchestration identity, persistence, validation, retry, and accounting; planners and
conditions remain behind injected adapters. Native dependencies are pinned, exact
emitted bytes are preserved before normalization, and native ranks and scores remain
semantically local
(`/Users/sesai/Documents/Code/Elixir/src/experiment-harness/AGENTS.md`, L1-L14).
The complete-pipeline report demonstrates the boundary: native planner captures are
retained, only outputs accepted by the pinned normalizer become route/step identities,
and prior captures are not reused as fabricated output for new target occurrences
(`/Users/sesai/Documents/Code/Elixir/research/reaction-viability/36-complete-10-target-pipeline/report.md`, L48-L60).

`Learn_v2` uses the analogous separation between campaign registry/preparation,
method-specific compilers, and finalization. The output catalog records method-owned
artifacts with role, type, relative path, hash, record count, lifecycle, and historical
grade, then rebuilds a query-facing catalog while rejecting changed or duplicate
artifacts
(`/Users/sesai/Documents/Code/Learn_v2/src/rdkit-agent/src/rdkit_agent/campaign/output_catalog.py`, L25-L77 and L97-L139;
`/Users/sesai/Documents/Code/Learn_v2/src/rdkit-agent/src/rdkit_agent/campaign/output_catalog.py`, L168-L218).

Recurring practice: make the shared spine responsible for lifecycle guarantees and
make adapters responsible for domain semantics. This allows new methods to be
compared without pretending their native outputs mean the same thing.

### 6. Make retries, artifacts, and accounting append-only and conflict-visible

Elixir's harness contract treats campaign manifests, ledger events, and
content-addressed artifacts as immutable; conflicts are rejected, and a retry is a
new method invocation inside the same logical attempt without changing frozen
configuration or randomness
(`/Users/sesai/Documents/Code/Elixir/src/experiment-harness/AGENTS.md`, L3-L6).
Its research ingestion note applies the same rule to source material: preserve each
source, derive artifacts with lineage, and report `already present`, `new version`, or
`content conflict` rather than silently overwriting
(`/Users/sesai/Documents/Code/Elixir/research/notes/2026-08-18 - research ingestion design sources.md`, L37-L45 and L79-L117).

`Learn_v2` implements a concurrency-safe run ledger with explicit call identity,
attempt/retry links, usage source, response lifecycle, and spend-guard state; provider
batch cost is reserved before launch
(`/Users/sesai/Documents/Code/Learn_v2/src/rdkit-agent/src/rdkit_agent/ledger.py`, L23-L70 and L172-L212;
`/Users/sesai/Documents/Code/Learn_v2/src/rdkit-agent/src/rdkit_agent/ledger.py`, L233-L286).
Its replay CLI verifies the retained program hash before evaluation and writes an
explicit values/error result
(`/Users/sesai/Documents/Code/Learn_v2/src/rdkit-agent/src/rdkit_agent/replay_cli.py`, L24-L49).

Recurring practice: never repair, overwrite, or silently merge an evidence-bearing
record. Preserve the failed or superseded state and make a new invocation or version.

### 7. Treat partial, zero, and no-go outcomes as evidence states

Elixir's evaluation contract distinguishes positive, negative, and unknown, and says
that unknown cannot be relabeled as negative
(`/Users/sesai/Documents/Code/Elixir/research/reaction-viability/31-target-evaluation-contract/report.md`, L53-L78).
The ten-target report carries this into execution: successful, empty, normalization
error, and intentional no-go counts all remain visible, while the aggregate output is
left empty because its schema contract is contradictory
(`/Users/sesai/Documents/Code/Elixir/research/reaction-viability/36-complete-10-target-pipeline/report.md`, L9-L22 and L71-L89).

`Learn_v2` uses explicit campaign states (`planned`, `prepared`, `in_progress`,
`executed`, `incomplete`, `superseded`) and controlled transitions rather than one
boolean completion flag
(`/Users/sesai/Documents/Code/Learn_v2/src/rdkit-agent/src/rdkit_agent/campaign/registry_contract.py`, L13-L23).
Native finalization also retains attempted counts, failed counts, target-closure
failures, prediction coverage, and the selected artifact status in the result
manifest
(`/Users/sesai/Documents/Code/Learn_v2/src/rdkit-agent/src/rdkit_agent/native_induction/finalization.py`, L95-L139 and L164-L215).

Recurring practice: a failed or incomplete unit is a typed observation about the
system, not missing data to be silently dropped. The state vocabulary itself is
project-specific; the preservation rule is not.

### 8. Close the loop with a fresh-reader handoff and bounded claims

Both projects require the final artifact to stand on its own. `Learn_v2` asks for a
fresh-reader pass, citation and lineage checks, reproducible calculations, and updates
to the synthesis and status surfaces; completion means another agent can locate the
evidence, distinguish interpretation from evidence, and reproduce the calculation
from pinned inputs
(`/Users/sesai/Documents/Code/Learn_v2/research/AGENTS.md`, L109-L133;
`/Users/sesai/Documents/Code/Learn_v2/docs/agents/research-reporting.md`, L116-L143).
`Elixir` gives every investigation the same durable minimum: question, evidence grade,
pinned inputs, reproduction command, result locations, and a report that updates the
question-owning program when the epistemic state changes
(`/Users/sesai/Documents/Code/Elixir/research/README.md`, L54-L67;
`/Users/sesai/Documents/Code/Elixir/research/notes/2026-08-18 - research ingestion design sources.md`, L47-L60 and L96-L108).

The reports also bound their conclusions. Elixir's ten-target prototype calls itself
an integration/accounting prototype, not planner or condition quality evidence, and
its target contract leaves predictive utility and laboratory feasibility as later
empirical questions
(`/Users/sesai/Documents/Code/Elixir/research/reaction-viability/36-complete-10-target-pipeline/README.md`, L29-L40;
`/Users/sesai/Documents/Code/Elixir/research/reaction-viability/31-target-evaluation-contract/report.md`, L149-L172).

Recurring practice: harvest durable state into a report, cite the exact evidence, state
what the run did not establish, and update the current research map. A result that
exists only in chat, an unreferenced output directory, or an unbounded conclusion is
not cumulative knowledge.

## Recurrent artifacts and their roles

| Role | Repeated practice in both projects | Why it compounds |
|---|---|---|
| Question contract | Report the claim, observation unit, eligible population, unknowns, and decision boundary | Prevents later work from answering a nearby question |
| Input freeze | Manifest, identity, version, checksum, split or membership rule | Makes reruns and comparisons refer to the same object |
| Preflight | Import/smoke/asset/schema check with a stop condition | Finds blockers before expensive execution |
| Execution spine | Logical unit, attempt identity, retry relation, terminal disposition | Preserves denominator and failure structure |
| Evidence store | Raw/native output plus derived result and lineage | Keeps interpretation traceable to bytes |
| Validation gate | Hash, schema, completeness, denominator, and conflict checks | Prevents plausible-looking invalid results |
| Research handoff | Report, status/progress update, reproduction command, exact artifact pointers | Lets the next session resume without reconstructing context |

These roles recur. The exact JSON schemas, chemistry labels, model names, and artifact
taxonomies are local design choices.

## Failure modes the harnesses actively prevent

1. **A nearby question is mistaken for the requested question.** The remedy is a
   claim-specific contract and scientific-fidelity gate.
2. **Unknown or missing observations are treated as failures.** The remedy is explicit
   evidence status, reason codes, and claim-specific denominators.
3. **A long run starts with an unverified dependency.** The remedy is a bounded
   preflight and an explicit no-go state.
4. **A method-specific output is normalized into a false shared meaning.** The remedy
   is adapter ownership, native capture retention, and a separate normalization gate.
5. **A retry or repair changes the experiment invisibly.** The remedy is immutable
   configuration, logical-attempt identity, append-only invocation records, and
   conflict rejection.
6. **A partial run disappears from the denominator.** The remedy is preallocation or
   explicit terminal dispositions for every planned unit.
7. **A result survives without enough provenance to replay it.** The remedy is pinned
   inputs, hashes, source manifests, exact commands, and fresh-reader review.
8. **A prototype is promoted to a scientific claim.** The remedy is an evidence grade
   and a report section naming what was not established.

## What is project-specific

The following choices should not be elevated into universal principles merely because
they are concrete:

- `Learn_v2`'s campaign IDs, endpoint-evidence freeze schema, RDKit/native-induction
  method names, provider price table, and protected-truth layout.
- `Elixir`'s reaction-site claims, planner profiles, RetroCast normalization boundary,
  target-occurrence sampling slice, and chemistry-specific reason codes.
- The particular filenames (`STATUS.md`, `PROGRESS.md`, `result.json`, and so on),
  branch conventions, hash algorithm, and JSONL/JSON/Parquet representation.
- Numerical gates such as Elixir's 95% precision example or any fixed attempt count.
  Their durable lesson is to prespecify and report a gate, not to reuse the number.

## Bottom line

The existing harnesses already encode a practical theory of cumulative engineering and
science: freeze the object of comparison, make lifecycle and evidence states explicit,
preserve raw failures and provenance, validate before interpreting, and publish a
bounded handoff that changes the durable research state. Their strongest common feature
is not automation depth. It is the refusal to let convenient execution erase what was
actually observed.
