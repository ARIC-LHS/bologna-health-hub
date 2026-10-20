# Bologna Health Hub - Pilot Audit
Version: 0.1
Status: Preliminary Audit
Date: 2026-10-20

## Baseline

### Repository
- Branch: main
- Working tree clean
- Origin synchronized

### Current Content
- Researchers: 61
- Topics: 13

## Repository Structure

### Data
- researchers.yml
- topics.yml
- capabilities.yml
- contributions.yml
- infrastructures.yml
- institutions.yml
- networks.yml
- projects.yml

### Layouts
- default.html
- researcher.html
- topic.html

### Scripts
- generate_pages.py
- generate_researchers.py
- generate_contributions.py
- validate_data.py

## Data Model Assessment

### Strengths

- Single source of truth based on YAML datasets.
- Static generation architecture.
- Clear separation between data and presentation.
- Scientific contribution text stored only once.
- No duplication of contribution narrative across entities.

### Architectural Principles Identified

1. YAML datasets are the authoritative source.
2. Pages are generated from structured data.
3. Contributions act as the relationship layer between researchers and topics.
4. Scientific text should not be duplicated.

## Strengths

- Simple architecture.
- Data-driven approach based on YAML datasets.
- Clear separation between data and presentation.
- Automatic generation of researcher and topic pages.
- Static deployment model with low maintenance burden.
- Contribution entity acts as a single source of truth for topic-specific scientific content.

## Weaknesses

- Limited technical documentation.
- README provides only a minimal project description.
- No documented deployment workflow.
- No documented data update workflow.
- No documented governance model.
- No documented onboarding instructions for contributors.
- No documented roadmap.

## KEEP

- Jekyll static architecture.
- YAML source-of-truth approach.
- Researcher entity.
- Topic entity.
- Contribution entity.
- Auto-generated page wrappers.

## REFACTOR

- Researcher profile richness.
- Navigation and discovery layer.
- Capability taxonomy.
- Cross-linking among entities.
- Documentation quality.

## REPLACE

None identified.

## REMOVE

None identified.

## Recommendations
1. Preserve the current YAML-based source-of-truth architecture.

2. Preserve the Contribution entity as the only location for topic-specific scientific contribution text, avoiding duplication across researchers, topics and other entities.

3. Refactor researcher profiles after completion of the researcher data audit, using the validated outputs produced in `Researcher_Audit_Bologna_Health_Hub.xlsx`.

4. Improve navigation and cross-linking among Researchers, Topics, Contributions, Capabilities and Infrastructures.

5. Review and consolidate the Capability taxonomy before expanding the pilot dataset.

6. Document the data update, validation, page generation and deployment workflows.

7. Expand the README with:
   - project purpose and scope;
   - repository structure;
   - local setup instructions;
   - data update workflow;
   - validation and generation commands;
   - deployment workflow.

8. Treat the current repository as the architectural baseline for the next version of the portal, rather than rebuilding the system from scratch.

9. Defer replacement or removal decisions until the researcher audit and the review of entity relationships have been completed.

10. Use the pilot audit and the validated researcher dataset as inputs for updating the implementation masterplan.

## Strategic Assessment

### What already works

The pilot already demonstrates that a data-driven research matchmaking portal can be maintained through structured YAML datasets and static page generation.

The core architectural pattern appears sound:

Dataset
→ Contribution Layer
→ Generated Pages
→ Public Portal

The architecture is simple, understandable and maintainable.

### Main Risk

The principal risk is not technical.

The principal risk is content quality, completeness and maintenance of researcher profiles, contributions, capabilities and relationships.

### Main Opportunity

The current architecture is sufficiently mature to support iterative growth.

Future effort should focus primarily on:

- researcher data quality;
- profile enrichment;
- capability mapping;
- infrastructure mapping;
- discovery and navigation features.

Rather than architectural redesign.

## Audit Conclusion

The pilot should be considered a successful architectural proof of concept.

No evidence was identified requiring a complete redesign of the platform.

The recommended strategy is evolutionary:

- preserve the current architecture;
- improve data quality;
- enrich entities and relationships;
- strengthen navigation and discovery;
- progressively expand coverage of the Bologna health research ecosystem.

The next major input should be the validated researcher audit produced from the researcher booklet review process.