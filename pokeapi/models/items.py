from __future__ import annotations
from pydantic import BaseModel, Field

from .common import (
    NamedAPIResource,
    APIResource,
    Name,
    Description,
    Effect,
    VerboseEffect,
    VersionGroupFlavorText,
    GenerationGameIndex,
    MachineVersionDetail,
)


class Item(BaseModel):
    """
    An item is an object in the games which the player can pick up, 
    keep in their bag, and use in some manner. They have various uses, 
    including healing, powering up, helping catch Pokémon, or to access a new area.

    Attributes:
        id
    """
    id: int = Field(description="The identifer for this resource")
    name: str = Field(description="The name for this resource.")
    cost: int = Field(description="The price of this item in stores.")
    fling_power: int = Field(
        description="The power of the move Fling when used with this item.")
    fling_effect: "NamedAPIResource" = Field(
        description="The effect of the move Fling when used with this item.")
    attributes: list["NamedAPIResource"] = Field(
        default_factory=list,
        description="A list of attributes this item has.")
    category: "NamedAPIResource" = Field(
        description="The category of items this item falls into.")
    effect_entries: list["VerboseEffect"] = Field(
        default_factory=list,
        description="The effect of this item listed in different languages.")
    flavor_text_entries: list["VersionGroupFlavorText"] = Field(
        default_factory=list,
        description="The flavor text of this item listed in different languages.")
    game_indices: list["GenerationGameIndex"] = Field(
        default_factory=list,
        description="A list of game indices relevant to this item by generation.")
    names: list["Name"] = Field(
        default_factory=list,
        description="The name of this item listed in different languages.")
    sprites: "ItemSprites" = Field(
        description="A set of sprites used to depict this item in the game.")
    held_by_pokemon: list["ItemHolderPokemon"] = Field(
        default_factory=list,
        description="A list of Pokémon that may be found holding this item.")
    baby_trigger_for: "APIResource" = Field(
        description="An evolution chain this item requires to produce a baby Pokémon.")
    machines: list["MachineVersionDetail"] = Field(
        default_factory=list,
        description="A list of the machines related to this item.")


class ItemSprites(BaseModel):
    """
    A set of sprites used to depict this item in the game.

    Attributes:
        default (str): The default depiction of this item.
    """
    default: str = Field(description="The default depiction of this item.")


class ItemHolderPokemon(BaseModel):
    """
    A Pokémon that may be found holding this item.

    Attributes:
        pokemon (NamedAPIResource): The Pokémon that holds this item.
        version_details (list[ItemHolderPokemonVersionDetail]): The details for the version that this item is held in by the Pokémon.
    """
    pokemon: "NamedAPIResource" = Field(
        description="The Pokémon that holds this item.")
    version_details: list["ItemHolderPokemonVersionDetail"] = Field(
        default_factory=list,
        description="The details for the version that this item is held in by the Pokémon.")


class ItemHolderPokemonVersionDetail(BaseModel):
    """
    The details for the version that this item is held in by the Pokémon.

    Attributes:
        rarity (int): How often this Pokémon holds this item in this version.
        version (NamedAPIResource): The version that this item is held in by the Pokémon.
    """
    rarity: int = Field(
        description="How often this Pokémon holds this item in this version.")
    version: "NamedAPIResource" = Field(
        description="The version that this item is held in by the pokemon.")


class ItemAttribute(BaseModel):
    """
    An item attribute is a characteristic of an item that affects how it is used in the game.

    Attributes:
        id (int): The identifier for this resource.
        name (str): The name for this resource.
        items (list[NamedAPIResource]): A list of items that have this attribute.
        names (list[Name]): The name of this item attribute listed in different languages.
        descriptions (list[Description]): The description of this item attribute listed in different languages.
    """
    id: int = Field(description="The identifier for this resource.")
    name: str = Field(description="The name for this resource.")
    items: list["NamedAPIResource"] = Field(
        default_factory=list,
        description="A list of items that have this attribute.")
    names: list["Name"] = Field(
        default_factory=list,
        description="The name of this item attribute listed in different languages.")
    descriptions: list["Description"] = Field(
        default_factory=list,
        description="The description of this item attribute listed in different languages.")


class ItemCategories(BaseModel):
    """
    An item category is a classification of items that share similar characteristics.

    Attributes:
        id (int): The identifier for this resource.
        name (str): The name for this resource.
        items (list[NamedAPIResource]): A list of items that are a part of this category.
        names (list[Name]): The name of this item category listed in different languages.
        pocket (NamedAPIResource): The pocket this item category is a part of.
    """
    id: int = Field(description="The identifier for this resource.")
    name: str = Field(description="The name for this resource.")
    items: list["NamedAPIResource"] = Field(default_factory=list,
                                            description="A list of items that are a part of this category.")
    names: list["Name"] = Field(
        default_factory=list,
        description="The name of this item category listed in different languages.")
    pocket: "NamedAPIResource" = Field(
        description="The pocket this item category is a part of.")


class ItemFlingEffects(BaseModel):
    """
    A fling effect is an effect that occurs when a Pokémon uses the move Fling with this item.

    Attributes:
        id (int): The identifier for this resource.
        name (str): The name for this resource.
        effect_entries (list[Effect]): The effect of this fling effect listed in different languages.
        items (list[NamedAPIResource]): A list of items that have this fling effect.
    """
    id: int = Field(description="The identifier for this resource.")
    name: str = Field(description="The name for this resource.")
    effect_entries: list["Effect"] = Field(
        default_factory=list,
        description="The effect of this fling effect listed in different languages.")
    items: list["NamedAPIResource"] = Field(
        default_factory=list,
        description="A list of items that have this fling effect.")


class ItemPocket(BaseModel):
    """
    An item pocket is a storage area for items in the player's bag.

    Attributes:
        id (int): The identifier for this resource.
        name (str): The name for this resource.
        categories (list[NamedAPIResource]): A list of item categories that are relevant to this item pocket.
        names (list[Name]): The name of this resource listed in different languages.
    """
    id: int = Field(description="The identifier for this resource.")
    name: str = Field(description="The name for this resource.")
    categories: list["NamedAPIResource"] = Field(
        default_factory=list,
        description="A list of item categories that are relevant to this item pocket.")
    names: list["Name"] = Field(
        default_factory=list,
        description="The name of this resource listed in different languages.")
