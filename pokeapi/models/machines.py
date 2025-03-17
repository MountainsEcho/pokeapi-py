from __future__ import annotations
from pydantic import BaseModel, Field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .common import NamedAPIResource


class Machine(BaseModel):
    """
    A machine is a device that teaches a move to a Pokémon. Machines are used in
    Pokémon games to teach moves to Pokémon. Each machine has a unique identifier
    and can only be used once per Pokémon.

    Attributes:
        id (int): The identifier for this resource.
        item (NamedAPIResource): The TM or HM item that corresponds to this machine.
        move (NamedAPIResource): The move that is taught by this machine.
        version_group (NamedAPIResource): The version group that this machine applies to.
    """
    id: int = Field(description="The identifier for this resource.")
    item: "NamedAPIResource" = Field(
        description="The TM or HM item that corresponds to this machine.")
    move: "NamedAPIResource" = Field(
        description="The move that is taught by this machine.")
    version_group: "NamedAPIResource" = Field(
        description="The version group that this machine applies to.")
