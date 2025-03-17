from __future__ import annotations
from pydantic import BaseModel, Field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .common import NamedAPIResource, Name


class Berry(BaseModel):
    """
    A berry is a small fruit that can be used in various ways, 
    such as healing or enhancing the effects of moves.

    Attributes:
        id (int): The identifier for this resource.
        name (str): The name for this resource.
        growth_time (int): The time it takes for this berry to grow, in hours.
            Berry trees go through four of these growth stages before they
            can be harvested.
        max_harvest (int): The maximum number of berries that can be harvested
            from a single berry tree in Generation IV.
        natural_gift_power (int): The power of the natural gift move that can be
            obtained from this berry.
        size (int): The size of the berry, in millimeters.
        smoothness (int): The smoothness of the berry, which can affect its use
            in contests.
        soil_dryness (int): The dryness of the soil in which this berry grows.
        firmness (NamedAPIResource): The firmness of the berry.
        flavors (list[BerryFlavorMap]): A list of flavors and their intensities
            for this berry.
        item (NamedAPIResource): The item associated with this berry.
        natural_gift_type (NamedAPIResource): The type associated with the
            natural gift move for this berry.
    """
    id: int = Field(description="The identifier for this resource.")
    name: str = Field(description="The name for this resource.")
    growth_time: int = Field(
        description="Time it takes the tree to grow one stage, in hours. Berry trees go through four of these growth stages before they can be picked.")
    max_harvest: int = Field(
        description="The maximum number of these berries that can grow on one tree in Generation IV.")
    natural_gift_power: int = Field(
        description="The power of the move \"Natural Gift\" when used with this Berry.")
    size: int = Field(description="The size of this Berry, in millimeters.")
    smoothness: int = Field(
        description="The smoothness of this Berry, used in making Pokéblocks or Poffins.")
    soil_dryness: int = Field(
        description="The speed at which this Berry dries out the soil as it grows. A higher rate means the soil dries more quickly.")
    firmness: "NamedAPIResource" = Field(
        description="The firmness of this berry, used in making Pokéblocks or Poffins.")
    flavors: list["BerryFlavorMap"] = Field(
        default_factory=list, description="A list of references to each flavor a berry can have and the potency of each of those flavors in regard to this berry.")
    item: "NamedAPIResource" = Field(
        description="Berries are actually items. This is a reference to the item specific data for this berry.")
    natural_gift_type: "NamedAPIResource" = Field(
        description="The type inherited by \"Natural Gift\" when used with this Berry.")


class BerryFirmness(BaseModel):
    """
    The firmness of a berry determines how hard it is, 
    which can affect its use in cooking and other applications.

    Attributes:
        id (int): The identifier for this resource.
        name (str): The name for this resource.
        berries (list[NamedAPIResource]): A list of the berries with this firmness.
        names (list[Name]): The name of this resource listed in different languages.
    """
    id: int = Field(description="The identifier for this resource.")
    name: str = Field(description="The name for this resource.")
    berries: list["NamedAPIResource"] = Field(
        default_factory=list,
        description="A list of the berries with this firmness.")
    names: list["Name"] = Field(
        default_factory=list,
        description="The name of this resource listed in different languages.")


class BerryFlavor(BaseModel):
    """
    The flavor of a berry, which can affect its taste and effects.
    """
    id: int = Field(description="The identifier for this resource.")
    name: str = Field(description="The name for this resource.")
    berries: list["NamedAPIResource"] = Field(
        default_factory=list,
        description="A list of the berries with this flavor.")
    contest_type: "NamedAPIResource" = Field(
        description="The contest type that correlates with this berry flavor.")
    names: list["Name"] = Field(
        default_factory=list,
        description="The name of this resource listed in different languages.")


class BerryFlavorMap(BaseModel):
    """
    A mapping of berry flavors to their intensities.

    Attributes:
        potency (int): The intensity of the flavor for this berry.
        flavor (NamedAPIResource): The referenced berry flavor.
    """
    potency: int = Field(
        description="How powerful the referenced flavor is for this berry.")
    flavor: "NamedAPIResource" = Field(
        description="The berry with the referenced flavor.")
