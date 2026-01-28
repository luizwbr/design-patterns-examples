# Contributing to Design Patterns Examples

Thank you for your interest in contributing to this design patterns educational repository! This document provides guidelines for contributing to the project.

**📍 Quick Links**:
- [Quick Start Guide](QUICKSTART.md) - New to the project? Start here!
- [Project Roadmap](ROADMAP.md) - See what we're working on in 2026-2027
- [Governance](GOVERNANCE.md) - How decisions are made
- [Roles](ROLES.md) - Who does what

## 🌟 How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues to avoid duplicates. When creating a bug report, include as many details as possible using our bug report template.

**To report a bug:**
1. Navigate to the [Issues](../../issues) page
2. Click "New Issue"
3. Select the "Bug Report" template
4. Fill in all required information

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, use our feature request template and provide:

- A clear and descriptive title
- A detailed description of the proposed feature
- Explain why this enhancement would be useful
- List any alternatives you've considered

**Note**: Check the [Project Roadmap](ROADMAP.md) to see if your suggestion aligns with planned work or explicitly out-of-scope items.

### Adding New Pattern Implementations

We welcome new pattern implementations! When adding a new design pattern:

1. **Create the pattern directory** following the existing structure:
   ```
   patterns/pattern-name/
   ├── README.en.md
   ├── README.pt-br.md
   ├── go/
   ├── reactjs/
   ├── php/
   ├── typescript/
   ├── java/
   ├── angularjs/
   └── angular2/
   ```

2. **Implement in all 7 languages** for consistency (or at least in multiple languages)

3. **Follow language-specific conventions**:
   - **Go**: Use PascalCase for exported types, follow Go idioms
   - **TypeScript/JavaScript**: Use PascalCase for classes, camelCase for functions
   - **Java**: Follow standard Java conventions
   - **PHP**: Follow PSR-12 coding standards
   - **React.js**: Use functional components with hooks when appropriate
   - **Angular**: Follow Angular style guide

4. **Include clear comments** explaining pattern-specific concepts

5. **Create bilingual documentation** (English and Portuguese)

### Improving Existing Implementations

When improving existing code:

- Maintain conceptual consistency across language implementations
- Keep examples simple and focused on the pattern
- Ensure code is educational and easy to understand
- Add comments for clarity
- Test that the implementation works correctly

## 📋 Pull Request Process

1. **Fork the repository** and create your branch from `main` or `master`

2. **Make your changes** following the guidelines above

3. **Test your code**:
   - Ensure all implementations compile/run without errors
   - Verify that pattern behavior is demonstrated correctly
   - Test in the target language environment

4. **Update documentation**:
   - ✅ **REQUIRED**: Update README files if adding new patterns or changing behavior
   - ✅ **REQUIRED**: Include code comments in English
   - ✅ **REQUIRED**: Update both English and Portuguese documentation when changing patterns
   - ✅ **REQUIRED**: Test that all documented examples still work
   - ✅ Update Quick Start guide if changing getting started steps
   - ✅ Update any affected governance or process documents
   - 📖 See [Documentation Policy](DOCUMENTATION_POLICY.md) for full requirements

   **Why this matters**: Documentation must stay consistent with code. Outdated docs confuse users and waste everyone's time.

5. **Commit your changes**:
   - Use clear, descriptive commit messages
   - Reference issues if applicable (e.g., "Fixes #123")
   - Keep commits focused and atomic
   - **Sign off your commits** (see [DCO](#-developer-certificate-of-origin-dco) section below)

6. **Submit a Pull Request**:
   - Fill out the PR template completely
   - Link related issues
   - Describe what you changed and why
   - Include screenshots for UI changes (if applicable)

7. **Respond to feedback**:
   - Be open to suggestions and constructive criticism
   - Make requested changes promptly
   - Ask questions if anything is unclear

## 🎯 Code Quality Standards

### General Guidelines

- **Educational First**: Prioritize clarity and simplicity over optimization
- **Consistency**: Maintain alignment across language implementations
- **Comments**: Use inline comments to explain pattern concepts
- **Naming**: Use meaningful, descriptive names for classes, methods, and variables
- **Examples**: Use real-world, practical examples

### Language-Specific Requirements

#### Go
- Use `go fmt` for formatting
- Follow effective Go guidelines
- Use interfaces to define contracts
- Include `main.go` with usage example

#### TypeScript/JavaScript
- Use TypeScript features appropriately
- Leverage type safety
- Follow ESLint rules if configured
- Export classes/functions properly

#### Java
- Use proper access modifiers
- Follow Java naming conventions
- Include proper documentation comments
- Organize with packages when appropriate

#### PHP
- Follow PSR-12 coding standards
- Use type hints (PHP 7.4+)
- Proper visibility modifiers
- Use namespaces appropriately

#### React.js
- Use functional components with hooks
- Keep components focused
- Use descriptive names
- Include prop types or TypeScript types

#### Angular (both versions)
- Follow Angular style guide
- Use proper component structure
- Implement lifecycle hooks correctly
- Use TypeScript typing

## 📖 Documentation Standards

**Important**: Documentation must be kept current with code. See [Documentation Policy](DOCUMENTATION_POLICY.md) for full details.

### Code Documentation
- Write comments in English
- Explain the "why" not just the "what"
- Document complex logic
- Include usage examples in code
- Keep examples tested and working

### README Files
- Maintain bilingual documentation (English and Portuguese)
- Use clear, educational language
- Include usage examples that work with current code
- Explain pattern benefits and use cases
- Update when pattern implementation changes
- Test all commands and examples before committing

### Documentation Currency
- ✅ All code examples must work with current code
- ✅ Update docs in the same PR as code changes
- ✅ Report documentation issues via GitHub Issues (use "documentation" label)
- ✅ No PR will be merged with known documentation inconsistencies

### Accessibility Best Practices

We strive to make our project accessible to persons with disabilities. Please follow these guidelines:

#### Documentation Accessibility
- ✅ Use descriptive link text (not "click here" or "read more")
- ✅ Provide alt text for images (if images are added to documentation)
- ✅ Use proper heading hierarchy (H1 → H2 → H3, don't skip levels)
- ✅ Use semantic Markdown (headings, lists, code blocks, not just bold text)
- ✅ Ensure code examples have sufficient color contrast if using syntax highlighting
- ✅ Use clear, simple language for better comprehension

#### Code Example Accessibility (React/Angular Components)
- ✅ Include semantic HTML elements (button, nav, main, etc.)
- ✅ Add ARIA labels where appropriate (`aria-label`, `aria-describedby`)
- ✅ Ensure keyboard navigation works (tab order, focus indicators)
- ✅ Use sufficient color contrast ratios (WCAG AA: 4.5:1 for text)
- ✅ Don't rely solely on color to convey information
- ✅ Add meaningful alt text for any images in components
- ✅ Include visible focus indicators for interactive elements

#### Example:
```typescript
// ❌ Poor accessibility
<div onClick={handleClick}>Submit</div>

// ✅ Good accessibility
<button 
  onClick={handleClick}
  aria-label="Submit form"
  type="submit"
>
  Submit
</button>
```

**Note**: While we aim for accessibility, we recognize that some pattern demonstrations may prioritize educational clarity. When conflicts arise, document accessibility limitations in comments.
- Keep consistent structure across patterns

## 🔍 Review Process

All contributions go through a review process:

1. **Automated checks**: Code must pass any automated tests
2. **Manual review**: Maintainers review code quality and adherence to guidelines
3. **Educational value**: Ensure contribution enhances learning
4. **Consistency**: Verify alignment with existing patterns
5. **Documentation**: Check that documentation is complete and clear

## ❓ Questions?

If you have questions about contributing:

- Open an issue with the "question" label
- Check existing issues and discussions
- Review the [Copilot Instructions](.github/copilot-instructions.md) for detailed guidelines
- See [GOVERNANCE.md](GOVERNANCE.md) for information about decision-making and project roles

## 🙏 Thank You!

Your contributions help make this educational resource better for developers learning design patterns worldwide. We appreciate your time and effort!

---

## 📜 Code of Conduct

This project adheres to a [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to the project maintainers.

## 🏛️ Project Governance

This project follows a defined governance model. For information about:
- How decisions are made
- Key roles and responsibilities
- Contribution review process
- Conflict resolution

See our [Governance Document](GOVERNANCE.md).

**Current role holders and detailed responsibilities**: [ROLES.md](ROLES.md)

## ✍️ Developer Certificate of Origin (DCO)

All contributors are required to sign off on their commits to certify that they have the right to submit the code under the project's open source license. This is done using the Developer Certificate of Origin (DCO).

### How to Sign Off Your Commits

Add a `Signed-off-by` line to your commit messages. You can do this automatically by using the `-s` or `--signoff` flag:

```bash
git commit -s -m "Add new pattern implementation"
```

This will add a line like this to your commit message:

```
Signed-off-by: Your Name <your.email@example.com>
```

### Configuring Git

Ensure your git user name and email are set correctly:

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### What Does This Mean?

By signing off, you certify that:
- You wrote the code yourself, OR
- You have the right to submit the code under the project's license, OR
- Someone who certified the above provided you with the contribution

For the full DCO text and more information, see [DCO.md](DCO.md) or visit [developercertificate.org](https://developercertificate.org/).

**Note**: Pull requests without proper sign-off may not be accepted.

## 📄 License

By contributing to this project, you agree that your contributions will be licensed under the [MIT License](LICENSE).
