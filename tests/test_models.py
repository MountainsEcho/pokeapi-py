from typing import Optional
import pytest

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
def test_berries_api(
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
