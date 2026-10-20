# Data model

## Core entities

Institution

Capability

Infrastructure

Network

Researcher

Topic

Contribution

---

## Core Principle

The Bologna Health Hub is contribution-centric.

The central matchmaking relationship is:

Topic ↔ Contribution ↔ Researcher

A Topic describes a funding need.

A Contribution describes how a researcher can contribute to that need.

A Researcher describes the person providing the contribution.

---

## Core Relationships

Topic → Contribution

Contribution → Researcher

Contribution → Capability

Contribution → Infrastructure

Researcher → Institution

Infrastructure → Institution

---

## Contribution

Contribution is the central entity of the system.

Contribution stores:

- topic-specific expertise
- scientific contribution
- assets
- potential role
- capability mapping

Contribution is the only location where topic-specific contribution text is stored.

Scientific contribution text MUST NOT be duplicated across entities.

---

## Capability

Capabilities represent the controlled vocabulary used for knowledge discovery.

Current taxonomy:

- ai-data
- digital-biomarkers
- interoperability
- clinical-cohorts
- clinical-trials
- omics
- biobanking
- implementation-science
- ssh
- ethics-regulation

Each Contribution should be linked to at least one Capability.

---

## Source of truth

All content is stored in YAML files under:

_data/

Topics and researcher pages are generated from YAML data.

Scientific contribution text MUST NOT be duplicated across entities.

---

## Current Status

Capability mapping coverage:

- Contributions: 97
- Contributions without capability mapping: 0

The capability taxonomy has been validated against the current pilot dataset.