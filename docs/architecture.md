# Agent Circle — Architecture

## Architectural Goal

Agent Circle is designed as a **research-first intelligence system**, not an interaction-first application. The architecture prioritizes:

* Grounded reasoning
* Interpretability
* Incremental capability growth
* Decoupling between knowledge, reasoning, and interfaces

The system is intentionally modular so that each layer can evolve independently without compromising epistemic integrity.

---

## High-Level System Overview

Agent Circle is composed of five primary layers:

1. Research Corpus
2. Ingestion & Processing
3. Knowledge Storage
4. Agent Core
5. Interfaces & Integrations

```
Research Corpus
      ↓
Ingestion & Processing (RAG)
      ↓
Knowledge Storage
      ↓
Agent Core (Reasoning)
      ↓
Interfaces (Read-only → Interactive)
```

Each layer has a **single responsibility** and explicit boundaries.

---

## 1. Research Corpus Layer

### Purpose

The Research Corpus represents the *source of truth* for the system.

### Contents

* Academic papers (PDFs, text)
* Metadata (authors, venue, year, domain)
* Paper identifiers and provenance

### Constraints

* Only explicitly ingested documents exist for the agent
* No external web search or speculative sources

> If it is not in the corpus, it does not exist to the agent.

---

## 2. Ingestion & Processing Layer (RAG)

### Purpose

Transforms raw research papers into structured, retrievable knowledge.

### Responsibilities

* PDF parsing and text extraction
* Semantic chunking
* Metadata attachment
* Embedding generation
* Index construction

### Non-Responsibilities

* No reasoning
* No interpretation
* No synthesis

This layer answers only one question:

> *Where is relevant information located?*

---

## 3. Knowledge Storage Layer

### Purpose

Stores processed research data in forms optimized for retrieval and structure.

### Components

* Vector stores (semantic similarity)
* Structured metadata storage
* Concept references and identifiers

### Design Principle

Knowledge storage is **passive**. It does not think or infer — it only stores and retrieves.

---

## 4. Agent Core Layer

### Purpose

The Agent Core is the **reasoning center** of Agent Circle.

### Responsibilities

* Concept extraction from retrieved content
* Linking ideas across papers
* Identifying assumptions, methods, and frameworks
* Resolving conceptual overlap and contradiction
* Maintaining long-term research memory

### Internal Components

* Agent controller
* Reasoning engine
* Concept graph builder
* Memory manager

### Constraints

* The agent may only reason over retrieved, grounded content
* No free-form generation disconnected from sources

This enforces epistemic discipline.

---

## 5. Interfaces & Integrations Layer

### Purpose

Expose Agent Circle capabilities without compromising grounding or control.

### Current State

* Read-only interfaces
* Status and capability visibility
* No live query execution

### Future State

* Research-question interfaces
* PaperSupe integration via API
* Controlled interaction loops

All interfaces communicate **only** through the Agent Core API.

---

## Data Flow (Reading Mode)

1. Paper added to corpus
2. Ingestion pipeline processes content
3. Knowledge is indexed and stored
4. Agent analyzes and extracts concepts
5. Concept relationships are recorded
6. System state updates

No user interaction occurs in this mode.

---

## Capability Gating Mechanism

Capabilities are unlocked through explicit architectural switches, not UI changes.

Examples:

* Query answering disabled at API level
* Action execution not implemented
* Reasoning limited to analysis, not response

This prevents premature exposure of immature intelligence.

---

## Integration with PaperSupe

Agent Circle exposes a clean API boundary that allows PaperSupe to:

* Request concept summaries
* Retrieve linked research ideas
* Display agent status and progress

PaperSupe does **not** control the agent’s reasoning logic.

---

## Architectural Non-Goals

* Real-time conversational performance
* Multi-agent coordination (for now)
* Autonomous action execution
* Web-wide search or crawling

These may be explored only if they align with the core vision.

---

## Architectural Guiding Statement

Agent Circle is built to **understand before it speaks**, **structure before it responds**, and **grow only when grounded**.
