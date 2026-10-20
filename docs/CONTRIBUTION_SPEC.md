# Contribution Specification v1.0

## Purpose

A Contribution describes how a specific researcher can contribute to a specific topic.

The Contribution is the central matchmaking entity of the Bologna Health Hub.

---

## Core Model

Topic
↕
Contribution
↕
Researcher

---

## Design Principles

1. Contributions describe value for a specific topic.
2. Researchers describe people.
3. Topics describe funding opportunities.
4. Capabilities describe structured expertise.
5. Scientific contribution text exists only in contributions.yml.

---

## Minimum Schema

```yaml
id:

researcher_id:

topic_id:

title:

contribution:

capability_ids:
```

---

## Recommended Schema

```yaml
id:

researcher_id:

topic_id:

title:

challenge_addressed:

contribution:

potential_roles:

key_assets:

capability_ids:

infrastructure_ids:

evidence_urls:

verification_status:
```

---

## Rules

### R1

Each contribution links exactly:

- one researcher
- one topic

### R2

Each contribution should have at least one capability.

### R3

Typical capability assignment:

1–3 capability_ids

### R4

Contribution text must not be duplicated in:

- researchers.yml
- topics.yml
- capabilities.yml

### R5

Topic pages aggregate Contributions.

### R6

Researcher pages aggregate Contributions.

### R7

Capability pages aggregate Contributions.

---

## Current Priority

Reduce contributions without capability mapping.

Current baseline:

97 Contributions

Target:

All Contributions linked to at least one Capability.