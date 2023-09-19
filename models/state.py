#!/usr/bin/python3
"""State Module for HBNB project."""
from models.base_model import BaseModel

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

import os
env_value = os.environ.get('HBNB_TYPE_STORAGE')


class State(BaseModel):
    """State class."""

    __tablename__ = "states"
    if env_value == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state')
    name = ""

    @property
    def cities(self):
        """Cities for State.

        Returns:
            _type_: _description_
        """
        from models.__init__ import storage
        from models.city import City
        obj_list = []
        strg = storage.all(City)
        for value in strg:
            if self.id == value.state_id:
                obj_list.append(value)
        return obj_list
