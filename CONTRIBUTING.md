# Contributing to Guessquest

First off, thank you for considering contributing to Guessquest!

## Development Setup

1. Fork and clone the repository.
2. Ensure you have Python 3.9+ installed.
3. Install the project in editable mode with development dependencies:
   ```bash
   pip install -e ".[dev]"
   ```
4. Install the pre-commit hooks:
   ```bash
   pre-commit install
   ```

## Workflow

1. Create a new branch for your feature or bugfix.
2. Write your code and add corresponding tests in the `tests/` directory.
3. Run formatting, linting, and tests:
   ```bash
   ruff check .
   ruff format .
   mypy .
   pytest
   ```
4. Submit a Pull Request with a clear description of the changes.

## Guidelines
- Follow PEP 8 and use Ruff for formatting.
- Ensure all new code has type hints and passes Mypy strict mode.
- Write unit tests for new functionality to maintain coverage.
