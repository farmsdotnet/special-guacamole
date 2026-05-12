# Agentified Release Management Workflow - Requirements & Context

**Date**: 2026-05-12  
**Owner**: farmsdotnet  
**Repository**: farmsdotnet/special-guacamole

---

## Overview

This document captures the complete requirements and context for building an agentified workflow that automates release management tasks using Jira and GitHub Actions.

---

## Release Management Flow

### 1. Jira Verification Phase
- Agent monitors Jira release epic for a specific version (e.g., v7.3.20)
- Checks all linked tickets are in "verified" status
- When **all tickets verified** → proceed to next step

### 2. Commit Cross-Reference Phase
- Agent retrieves commits merged into the release branch (tagged with version in GitHub)
- Cross-references commits against Jira ticket keys (from PR descriptions/commit messages)
- Validates that all verified Jira tickets have corresponding commits

### 3. Changelog Validation Phase
- For each included ticket, confirm a CHANGELOG.md entry exists
- This might be per-service/module or a central changelog
- Verify ticket ID is mentioned in the changelog

### 4. Release Candidate Build Trigger
- Once all validations pass, trigger the GitHub Actions build workflow
- Build workflow tags the release branch and creates the RC

---

## Clarifying Questions (To Be Answered)

### Jira Setup
- [ ] What field/status name is "verified"? (Is it a standard Jira status or custom?)
- [ ] How are tickets linked to the release epic? (Epic Link field?)
- [ ] Do you have a specific Jira project key? (e.g., PROJ-123)

### Release Branch Naming
- [ ] What's the release branch naming convention? (e.g., `release/v7.3.20`, `releases/7.3.20`)
- [ ] Are releases tagged in git? (e.g., `v7.3.20`, `7.3.20`)

### Changelog Details
- [ ] Single CHANGELOG.md at repo root, or per-service/module?
- [ ] What format? (Markdown, JSON, custom?)
- [ ] Should the agent verify the ticket ID is mentioned in the changelog?

### Commit Cross-Reference
- [ ] How are Jira ticket IDs embedded in commits? (e.g., `PROJ-123: description`, `[PROJ-123]`, PR title?)
- [ ] Should the agent look at commit messages, PR descriptions, or both?

### Trigger & Approval
- [ ] Should the agent automatically trigger the build, or should it require approval before triggering?
- [ ] Should there be notifications/reports generated for visibility?

### Error Handling
- [ ] If validation fails (e.g., missing changelog, ticket not verified), should it report details and halt?
- [ ] Should there be retry logic?

---

## Environment Details (To Be Provided)

### Jira Configuration
- [ ] Jira URL / Organization
- [ ] Jira Project Key(s)
- [ ] Release Epic naming convention
- [ ] Jira API token / credentials approach
- [ ] Ticket status workflow (current status name for "verified")

### GitHub Configuration
- [ ] Repository structure (single repo or multi-repo releases?)
- [ ] Release branch naming convention
- [ ] Release tag naming convention
- [ ] GitHub organization / team
- [ ] Build workflow name/file path (to trigger RC build)

### Integration Points
- [ ] Secrets management (GitHub Secrets vs. other)
- [ ] Notification channels (Slack, email, GitHub comments?)
- [ ] Reporting format (summary table, detailed log, etc.)

---

## Implementation Considerations

### Agent Autonomy
- Decision: When should the agent auto-proceed vs. require human approval?
- Recommendation: Auto-validate, require approval before triggering RC build

### Failure Scenarios
- Missing changelogs for tickets
- Commits without matching Jira tickets
- Jira tickets not in "verified" status
- Release branch doesn't exist or naming mismatch
- Build workflow failure

### Audit Trail
- Log all validations performed
- Record timestamp and user (if manual trigger)
- Create summary report in GitHub/Jira

### Extensibility
- Support for multiple services/modules
- Support for hotfix vs. standard releases
- Support for version bumping strategies (semantic versioning, calver, etc.)

---

## Next Steps

1. Provide answers to "Clarifying Questions" section above
2. Provide "Environment Details" (Jira config, GitHub config, integration points)
3. Design GitHub Actions workflow YAML structure
4. Create supporting scripts/actions (Jira API calls, commit parsing, validation logic)
5. Build the agent orchestration logic
6. Test with a pilot release version
7. Document runbook for manual intervention scenarios

---

## Document Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-05-12 | Initial context capture and requirements |
