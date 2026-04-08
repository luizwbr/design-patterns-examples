# Design Patterns Examples / Exemplos de Padrões de Projeto

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Tests](https://github.com/luizwbr/design-patterns-examples/workflows/Run%20Pattern%20Tests/badge.svg)](https://github.com/luizwbr/design-patterns-examples/actions)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](.github/PULL_REQUEST_TEMPLATE.md)
[![OpenSSF Best Practices](https://www.bestpractices.dev/projects/11714/badge)](https://www.bestpractices.dev/projects/11714)
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fluizwbr%2Fdesign-patterns-examples.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2Fluizwbr%2Fdesign-patterns-examples?ref=badge_shield)

[en] All 23 Gang of Four design patterns implemented in **8 languages**: Go · Python · TypeScript · Java · PHP · React.js · AngularJS · Angular 2+.  
[pt-br] Todos os 23 padrões de projeto GoF implementados em **8 linguagens**: Go · Python · TypeScript · Java · PHP · React.js · AngularJS · Angular 2+.

Inspired by / Inspirado por: <a href="https://refactoring.guru/design-patterns/catalog" target="_blank">Refactoring Guru</a>

---

## ⚡ Quick Start / Início Rápido

```bash
# Clone the repo
git clone https://github.com/luizwbr/design-patterns-examples.git
cd design-patterns-examples

# Pick a pattern and a language, then run it:

# Go
go run patterns/singleton/go/main.go

# Python
python patterns/singleton/python/Singleton.py

# TypeScript
tsx patterns/singleton/typescript/Singleton.ts

# Java
cd patterns/singleton/java && javac Singleton.java && java Singleton

# PHP
php patterns/singleton/php/Singleton.php
```

---

## 🎨 Patterns / Padrões

### Creational / Criacionais

| Pattern | Go | Python | TS | Java | PHP | React | AngularJS | Angular 2 |
|---------|:--:|:------:|:--:|:----:|:---:|:-----:|:---------:|:---------:|
| [Factory Method](patterns/factory-method) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| [Abstract Factory](patterns/abstract-factory) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| [Builder](patterns/builder) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| [Prototype](patterns/prototype) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| [Singleton](patterns/singleton) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

### Structural / Estruturais

| Pattern | Go | Python | TS | Java | PHP | React | AngularJS | Angular 2 |
|---------|:--:|:------:|:--:|:----:|:---:|:-----:|:---------:|:---------:|
| [Adapter](patterns/adapter) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| [Bridge](patterns/bridge) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| [Composite](patterns/composite) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| [Decorator](patterns/decorator) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| [Facade](patterns/facade) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| [Flyweight](patterns/flyweight) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| [Proxy](patterns/proxy) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

### Behavioral / Comportamentais

| Pattern | Go | Python | TS | Java | PHP | React | AngularJS | Angular 2 |
|---------|:--:|:------:|:--:|:----:|:---:|:-----:|:---------:|:---------:|
| [Chain of Responsibility](patterns/chain-of-responsibility) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| [Command](patterns/command) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| [Iterator](patterns/iterator) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| [Mediator](patterns/mediator) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| [Memento](patterns/memento) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| [Observer](patterns/observer) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| [State](patterns/state) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| [Strategy](patterns/strategy) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| [Template Method](patterns/template-method) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| [Visitor](patterns/visitor) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

## 📁 Structure / Estrutura

```
patterns/
└── pattern-name/
    ├── go/
    ├── python/
    ├── typescript/
    ├── java/
    ├── php/
    ├── reactjs/
    ├── angularjs/
    └── angular2/
```

---

## 🧪 CI / Testes

[en] Automated tests run on every push via GitHub Actions for Go, Python, TypeScript, Java, and PHP.  
[pt-br] Testes automatizados rodam a cada push via GitHub Actions para Go, Python, TypeScript, Java e PHP.

---

## 🌍 Full Documentation / Documentação Completa

- **[English](doc/en/README.md)**
- **[Português BR](doc/pt-br/README.md)**

---

## 🤝 Contributing / Contribuindo

[en] Read [CONTRIBUTING.md](CONTRIBUTING.md) to get started. All contributions require a [DCO sign-off](DCO.md).  
[pt-br] Leia [CONTRIBUTING.md](CONTRIBUTING.md) para começar. Todas as contribuições requerem [DCO sign-off](DCO.md).

---

## 📝 License / Licença

MIT — see [LICENSE](LICENSE).

[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fluizwbr%2Fdesign-patterns-examples.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2Fluizwbr%2Fdesign-patterns-examples?ref=badge_large)
