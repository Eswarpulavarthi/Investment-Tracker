# Contributing to Investment Tracker

Thank you for your interest in contributing! This document outlines the process for contributing to this project.

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR-USERNAME/Investment-Tracker.git
   cd Investment-Tracker
   ```

3. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Development Workflow

### Creating a Feature Branch
```bash
git checkout -b feature/your-feature-name
```

### Code Style
- Follow PEP 8 guidelines
- Use `black` for code formatting
- Use `flake8` for linting
- Write docstrings for all functions

### Running Tests
```bash
pytest tests/
pytest --cov=src tests/  # With coverage
```

### Committing Changes
Use descriptive commit messages following conventional commits:
```bash
git commit -m "feat: Add new portfolio analysis feature"
git commit -m "fix: Resolve calculation bug in returns"
git commit -m "docs: Update README with new examples"
```

## Pull Request Process

1. **Update documentation** if needed
2. **Add tests** for new functionality
3. **Run all tests locally** to ensure they pass
4. **Format code** with black and flake8:
   ```bash
   black src/
   flake8 src/
   ```
5. **Push to your branch:**
   ```bash
   git push origin feature/your-feature-name
   ```
6. **Create a Pull Request** with a clear title and description

## Issue Reporting

When reporting issues:
- Use descriptive titles
- Include steps to reproduce
- Mention Python version and OS
- Attach error logs if available

## Project Structure
- `src/` - Main source code
- `tests/` - Test suite
- `docs/` - Documentation
- `data/` - Sample data and schemas

## Areas for Contribution

- **Backend**: Enhanced analytics, new asset types, database optimization
- **Frontend**: Web interface development (FastAPI + React)
- **Documentation**: API docs, user guides, tutorials
- **Testing**: Unit tests, integration tests
- **DevOps**: Docker setup, CI/CD pipeline, deployment guides

## Code of Conduct

Be respectful, inclusive, and professional. We're building this together!

## Questions?

Feel free to open an issue or discussion on GitHub.

Happy contributing! 🚀
