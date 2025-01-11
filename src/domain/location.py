from pydantic import BaseModel, Field


class Location(BaseModel):
    prefecture: str = Field(alias="pref")
    city: str
    id_: str = Field(alias="id")
