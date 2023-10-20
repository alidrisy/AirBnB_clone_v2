#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, merge, save-update',
                          backref='state')

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """getter attribute cities that returns the list of City"""
            from models import storage
            dict1 = storage.all("City")
            list1 = []
            for v in dict1.values():
                if v.state_id == self.id:
                    list1.append(v)
            return list1
