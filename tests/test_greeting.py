import pytest

from example_package import greet


def test_greet_defaults_to_world() -> None:
    assert greet() == "Hello, world!"


def test_greet_uses_the_given_name() -> None:
    assert greet("  Ada ") == "Hello, Ada!"


@pytest.mark.parametrize("name", ["", "   "])
def test_greet_rejects_blank_names(name: str) -> None:
    with pytest.raises(ValueError, match="must not be empty"):
        greet(name)
