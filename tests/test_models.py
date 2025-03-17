from typing import Optional
import pytest
from rich import print

from pokeapi import models
from pokeapi.api import Api


@pytest.fixture
def api() -> Api:
    """
    Fixture to create an instance of the Api class.
    """
    return Api()


@pytest.mark.parametrize(
    [
        "id",
        "name",
        "expected",
    ],
    [
        (1, None, models.Berry),
        (None, "cheri", models.Berry),
    ]
)
def test_get_berry_by_id(
    api: "Api",
    id: Optional[int],
    name: Optional[str],
    expected: models.Berry,
) -> None:
    """
    Testing the berries API.

    api (Api): The API instance.
    id (Optional[int]): The ID of the berry.
    name (Optional[str]): The name of the berry.
    expected (models.Berry): The expected result.
    """

    expected = api.get_berry(id=id, name=name)
    assert isinstance(expected, models.Berry)


@pytest.mark.parametrize(
    [
        "limit",
        "offset",
    ],
    [
        (None, None),
        (5, 0),
        (100, 0),
    ]
)
def test_get_all_berries(
    api: "Api",
    limit: Optional[int],
    offset: Optional[int],
) -> None:
    """
    Testing the berries API.

    api (Api): The API instance.
    limit (Optional[int]): The limit of the berries.
    offset (Optional[int]): The offset of the berries.
    """

    berries = api.get_all_berries(limit=limit, offset=offset)
    print(berries)
    assert isinstance(berries, models.NamedAPIResourceList)
    assert len(berries.results) <= limit
    assert berries.count > 0
