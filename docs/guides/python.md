# Python guide

How to use the package from your own code. Replace this page with a walkthrough of your real API.

```bash
pip install python-public-repo-template
# or
uv add python-public-repo-template
```

Requires Python 3.11 or newer. The package is typed.

```python
import example_package

print(example_package.__version__)
```

## The public API

Everything in `example_package.__all__` is public and follows [Semantic Versioning](https://semver.org/):

| Name | What it is |
| --- | --- |
| `__version__` | The installed version, as a string. |

Anything else, and any name starting with `_`, is internal and may change without notice. A test (`tests/unit/test_exports.py`) checks that every name in `__all__` exists.

## Conventions

- Invalid input raises a standard exception (`ValueError`, `TypeError`) with a message you can show to a user.
- The package does not print or exit, so any application can use it.
- Nothing is read from the environment or the file system unless a function's description says so.

## Adding a guide

Write one page per feature under `guides/`, linked from the table above: a short example, the arguments, what is returned, and the exceptions it raises.
