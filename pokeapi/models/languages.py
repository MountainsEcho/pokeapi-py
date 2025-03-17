from __future__ import annotations
from pydantic import BaseModel, Field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .common import Name


class Language(BaseModel):
    id: int = Field(description="The identifier for this resource.")
    name: str = Field(description="The name for this resource.")
    official: bool = Field(description="Whether this language is the primary language "
                           "for API responses.")
    iso639: str = Field(description="The two-letter code of the country. "
                        "Note that this is not Unique")
    iso3166: str = Field(description="The two-letter code of the language. "
                         "Note that this is not Unique")
    names: list["Name"] = Field(default_factory=list, description="The name of this resource "
                                "listed in different languages.")
