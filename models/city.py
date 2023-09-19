#!/usr/bin/python3
"""City Module for HBNB project."""
from models.base_model import BaseModel


class City(BaseModel):
    """The city class, contains state ID and name."""

    __tablename__ = "cities"
    state_id = ""
    name = ""
