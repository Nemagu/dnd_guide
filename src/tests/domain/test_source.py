from uuid import UUID, uuid4

import pytest

from domain.exception import DomainException
from domain.source import Source

NAME = "It is valid name"
DESCRIPTION = "It is valid description"
SOURCE_ID = uuid4()
NAME_IN_ENGLISH = "It is valid name in english"


def generate_source(
    source_id: UUID = SOURCE_ID,
    name: str = NAME,
    description: str = DESCRIPTION,
    name_in_english: str = NAME_IN_ENGLISH,
):
    return Source(
        source_id=source_id,
        name=name,
        description=description,
        name_in_english=name_in_english,
    )


def test_name_ok():
    source = generate_source()
    assert source.name == NAME


@pytest.mark.parametrize("name", ["", "I" * 101], ids=["empty", "too_long"])
def test_name_invalid(name):
    with pytest.raises(DomainException):
        generate_source(name=name)


def test_description_ok():
    source = generate_source()
    assert source.description == DESCRIPTION


def test_description_invalid():
    with pytest.raises(DomainException):
        generate_source(description="")


def test_name_in_english_ok():
    source = generate_source()
    assert source.name_in_english == NAME_IN_ENGLISH


@pytest.mark.parametrize("name", ["I" * 101], ids=["too_long"])
def test_name_in_english_invalid(name):
    with pytest.raises(DomainException):
        generate_source(name_in_english=name)


def test_new_name_ok():
    source = generate_source()
    new_name = "New name"
    source.new_name(new_name)
    assert source.name == new_name


@pytest.mark.parametrize(
    "new_name", ["", "I" * 101, NAME], ids=["empty", "too_long", "the_same"]
)
def test_new_name_invalid(new_name):
    source = generate_source()
    with pytest.raises(DomainException):
        source.new_name(new_name)


def test_new_description_ok():
    source = generate_source()
    new_description = "New description"
    source.new_description(new_description)
    assert source.description == new_description


def test_new_description_invalid():
    source = generate_source()
    with pytest.raises(DomainException):
        source.new_description("")


def test_new_name_in_english_ok():
    source = generate_source()
    new_name_in_english = "New name in english"
    source.new_name_in_english(new_name_in_english)
    assert source.name_in_english == new_name_in_english


def test_new_name_in_english_invalid():
    source = generate_source()
    with pytest.raises(DomainException):
        source.new_name_in_english("I" * 101)
