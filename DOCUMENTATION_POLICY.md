## Compliance Statement

**The Design Patterns Examples project commits to keeping documentation consistent with the current version of the project.**

### Current Compliance Status

✅ **Documentation Policy Established**: This document defines our commitment  
✅ **Issue Tracking**: GitHub Issues used to track documentation defects (label: "documentation")  
✅ **Review Schedule**: Quarterly reviews defined (March, June, September, December)  
✅ **Responsibilities Assigned**: Project Lead responsible for documentation currency  
✅ **PR Requirements**: Documentation updates required for code changes  
✅ **Fix Process**: Clear process for detecting and fixing documentation defects  

### Known Documentation Defects

**As of January 28, 2026**: No known critical or high-priority documentation defects.

- All core documentation reviewed and current
- Pattern examples tested and working
- Links verified
- Version numbers and dates updated

**Tracking**: Any discovered documentation issues will be tracked in [GitHub Issues](../../issues?q=is%3Aissue+is%3Aopen+label%3Adocumentation) with the "documentation" label.

### How We Ensure Currency

1. **Pull Request Reviews**: Documentation checked during every PR review
2. **Automated Testing**: CI/CD verifies code examples work
3. **Quarterly Audits**: Systematic review every 3 months
4. **Community Reporting**: Users can report doc issues via GitHub Issues
5. **Same-PR Updates**: Documentation updated in same PR as code changes

**See full policy below for details.**

---

# Documentation Maintenance Policy

## Purpose

This document defines how the Design Patterns Examples project maintains documentation currency and consistency with the current version of the project.

**Commitment**: Documentation MUST be kept consistent with the current state of the project. Any known documentation defects making it inconsistent MUST be tracked and fixed.

---

## Documentation Scope

### Project Documentation

All documentation in the repository is subject to this policy:

**Core Governance & Process**:
- [README.md](README.md) - Main project overview
- [CONTRIBUTING.md](CONTRIBUTING.md) - Contribution guidelines
- [GOVERNANCE.md](GOVERNANCE.md) - Governance model
- [ROLES.md](ROLES.md) - Roles and responsibilities
- [ACCESS_CONTINUITY.md](ACCESS_CONTINUITY.md) - Continuity planning
- [ROADMAP.md](ROADMAP.md) - Project roadmap
- [DCO.md](DCO.md) - Developer Certificate of Origin
- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) - Community standards
- [SECURITY.md](SECURITY.md) - Security policy

**User & Developer Guides**:
- [QUICKSTART.md](QUICKSTART.md) - Quick start guide
- [docs/DEVELOPER_GUIDE.md](docs/DEVELOPER_GUIDE.md) - Developer guide
- [docs/CI_TESTING.md](docs/CI_TESTING.md) - CI/CD documentation

**Pattern Documentation**:
- Pattern README files (`patterns/*/README.en.md`, `patterns/*/README.pt-br.md`)
- Code comments in all implementations
- Full documentation in `doc/en/` and `doc/pt-br/`

**Process Documentation**:
- [CHANGELOG.md](CHANGELOG.md) - Change history
- GitHub issue templates
- Pull request templates
- Workflow documentation

---

## Documentation Currency Standards

### Definition of "Current"

Documentation is considered **current** when it:
- ✅ Accurately describes the current state of the project
- ✅ Reflects the latest code, processes, and policies
- ✅ Contains no known factual errors or outdated information
- ✅ Includes up-to-date version numbers where applicable
- ✅ Links work and point to existing resources
- ✅ Examples run successfully with current code

### Definition of "Inconsistent"

Documentation is **inconsistent** when it:
- ❌ Describes features, processes, or code that no longer exist
- ❌ Contains outdated version numbers or dates
- ❌ References deprecated APIs or removed functionality
- ❌ Has broken links or missing references
- ❌ Shows examples that don't work with current code
- ❌ Contradicts other documentation or actual project behavior

---

## Maintenance Process

### 1. Preventing Documentation Defects

**During Development**:
- Every code change MUST include documentation updates if it affects documented behavior
- Pull requests MUST update relevant README files, comments, and guides
- Pattern implementations MUST have current, working examples in all languages
- New features MUST be documented before or at time of merge

**Code Review Requirements**:
- Reviewers MUST verify documentation is updated
- PR template includes documentation checklist
- No merge without documentation review

**Automated Checks**:
- CI/CD tests verify code examples in documentation still work
- Link checkers verify internal and external links (where feasible)
- Spell checkers catch obvious errors

### 2. Detecting Documentation Defects

**Regular Reviews**:
- Quarterly documentation audit (see [Review Schedule](#review-schedule))
- Check for outdated version numbers, dates, or references
- Verify all links work
- Test all examples and commands
- Review against current codebase

**Issue Reporting**:
- Anyone can report documentation issues via GitHub Issues
- Use "documentation" label for documentation defects
- Treated with same priority as code bugs

**Automated Monitoring**:
- Dependabot alerts for outdated dependencies mentioned in docs
- CI failures highlight when documented commands don't work
- Link rot detection (planned for Q3 2026)

### 3. Tracking Documentation Defects

**GitHub Issues**:
- All documentation defects tracked as GitHub issues
- Label: `documentation`
- Priority labels: `critical`, `high`, `medium`, `low`
- Assigned to maintainers for resolution

**Documentation Debt**:
- Known but unfixed documentation issues listed in issues
- Tracked in project board (if/when created)
- Addressed during quarterly reviews

**Prioritization**:
- **Critical**: Documentation that could cause user harm or major confusion (fix within 1 week)
- **High**: Incorrect information about core features (fix within 1 month)
- **Medium**: Outdated but not misleading information (fix within quarter)
- **Low**: Minor inconsistencies, typos (fix opportunistically)

### 4. Fixing Documentation Defects

**Fix Process**:
1. Documentation issue created with clear description of defect
2. Issue triaged and prioritized
3. Assigned to maintainer or volunteer contributor
4. Fixed via pull request
5. Review and merge
6. Issue closed with reference to fixing PR

**Urgent Fixes**:
- Critical documentation defects can be fast-tracked
- Direct commits to main branch allowed for critical docs fixes
- Post-merge review for urgent documentation PRs

**Batch Updates**:
- Minor issues can be batched in quarterly reviews
- Single PR for multiple small documentation fixes
- Documented in PR description

---

## Review Schedule

### Quarterly Reviews (Every 3 Months)

**Schedule**:
- **Q1**: End of March
- **Q2**: End of June
- **Q3**: End of September
- **Q4**: End of December

**Review Scope**:
1. All README files (main and patterns)
2. Governance documents (GOVERNANCE.md, ROLES.md, etc.)
3. Quick Start and user guides
4. CI/CD and developer documentation
5. Links and references
6. Version numbers and dates
7. Code examples

**Review Process**:
1. Create review checklist issue
2. Go through all documentation systematically
3. Test all commands and examples
4. Check all links
5. Update version numbers and dates
6. Create issues for any defects found
7. Fix issues or schedule for fixing
8. Update "Last Updated" dates in reviewed documents

### Annual Deep Review (January)

**Additional Scope**:
- Full pattern documentation review (all 23 patterns × 2 languages)
- Cross-reference documentation consistency
- Major restructuring if needed
- Update all "Last Updated" and "Next Review" dates

---

## Achievement Recognition

### 48-Hour Display Requirement

**Commitment**: The project repository front page (README.md) MUST identify and hyperlink to any achievements within **48 hours** of public recognition that the achievement has been attained.

### What Qualifies as an Achievement

**Achievements include**:
- ✅ Best practices badges (OpenSSF, CII, etc.)
- ✅ Security certifications or audits
- ✅ Industry awards or recognition
- ✅ Milestone achievements (stars, contributors, downloads)
- ✅ Featured on notable platforms or publications
- ✅ Conference talks or presentations about the project
- ✅ Academic citations in published research
- ✅ Integration with major platforms or ecosystems

### Recognition Process

**When Achievement is Attained**:
1. **Notification** - Project Lead or community member becomes aware of achievement
2. **Verification** - Confirm achievement is publicly verifiable
3. **Documentation** - Update README.md achievements section within 48 hours
4. **Format**:
   - Add to "🏆 Achievements & Recognition" section in README.md
   - Include hyperlink to achievement verification
   - Add date or year of recognition
   - Provide brief description of what it represents

**Timeline**:
- ⏱️ 0-24 hours: Verify achievement is real and public
- ⏱️ 24-48 hours: Update README.md with achievement
- ⏱️ Within 1 week: Update any additional relevant documentation

### Achievement Display Format

**In README.md**:
```markdown
## 🏆 Achievements & Recognition

- **[Achievement Name](link)** - Description (Year/Date)
  - Optional explanation or significance
```

**Current Location**: 
- English: Lines ~15-30 of README.md
- Portuguese: Lines ~110-125 of README.md

### Examples

**OpenSSF Best Practices Badge**:
```markdown
- **[OpenSSF Best Practices Badge](https://www.bestpractices.dev/projects/11714)** - Passing Level (2024)
  - Demonstrates commitment to security, quality, and best practices
  - Working towards Gold level certification
```

**Star Milestones**:
```markdown
- **1000 GitHub Stars** - Achieved December 2026
  - Thank you to our amazing community!
```

### Responsibilities

**Project Lead**:
- Monitor for new achievements
- Update README.md within 48 hours
- Ensure hyperlinks are correct and working

**Community Members**:
- Can notify Project Lead of achievements via GitHub Issue
- Use "achievement" or "recognition" label

**Verification**:
- All achievements must be publicly verifiable via provided link
- No self-proclaimed achievements without external validation
- Badges must be officially granted by recognized organizations

### Tracking

**Achievement History**:
- Current achievements listed in README.md
- Historical achievements can be maintained in CHANGELOG.md
- Major milestones noted in roadmap updates

---

## Version Control for Documentation

### Version Numbers

Key documents include version numbers:
- GOVERNANCE.md
- ROLES.md
- ACCESS_CONTINUITY.md
- ROADMAP.md
- This policy document

**Versioning Scheme**:
- Major version (X.0): Significant restructuring or scope changes
- Minor version (1.X): Substantive updates, new sections
- Updates without version increment: Typo fixes, minor clarifications

### Last Updated Dates

Documents include "Last Updated" field:
- Updated whenever document changes
- Format: "January 28, 2026"
- Helps users assess currency

### Changelog Sections

Long-lived documents include changelog:
- Lists version, date, and changes
- Bottom of document or dedicated section
- Brief description of what changed

---

## Responsibilities

### Project Lead

**Documentation Responsibilities**:
- ✅ Ensure documentation is reviewed quarterly
- ✅ Triage documentation issues
- ✅ Approve major documentation changes
- ✅ Maintain this documentation policy
- ✅ Update governance documents as needed

### Collaborators (when appointed)

**Documentation Responsibilities**:
- ✅ Review PRs for documentation accuracy
- ✅ Help with quarterly documentation reviews
- ✅ Fix documentation defects
- ✅ Keep developer guides current

### Contributors

**Documentation Responsibilities**:
- ✅ Update documentation when code changes affect it
- ✅ Report documentation issues when found
- ✅ Include documentation in PRs
- ✅ Test examples before including them in docs
- ✅ Write clear commit messages for docs changes

### Community Members

**Documentation Responsibilities**:
- ✅ Report documentation issues via GitHub Issues
- ✅ Suggest improvements
- ✅ Verify examples work as documented

---

## Documentation Standards

### Writing Standards

**Clarity**:
- Use clear, simple language
- Define technical terms
- Provide examples
- Use active voice

**Accuracy**:
- Test all commands before documenting
- Verify all links work
- Include version requirements where relevant
- Show expected output for commands

**Bilingual (English/Portuguese)**:
- Core pattern docs in both languages
- Governance docs primarily in English (translate if community needs)
- Keep translations synchronized when possible

**Formatting**:
- Use Markdown consistently
- Include table of contents for long documents
- Use headers, lists, and code blocks appropriately
- Include emojis for visual scanning (in user-facing docs)

### Code Example Standards

**In Documentation**:
- Must be tested and work with current code
- Include language version requirements
- Show expected output
- Include full context (imports, setup, etc.)

**In Pattern READMEs**:
- Link to actual working code
- Don't duplicate full code in README (link to source files)
- Explain what the code demonstrates
- Include usage instructions

---

## Tools and Automation

### Current Tools

**Manual**:
- Quarterly review checklist
- GitHub Issues for tracking
- Pull request reviews

**Automated** (current):
- CI/CD tests pattern examples
- Markdown linters (where configured)

### Planned Tools (Roadmap Q3 2026)

- Link checker automation
- Documentation freshness alerts
- Spell checking automation
- Automated cross-reference validation

---

## Handling Documentation Exceptions

### Deprecated Features

When features are deprecated:
1. Mark as deprecated in documentation
2. Include migration guide
3. State when feature will be removed
4. Keep documentation until feature removed
5. Remove or archive documentation when feature removed

### Experimental Features

Experimental features should:
- Be clearly marked as experimental
- Include stability warnings
- State that API may change
- Not be included in Quick Start guide

### Known Issues

If documentation can't be immediately fixed:
- Create GitHub issue describing the problem
- Link to issue from the documentation if helpful
- Set expected resolution timeline
- Update when fixed

---

## Metrics and Compliance

### Documentation Health Metrics

**Tracked Quarterly**:
- Number of open documentation issues
- Age of oldest documentation issue
- Percentage of documents reviewed this quarter
- Number of broken links found and fixed
- Test success rate for documented examples

**Targets**:
- 🎯 100% of critical documentation issues fixed within 1 week
- 🎯 100% of documents reviewed annually
- 🎯 <5 open documentation issues at any time
- 🎯 Zero critical documentation defects

### Compliance Verification

**How We Verify**:
- ✅ Quarterly review completed on schedule
- ✅ All examples tested and working
- ✅ No known critical documentation defects
- ✅ Documentation issues tracked in GitHub
- ✅ Version numbers and dates current

**Audit Trail**:
- Review issues in GitHub
- Closed documentation issues show fixes
- Commit history shows documentation updates
- PR reviews show documentation verification

---

## Policy Updates

This policy itself is documentation and subject to review.

**Review Schedule**: Annually (January)

**Update Process**:
1. Propose changes via GitHub issue
2. Discussion period (7 days minimum)
3. Update policy document
4. Increment version number
5. Update changelog

---

## Document History

**Version**: 1.1  
**Created**: January 28, 2026  
**Last Updated**: January 28, 2026  
**Next Review**: January 2027  
**Owner**: @luizwbr

**Changelog**:
- v1.1 (2026-01-28): Added achievement recognition policy (48-hour display requirement)
- v1.0 (2026-01-28): Initial documentation maintenance policy

---

## Related Documents

- [Contributing Guidelines](CONTRIBUTING.md) - Includes documentation requirements
- [Project Roadmap](ROADMAP.md) - Plans for documentation improvements
- [Governance](GOVERNANCE.md) - Overall project governance
- [Roles](ROLES.md) - Documentation responsibilities by role

---

## Questions?

If you have questions about documentation maintenance:
- Open an issue with "documentation" label
- Tag maintainers for clarification
- Suggest improvements to this policy
