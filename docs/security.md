# Security

How this project is protected, and the rules to keep as you extend it. To report a vulnerability, see [SECURITY.md](../SECURITY.md).

## Repository

- **Branch ruleset.** `main` needs a pull request with a code owner review and resolved conversations, the `ci` and `dependency-review` checks with an up-to-date branch, CodeQL results, squash merge only, and no deletion or force push. See [architecture](architecture.md#branch-governance).
- **Secrets.** Secret scanning with push protection is on, and gitleaks runs in pre-commit. No token is stored for publishing: PyPI uses trusted publishing.
- **Workflows.** Workflows ask for read-only permissions by default and raise them per job. Actions are pinned to version tags and kept current by Dependabot (seven-day cooldown), and `actionlint` and Semgrep's `p/github-actions` rules check them. Event values are passed through `env`, never expanded inside scripts.
- **Release.** Publishing runs from the `pypi` environment, restricted to `v*` tags, so a branch cannot publish and a reviewer approves each release.

## Supply chain

- Dependencies are locked in `uv.lock` and CI installs with `--locked`.
- `audit.yml` runs `pip-audit` on the locked dependencies, including the dev tools, weekly and when `uv.lock` changes. Dependency review blocks vulnerable additions on pull requests.
- `security.yml` runs Semgrep (`p/python`, `p/owasp-top-ten`, and `p/github-actions` for the workflows) and uploads the results to the Security tab. It is not a required check, so a new rule does not block unrelated pull requests.
- CI fails on a dependency licence matching `GPL`.

## Semgrep exclusions

The `semgrep` action excludes two rules, and tests are not scanned. Review them when things change:

| Rule | Why it is off | When to turn it back on |
| --- | --- | --- |
| `github-actions-mutable-action-tag` | Actions are pinned to version tags, kept current by Dependabot, instead of commit SHAs. | If you want SHA pinning (Dependabot can update SHAs too). |
| `dangerous-subprocess-use-tainted-env-args` | The only hits are in `scripts/`, which call the trusted `gh` CLI with values the maintainer passes. | If you add code that passes untrusted input to a subprocess. |

A finding silenced in the source with `nosemgrep` is left out of the report, so it does not show up as an open alert.

## Rules to keep

1. Treat all input as untrusted: validate values and sizes, and never build shell commands, SQL or file paths from them with string formatting.
2. Keep secrets out of messages and logs, and out of the repository.
3. Add a dependency only when it earns its place, and check its licence and maintenance.
4. Do not use `eval`, `exec` or `pickle` on external data, and do not disable TLS verification. Ruff's `S` rules flag the common mistakes.
5. Keep workflows least-privilege: add a permission to the job that needs it, not to the whole workflow.
6. Keep private vulnerability reporting enabled so the route in `SECURITY.md` works.
