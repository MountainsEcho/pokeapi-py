from __future__ import annotations
from pydantic import BaseModel, Field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .common import NamedAPIResource, FlavorText, Effect


class ContestType(BaseModel):
    """
    A type of contest in which Pokémon can compete.

    Attributes:
        id (int): The identifier for this resource.
        name (str): The name for this resource.
        berry_flavors (list[NamedAPIResource]): The berry flavor that correlates with
            this contest type.
        names (list[ContestName]): The name of this contest type listed in different
            languages.
    """
    id: int = Field(description="The identifier for this resource.")
    name: str = Field(description="The name for this resource.")
    berry_flavors: list["NamedAPIResource"] = Field(
        default_factory=list,
        description="The berry flavor that correlates with this contest type.")
    names: list["ContestName"] = Field(
        default_factory=list,
        description="The name of this contest type listed in different languages.")


class ContestName(BaseModel):
    """
    A name for a contest.

    Attributes:
        name (str): The name for this contest.
        color (str): The color associated with this contest's name.
        language (NamedAPIResource): The language that this name is in.
    """
    name: str = Field(description="The name for this contest.")
    color: str = Field(
        description="The color associated with this contest's name.")
    language: "NamedAPIResource" = Field(
        description="The language that this name is in.")


class ContestEffect(BaseModel):
    """
    The effect of a contest move.

    Attributes:
        id (int): The identifier for this resource.
        appeal (int): The base number of hearts the user of this move gets.
        jam (int): The base number of hearts the user's opponent loses.
        effect_entries (list[Effect]): The result of this contest effect listed in
            different languages.
        flavor_text_entries (list[FlavorText]): The flavor text of this contest effect
            listed in different languages.
    """
    id: int = Field(
        description="The identifier for this resource.")
    appeal: int = Field(
        description="The base number of hearts the user of this move gets.")
    jam: int = Field(
        description="The base number of hearts the user's opponent loses.")
    effect_entries: list["Effect"] = Field(
        description="The result of this contest effect listed in different languages.")
    flavor_text_entries: list["FlavorText"] = Field(
        default_factory=list,
        description="The flavor text of this contest effect listed in different languages.")


class SuperContestEffect(BaseModel):
    """
    The effect of a super contest move.

    Attributes:
        id (int): The identifier for this resource.
        appeal (int): The level of appeal this super contest effect has.
        flavor_text_entries (list[FlavorText]): The flavor text of this super contest
            effect listed in different languages.
        moves (list[NamedAPIResource]): A list of moves that have the effect when used
            in super contests.
    """
    id: int = Field(description="The identifier for this resource.")
    appeal: int = Field(
        description="The level of appeal this super contest effect has.")
    flavor_text_entries: list["FlavorText"] = Field(
        default_factory=list,
        description="The flavor text of this super contest effect listed in different languages.")
    moves: list["NamedAPIResource"] = Field(
        default_factory=list,
        description="A list of moves that have the effect when used in super contests.")
