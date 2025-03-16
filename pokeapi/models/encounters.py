from __future__ import annotations
from pydantic import BaseModel, Field

from .common import NamedAPIResource, Name


class EncounterMethod(BaseModel):
    """
    An encounter method is a way of encountering a Pokémon in the wild.

    Attributes:
        id (int): The identifier for this resource.
        name (str): The name for this resource.
        order (int): A good value for sorting.
        names (list[Name]): The name of this encounter method listed in different
            languages.
    """
    id: int = Field(description="The identifier for this resource.")
    name: str = Field(description="The name for this resource.")
    order: int = Field(description="A good value for sorting.")
    names: list["Name"] = Field(
        default_factory=list,
        description="The name of this encounter method listed in different languages.")


class EncounterCondition(BaseModel):
    """
    An encounter condition is a way of determining the conditions under which a
    Pokémon can be encountered in the wild.

    Attributes:
        id (int): The identifier for this resource.
        name (str): The name for this resource.
        names (list[Name]): The name of this encounter condition listed in different
            languages.
    """
    id: int = Field(description="The identifier for this resource.")
    name: str = Field(description="The name for this resource.")
    names: list["Name"] = Field(
        default_factory=list,
        description="The name of this encounter condition listed in different languages.")
    values: list["NamedAPIResource"] = Field(
        default_factory=list,
        description="A list of values for this encounter condition.")


class EncounterConditionValue(BaseModel):
    """
    An encounter condition value is a specific value for an encounter condition.

    Attributes:
        id (int): The identifier for this resource.
        name (str): The name for this resource.
        condition (NamedAPIResource): The condition this encounter condition value pertains to.
        names (list[Name]): The name of this encounter condition value listed in
            different languages.
    """
    id: int = Field(description="The identifier for this resource.")
    name: str = Field(description="The name for this resource.")
    condition: "NamedAPIResource" = Field(
        description="The condition this encounter condition value pertains to.")
    names: list["Name"] = Field(
        default_factory=list,
        description="The name of this resource listed in different languages.")
