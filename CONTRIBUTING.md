# Contributing to Design Patterns Examples

Thank you for your interest in contributing to this project! This document provides guidelines for contributing to the Design Patterns Examples repository.

## How to Contribute

### Reporting Bugs

If you find a bug, please create an issue on GitHub with the following information:

- A clear and descriptive title
- A detailed description of the issue
- Steps to reproduce the problem
- Expected behavior
- Actual behavior
- Screenshots (if applicable)
- Your environment (OS, language version, etc.)

### Suggesting Enhancements

We welcome suggestions for new features or improvements! Please create an issue with:

- A clear and descriptive title
- A detailed description of the proposed enhancement
- Why this enhancement would be useful
- Example use cases

### Pull Requests

1. **Fork the repository** and create your branch from `main`
2. **Make your changes** following the coding standards below
3. **Test your changes** to ensure they work correctly
4. **Update documentation** if you're changing functionality
5. **Commit your changes** with clear, descriptive commit messages
6. **Push to your fork** and submit a pull request

#### Pull Request Guidelines

- Keep pull requests focused on a single feature or fix
- Write clear, descriptive commit messages
- Include comments in your code where necessary
- Update the README.md if needed
- Ensure your code follows the existing style

## Adding New Design Patterns

When adding a new design pattern:

1. Create a directory with the pattern name in kebab-case
2. Include implementations in all supported languages:
   - Go (go/)
   - React.js (reactjs/)
   - PHP (php/)
   - TypeScript (typescript/)
   - Java (java/)
   - AngularJS (angularjs/)
   - Angular 2+ (angular2/)
3. Add a README.md explaining the pattern
4. Include practical examples
5. Add comments to explain the code

## Coding Standards

### General Guidelines

- Write clear, self-documenting code
- Use meaningful variable and function names
- Add comments for complex logic
- Keep functions small and focused
- Follow the existing code style in each language

### Language-Specific Standards

#### Go
- Follow [Effective Go](https://golang.org/doc/effective_go.html)
- Use `gofmt` to format your code
- Add godoc comments for public functions

#### JavaScript/TypeScript
- Use ES6+ syntax
- Follow consistent naming conventions
- Use meaningful variable names

#### PHP
- Follow [PSR-12](https://www.php-fig.org/psr/psr-12/) coding standard
- Use type hints where possible

#### Java
- Follow [Java Code Conventions](https://www.oracle.com/java/technologies/javase/codeconventions-contents.html)
- Use meaningful class and method names

## Adding Translations

We welcome translations to additional languages! To add a new language:

1. Create a directory using the language code (e.g., `es/` for Spanish, `fr/` for French)
2. Translate the main README.md
3. Translate individual pattern documentation
4. Update the main README.md to link to your translation

## Code of Conduct

Please note that this project has a [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

## Questions?

If you have questions about contributing, feel free to create an issue labeled "question" or reach out to the maintainers.

## License

By contributing to this project, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to Design Patterns Examples! 🎉
