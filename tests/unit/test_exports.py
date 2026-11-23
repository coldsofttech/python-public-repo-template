import example_package


def test_every_exported_name_exists() -> None:
    for name in example_package.__all__:
        assert hasattr(example_package, name), name


def test_version_is_exported() -> None:
    assert "__version__" in example_package.__all__
