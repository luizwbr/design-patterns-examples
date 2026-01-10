# Contributing to Design Patterns Examples

Thank you for your interest in contributing to this design patterns educational repository! This document provides guidelines for contributing to the project.

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
   - Update README files if adding new patterns
   - Include code comments in English
   - Update both English and Portuguese documentation

5. **Commit your changes**:
   - Use clear, descriptive commit messages
   - Reference issues if applicable (e.g., "Fixes #123")
   - Keep commits focused and atomic

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

### Code Documentation
- Write comments in English
- Explain the "why" not just the "what"
- Document complex logic
- Include usage examples in code

### README Files
- Maintain bilingual documentation (English and Portuguese)
- Use clear, educational language
- Include usage examples
- Explain pattern benefits and use cases
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

## 🙏 Thank You!

Your contributions help make this educational resource better for developers learning design patterns worldwide. We appreciate your time and effort!

---

## 📜 Code of Conduct

This project adheres to a [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to the project maintainers.

## 📄 License

By contributing to this project, you agree that your contributions will be licensed under the [MIT License](LICENSE).
