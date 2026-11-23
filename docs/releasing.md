# Releasing

How a release is built and published. For the one-time set-up, see [repository setup](repo-setup.md).

## What a release does

Publishing a GitHub release tagged `v<version>` runs `release.yml`:

1. **Build.** Checks that the tag equals the package version (`v0.2.0` for `__version__ = "0.2.0"`), builds the sdist and wheel, and checks them with `twine check --strict`.
2. **Publish.** The next job waits for a reviewer of the `pypi` environment (Settings > Environments), then publishes to PyPI with [trusted publishing](https://docs.pypi.org/trusted-publishers/): no token is stored, and only this job has the `id-token` permission.
3. **Attach.** The files are attached to the GitHub release with `SHA256SUMS.txt`, so downloads can be checked.

If the tag and the version differ, the workflow fails before anything is built.

## Each release

1. Bump `__version__` in `src/<package>/__init__.py` and move the `[Unreleased]` entries of `CHANGELOG.md` under a version heading, in a pull request.
2. After it is merged, publish a GitHub release tagged `v<version>`. Mark it as a pre-release for a pre-release version such as `0.2.0rc1`.
3. Approve the `pypi` environment when asked.

Follow [Semantic Versioning](https://semver.org/): the names in `__all__` are the public API.

## One-time set-up

1. On PyPI, add a trusted publisher for this repository: workflow `release.yml`, environment `pypi`.
2. Create the `pypi` environment. `scripts/apply_repo_settings.py` does this and restricts it to `v*` tags; add required reviewers if you want an approval step.
3. Run the settings script for the branch ruleset and the other protections.

## If a release fails

- **Tag does not match the version:** delete the release and the tag, fix the version, and publish again.
- **PyPI rejects the upload:** a version can be published only once. Bump the version and release again; do not try to reuse the number.
- **Publisher not found:** check the workflow name (`release.yml`) and environment name (`pypi`) on PyPI.
