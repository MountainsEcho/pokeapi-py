from __future__ import annotations
from pydantic import BaseModel, Field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .common import NamedAPIResource, Name


class EvolutionChains(BaseModel):
    """
    An evolution chain is a series of Pokémon that evolve from one to another.

    Attributes:
        id (int): The identifier for this resource.
        baby_trigger_item (NamedAPIResource): The item that a Pokémon would be holding when mating that would trigger the egg hatching a baby Pokémon rather than a basic Pokémon.
        chain (ChainLink): The base chain link object. Each link contains evolution details for a Pokémon in the chain. Each link references the next Pokémon in the natural evolution order.
    """
    id: int = Field(description="The identifier for this resource.")
    baby_trigger_item: NamedAPIResource = Field(
        description="The item that a Pokémon would be holding when mating that would trigger the egg hatching a baby Pokémon rather than a basic Pokémon.")
    chain: "ChainLink" = Field(
        description="The base chain link object. Each link contains evolution details for a Pokémon in the chain. Each link references the next Pokémon in the natural evolution order.")


class ChainLink(BaseModel):
    """
    A link in an evolution chain. Each link contains evolution details for a Pokémon in the chain. Each link references the next Pokémon in the natural evolution order.

    Attributes:
        species (NamedAPIResource): The Pokémon species at this point in the evolution chain.
        is_baby (bool): Whether this Pokémon is a baby Pokémon.
        evolution_details (list[EvolutionDetail]): The details of this Pokémon's evolution.
        evolves_to (list[ChainLink]): The next Pokémon in the evolution chain.
    """
    is_baby: bool = Field(
        description="Whether this Pokémon is a baby Pokémon.")
    species: "NamedAPIResource" = Field(
        description="The Pokémon species at this point in the evolution chain.")
    evolution_details: list["EvolutionDetail"] = Field(
        default_factory=list,
        description="All details regarding the specific details of the referenced Pokémon species evolution.")
    evolves_to: list["ChainLink"] = Field(
        default_factory=list,
        description="The next Pokémon in the evolution chain.")


class EvolutionDetail(BaseModel):
    """
    The details of a Pokémon's evolution.

    Attributes:
        trigger (NamedAPIResource): The trigger for this evolution.
    """
    item: "NamedAPIResource" = Field(
        description="The item required to cause evolution this into Pokémon species.")
    trigger: "NamedAPIResource" = Field(
        description="The type of event that triggers evolution into this Pokémon species.")
    gender: int = Field(
        description="The id of the gender of the evolving Pokémon species must be in order to evolve into this Pokémon species.")
    held_item: "NamedAPIResource" = Field(
        description="The item the evolving Pokémon species must be holding during the evolution trigger event to evolve into this Pokémon species.")
    known_move: "NamedAPIResource" = Field(
        description="The move that must be known by the evolving Pokémon species during the evolution trigger event in order to evolve into this Pokémon species.")
    known_move_type: "NamedAPIResource" = Field(
        description="The evolving Pokémon species must know a move with this type during the evolution trigger event in order to evolve into this Pokémon species.")
    location: "NamedAPIResource" = Field(
        description="The location the evolution must be triggered at.")
    min_level: int = Field(
        description="The minimum required level of the evolving Pokémon species to evolve into this Pokémon species.")
    min_happiness: int = Field(
        description="The minimum required level of happiness the evolving Pokémon species to evolve into this Pokémon species.")
    min_beauty: int = Field(
        description="The minimum required level of beauty the evolving Pokémon species to evolve into this Pokémon species.")
    min_affection: int = Field(
        description="The minimum required level of affection the evolving Pokémon species to evolve into this Pokémon species.")
    needs_overworld_rain: bool = Field(
        description="Whether or not it must be raining in the overworld to cause evolution this Pokémon species.")
    party_species: "NamedAPIResource" = Field(
        description="The Pokémon species that must be in the players party in order for the evolving Pokémon species to evolve into this Pokémon species.")
    party_type: "NamedAPIResource" = Field(
        description="The player must have a Pokémon of this type in their party during the evolution trigger event in order for the evolving Pokémon species to evolve into this Pokémon species.")
    relative_physical_stats: int = Field(
        description="The required relation between the Pokémon's Attack and Defense stats. 1 means Attack > Defense. 0 means Attack = Defense. -1 means Attack < Defense.")
    time_of_day: str = Field(
        description="The required time of day. Day or night.")
    trade_species: "NamedAPIResource" = Field(
        description="Pokémon species for which this one must be traded.")
    turn_upside_down: bool = Field(
        description="Whether or not the 3DS needs to be turned upside-down as this Pokémon levels up.")


class EvolutionTrigger(BaseModel):
    """
    """
    id: int = Field(description="The identifier for this resource.")
    name: str = Field(description="The name for this resource.")
    names: list["Name"] = Field(
        default_factory=list,
        description="The name of this resource listed in different languages.")
    pokemon_species: list["NamedAPIResource"] = Field(
        default_factory=list,
        description="A list of pokemon species that result from this evolution trigger.")
