"""A sample module. Replace it with your own code."""


def greet(name: str = "world") -> str:
    """Return a greeting for ``name``.

    Raises:
        ValueError: If ``name`` is empty or only whitespace.
    """
    name = name.strip()
    if not name:
        raise ValueError("name must not be empty")
    return f"Hello, {name}!"
