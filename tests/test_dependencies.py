import pytest

import prepare_tests
from ds_lib.utils import find_python_version

# this is just dummy test case


@pytest.mark.skip(reason="This is just to check parameterize - not implemented in real scenario")
@pytest.mark.parametrize(
    "version_input, expected_version",
    [
        ("3.8", "v3.8"),
        ("3.9", "v3.9"),
        ("3.10", "v3.10"),
        ("3.11", "v3.11"),
        ("3.12", "v3.12"),

    ]
)
def test_python_versions(version_input, expected_version):
    assert (lambda: "v" + version_input)() == expected_version


# test case to test if we are in the latest 3.12 version which is still in release candidate 1
@pytest.mark.xfail  # expected fail is not used 3.12
def test_python_version():
    assert find_python_version() == "3.12"
