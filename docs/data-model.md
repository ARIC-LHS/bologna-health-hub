# Data model

## Core entities

Institution
Capability
Infrastructure
Network
Researcher
Topic
Contribution

## Central relationship

Topic ↔ Contribution ↔ Researcher

A researcher may contribute to multiple topics.

A topic may contain multiple researchers.

Contribution is the only location where topic-specific contribution text is stored.

## Source of truth

All content is stored in YAML files under:

_data/

Topics and researcher pages are generated from YAML data.

Scientific contribution text MUST NOT be duplicated across entities.
