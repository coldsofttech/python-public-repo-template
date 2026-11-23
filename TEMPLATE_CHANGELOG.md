# Template changelog

Changes to the template itself. This file is removed when you initialise a repository from the template; your own history belongs in `CHANGELOG.md`.

## [Unreleased]

### Added

- Composite GitHub actions under `.github/actions/` (`setup-uv`, `lint-python`, `run-pytest`, `audit-python`, `semgrep`, `check-release-tag`, `attach-release-files`) shared by the workflows.
- A `changes` workflow that limits pull requests to the parts they touch, `ci-package` and `ci-repo` workflows, and a Semgrep `security` workflow that reports to the Security tab.
- Release files are attached to the GitHub release with `SHA256SUMS.txt`.
- An issue template config that points security reports and questions to the right place.
- Documentation: `security.md`, `releasing.md` and a Python guide.

### Changed

- Tests are split into `tests/unit` and `tests/integration`, and the package declares `__all__`.
- The `audit` workflow uses the shared action and also audits the dev tools.
- Dependabot also updates the composite actions, with a seven-day cooldown.

## [0.1.0] - 2026-11-20

### Added

- The first version of the template: a typed `src` package, tests, linting, type checking, pre-commit hooks, CI, dependency review, audit and release to PyPI, and the community and security files a public repository needs.
