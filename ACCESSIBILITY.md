# Accessibility Statement

## Our Commitment

The Design Patterns Examples project strives to follow accessibility best practices so that persons with disabilities can participate in the project and use the project results where it is reasonable to do so.

**Status**: 🟡 In Progress - Actively working to improve accessibility

---

## Scope

This accessibility commitment applies to:

### Project Sites
- GitHub repository (documentation, issues, discussions)
- README and all Markdown documentation
- GitHub Pages website (if/when implemented)

### Project Results
- React.js component examples
- Angular component examples
- AngularJS examples
- Documentation and code comments
- Quick start guides and tutorials

---

## Current Accessibility Features

### Documentation Accessibility ✅

**Implemented**:
- ✅ Semantic Markdown structure (proper heading hierarchy)
- ✅ Descriptive link text throughout documentation
- ✅ Clear, simple language for better comprehension
- ✅ Bilingual support (English and Portuguese) for broader access
- ✅ Code blocks with language specification for syntax highlighting
- ✅ Keyboard-navigable documentation structure
- ✅ Logical reading order in all documentation

**Examples**:
- Using `[Contributing Guidelines](CONTRIBUTING.md)` instead of "click here"
- Proper H1 → H2 → H3 heading hierarchy in all README files
- Lists and tables for structured information

### Code Examples

**Current Status**:
- ✅ Go, TypeScript, Java, PHP examples are primarily backend/console - minimal accessibility concerns
- 🟡 React/Angular examples being reviewed for accessibility improvements
- ✅ Code comments explain pattern purpose, improving comprehension for all users

---

## Accessibility Best Practices We Follow

### 1. Documentation (Markdown)

**Heading Hierarchy**:
```markdown
# Main Title (H1)
## Section (H2)
### Subsection (H3)
```

**Descriptive Links**:
```markdown
✅ See [Contributing Guidelines](CONTRIBUTING.md)
❌ Click [here](CONTRIBUTING.md) to contribute
```

**Alt Text for Images** (when images are used):
```markdown
![OpenSSF Best Practices Badge showing Passing level](badge-url)
```

**Semantic Structure**:
- Use lists for related items
- Use tables for tabular data
- Use code blocks for code examples
- Use blockquotes for important notes

### 2. Web Components (React/Angular)

**Semantic HTML**:
```tsx
// ✅ Good
<button onClick={handleClick}>Submit</button>
<nav aria-label="Main navigation">...</nav>

// ❌ Avoid
<div onClick={handleClick}>Submit</div>
```

**ARIA Labels**:
```tsx
<button 
  aria-label="Close dialog"
  onClick={handleClose}
>
  ×
</button>
```

**Keyboard Navigation**:
- Ensure all interactive elements are keyboard accessible
- Maintain logical tab order
- Provide visible focus indicators

**Color Contrast**:
- Text: minimum 4.5:1 contrast ratio (WCAG AA)
- Large text (18pt+): minimum 3:1 contrast ratio
- Don't rely solely on color to convey information

### 3. Code Comments

**Clear Explanations**:
```typescript
// Singleton pattern ensures only one instance exists
// This is useful for database connections or configuration managers
class Database {
  private static instance: Database;
  // ...
}
```

---

## Known Limitations

### Current Limitations

1. **Web Component Examples**: Not all React/Angular examples may follow accessibility best practices
   - **Why**: Focus has been on demonstrating design patterns clearly
   - **Plan**: Gradual improvement as components are reviewed (Q2-Q3 2026)

2. **Visual Examples**: Some pattern visualizations may rely on visual cues
   - **Mitigation**: Textual explanations always provided alongside visual examples

3. **Language Support**: Currently only English and Portuguese
   - **Plan**: Open to community translations to additional languages

### Reasonable Limitations

Some accessibility features are not applicable:
- **Backend Examples**: Go, Java, PHP examples are console-based (no UI accessibility concerns)
- **Educational Clarity**: In some cases, accessibility might conflict with pattern demonstration clarity
  - When this occurs, we document the limitation in comments

---

## How We're Improving

### Roadmap (2026-2027)

**Q1 2026** (Current):
- [x] Establish accessibility guidelines in CONTRIBUTING.md
- [x] Create this accessibility statement
- [ ] Audit React component examples for accessibility
- [ ] Add accessibility checklist to PR template

**Q2 2026**:
- [ ] Review and update React/Angular components for accessibility
- [ ] Add accessibility examples to pattern implementations
- [ ] Include accessibility notes in component README files

**Q3 2026**:
- [ ] Complete accessibility audit of all web components
- [ ] Add automated accessibility testing (if feasible)
- [ ] Update documentation with accessibility best practices

**Q4 2026**:
- [ ] Ensure all new components follow accessibility guidelines
- [ ] Community feedback on accessibility improvements
- [ ] Document accessibility testing approach

---

## Guidelines for Contributors

When contributing, please consider accessibility:

### For Code Contributions

**React/Angular Components**:
- Use semantic HTML elements
- Add ARIA labels where helpful
- Ensure keyboard navigation
- Test with keyboard only (no mouse)
- Check color contrast

**Documentation**:
- Use descriptive link text
- Maintain heading hierarchy
- Use semantic Markdown
- Write clear, simple explanations

See full guidelines in [CONTRIBUTING.md](CONTRIBUTING.md#accessibility-best-practices)

### For Reviewers

**Check for**:
- Proper semantic HTML in components
- Descriptive link text in documentation
- Logical heading hierarchy
- ARIA labels on custom components
- Keyboard accessibility

---

## Reporting Accessibility Issues

We welcome feedback on accessibility:

### How to Report

1. **Create a GitHub Issue**
2. **Label**: Use "accessibility" label
3. **Describe**:
   - What accessibility issue you found
   - Where (file, component, documentation)
   - Impact (who is affected, how)
   - Suggested improvement (if you have one)

### What We'll Do

- Acknowledge issue within 1 week
- Assess impact and priority
- Fix critical accessibility issues within 1 month
- Address medium/low priority issues in quarterly updates

---

## Standards and References

We aim to align with recognized accessibility standards where applicable:

### Web Content Accessibility Guidelines (WCAG)

For web components (React, Angular):
- **Target**: WCAG 2.1 Level AA where reasonable
- **Focus Areas**:
  - Perceivable: Text alternatives, color contrast
  - Operable: Keyboard accessible, navigable
  - Understandable: Readable, predictable
  - Robust: Compatible with assistive technologies

### Documentation Accessibility

For Markdown documentation:
- Semantic structure
- Clear language
- Descriptive links
- Proper heading hierarchy
- Alternative text for images

---

## Testing

### How We Test

**Manual Testing**:
- Keyboard-only navigation
- Screen reader testing (when feasible)
- Color contrast checking
- Heading structure review

**Automated Testing** (Planned Q3 2026):
- Accessibility linters for React/Angular
- Link checking
- Contrast ratio verification

**Community Testing**:
- Welcome reports from users with disabilities
- Open to accessibility feedback
- Community contributions for improvements

---

## Contact

For accessibility questions or concerns:
- **GitHub Issues**: Use "accessibility" label
- **Email**: (if needed) Contact maintainers via GitHub profile
- **Discussion**: Open a GitHub Discussion

---

## Acknowledgments

We recognize that:
- Accessibility is an ongoing journey, not a destination
- Not all accessibility features may be applicable to educational code examples
- We're committed to continuous improvement
- Community feedback is valuable and welcome

**Our goal**: Make this educational resource accessible to as many people as possible, while maintaining the clarity and effectiveness of design pattern demonstrations.

---

## Related Documents

- [Contributing Guidelines](CONTRIBUTING.md) - Accessibility guidelines for contributors
- [Code of Conduct](CODE_OF_CONDUCT.md) - Inclusive community standards
- [Documentation Policy](DOCUMENTATION_POLICY.md) - Documentation standards
- [Roadmap](ROADMAP.md) - Accessibility improvement timeline

---

**Document Version**: 1.0  
**Last Updated**: January 28, 2026  
**Next Review**: Quarterly (March, June, September, December 2026)  
**Owner**: @luizwbr

**Changelog**:
- v1.0 (2026-01-28): Initial accessibility statement
