from __future__ import annotations
from pydantic import BaseModel, Field

from .common import (
    NamedAPIResource,
    APIResource,
    Name,
    VerboseEffect,
    MachineVersionDetail
)
from .pokemon import AbilityEffectChange


class Move(BaseModel):
    """"""
    id: int = Field(description="The identifier for this resource.")
    name: str = Field(description="The name for this resource.")
    accuracy: int = Field(
        description="The percent value of how likely this move is to be successful.")
    effect_chance: int = Field(
        description="The percent value of how likely it is this moves effect will happen.")
    pp: int = Field(
        description="Power points. The number of times this move can be used.")
    priority: int = Field(
        description="A value between -8 and 8. Sets the order in which moves are executed during battle. See Bulbapedia for greater detail.")
    power: int = Field(
        description="The base power of this move with a value of 0 if it does not have a base power.")
    contest_combos: "ContestComboSets" = Field(
        description="A detail of normal and super contest combos that require this move.")
    contest_type: "NamedAPIResource" = Field(
        description="The type of appeal this move gives a Pokémon when used in a contest.")
    contest_effect: "APIResource" = Field(
        description="The effect the move has when used in a contest.")
    damage_class: "NamedAPIResource" = Field(
        description="The type of damage the move inflicts on the target.")
    effect_entries: list["VerboseEffect"] = Field(
        default_factory=list,
        description="The effect of this move listed in different languages.",
    )
    effect_changes: list["AbilityEffectChange"] = Field(
        default_factory=list,
        description="The list of previous effects this move has had across version groups of the games.",
    )
    learned_by_pokemon: list["NamedAPIResource"] = Field(
        default_factory=list,
        description="A list of Pokémon that can learn this move.",
    )
    flavor_text_entries: list["MoveFlavorText"] = Field(
        default_factory=list,
        description="The flavor text of this move listed in different languages.",
    )
    generation: "NamedAPIResource" = Field(
        description="The generation in which this move was introduced.",
    )
    machines: list["MachineVersionDetail"] = Field(
        default_factory=list,
        description="A list of the machines that teach this move.",
    )
    meta: "MoveMetaData" = Field(
        description="Metadata about this move.",
    )
    names: list["Name"] = Field(
        default_factory=list,
        description="The name of this resource listed in different languages.",
    )
    past_values: list["PastMoveStatValues"] = Field(
        default_factory=list,
        description="A list of move resource value changes across version groups of the game.",
    )
    stat_changes: list["MoveStatChange"] = Field(
        default_factory=list,
        description="A list of stats this moves effects and how much it effects them.",
    )
    super_contest_effect: "APIResource" = Field(
        description="The effect the move has when used in a super contest.",
    )
    target: "NamedAPIResource" = Field(
        description="The type of target that will receive the effects of the attack.",
    )
    type: "NamedAPIResource" = Field(
        description="The type of damage the move inflicts on the target.",
    )


class ContestComboSets(BaseModel):
    """"""
    normal: "ContestComboDetail" = Field(
        description="A detail of moves this move can be used before or after, granting additional appeal points in contests."
    )
    super: "ContestComboDetail" = Field(
        description="A detail of moves this move can be used before or after, granting additional appeal points in super contests."
    )


class ContestComboDetail(BaseModel):
    """"""
    use_before: list["NamedAPIResource"] = Field(
        description="A list of moves to use before this move.")
    use_after: list["NamedAPIResource"] = Field(
        description="A list of moves to use after this move.")


class MoveFlavorText(BaseModel):
    """"""
    flavor_text: str = Field(
        description="The localized flavor text for an api resource in a specific language."
    )
    language: "NamedAPIResource" = Field(
        description="The language this name is in."
    )
    version_group: "NamedAPIResource" = Field(
        description="The version group that uses this flavor text."
    )


class MoveMetaData(BaseModel):
    """"""
    ailment: "NamedAPIResource" = Field(
        description="The status ailment this move inflicts on its target."
    )
    category: "NamedAPIResource" = Field(
        description="The category of move this move falls under, e.g. damage or ailment."
    )
    min_hits: int = Field(
        description="The minimum number of times this move hits."
    )
    max_hits: int = Field(
        description="The maximum number of times this move hits. Null if it always only hits once."
    )
    min_turns: int = Field(
        description="The minimum number of turns this move continues to take effect. Null if it always only lasts one turn."
    )
    max_turns: int = Field(
        description="The maximum number of turns this move continues to take effect. Null if it always only lasts one turn."
    )
    drain: int = Field(
        description="HP drain (if positive) or Recoil damage (if negative), in percent of damage done."
    )
    healing: int = Field(
        description="The amount of hp gained by the attacking Pokemon, in percent of it's maximum HP.")
    crit_rate: int = Field(
        description="Critical hit rate bonus."
    )
    ailment_chance: int = Field(
        description="The likelihood this attack will cause an ailment.")
    flinch_chance: int = Field(
        description="The likelihood this attack will cause the target Pokémon to flinch.")
    stat_chance: int = Field(
        description="The likelihood this attack will cause a stat change in the target Pokémon.")


class MoveStatChange(BaseModel):
    """"""
    change: int = Field(description="The amount of change.")
    stat: "NamedAPIResource" = Field(description="The stat being affected.")


class PastMoveStatValues(BaseModel):
    """"""
    accuracy: int = Field(
        description="The percent value of how likely this move is to be successful."
    )
    effect_chance: int = Field(
        description="The percent value of how likely it is this moves effect will take effect."
    )
    power: int = Field(
        description="The base power of this move with a value of 0 if it does not have a base power."
    )
    pp: int = Field(
        description="Power points. The number of times this move can be used."
    )
    effect_entries: list["VerboseEffect"] = Field(
        default_factory=list,
        description="The effect of this move listed in different languages.",
    )
    type: "NamedAPIResource" = Field(
        description="The type of damage the move inflicts on the target."
    )
    version_group: "NamedAPIResource" = Field(
        description="The version group in which these move stat values were in effect."
    )
