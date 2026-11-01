# Contributing to Personal TDEE & Calorie Planning Calculator

Thank you for considering contributing to this project! As an academic DevOps project, adherence to standard development workflows is essential.

## How to Suggest Improvements or Report Problems
* **Bug Reports:** Open a GitHub Issue using the **Bug Report** template. Please include steps to reproduce the issue and expected behavior.
* **Feature Requests:** Open a GitHub Issue using the **Feature Request** template, explaining why the feature would be useful.

## Development Workflow (GitHub Flow)
1. **Never commit directly to `main`.** All work must be done on a dedicated feature or bug-fix branch.
   * Branch naming convention: `feature/issue-number-short-description` (e.g., `feature/1-user-profile`) or `fix/issue-number-description`.
2. **Semantic Commit Messages:** Every commit must follow semantic conventions:
   * Format: `type(scope): short description`
   * Allowed types: `feat`, `fix`, `docs`, `test`, `refactor`, `build`, `ci`, `chore`.
3. **Pull Requests:** Once your feature or bug fix is complete:
   * Push your branch to GitHub.
   * Open a Pull Request (PR) targeting the `main` branch.
   * Complete the PR self-review checklist.
   * Ensure all automated tests pass successfully before merging.

## Coding Standards
* Follow standard Python PEP 8 naming conventions (e.g., `snake_case` for functions and variables, `PascalCase` for classes).
* Keep functions modular, readable, and properly documented with docstrings where appropriate.