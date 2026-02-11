# Health Skill Quality Specification

## Overview

Establish quality standards and templates specifically for health plugin skills. These standards ensure consistency across all 30 planned health skills, with healthcare-specific considerations for compliance, privacy, and clinical accuracy.

## Health-Specific Quality Requirements

### 1. Regulatory & Compliance Context
Every health skill must include:
- **Applicable regulations** (HIPAA, HITECH, state privacy laws, etc.)
- **Compliance checkpoints** specific to the workflow
- **Documentation requirements** for audit trails

### 2. Clinical Accuracy Standards
- **Disclaimer placement** - "This skill assists with clinical workflows but does not provide clinical advice"
- **Validation requirements** - When outputs require clinical review
- **Escalation criteria** - When to involve subject matter experts

### 3. Privacy & Security
- **PHI handling** - Identifiable data considerations
- **Data minimization** - Using minimum necessary information
- **Retention guidance** - How long to retain generated documents
- **De-identification** - When and how to de-identify data

### 4. Healthcare Workflow Integration
- **EHR/EMR considerations** - How skill integrates with clinical systems
- **Documentation standards** - Formatting for medical records
- **Communication protocols** - Appropriate channels for different content types

## Standard Health Skill Structure

```markdown
---
name: health-skill-name
description: One-line description. Use when [trigger condition 1], [trigger condition 2].
---

# Skill Name

Brief introduction (1-2 sentences).

**Important**: [Appropriate disclaimer for healthcare context]

## When to Use This Skill

Invoke when:
- User mentions [specific healthcare scenario]
- User asks about [specific workflow]
- Context indicates [specific need]

## Regulatory Context

| Regulation | Relevance | Key Requirements |
|------------|-----------|------------------|
| HIPAA | [How it applies] | [Specific requirements] |
| [Other] | [How it applies] | [Specific requirements] |

## Quick Reference

[Condensed guidance for simple/common cases - 5-10 bullet points]

## Detailed Guidance

[Main content organized with clear headers]

### Step-by-Step Process

1. ...
2. ...

## Documentation Requirements

- [ ] Required documentation element 1
- [ ] Required documentation element 2
- [ ] Audit trail requirements

## Common Mistakes

| Mistake | Why It's Wrong | Instead |
|---------|----------------|---------|
| ... | ... | ... |

## When to Escalate

Escalate to [appropriate party] when:
- [Escalation criterion 1]
- [Escalation criterion 2]

## Privacy Considerations

- **PHI involved**: [Yes/No/Conditional]
- **Data minimization**: [Guidance]
- **Retention**: [How long to keep outputs]

## Tool Requirements

- \`~~cloud storage\` - For document storage
- \`~~project tracker\` - For workflow tracking
- \`~~clinical systems\` - For EHR integration (if applicable)

## Success Indicators

You've applied this skill well when:
- [ ] All required documentation is complete
- [ ] Compliance checkpoints verified
- [ ] Output meets documentation standards

## Related Skills

- \`~~health/related-skill\` - Brief description of relationship
- \`~~health/related-skill\` - Brief description of relationship
```

## Section Guidelines for Health Skills

| Section | Required | Min Lines | Healthcare-Specific Purpose |
|---------|----------|-----------|----------------------------|
| Frontmatter | Yes | 3 | Name, description with clinical triggers |
| When to Use | Yes | 5 | Explicit clinical/operational scenarios |
| Regulatory Context | Yes | 10 | HIPAA, state laws, accreditation standards |
| Quick Reference | Complex skills | 10 | Fast path for routine cases |
| Detailed Guidance | Yes | 50+ | Step-by-step clinical/operational procedures |
| Documentation Requirements | Yes | 10 | Required elements for medical records |
| Common Mistakes | Yes | 10 | Healthcare-specific anti-patterns |
| When to Escalate | Yes | 5 | Criteria for involving SMEs/leadership |
| Privacy Considerations | Yes | 10 | PHI handling, de-identification, retention |
| Tool Requirements | Yes | 5 | MCP connector dependencies |
| Success Indicators | Yes | 5 | Compliance and quality gates |
| Related Skills | Yes | 3 | Cross-references within health plugin |

## Quality Gates for Health Skills

Before any health skill is considered complete:

- [ ] Minimum 200 lines total (health skills require more detail)
- [ ] All required sections present
- [ ] Regulatory context includes at least HIPAA relevance
- [ ] At least 3 "Common Mistakes" documented
- [ ] At least 2 "Related Skills" referenced (within health plugin preferred)
- [ ] At least 3 "Success Indicators" defined
- [ ] Privacy considerations section complete
- [ ] When to Escalate section with clear criteria
- [ ] Appropriate healthcare disclaimers included
- [ ] No placeholder content (e.g., "TODO", "TBD")
- [ ] Documentation requirements align with medical record standards

## Health Domain-Specific Improvements

### Complaints Management Skills
- Patient satisfaction framework references
- Service recovery guidelines
- Regulatory reporting thresholds (state-specific)

### Incident Reporting Skills
- Sentinel event criteria
- Root cause analysis methodology
- CAP (Corrective Action Plan) templates
- Joint Commission requirements

### Risk Management Skills
- Risk matrix with healthcare-specific likelihood/severity
- Enterprise risk management framework
- Insurance/notification requirements

### Information Governance Skills
- ROI (Release of Information) processing standards
- Consent requirements by jurisdiction
- Records retention schedules by document type

### Clinical Coding Skills
- ICD-10/CPT validation rules
- Query physician guidelines
- Audit preparation checklists

### Governance Skills
- Policy lifecycle management
- Approval workflow requirements
- Accreditation standard mapping

### Credentialing Skills
- Primary source verification requirements
- FPPE/OPPE framework
- Expiration tracking requirements

### Procurement Skills
- Value analysis committee process
- FDA clearance/approval verification
- Business case templates for capital equipment

### Quality Improvement Skills
- PDSA cycle methodology
- Statistical process control basics
- Accreditation readiness checklists

### Financial Skills
- Payer contract red flags
- Charge capture audit points
- Denial management workflows

### Evidence Review Skills
- PRISMA guidelines
- GRADE methodology
- Literature search strategies

### Data Analysis Skills
- Statistical methods for healthcare data
- Risk adjustment concepts
- Dashboard design principles

### Ethics Skills
- IRB submission requirements
- Ethics committee consultation process
- Conflict of interest disclosure

### Health Economics Skills
- HTA submission requirements
- Cost-effectiveness analysis methods
- Budget impact model structure

### Manuscript Skills
- Journal selection criteria
- Authorship guidelines (ICMJE)
- Peer review response templates

### Grants Skills
- Funder alignment assessment
- Budget justification templates
- Compliance requirements (federal vs. foundation)

### Medicolegal Skills
- Child protection reporting requirements (jurisdiction-specific)
- Affidavit formatting standards
- Court testimony preparation

## Deliverables

### Phase 1: Standards & Templates
- Health skill template with all required sections
- Healthcare style guide (voice, tone, terminology)
- Quality checklist specific to health skills
- Validation script for health skill standards

### Phase 2: Skill Development Support
- Apply standards as skills are created in health tracks
- Provide templates to track implementers
- Quality review of completed skills

## Success Metrics

| Metric | Target |
|--------|--------|
| Skills with "Regulatory Context" section | 100% |
| Skills with "When to Escalate" section | 100% |
| Skills with "Privacy Considerations" section | 100% |
| Average skill length | 200-400 lines |
| Cross-skill references within health | 2+ per skill |
| Skills with healthcare disclai
