from __future__ import annotations
from pydantic import BaseModel, Field
import importlib
from typing import TYPE_CHECKING

from .common import (
    NamedAPIResource,
    APIResource,
    Name,
    VerboseEffect,
    Effect,
    Description,
    FlavorText,
    VersionDetailEncounter,
    VersionGameIndex,
    GenerationGameIndex,
)

# needed to avoid circular imports
if TYPE_CHECKING:
    from .games import Generation
    from .moves import Move


def _get_generation() -> "Generation":
    """
    Get the Generation model class. Needed to avoid circular imports.
    """
    games = importlib.import_module("pokeapi.models.games")
    return games.Generation


def _get_move() -> "Move":
    """
    Get the Move model class. Needed to avoid circular imports.
    """
    moves = importlib.import_module("pokeapi.models.moves")
    return moves.Move


class Ability(BaseModel):
    """"""
    id: int = Field(description="The identifier for this resource.")
    name: str = Field(description="The name for this resource.")
    is_main_series: bool = Field(
        description="Whether or not this ability originated in the main series of the video games."
    )
    generation: "NamedAPIResource" = Field(
        description="The generation this ability originated in.")
    names: list["Name"] = Field(
        default_factory=list,
        description="The name of this resource listed in different languages."
    )
    effect_entries: list["VerboseEffect"] = Field(
        default_factory=list,
        description="The effect of this ability listed in different languages."
    )
    effect_changes: list["AbilityEffectChange"] = Field(
        default_factory=list,
        description="The list of previous effects this ability has had across version groups."
    )
    flavor_text_entries: list["AbilityFlavorText"] = Field(
        default_factory=list,
        description="The flavor text of this ability listed in different languages."
    )
    pokemon: list["AbilityPokemon"] = Field(
        default_factory=list,
        description="A list of Pokémon that have this ability."
    )


class AbilityEffectChange(BaseModel):
    """"""
    effect_entries: list["Effect"] = Field(
        default_factory=list,
        description="The effect of this ability listed in different languages."
    )
    version_group: "NamedAPIResource" = Field(
        description="The version group in which the effect is found."
    )


class AbilityFlavorText(BaseModel):
    """"""
    flavor_text: str = Field(
        description="The localized flavor text for an API resource in a specific language."
    )
    language: "NamedAPIResource" = Field(
        description="The language this text resource is in."
    )
    version_group: "NamedAPIResource" = Field(
        description="The version group this flavor text was extracted from."
    )


class AbilityPokemon(BaseModel):
    """"""
    is_hidden: bool = Field(
        description="Whether or not this is a hidden ability for the referenced Pokémon."
    )
    slot: int = Field(
        description="The slot this ability occupies in the Pokémon referenced."
    )
    pokemon: "NamedAPIResource" = Field(
        description="The Pokémon this ability could belong to."
    )


class Characteristic(BaseModel):
    """"""
    id: int = Field(description="The identifier for this resource.")
    gene_modulo: int = Field(
        description="The remainder of the highest stat/IV divided by 5."
    )
    possible_values: list[int] = Field(
        default_factory=list,
        description="The possible values of the highest stat that would result in a Pokémon recieving this characteristic when divided by 5."
    )
    highest_stat: "NamedAPIResource" = Field(
        description="The highest stat that can be affected by this characteristic."
    )
    descriptions: list["Description"] = Field(
        default_factory=list,
        description="The descriptions of this characteristic listed in different languages."
    )


class EggGroup(BaseModel):
    """"""
    id: int = Field(description="The identifier for this resource.")
    name: str = Field(description="The name for this resource.")
    names: list["Name"] = Field(
        default_factory=list,
        description="The name of this resource listed in different languages."
    )
    pokemon_species: list["NamedAPIResource"] = Field(
        default_factory=list,
        description="The name of this resource listed in different languages."
    )


class Gender(BaseModel):
    """"""
    id: int = Field(description="The identifier for this resource.")
    name: str = Field(description="The name for this resource.")
    pokemon_species_details: list["PokemonSpeciesGender"] = Field(
        default_factory=list,
        description="A list of Pokémon species that can be this gender and how likely it is that they will be."
    )
    required_for_evolution: list["NamedAPIResource"] = Field(
        default_factory=list,
        description="A list of Pokémon species that required this gender in order for a Pokémon to evolve into them."
    )


class PokemonSpeciesGender(BaseModel):
    """"""
    rate: int = Field(
        description="The chance of this Pokémon being female, in eighths; or -1 for genderless."
    )
    pokemon_species: "NamedAPIResource" = Field(
        description="A Pokémon species that can be the referenced gender."
    )


class GrowthRate(BaseModel):
    id: int = Field(description="The identifier for this resource.")
    name: str = Field(description="The name for this resource.")
    formula: str = Field(
        description="The formula used to calculate the rate at which the Pokémon species gains level."
    )
    descriptions: list["Description"] = Field(
        default_factory=list,
        description="The descriptions of this characteristic listed in different languages."
    )
    levels: list["GrowthRateExperienceLevel"] = Field(
        default_factory=list,
        description="A list of levels and the amount of experienced needed to atain them based on this growth rate."
    )
    pokemon_species: list["NamedAPIResource"] = Field(
        default_factory=list,
        description="A list of Pokémon species that gain levels at this growth rate."
    )


class GrowthRateExperienceLevel(BaseModel):
    """"""
    level: int = Field(
        description="The level gained."
    )
    experience: int = Field(
        description="The amount of experience required to reach the referenced level."
    )


class Nature(BaseModel):
    """"""
    id: int = Field(description="The identifier for this resource.")
    name: str = Field(description="The name for this resource.")
    decreased_stat: "NamedAPIResource" = Field(
        description="The stat decreased by 10% in Pokémon with this nature."
    )
    increased_stat: "NamedAPIResource" = Field(
        description="The stat increased by 10% in Pokémon with this nature."
    )
    hates_flavor: "NamedAPIResource" = Field(
        description="The flavor hated by Pokémon with this nature."
    )
    likes_flavor: "NamedAPIResource" = Field(
        description="The flavor liked by Pokémon with this nature."
    )
    pokeathlon_stat_changes: list["NatureStatChange"] = Field(
        default_factory=list,
        description="A list of Pokéathlon stats this nature effects and how much it effects them."
    )
    move_battle_style_preferences: list["MoveBattleStylePreference"] = Field(
        default_factory=list,
        description="A list of battle styles and how likely a Pokémon with this nature is to use them in the Battle Palace or Battle Tent."
    )
    names: list["Name"] = Field(
        default_factory=list,
        description="The name of this resource listed in different languages."
    )


class NatureStatChange(BaseModel):
    """"""
    max_change: int = Field(
        description="The maximum amount of change."
    )
    pokeathlon_stat: "NamedAPIResource" = Field(
        description="The stat being affected."
    )


class MoveBattleStylePreference(BaseModel):
    """"""
    low_hp_preference: int = Field(
        description="Chance of using the move, in percent, if HP is under one half."
    )
    high_hp_preference: int = Field(
        description="Chance of using the move, in percent, if HP is over one half."
    )
    move_battle_style: "NamedAPIResource" = Field(
        description="The move battle style being referenced."
    )


class PokeathlonStat(BaseModel):
    id: int = Field(description="The identifier for this resource.")
    name: str = Field(description="The name for this resource.")
    names: list["Name"] = Field(
        default_factory=list,
        description="The name of this resource listed in different languages."
    )
    affecting_natures: "NaturePokeathlonStatAffectSets" = Field(
        description="A list of natures which affect this Pokéathlon stat positively or negatively."
    )


class NaturePokeathlonStatAffectSets(BaseModel):
    """"""
    increase: list["NaturePokeathlonStatAffect"] = Field(
        default_factory=list,
        description="A list of natures which affect this Pokéathlon stat positively."
    )
    decrease: list["NaturePokeathlonStatAffect"] = Field(
        default_factory=list,
        description="A list of natures which affect this Pokéathlon stat negatively."
    )


class NaturePokeathlonStatAffect(BaseModel):
    """"""
    max_change: int = Field(
        description="The maximum amount of change."
    )
    nature: "NamedAPIResource" = Field(
        description="The nature being referenced."
    )


class Pokemon(BaseModel):
    id: int = Field(description="The identifier for this resource.")
    name: str = Field(description="The name for this resource.")
    base_experience: int = Field(
        description="The base experience gained for defeating this Pokémon."
    )
    height: int = Field(
        description="The height of this Pokémon in decimetres."
    )
    is_default: bool = Field(
        description="Set for exactly one Pokémon used as the default for each species."
    )
    order: int = Field(
        description="Order for sorting. Almost national order, except families are grouped together."
    )
    weight: int = Field(
        description="The weight of this Pokémon in hectograms."
    )
    abilities: list["PokemonAbility"] = Field(
        default_factory=list,
        description="A list of abilities this Pokémon could potentially have."
    )
    forms: list["NamedAPIResource"] = Field(
        default_factory=list,
        description="A list of forms this Pokémon can take on."
    )
    game_indices: list["VersionGameIndex"] = Field(
        default_factory=list,
        description="A list of game indices relevent to Pokémon species by generation."
    )
    held_items: list["PokemonHeldItem"] = Field(
        default_factory=list,
        description="A list of items this Pokémon may be holding when encountered."
    )
    location_area_encounters: str = Field(
        description="A link to a list of location areas, as well as encounter details pertaining to specific versions."
    )
    moves: list["PokemonMove"] = Field(
        default_factory=list,
        description="A list of moves along with learn methods and level details pertaining to specific version groups."
    )
    past_types: list["PokemonTypePast"] = Field(
        default_factory=list,
        description="A list of details showing types this Pokémon had in previous generations."
    )
    sprites: "PokemonSprites" = Field(
        description="A set of sprites used to depict this Pokémon in the game. A visual representation of the various sprites can be found at PokeAPI/sprites"
    )
    cries: "PokemonCries" = Field(
        description="A set of cries used to depict this Pokémon in the game. A visual representation of the various cries can be found at PokeAPI/cries"
    )
    species: "NamedAPIResource" = Field(
        description="The species this Pokémon belongs to."
    )
    stats: list["PokemonStat"] = Field(
        default_factory=list,
        description="A list of base stat values for this Pokémon."
    )
    types: list["PokemonType"] = Field(
        default_factory=list,
        description="A list of details showing types this Pokémon has."
    )


class PokemonAbility(BaseModel):
    is_hidden: bool = Field(
        description="Whether or not this is a hidden ability."
    )
    slot: int = Field(
        description="The slot this ability occupies in this Pokémon species."
    )
    ability: "NamedAPIResource" = Field(
        description="The ability the Pokémon may have."
    )


class PokemonType(BaseModel):
    slot: int = Field(
        description="The order the Pokémon's types are listed in."
    )
    type: "NamedAPIResource" = Field(
        description="The type the Pokémon is."
    )


class PokemonFormType(BaseModel):
    slot: int = Field(
        description="The order the referenced types are listed in."
    )
    type: "NamedAPIResource" = Field(
        description="The type the referenced form is."
    )


class PokemonTypePast(BaseModel):
    generation: "NamedAPIResource" = Field(
        description="The generation in which the referenced pokémon had the listed types."
    )
    types: list["NamedAPIResource"] = Field(
        default_factory=list,
        description="The types the referenced pokémon had in the listed generation."
    )


class PokemonHeldItem(BaseModel):
    item: "NamedAPIResource" = Field(
        description="The item the referenced Pokémon holds."
    )
    version_details: list["PokemonHeldItemVersion"] = Field(
        default_factory=list,
        description="The details of the different versions in which the item is held."
    )


class PokemonHeldItemVersion(BaseModel):
    version: "NamedAPIResource" = Field(
        description="The version in which the item is held."
    )
    rarity: int = Field(
        description="How often the item is held."
    )


class PokemonMove(BaseModel):
    move: "NamedAPIResource" = Field(
        description="The move the Pokémon can learn."
    )
    version_group_details: list["PokemonMoveVersion"] = Field(
        default_factory=list,
        description="The details of the version group in which the Pokémon can learn the move."
    )


class PokemonMoveVersion(BaseModel):
    move_learn_method: "NamedAPIResource" = Field(
        description="The method by which the Pokémon can learn the move."
    )
    version_group: "NamedAPIResource" = Field(
        description="The version group in which the Pokémon can learn the move."
    )
    level_learned_at: int = Field(
        description="The minimum level to learn the move."
    )


class PokemonStat(BaseModel):
    stat: "NamedAPIResource" = Field(
        description="The stat the Pokémon has."
    )
    effort: int = Field(
        description="The effort points (EV) the Pokémon has in the stat."
    )
    base_stat: int = Field(
        description="The base value of the stat."
    )


class PokemonSprites(BaseModel):
    front_default: str = Field(
        description="The default depiction of this Pokémon from the front in battle."
    )
    front_shiny: str = Field(
        description="The shiny depiction of this Pokémon from the front in battle."
    )
    front_female: str = Field(
        description="The female depiction of this Pokémon from the front in battle."
    )
    front_shiny_female: str = Field(
        description="The shiny female depiction of this Pokémon from the front in battle."
    )
    back_default: str = Field(
        description="The default depiction of this Pokémon from the back in battle."
    )
    back_shiny: str = Field(
        description="The shiny depiction of this Pokémon from the back in battle."
    )
    back_female: str = Field(
        description="The female depiction of this Pokémon from the back in battle."
    )
    back_shiny_female: str = Field(
        description="The shiny female depiction of this Pokémon from the back in battle."
    )


class PokemonCries(BaseModel):
    latest: str = Field(
        description="The latest depiction of this Pokémon's cry."
    )
    legacy: str = Field(
        description="The legacy depiction of this Pokémon's cry."
    )


class LocationAreaEncounter(BaseModel):
    location_area: "NamedAPIResource" = Field(
        description="The location area the referenced Pokémon can be encountered in."
    )
    version_details: list["VersionDetailEncounter"] = Field(
        default_factory=list,
        description="A list of version details for this encounter method."
    )


class PokemonColor(BaseModel):
    id: int = Field(description="The identifier for this resource.")
    name: str = Field(description="The name for this resource.")
    names: list["Name"] = Field(
        default_factory=list,
        description="The name of this resource listed in different languages."
    )
    pokemon_species: list["NamedAPIResource"] = Field(
        default_factory=list,
        description="The name of this resource listed in different languages."
    )


class PokemonForm(BaseModel):
    id: int = Field(description="The identifier for this resource.")
    name: str = Field(description="The name for this resource.")
    order: int = Field(
        description="The order in which forms should be sorted within all forms. Multiple forms may have equal order, in which case they should fall back on sorting by name."
    )
    form_order: int = Field(
        description="The order in which forms should be sorted within a species' forms."
    )
    is_default: bool = Field(
        description="True for exactly one form used as the default for each Pokémon."
    )
    is_battle_only: bool = Field(
        description="Whether or not this form can only happen during battle."
    )
    is_mega: bool = Field(
        description="Whether or not this form requires mega evolution."
    )
    form_name: str = Field(
        description="the name of this form."
    )
    pokemon: "NamedAPIResource" = Field(
        description="The Pokémon that can take on this form."
    )
    types: list["PokemonFormType"] = Field(
        default_factory=list,
        description="A list of details showing types this Pokémon form has."
    )
    sprites: "PokemonFormSprites" = Field(
        description="A set of sprites used to depict this Pokémon form in the game."
    )
    version_group: "NamedAPIResource" = Field(
        description="The version group this Pokémon form was introduced in."
    )
    names: list["Name"] = Field(
        default_factory=list,
        description="The name of this resource listed in different languages."
    )
    form_names: list["Name"] = Field(
        default_factory=list,
        description="The form specific form name of this Pokémon form, or empty if the form does not have a specific name."
    )


class PokemonFormSprites(BaseModel):
    front_default: str = Field(
        description="The default depiction of this Pokémon form from the front in battle.")
    front_shiny: str = Field(
        description="The shiny depiction of this Pokémon form from the front in battle.")
    back_default: str = Field(
        description="The default depiction of this Pokémon form from the back in battle.")
    back_shiny: str = Field(
        description="The shiny depiction of this Pokémon form from the back in battle.")


class PokemonHabitat(BaseModel):
    id: int = Field(description="The identifier for this resource.")
    name: str = Field(description="The name for this resource.")
    names: list["Name"] = Field(
        default_factory=list,
        description="The name of this resource listed in different languages."
    )
    pokemon_species: list["NamedAPIResource"] = Field(
        default_factory=list,
        description="A list of Pokémon species that can be found in this habitat."
    )


class PokemonShape(BaseModel):
    id: int = Field(description="The identifier for this resource.")
    name: str = Field(description="The name for this resource.")
    awesome_names: list["AwesomeName"] = Field(
        default_factory=list,
        description="The scientific name of this Pokémon shape listed in different languages."
    )
    names: list["Name"] = Field(
        default_factory=list,
        description="The name of this resource listed in different languages."
    )
    pokemon_species: list["NamedAPIResource"] = Field(
        default_factory=list,
        description="A list of the Pokémon species that have this shape."
    )


class AwesomeName(BaseModel):
    awesome_name: str = Field(
        description="The localized \"scientific\" name for an API resource in a specific language."
    )
    language: "NamedAPIResource" = Field(
        description="The language this \"scientific\" name is in."
    )


class PokemonSpecies(BaseModel):
    id: int = Field(description="The identifier for this resource.")
    name: str = Field(description="The name for this resource.")
    order: int = Field(
        description="The order in which species should be sorted. Based on National Dex order, except families are grouped together and sorted by stage."
    )
    gender_rate: int = Field(
        description="The chance of this Pokémon being female, in eighths; or -1 for genderless."
    )
    capture_rate: int = Field(
        description="The base capture rate; up to 255. The higher the number, the easier the catch."
    )
    base_happiness: int = Field(
        description="The happiness when caught by a normal Pokéball; up to 255. The higher the number, the happier the Pokémon."
    )
    is_baby: bool = Field(
        description="Whether or not this is a baby Pokémon."
    )
    is_legendary: bool = Field(
        description="Whether or not this is a legendary Pokémon."
    )
    is_mythical: bool = Field(
        description="Whether or not this is a mythical Pokémon."
    )
    hatch_counter: int = Field(
        description="Initial hatch counter: one must walk Y x (hatch_counter + 1) steps before this Pokémon's egg hatches, unless utilizing bonuses like Flame Body's. Y varies per generation. In Generations II, III, and VII, Egg cycles are 256 steps long. In Generation IV, Egg cycles are 255 steps long. In Pokémon Brilliant Diamond and Shining Pearl, Egg cycles are also 255 steps long, but are shorter on special dates. In Generations V and VI, Egg cycles are 257 steps long. In Pokémon Sword and Shield, and in Pokémon Scarlet and Violet, Egg cycles are 128 steps long."
    )
    has_gender_differences: bool = Field(
        description="Whether or not this Pokémon has visual gender differences."
    )
    forms_switchable: bool = Field(
        description="Whether or not this Pokémon has multiple forms and can switch between them."
    )
    growth_rate: "NamedAPIResource" = Field(
        description="The growth rate of this Pokémon species."
    )
    pokedex_numbers: list["PokemonSpeciesDexEntry"] = Field(
        default_factory=list,
        description="A list of Pokedexes and the indexes reserved within them for this Pokémon species."
    )
    egg_groups: list["NamedAPIResource"] = Field(
        default_factory=list,
        description="A list of egg groups this Pokémon species is a member of."
    )
    color: "NamedAPIResource" = Field(
        description="The color of this Pokémon species for Pokédex search."
    )
    shape: "NamedAPIResource" = Field(
        description="The shape of this Pokémon for Pokédex search."
    )
    evolves_from_species: "NamedAPIResource" = Field(
        description="The Pokémon species that evolves into this Pokémon species."
    )
    evolution_chain: "APIResource" = Field(
        description="The evolution chain this Pokémon species is a member of."
    )
    habitat: "NamedAPIResource" = Field(
        description="The habitat this Pokémon species can be encountered in."
    )
    generation: "NamedAPIResource" = Field(
        description="The generation this Pokémon species was introduced in."
    )
    names: list["Name"] = Field(
        default_factory=list,
        description="The name of this resource listed in different languages."
    )
    pal_park_encounters: list["PalParkEncounterArea"] = Field(
        default_factory=list,
        description="A list of encounters that can be had with this Pokémon species in pal park."
    )
    flavor_text_entries: list["FlavorText"] = Field(
        default_factory=list,
        description="A list of localized flavor text for this Pokémon species."
    )
    form_descriptions: list["Description"] = Field(
        default_factory=list,
        description="Descriptions of different forms Pokémon take on within the Pokémon species."
    )
    genera: list["Genus"] = Field(
        default_factory=list,
        description="The genus of this Pokémon species listed in multiple languages."
    )
    varieties: list["PokemonSpeciesVariety"] = Field(
        default_factory=list,
        description="A list of the Pokémon that exist within this Pokémon species."
    )


class Genus(BaseModel):
    genus: str = Field(
        description="The localized genus for this Pokémon species."
    )
    language: "NamedAPIResource" = Field(
        description="The language this genus is in."
    )


class PokemonSpeciesDexEntry(BaseModel):
    entry_number: int = Field(
        description="The index number within the Pokédex."
    )
    pokedex: "NamedAPIResource" = Field(
        description="The Pokédex the referenced Pokémon species can be found in."
    )


class PalParkEncounterArea(BaseModel):
    base_score: int = Field(
        description="The base score given to the player when this Pokémon is caught during a pal park run."
    )
    rate: int = Field(
        description="The base rate for encountering this Pokémon in this pal park area."
    )
    area: "NamedAPIResource" = Field(
        description="The pal park area where this encounter happens."
    )


class PokemonSpeciesVariety(BaseModel):
    is_default: bool = Field(
        description="Whether this variety is the default variety."
    )
    pokemon: "NamedAPIResource" = Field(
        description="The Pokémon variety."
    )


class Stat(BaseModel):
    id: int = Field(description="The identifier for this resource.")
    name: str = Field(description="The name for this resource.")
    game_index: int = Field(
        description="The identifier for this resource in game indices."
    )
    is_battle_only: bool = Field(
        description="Whether this stat only exists within a battle."
    )
    affecting_moves: "MoveStatAffectSets" = Field(
        description="A detail of moves which affect this stat positively or negatively."
    )
    affecting_natures: "NatureStatAffectSets" = Field(
        description="A detail of natures which affect this stat positively or negatively."
    )
    characteristics: list["APIResource"] = Field(
        default_factory=list,
        description="A list of characteristics that are set on a Pokémon when its highest base stat is this stat."
    )
    move_damage_class: "NamedAPIResource" = Field(
        description="The class of damage this stat is directly related to."
    )
    names: list["Name"] = Field(
        default_factory=list,
        description="The name of this resource listed in different languages."
    )


class MoveStatAffectSets(BaseModel):
    increase: list["MoveStatAffect"] = Field(
        default_factory=list,
        description="A list of moves and how they change the referenced stat."
    )
    decrease: list["MoveStatAffect"] = Field(
        default_factory=list,
        description="A list of moves and how they change the referenced stat."
    )


class MoveStatAffect(BaseModel):
    change: int = Field(
        description="The amount of change."
    )
    move: "NamedAPIResource" = Field(
        description="The move being referenced."
    )


class NatureStatAffectSets(BaseModel):
    increase: list["NamedAPIResource"] = Field(
        default_factory=list,
        description="A list of natures and how they change the referenced stat."
    )
    decrease: list["NamedAPIResource"] = Field(
        default_factory=list,
        description="A list of nature sand how they change the referenced stat."
    )


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

    def __init__(self, **data) -> None:
        super().__init__(**data)
        self.generation = _get_generation()
        self.moves = [_get_move()(**move)  # type: ignore
                      for move in self.moves]


class TypePokemon(BaseModel):
    slot: int = Field(
        description="The order the Pokémon's types are listed in."
    )
    pokemon: "NamedAPIResource" = Field(
        description="The Pokémon that has the referenced type."
    )


class TypeRelations(BaseModel):
    no_damage_to: list["NamedAPIResource"] = Field(
        default_factory=list,
        description="A list of types this type has no effect on."
    )
    half_damage_to: list["NamedAPIResource"] = Field(
        default_factory=list,
        description="A list of types this type is not very effective against."
    )
    double_damage_to: list["NamedAPIResource"] = Field(
        default_factory=list,
        description="A list of types this type is very effective against."
    )
    no_damage_from: list["NamedAPIResource"] = Field(
        default_factory=list,
        description="A list of types that have no effect on this type."
    )
    half_damage_from: list["NamedAPIResource"] = Field(
        default_factory=list,
        description="A list of types that are not very effective against this type."
    )
    double_damage_from: list["NamedAPIResource"] = Field(
        default_factory=list,
        description="A list of types that are very effective against this type."
    )


class TypePastRelations(BaseModel):
    generation: "NamedAPIResource" = Field(
        description="The generation in which the referenced type had the listed damage relations."
    )
    damage_relations: "TypeRelations" = Field(
        description="The damage relations the referenced type had up to and including the listed generation"
    )
