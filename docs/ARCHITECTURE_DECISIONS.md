# Architecture Decisions

## AD-001 Contribution-centric architecture

Decision:
The Bologna Health Hub is contribution-centric.

Model:

Topic
↕
Contribution
↕
Researcher

Rationale:

The matchmaking value of the platform comes from structured contributions associated with specific Horizon topics.

Status: Approved

---

## AD-002 Researchers remain lightweight

Decision:

Researcher records describe people.

Contribution records describe what they can bring to a specific topic.

Status: Approved

---

## AD-003 Contribution is the only source of scientific contribution text

Decision:

Scientific contribution narratives are stored exclusively in contributions.yml.

No duplication in:

- researchers.yml
- topics.yml
- capabilities.yml

Status: Approved

---

## AD-004 Current capability taxonomy retained

Decision:

Current capability taxonomy is sufficient for pilot expansion.

Capabilities:

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

Status: Approved

---

## AD-005 No taxonomy expansion before capability mapping completion

Decision:

No new capability categories should be added until the majority of contributions have been classified.

Status: Approved