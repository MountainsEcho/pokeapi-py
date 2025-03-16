from __future__ import annotations
from pydantic import BaseModel, Field


class Type(BaseModel):
    """
    A type of Pokémon, which determines its strengths and weaknesses against other types.
    """
    id: int = Field(description="The identifier for this resource.")
    name: str = Field(description="The name for this resource.")
    damage_relations: "TypeRelations" = Field(
        description="The damage relations of this type.")
    past_damage_relations: list["TypePastRelations"] = \
        Field(default_factory=list,
              description="The past damage relations of this type.")
    game_indices: list["GenerationGameIndex"] = \
        Field(default_factory=list,
              description="The game indices of this type.")
    generation: "Generation" = \
        Field(description="The generation this type was introduced in.")
    names: list["Name"] = Field(
        default_factory=list,
        description="The name of this resource listed in different languages.")
    pokemon: list["TypePokemon"] = \
        Field(default_factory=list,
              description="A list of Pokémon that have this type.")
    moves: list["Move"] = \
        Field(default_factory=list,
              description="A list of moves that have this type.")
