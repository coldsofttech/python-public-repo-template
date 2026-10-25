# public-repo-template

A ready-to-use starting point for public GitHub repositories, with community files, issue and pull request templates, automated dependency updates and security checks already in place.

## What you get

- Contribution, conduct, support and security-reporting guidelines
- Issue forms and a pull request template
- Automated dependency updates and dependency review
- A changelog ready for your first release
- Consistent editor and line-ending settings
- Secret scanning before every commit

## Getting started

1. Click **Use this template** on GitHub and create your new repository.
2. Replace this README with a description of your project.
3. Run the **Init** workflow from the Actions tab and merge the pull request it opens. This fills in your owner and repository name. Then add your contact details in `CODE_OF_CONDUCT.md`, delete `.github/workflows/init.yml`, and replace the description above.
4. Apply the repository protections by following the [setup guide](docs/repo-setup.md).
5. Install the commit checks: `pip install pre-commit && pre-commit install --hook-type pre-commit --hook-type post-commit`.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Please report security issues privately as described in [SECURITY.md](SECURITY.md).

## License

Released under the [MIT License](LICENSE).
