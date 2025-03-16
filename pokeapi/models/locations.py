from __future__ import annotations
from pydantic import BaseModel, Field

from .common import (
    NamedAPIResource,
    Name,
    GenerationGameIndex,
    VersionDetailEncounter,
)


class Location(BaseModel):
    """
    A location is a place where Pokémon can be found in the wild. It is used to
    determine which Pokémon can be encountered in a specific area of a location.
    Locations are also used to determine which Pokémon can be encountered in a
    specific area of a location area.

    Attributes:
        id (int): The identifier for this resource.
        name (str): The name for this resource.
        region (NamedAPIResource): The region this location can be found in.
        names (list[Name]): The name of this resource listed in different languages.
        game_indices (list[GenerationGameIndex]): A list of game indices relevent to this location by generation.
        areas (list[NamedAPIResource]): A list of location areas in this location.
    """
    id: int = Field(description="The identifier for this resource.")
    name: str = Field(description="The name for this resource.")
    region: "NamedAPIResource" = Field(
        description="The region this location can be found in.",
    )
    names: list["Name"] = Field(
        default_factory=list,
        description="The name of this resource listed in different languages.",
    )
    game_indices: list["GenerationGameIndex"] = Field(
        default_factory=list,
        description="A list of game indices relevent to this location by generation.",
    )
    areas: list["NamedAPIResource"] = Field(
        default_factory=list,
        description="A list of location areas in this location.",
    )


class LocationArea(BaseModel):
    """
    A location area is a specific area within a location where Pokémon can be
    encountered. It is used to determine which Pokémon can be encountered in a
    specific area of a location.

    Attributes:
        id (int): The identifier for this resource.
        name (str): The name for this resource.
        game_index (int): The internal id of an API resource within game data.
        encounter_method_rates (list[EncounterMethodRate]): A list of methods in which Pokémon may be encountered in this area and how likely the method will occur depending on the version of the game.
        location (NamedAPIResource): The location this location area can be found in.
        names (list[Name]): The name of this resource listed in different languages.
        pokemon_encounters (list[PokemonEncounter]): A list of Pokémon that can be encountered in this area.
    """
    id: int = Field(description="The identifier for this resource.")
    name: str = Field(description="The name for this resource.")
    game_index: int = Field(
        description="The internal id of an API resource within game data.")
    encounter_method_rates: list["EncounterMethodRate"] = Field(
        default_factory=list,
        description="A list of methods in which Pokémon may be encountered in this area "
                    "and how likely the method will occur depending on the version of the game.",
    )
    location: "NamedAPIResource" = Field(
        description="The location this location area can be found in.",
    )
    names: list["Name"] = Field(
        default_factory=list,
        description="The name of this resource listed in different languages.",
    )
    pokemon_encounters: list["PokemonEncounter"] = Field(
        default_factory=list,
        description="A list of Pokémon that can be encountered in this area.",
    )


class EncounterMethodRate(BaseModel):
    """
    A method in which Pokémon may be encountered in a location area and how likely
    the method will occur depending on the version of the game.

    Attributes:
        encounter_method (NamedAPIResource): The method in which Pokémon may be encountered in this area.
        version_details (list[EncounterVersionDetails]): A list of version details for this encounter method.
    """
    encounter_method: "NamedAPIResource" = Field(
        description="The method in which Pokémon may be encountered in this area.",
    )
    version_details: list["EncounterVersionDetails"] = Field(
        default_factory=list,
        description="A list of version details for this encounter method.",
    )


class EncounterVersionDetails(BaseModel):
    """
    A list of version details for an encounter method.

    Attributes:
        rate (int): The chance of an encounter to occur.
        version (NamedAPIResource): The version of the game in which the encounter can occur with the given chance.
    """
    rate: int = Field(
        description="The chance of an encounter to occur.",
    )
    version: "NamedAPIResource" = Field(
        description="The version of the game in which the encounter can occur with the given chance.",
    )


class PokemonEncounter(BaseModel):
    """
    A Pokémon that can be encountered in a location area.

    Attributes:
        pokemon (NamedAPIResource): The Pokémon being encountered.
        version_details (list[VersionDetailEncounter]): A list of versions and encounters with Pokémon that might happen in the referenced location area.
    """
    pokemon: "NamedAPIResource" = Field(
        description="The Pokémon being encountered.")
    version_details: list["VersionDetailEncounter"] = Field(
        default_factory=list,
        description="A list of versions and encounters with Pokémon that might happen in the referenced location area.",
    )


class PalParkArea(BaseModel):
    """
    A pal park area is a specific area within a pal park where Pokémon can be
    encountered. It is used to determine which Pokémon can be encountered in a
    specific area of a pal park.

    Attributes:
        id (int): The identifier for this resource.
        name (str): The name for this resource.
        names (list[Name]): The name of this resource listed in different languages.
        pokemon_encounters (list[PalParkEncounterSpecies]): A list of Pokémon encountered in this pal park area along with details.
    """
    id: int = Field(
        description="The identifier for this resource.",
    )
    name: str = Field(description="The name for this resource.")
    names: list["Name"] = Field(
        default_factory=list,
        description="The name of this resource listed in different languages.")
    pokemon_encounters: list["PalParkEncounterSpecies"] = Field(
        default_factory=list,
        description="A list of Pokémon encountered in this pal park area along with details.",
    )


class PalParkEncounterSpecies(BaseModel):
    """
    A Pokémon species encountered in a pal park area along with details.

    Attributes:
        base_score (int): The base score given to the player when this Pokémon is caught during a pal park run.
        rate (int): The base rate for encountering this Pokémon in this pal park area.
        pokemon_species (NamedAPIResource): The Pokémon species being encountered.
    """
    base_score: int = Field(
        description="The base score given to the player when this Pokémon is caught during a pal park run.",
    )
    rate: int = Field(
        description="The base rate for encountering this Pokémon in this pal park area.",
    )
    pokemon_species: "NamedAPIResource" = Field(
        description="The Pokémon species being encountered.")


class Regions(BaseModel):
    """
    A region is a geographical area in the Pokémon world. It is used to determine
    which Pokémon can be encountered in a specific area of a location. Regions are
    also used to determine which Pokémon can be encountered in a specific area of a
    location area.

    Attributes:
        id (int): The identifier for this resource.
        name (str): The name for this resource.
        locations (list[NamedAPIResource]): A list of locations that can be found in this region.
        names (list[Name]): The name of this resource listed in different languages.
        main_generation (NamedAPIResource): The main generation of this region.
        pokedexes (list[NamedAPIResource]): A list of pokédexes that catalogue Pokémon in this region.
        version_groups (list[NamedAPIResource]): A list of version groups where this region can be visited.
    """
    id: int = Field(description="The identifier for this resource.")
    locations: list["NamedAPIResource"] = Field(
        default_factory=list,
        description="A list of locations that can be found in this region.",
    )
    name: str = Field(description="The name for this resource.")
    names: list["Name"] = Field(
        default_factory=list,
        description="The name of this resource listed in different languages.",
    )
    main_generation: "NamedAPIResource" = Field(
        description="The main generation of this region.",
    )
    pokedexes: list["NamedAPIResource"] = Field(
        default_factory=list,
        description="A list of pokédexes that catalogue Pokémon in this region.",
    )
    version_groups: list["NamedAPIResource"] = Field(
        default_factory=list,
        description="A list of version groups where this region can be visited.",
    )
