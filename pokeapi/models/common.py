from __future__ import annotations
from pydantic import BaseModel, Field


class NamedAPIResource(BaseModel):
    """
    A generic resource with a name and URL, that will need to be queried
    for more details.

    Attributes:
        name (str): The name of the resource.
        url (str): The URL of the resource.
    """
    name: str = Field(description="The name of the resource.")
    url: str = Field(description="The URL of the resource.")


class NamedAPIResourceList(BaseModel):
    """
    A generic resource with a name and URL, that will need to be queried
    for more details.

    Attributes:
        name (str): The name of the resource.
        url (str): The URL of the resource.

    Example:
        ```
        {
            count: 541,
            next: "https://pokeapi.co/api/v2/evolution-chain?offset=20&limit=20",
            previous: null,
            results: [
                {
                    name: "stench",
                    url: "https://pokeapi.co/api/v2/evolution-chain/1/"
                }
            ]
        }
        ```
    """
    count: int = Field(
        description="The total number of resources available from this API."
    )
    next: str = Field(
        description="The URL for the next page in the list."
    )
    previous: str = Field(
        description="The URL for the previous page in the list."
    )
    results: list["NamedAPIResource"] = Field(
        default_factory=list,
        description="A list of named API resources."
    )


class APIResource(BaseModel):
    """
    A generic resource with a URL

    Attributes:
        url (str): The URL of the referenced resource.
    """
    url: str = Field(description="The URL of the referenced resource.")


class APIResourceList(BaseModel):
    """
    A generic resource with a URL

    Attributes:
        count (int): The total number of resources available from this API.
        next (str): The URL for the next page in the list.
        previous (str): The URL for the previous page in the list.
        results (list[APIResource]): A list of named API resources.

    Example:
        ```
        {
            count: 541,
            next: "https://pokeapi.co/api/v2/evolution-chain?offset=20&limit=20",
            previous: null,
            results: [
                {
                    url: "https://pokeapi.co/api/v2/evolution-chain/1/"
                }
            ]
        }
        ```
    """

    count: int = Field(
        description="The total number of resources available from this API."
    )
    next: str = Field(
        description="The URL for the next page in the list."
    )
    previous: str = Field(
        description="The URL for the previous page in the list."
    )
    results: list["APIResource"] = Field(
        default_factory=list,
        description="A list of named API resources."
    )


class Name(BaseModel):
    """
    A name of a resource in a specific language.
    Attributes:
        name (str): The name of the resource.
        language (NamedAPIResource): The language this name is in.
    """
    name: str = Field(description="The name for this resource.")
    language: "NamedAPIResource" = Field(
        description="The language this name is in.")


class FlavorText(BaseModel):
    """
    A name of a resource in a specific language.

    Attributes:
        flavor_text (str): The localized flavor text for an API resource in a specific language.
        language (NamedAPIResource): The language this name is in.
        version (NamedAPIResource): The game version this flavor text is extracted from.
    """
    flavor_text: str = Field(
        description="The localized flavor text for an API resource in a specific language. Note that this text is left unprocessed as it is found in game files. This means that it contains special characters that one might want to replace with their visible decodable version. Please check out this issue to find out more."
    )
    language: "NamedAPIResource" = Field(
        description="The language this name is in.")
    version: "NamedAPIResource" = Field(
        description="The game version this flavor text is extracted from.")


class Effect(BaseModel):
    """
    A name of a resource in a specific language.

    Attributes:
        effect (str): The localized effect text for an API resource in a specific language.
        language (NamedAPIResource): The language this name is in.
    """
    effect: str = Field(
        description="The localized effect text for an API resource in a specific language.")
    language: "NamedAPIResource" = Field(
        description="The language this name is in.")


class Description(BaseModel):
    """
    A name of a resource in a specific language.

    Attributes:
        description (str): The localized description for an API resource in a specific language.
        language (NamedAPIResource): The language this name is in.
    """
    description: str = Field(
        description="The localized description for an API resource in a specific language."
    )
    language: "NamedAPIResource" = Field(
        description="The language this name is in.")


class VerboseEffect(BaseModel):
    """
    A name of a resource in a specific language.

    Attributes:
        effect (str): The localized effect text for an API resource in a specific language.
        short_effect (str): The localized effect text in brief.
        language (NamedAPIResource): The language this name is in.
    """
    effect: str = Field(
        description="The localized effect text for an API resource in a specific language."
    )
    short_effect: str = Field(
        description="The localized effect text in brief."
    )
    language: "NamedAPIResource" = Field(
        description="The language this effect is in.")


class VersionGroupFlavorText(BaseModel):
    """
    A name of a resource in a specific language.

    Attributes:
        text (str): The localized flavor text for an API resource in a specific language.
        language (NamedAPIResource): The language this name is in.
        version_group (NamedAPIResource): The version group this flavor text is extracted from.
    """
    text: str = Field(
        description="The localized flavor text for an API resource in a specific language."
    )
    language: "NamedAPIResource" = Field(
        description="The language this name is in.")
    version_group: "NamedAPIResource" = Field(
        description="The version group this flavor text is extracted from.")


class GenerationGameIndex(BaseModel):
    """
    A name of a resource in a specific language.

    Attributes:
        game_index (int): The internal id of an API resource within game data.
        generation (NamedAPIResource): The generation relevent to this game index.
    """
    game_index: int = Field(
        description="The internal id of an API resource within game data."
    )
    generation: "NamedAPIResource" = Field(
        description="The generation relevent to this game index."
    )


class MachineVersionDetail(BaseModel):
    """
    A machine version detail.

    Attributes:
        machine (APIResource): The machine that teaches a move from an item.
        version_group (NamedAPIResource): The version group of this specific machine.
    """
    machine: "APIResource" = Field(
        description="The machine that teaches a move from an item.")
    version_group: "NamedAPIResource" = Field(
        description="The version group of this specific machine.")


class VersionDetailEncounter(BaseModel):
    """"""
    version: NamedAPIResource = Field(
        description="The game version this encounter happens in."
    )
    max_chance: int = Field(
        description="The total percentage of all encounter potential.")
    encounter_details: list["Encounter"] = Field(
        default_factory=list,
        description="A list of encounters and their specifics."
    )


class Encounter(BaseModel):
    """
    A Pokémon encounter.

    Attributes:
        min_level (int): The lowest level the Pokémon could be encountered at.
        max_level (int): The highest level the Pokémon could be encountered at.
        condition_values (list[NamedAPIResource]): A list of condition values that must be in effect for this encounter to occur.
        chance (int): The chance of this encounter occurring.
        method (NamedAPIResource): The method by which this encounter happens.
    """
    min_level: int = Field(
        description="The lowest level the Pokémon could be encountered at."
    )
    max_level: int = Field(
        description="The highest level the Pokémon could be encountered at."
    )
    condition_values: list["NamedAPIResource"] = Field(
        default_factory=list,
        description="A list of condition values that must be in effect for this encounter to occur."
    )
    chance: int = Field(
        description="The chance of this encounter occurring."
    )
    method: "NamedAPIResource" = Field(
        description="The method by which this encounter happens."
    )


class VersionGameIndex(BaseModel):
    game_index: int = Field(
        description="The internal id of an API resource within game data."
    )
    version: "NamedAPIResource" = Field(
        description="The version relevent to this game index."
    )
