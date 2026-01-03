# Agent Circle — Roadmap

## Purpose of the Roadmap

This roadmap defines the **intentional, capability-gated evolution** of Agent Circle. Progression is not driven by feature demand, but by demonstrated understanding, stability, and epistemic safety.

Capabilities unlock only when prerequisites are met and validated.

---

## Guiding Principles

* **Understanding before interaction**
* **Grounding before generation**
* **Structure before scale**
* **Clarity before capability**

Each phase builds on the previous one without breaking architectural or epistemic constraints.

---

## Phase 0 — Foundation (Current)

**Status:** Active
**Mode:** Reading-Only

### Objectives

* Establish vision, architecture, and status constraints
* Build stable ingestion and storage pipelines
* Ensure reproducibility and traceability

### Enabled Capabilities

* Paper ingestion (PDF → text)
* Metadata preservation
* Semantic chunking
* Embedding generation
* Vector indexing

### Explicitly Disabled

* User queries
* Natural language responses
* External actions

---

## Phase 1 — Concept Extraction

**Status:** Planned

### Objectives

* Extract structured research elements
* Move beyond summaries to conceptual units

### Capabilities

* Identification of:

  * Research questions
  * Claims and hypotheses
  * Methods and assumptions
  * Theoretical frameworks

* Internal conceptual summaries

* Source-linked concept identifiers

### Validation Criteria

* Concepts are traceable to source text
* No hallucinated structures
* Repeatable extraction across similar papers

---

## Phase 2 — Concept Linking

**Status:** Planned

### Objectives

* Build cross-paper understanding
* Identify relationships across domains

### Capabilities

* Link shared concepts across papers
* Detect conceptual overlap and divergence
* Track lineage of ideas

### Validation Criteria

* Links are explainable via sources
* Conflicting concepts are preserved, not merged
* Graph structure remains interpretable

---

## Phase 3 — Guided Querying

**Status:** Future

### Objectives

* Introduce controlled interaction
* Expose reasoning without free-form generation

### Capabilities

* Predefined query templates
* Source-grounded responses
* Limited scope answers

### Constraints

* No open-ended prompts
* No speculative reasoning

---

## Phase 4 — Structured Q&A

**Status:** Future

### Objectives

* Enable research-oriented questions
* Maintain strict grounding guarantees

### Capabilities

* Natural language questions
* Multi-source reasoning
* Explicit citation trails

### Constraints

* No creative extrapolation
* Confidence tied to source coverage

---

## Phase 5 — Research Assistance

**Status:** Long-Term

### Objectives

* Support advanced research workflows
  n- Assist in hypothesis exploration and literature review

### Capabilities

* Comparative analysis
* Methodological contrast
* Identification of research gaps

### Safeguards

* Explicit uncertainty signaling
* Source coverage indicators
* Capability rollback mechanisms

---

## Out-of-Scope (Until Reconsidered)

* Autonomous agents
* Action execution
* Web-wide crawling
* Multi-agent debate systems

These may be explored only if they align with core principles.

---

## Roadmap Governance

Changes to this roadmap require:

* Documentation updates
* Architectural review
* Status reevaluation

This ensures Agent Circle evolves deliberately, not reactively.

---

## Roadmap Guiding Statement

Agent Circle advances by proving understanding, not by adding features.
