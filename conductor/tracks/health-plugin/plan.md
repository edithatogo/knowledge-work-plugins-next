# Health Plugin Program Plan

## Role

This is a meta-track coordinating 20 implementation tracks. No direct implementation work - that's delegated to individual tracks.

## Coordination Tasks

### Setup
- [x] Define program scope and track structure
- [x] Create track registry with dependencies
- [ ] Receive and analyze user templates (pending link)

### During Implementation
- [ ] Enforce [health skill standards](./skill-standards.md) and 14-section quality mandate
- [ ] Enforce AU/NZ-default jurisdiction guidance and US/EU-lite portability pattern
- [ ] Verify every skill includes Standard and Lite operating modes
- [ ] Monitor track progress
- [ ] Resolve cross-track dependencies
- [ ] Ensure consistent patterns across skills
- [ ] Coordinate documentation updates

### Integration
- [ ] Verify all tracks installed correctly
- [ ] Test cross-skill references
- [ ] Final README consolidation
- [ ] Marketplace preparation

## Dependencies

All implementation tracks depend on `health-core` completion.

## Checkpoints

- `conductor(checkpoint): Health program Phase 1 complete` - After health-core
- `conductor(checkpoint): Health program Phase 2 complete` - After core workflows
- `conductor(checkpoint): Health program Phase 3 complete` - After extended workflows
- `conductor(checkpoint): Health plugin ready for release` - Final integration
