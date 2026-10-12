import pytest

from playground import slugify


def test_slugify_issue_example():
    assert slugify("Smørrebrød & Øl: Top 10!") == "smoerrebroed-oel-top-10"


def test_slugify_empty():
    assert slugify("") == ""


@pytest.mark.parametrize(
    ("title", "expected"),
    [
        ("Hello World", "hello-world"),
        ("  --Hello,   World--  ", "hello-world"),
        ("Æble på Ærø", "aeble-paa-aeroe"),
        ("ÅRHUS", "aarhus"),
        ("Café déjà vu", "cafe-deja-vu"),
        ("!!!", ""),
        ("   ", ""),
        ("snake_case and CamelCase", "snake-case-and-camelcase"),
    ],
)
def test_slugify_cases(title, expected):
    assert slugify(title) == expected
