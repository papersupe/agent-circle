# Agent Circle — Agent Status

## Current Status

**Status:** Experimental
**Mode:** Reading-Only

Agent Circle is under active development. Its capabilities are intentionally constrained to ensure epistemic reliability and architectural integrity.

---

## What the Agent Can Do (Enabled)

### 1. Read Research Papers

* Ingest academic papers from the approved research corpus
* Parse PDFs and extract structured text
* Preserve metadata such as authorship, publication venue, and year

---

### 2. Extract Core Research Elements

From ingested papers, the agent can identify and record:

* Central research questions
* Core arguments and claims
* Methodologies and experimental designs
* Assumptions and limitations
* Theoretical frameworks

This extraction is analytical, not interpretive beyond source content.

---

### 3. Build Conceptual Summaries

* Generate internal summaries that reflect *conceptual structure*, not abstracts
* Organize ideas into coherent conceptual units
* Maintain traceability back to original sources

These summaries are not exposed as public-facing responses.

---

### 4. Link Ideas Across Papers

* Identify shared concepts across multiple papers
* Connect methods, assumptions, and frameworks
* Track conceptual lineages and overlaps

This enables cross-domain understanding without speculative synthesis.

---

## What the Agent Cannot Do (Explicitly Disabled)

### 1. Answer User Questions

* No live question answering
* No natural-language responses to prompts
* No interactive dialogue

The agent does not yet expose its reasoning as answers.

---

### 2. Perform Actions

* No external API calls
* No tool execution
* No data modification beyond ingestion pipelines

Agent Circle does not act on the world.

---

### 3. Generate Ungrounded Content

* No creative writing
* No speculative explanations
* No extrapolation beyond ingested research

If knowledge is not present in the corpus, the agent remains silent.

---

### 4. Learn Autonomously from Interaction

* No feedback-based learning from users
* No reinforcement from queries or responses

All learning occurs through controlled research ingestion.

---

## Capability Gating

Capabilities are unlocked only when both conditions are met:

1. **Technical readiness** — the system supports the capability safely
2. **Epistemic readiness** — the agent demonstrates grounded understanding

Capability changes are intentional, documented, and reversible.

---

## Status Transparency

The agent’s current status is intended to be visible to:

* Developers
* Researchers
* Users of the Agent Circle interface
* PaperSupe integrations

This transparency prevents overinterpretation of system output.

---

## Planned Status Transitions (High-Level)

* Reading-Only → Guided Querying
* Guided Querying → Structured Q&A
* Structured Q&A → Research Assistance

Each transition requires updates to:

* Architecture
* Evaluation methods
* Interface constraints

---

## Status Guiding Statement

Agent Circle is allowed to understand before it is allowed to respond.

The system remains intentionally limited until its reasoning can be trusted.
