# Self-publishing standards

This repository treats a durable artifact as self-published when an agent or researcher places it in the repository for another person or agent to inspect, verify, reuse, or extend.

## Required qualities

- **Canonical location:** Put the source in the directory that owns its purpose. Keep temporary notes, generated files, and durable artifacts distinguishable.
- **Clear status:** State whether the artifact is a prototype, working draft, or trusted reference. Do not present provisional material as settled.
- **Provenance:** Name the question, inputs, sources, tools, versions, and relevant issue or decision. Link primary sources where possible.
- **Inspectability:** Make the important claims, evidence, assumptions, uncertainty, and alternatives easy to find. Separate source claims from our interpretation.
- **Reproducibility:** Include the command, environment, and preserved inputs needed to regenerate or independently check the result, when applicable. Prefer repository-managed environments over undocumented local state.
- **Reliable handoff:** End with what changed, what remains unresolved, known limitations, and the next useful action. Link related artifacts rather than duplicating them.

## Practical conventions

- Use Markdown for durable notes and Quarto source when the artifact needs rendering, executable content, or a navigable teaching presentation.
- Keep generated output out of source documents. Commit it only when the project explicitly treats the rendered form as a deliverable.
- Preserve negative, inconclusive, and failed results when they affect interpretation or future work.
- Never publish credentials, private data, or unreviewed personal information. Redact or replace them with a precise explanation of what is missing.
- Before publishing, run the narrowest relevant checks and record what was and was not verified.

Self-publishing makes an artifact available; it does not by itself make the artifact correct, final, or endorsed.
