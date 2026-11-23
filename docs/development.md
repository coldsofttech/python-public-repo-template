# Development

## Layout

```text
src/example_package/   package source (src layout, typed)
tests/unit/            fast pytest tests
tests/integration/     end-to-end tests, marked `integration`
pyproject.toml         metadata, dependencies and tool configuration
uv.lock                locked dependencies (commit this file)
```

The package is named `example_package`. After creating a repo from this template, run the **Init** workflow: it replaces the template owner and name and deletes `TEMPLATE_CHANGELOG.md`, which records the template's own changes and is not meant for your repository (your history belongs in `CHANGELOG.md`). Then rename the package. Every place the name appears:

| Where | What to change |
| --- | --- |
| `src/example_package/` | Rename the folder to your import name. |
| `pyproject.toml` | `[tool.hatch.version] path`, `[tool.hatch.build.targets.wheel] packages` and `--cov=` in `addopts`. Add `known-first-party = ["<name>"]` under `[tool.ruff.lint.isort]` if Ruff sorts the import wrongly. |
| `tests/unit/` and `tests/integration/` | The `import example_package` lines and the name in the subprocess command of `test_installed_package.py`. |
| `README.md` | The usage example, which imports `example_package`. |
| `docs/architecture.md` and `docs/guides/python.md` | The layout and the examples. |

Then set the description in `pyproject.toml`, run `uv lock`, and check with `git grep example_package` that nothing is left. The workflows, composite actions and the release check read the name and version from `pyproject.toml`, so they need no edit.

## Tooling

| Purpose | Tool |
| --- | --- |
| Environment, dependencies, build | [uv](https://docs.astral.sh/uv/) with Hatchling |
| Lint and format | Ruff |
| Type checking | mypy (strict) |
| Tests and coverage | pytest with pytest-cov (80% minimum) |

```bash
uv sync                    # create .venv and install dev dependencies
uv run pytest              # unit tests with coverage (skips integration tests)
uv run pytest -m integration tests/integration --no-cov   # integration tests only
uv run ruff check .        # lint
uv run ruff format .       # format
uv run mypy                # type check
uv build                   # build sdist and wheel
```

## Integration tests

Tests under `tests/integration/` are marked `integration` automatically by that folder's `conftest.py`. They are excluded from the default `pytest` run, and therefore from the pre-commit hook, and run as their own job in CI. Put slower or end-to-end tests there.

## Continuous integration

The `ci` workflow calls `ci-package.yml` for the library and `ci-repo.yml` for everything outside `src/` and `tests/`. The package runs `package-lint` (Ruff, mypy, pre-commit and a dependency licence check), `package-test` (unit tests), `package-int-test` (tests marked `integration`) and `package-build` (build and `twine check`). The test jobs run on Python 3.11 to 3.15 on Ubuntu, and on 3.11 on Windows and macOS. On pull requests, `changes.yml` skips the parts a change cannot affect. A final `ci` job gates on all of them and is the single required check in the branch ruleset. Shared steps live in `.github/actions/` (`setup-uv`, `lint-python`, `run-pytest`, `audit-python`, `semgrep`, `check-release-tag`, `attach-release-files`). `audit.yml` and `security.yml` (Semgrep, uploaded to code scanning) are separate workflows.

## Releasing to PyPI

Publishing uses [trusted publishing](https://docs.pypi.org/trusted-publishers/), so no API token is stored.

1. On PyPI, add a trusted publisher for this repository: workflow `release.yml`, environment `pypi`.
2. Create an environment named `pypi`. The settings script does this and restricts it to `v*` tags.
3. Bump `__version__` in `src/<package>/__init__.py` and update `CHANGELOG.md`.
4. Publish a GitHub release tagged `v<version>`. The workflow fails if the tag and version differ.
