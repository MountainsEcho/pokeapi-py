from __future__ import annotations
from pydantic import BaseModel, Field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .common import NamedAPIResource, Name, Description


class Generation(BaseModel):
    """
    A generation is a grouping of Pokémon games that were released together.
    Generations are used to determine which Pokémon are available in a given game,
    as well as which moves, abilities, and other features are available.

    Attributes:
        id (int): The identifier for this resource.
        name (str): The name for this resource.
        abilities (list[NamedAPIResource]): A list of abilities that were introduced in
            this generation.
        names (list[Name]): The name of this generation listed in different languages.
        main_region (NamedAPIResource): The main region of this generation.
        moves (list[NamedAPIResource]): A list of moves that were introduced in this
            generation.
        pokemon_species (list[NamedAPIResource]): A list of Pokémon species that were
            introduced in this generation.
        types (list[NamedAPIResource]): A list of types that were introduced in this
            generation.
        version_groups (list[NamedAPIResource]): A list of version groups that were
            introduced in this generation.
    """
    id: int = Field(description="The identifier for this resource.")
    name: str = Field(description="The name for this resource.")
    abilities: list["NamedAPIResource"] = Field(
        default_factory=list,
        description="A list of abilities that were introduced in this generation.",
    )
    names: list["Name"] = Field(
        default_factory=list,
        description="The name of this generation listed in different languages.",
    )
    main_region: NamedAPIResource = Field(
        description="The main region of this generation.",
    )
    moves: list["NamedAPIResource"] = Field(
        default_factory=list,
        description="A list of moves that were introduced in this generation.",
    )
    pokemon_species: list["NamedAPIResource"] = Field(
        default_factory=list,
        description="A list of Pokémon species that were introduced in this generation.",
    )
    types: list["NamedAPIResource"] = Field(
        default_factory=list,
        description="A list of types that were introduced in this generation.",
    )
    version_groups: list["NamedAPIResource"] = Field(
        default_factory=list,
        description="A list of version groups that were introduced in this generation.",
    )


class Pokedexes(BaseModel):
    """
    A Pokédex is a handheld electronic encyclopedia device; one which is capable of recording and retaining information of the various Pokémon in a given region with the exception of the national dex and some smaller dexes related to portions of a region. 

    Attributes:
        id (int): The identifier for this resource.
        name (str): The name for this resource.
        is_main_series (bool): Whether or not this Pokédex originated in the main series of the video games.
        descriptions (list[Description]): The description of this resource listed in different languages.
        names (list[Name]): The name of this resource listed in different languages.
        pokemon_entries (list[PokemonEntry]): A list of Pokémon catalogued in this Pokédex and their indexes.
        region (NamedAPIResource): The region this Pokédex catalogues Pokémon for.
        version_groups (list[NamedAPIResource]): A list of version groups this Pokédex is relevant to.
    """
    id: int = Field(description="The identifier for this resource.")
    name: str = Field(description="The name for this resource.")
    is_main_series: bool = Field(
        description="Whether or not this Pokédex originated in the main series of the video games.")
    descriptions: list["Description"] = Field(
        default_factory=list, description="The description of this resource listed in different languages.")
    names: list["Name"] = Field(
        default_factory=list, description="The name of this resource listed in different languages.")
    pokemon_entries: list["PokemonEntry"] = Field(
        default_factory=list, description="A list of Pokémon catalogued in this Pokédex and their indexes.")
    region: "NamedAPIResource" = Field(
        description="The region this Pokédex catalogues Pokémon for.")
    version_groups: list["NamedAPIResource"] = Field(
        default_factory=list, description="A list of version groups this Pokédex is relevant to.")


class PokemonEntry(BaseModel):
    """
    A Pokémon species entry in a Pokédex.

    Attributes:
        entry_number (int): The index of this Pokémon species entry within the Pokédex.
        pokemon_species (NamedAPIResource): The Pokémon species being encountered.
    """
    entry_number: int = Field(
        description="The index of this Pokémon species entry within the Pokédex.")
    pokemon_species: "NamedAPIResource" = Field(
        description="The Pokémon species being encountered.")


class Version(BaseModel):
    """
    Information about a specific version of a Pokémon game.

    Attributes:
        id (int): The identifier for this resource.
        name (str): The name for this resource.
        names (list[Name]): The name of this resource listed in different languages.
        version_group (NamedAPIResource): The version group this version belongs to.
    """
    id: int = Field(description="The identifier for this resource.")
    name: str = Field(description="The name for this resource.")
    names: list["Name"] = Field(
        default_factory=list,
        description="The name of this resource listed in different languages.",
    )
    version_group: "NamedAPIResource" = Field(
        description="The version group this version belongs to.")


class VersionGroup(BaseModel):
    """
    Version groups categorize highly similar versions of the games.


    """
    id: int = Field(description="The identifier for this resource.")
    name: str = Field(description="The name for this resource.")
    order: int = Field(
        description="Order for sorting. Almost by date of release, except similar versions are grouped together.")
    generation: "NamedAPIResource" = Field(
        description="The generation this version was introduced in.")
    move_learn_methods: list["NamedAPIResource"] = Field(
        default_factory=list,
        description="A list of methods in which Pokémon can learn moves in this version group.",
    )
    pokedexes: list["NamedAPIResource"] = Field(
        default_factory=list,
        description="A list of Pokédexes introduces in this version group.",
    )
    regions: list["NamedAPIResource"] = Field(
        default_factory=list,
        description="A list of regions that can be visited in this version group.",
    )
    versions: list["NamedAPIResource"] = Field(
        default_factory=list,
        description="A list of versions that can be played in this version group.",
    )
