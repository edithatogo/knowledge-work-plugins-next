# Health Document Co-authoring Track Plan

## Phase 1: Clinical Document Co-authoring Skill
*Dependencies: health-core, health-governance*
*Estimated: 1-2 sessions*

- [ ] Create `health/skills/clinical-doc-coauthoring/SKILL.md`
  - Acceptance: Follows [health skill standards](../health-plugin/skill-standards.md) (14-section template)
  - Acceptance: AU/NZ documentation and evidence defaults are explicit, with US/EU-lite fallback
  - Acceptance: Standard mode and Lite mode are explicitly documented
  - Acceptance: Three-stage workflow documented
  - Acceptance: Document type templates
  - Acceptance: Evidence grading guidance (NHMRC levels)
  - Acceptance: Citation requirements for clinical claims
  - Acceptance: Stakeholder review workflow
  - Acceptance: Reader testing methodology

## Phase 2: Coauthor Command
*Dependencies: Phase 1*
*Estimated: 0.5 sessions*

- [ ] Create `health/commands/coauthor.md`
  - Acceptance: Document type selection
  - Acceptance: Stage selection/progression
  - Acceptance: Generates document checklist

**Checkpoint:** `conductor(checkpoint): Health document co-authoring workflow complete`

## Cross-References

- Outputs feed into `health-governance` (policies, guidelines)
- Supports `health-economics` (HTA submissions)
- Supports `health-ethics` (ethics applications)
