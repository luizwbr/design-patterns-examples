# Quick Start Guide

Welcome to Design Patterns Examples! This guide will help you quickly start learning and using design patterns with real code examples.

## ⚡ 5-Minute Quick Start

### 1. Choose a Pattern

Browse the available patterns in the `patterns/` directory:
- **Creational**: Singleton, Factory Method, Abstract Factory, Builder, Prototype
- **Structural**: Adapter, Bridge, Composite, Decorator, Facade, Flyweight, Proxy
- **Behavioral**: Chain of Responsibility, Command, Iterator, Mediator, Memento, Observer, State, Strategy, Template Method, Visitor

### 2. Pick Your Language

Each pattern is implemented in 7 languages:
- 🐹 **Go** - Simple, modern, great for learning
- 📘 **TypeScript** - Type-safe JavaScript
- ☕ **Java** - Classic OOP
- 🐘 **PHP** - Web-focused
- ⚛️ **React.js** - Modern web components
- 🅰️ **AngularJS** - Legacy web framework
- 🅰️ **Angular 2+** - Modern Angular

### 3. Run Your First Example

Let's try the **Singleton pattern** in Go:

```bash
# Clone the repository
git clone https://github.com/luizwbr/design-patterns-examples.git
cd design-patterns-examples

# Navigate to Singleton pattern in Go
cd patterns/singleton/go

# Run the example
go run main.go
```

**Expected Output:**
```
Creating database instance
Executing query: SELECT * FROM users on Database connection established
Executing query: SELECT * FROM products on Database connection established
db1 and db2 are the same instance: true
```

🎉 **Congratulations!** You just ran your first design pattern example.

---

## 📚 Running Examples in Different Languages

### Go
```bash
cd patterns/singleton/go
go run main.go
```

### TypeScript
```bash
cd patterns/singleton/typescript
npx tsx Singleton.ts
# or compile first
tsc Singleton.ts && node Singleton.js
```

### Java
```bash
cd patterns/singleton/java
javac Singleton.java
java Singleton
```

### PHP
```bash
cd patterns/singleton/php
php Singleton.php
```

### React.js
React components are meant to be imported into a React application. See the component files for usage examples in comments.

### Angular (2+)
Angular components are meant to be used in Angular applications. Check the `.ts` files for usage examples.

---

## 🎯 What to Learn Next

### Understand the Pattern

Each pattern directory includes:
- **README.en.md** - English explanation
- **README.pt-br.md** - Portuguese explanation (Brazil)
- **Code examples** - Working implementations in all 7 languages

Example for Singleton:
```bash
cd patterns/singleton
cat README.en.md  # Read the explanation
```

### Try Different Patterns

**Easy to start with:**
1. **Singleton** - One instance shared everywhere
2. **Factory Method** - Create objects without specifying exact class
3. **Observer** - Subscribe to events and get notified

**More complex:**
1. **Abstract Factory** - Families of related objects
2. **Decorator** - Add behavior dynamically
3. **Strategy** - Switch algorithms at runtime

### Compare Implementations

See how the same pattern differs across languages:

```bash
# Singleton in different languages
cat patterns/singleton/go/main.go
cat patterns/singleton/typescript/Singleton.ts
cat patterns/singleton/java/Singleton.java
cat patterns/singleton/php/Singleton.php
```

---

## 🛠️ Installation Requirements

### Required for Running Examples

| Language | Requirements | Installation |
|----------|-------------|--------------|
| **Go** | Go 1.16+ | [Download Go](https://go.dev/dl/) |
| **TypeScript** | Node.js + TypeScript | `npm install -g typescript tsx` |
| **Java** | JDK 11+ | [Download JDK](https://adoptium.net/) |
| **PHP** | PHP 8.0+ | [Download PHP](https://www.php.net/downloads) |
| **React** | Node.js + React | `npm install react react-dom` |
| **Angular** | Node.js + Angular CLI | `npm install -g @angular/cli` |

### Verify Your Setup

```bash
# Check Go
go version

# Check TypeScript
tsc --version
npx tsx --version

# Check Java
java -version
javac -version

# Check PHP
php -v

# Check Node (for React/Angular)
node -v
npm -v
```

---

## 📖 Learning Path

### Beginner (Week 1)
1. Read about what design patterns are
2. Run 3 examples: Singleton, Factory Method, Observer
3. Understand when to use each pattern

### Intermediate (Week 2-3)
1. Implement one pattern yourself in your preferred language
2. Compare your implementation with ours
3. Try 5 more patterns: Adapter, Decorator, Strategy, Command, Template Method

### Advanced (Week 4+)
1. Study complex patterns: Abstract Factory, Composite, Mediator
2. Combine multiple patterns in a project
3. Understand pattern interactions and trade-offs

---

## 💡 Common Use Cases

### When You Need...

**One shared instance across your app?**
→ Use **Singleton** pattern

**To create objects without knowing their exact type?**
→ Use **Factory Method** or **Abstract Factory**

**To notify multiple objects about state changes?**
→ Use **Observer** pattern

**To add features to objects without changing their code?**
→ Use **Decorator** pattern

**To simplify a complex system's interface?**
→ Use **Facade** pattern

**To switch algorithms at runtime?**
→ Use **Strategy** pattern

**To encapsulate a request as an object?**
→ Use **Command** pattern

---

## 🔍 Explore the Repository

### Key Directories

```
design-patterns-examples/
├── patterns/           # All 23 pattern implementations
│   ├── singleton/     # Example pattern
│   │   ├── go/
│   │   ├── typescript/
│   │   ├── java/
│   │   ├── php/
│   │   ├── reactjs/
│   │   ├── angularjs/
│   │   └── angular2/
│   └── ...
├── doc/               # Full documentation
│   ├── en/           # English docs
│   └── pt-br/        # Portuguese docs
└── scripts/          # Testing scripts
```

### Browse Patterns

| Pattern | Category | Difficulty | Use Case |
|---------|----------|------------|----------|
| Singleton | Creational | ⭐ Easy | One shared instance |
| Factory Method | Creational | ⭐⭐ Medium | Object creation |
| Observer | Behavioral | ⭐⭐ Medium | Event handling |
| Decorator | Structural | ⭐⭐⭐ Hard | Add features dynamically |
| Strategy | Behavioral | ⭐⭐ Medium | Swap algorithms |

---

## 🧪 Test Your Understanding

### Quick Quiz

After running examples, ask yourself:

1. **What problem does this pattern solve?**
2. **When should I use it?**
3. **What are the trade-offs?**
4. **How does it differ across languages?**

### Hands-On Exercise

Pick a pattern and:
1. Run all 7 language implementations
2. Modify one to add a new feature
3. Test your modification
4. Compare your approach with the original

---

## 🤝 Next Steps

### Learn More

- 📖 Read full documentation: [English](doc/en/README.md) | [Portuguese](doc/pt-br/README.md)
- 🎓 Study pattern descriptions in each pattern's README
- 🔗 Visit [Refactoring Guru](https://refactoring.guru/design-patterns) for more details

### Contribute

- ⭐ Star this repository if it helped you
- 🐛 Report bugs or issues
- 💡 Suggest improvements
- 🔧 Submit your own pattern improvements
- 📚 See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines

### Get Help

- ❓ Open an [issue](https://github.com/luizwbr/design-patterns-examples/issues) for questions
- 💬 Check existing issues for common problems
- 📧 Review [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for community guidelines

---

## 🚀 Example Workflow

Here's a typical learning session:

```bash
# 1. Clone the repo (one time)
git clone https://github.com/luizwbr/design-patterns-examples.git
cd design-patterns-examples

# 2. Pick a pattern to learn today
cd patterns/observer

# 3. Read about it
cat README.en.md

# 4. Try it in your preferred language
cd go
go run main.go

# 5. Compare with another language
cd ../typescript
npx tsx Observer.ts

# 6. Understand the differences
# Go uses channels, TypeScript uses callbacks

# 7. Move to next pattern
cd ../../decorator
```

---

## 📊 Testing (Optional)

Want to test all patterns at once?

```bash
# Test all patterns in all languages
./scripts/test-all-patterns.sh

# Test specific language
./scripts/test-go-patterns.sh
./scripts/test-typescript-patterns.sh
./scripts/test-java-patterns.sh
./scripts/test-php-patterns.sh
```

See [docs/CI_TESTING.md](docs/CI_TESTING.md) for details.

---

## 🎓 Educational Resources

### Recommended Reading Order

1. **Start Here**: [README.md](README.md) - Project overview
2. **Learn Patterns**: Browse `patterns/` directory
3. **Deep Dive**: Read full docs in `doc/en/` or `doc/pt-br/`
4. **Reference**: Use as needed when coding

### External Resources

- 📖 [Refactoring Guru](https://refactoring.guru/design-patterns) - Comprehensive guide
- 📘 "Design Patterns" by Gang of Four - The original book
- 🎥 YouTube tutorials on design patterns
- 💻 Practice on your own projects

---

## ⚡ Troubleshooting

### "Command not found" errors

Install the required language tools (see [Installation Requirements](#installation-requirements))

### "File not found" errors

Make sure you're in the correct directory:
```bash
pwd                    # Check current directory
ls patterns/singleton  # Verify pattern exists
```

### Compilation errors

- Check you're using the correct language version
- Review error messages carefully
- Compare with the original code in the repository

### Still stuck?

Open an issue: [Create Issue](https://github.com/luizwbr/design-patterns-examples/issues/new)

---

## 📝 Summary

**You've learned how to:**
✅ Clone and navigate the repository  
✅ Run pattern examples in different languages  
✅ Understand what each pattern does  
✅ Find documentation and examples  
✅ Set up your development environment  
✅ Test patterns and verify they work  

**Now you're ready to:**
🚀 Explore all 23 design patterns  
🚀 Learn in your preferred programming language  
🚀 Apply patterns to your own projects  
🚀 Contribute improvements back to the project  

---

**Happy Learning! 🎉**

*Questions? Check [CONTRIBUTING.md](CONTRIBUTING.md) or open an issue.*

---

## Related Documentation

- [Full Documentation (English)](doc/en/README.md)
- [Full Documentation (Portuguese)](doc/pt-br/README.md)
- [Contributing Guidelines](CONTRIBUTING.md)
- [Project Roadmap](ROADMAP.md)
- [Developer Guide](docs/DEVELOPER_GUIDE.md)
- [CI Testing Documentation](docs/CI_TESTING.md)
