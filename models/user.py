#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

import os
env_value = os.environ.get('HBNB_TYPE_STORAGE')


class User(BaseModel):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    if env_value == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship('Place', backref='user')
        reviews = relationship('Review', backref='user')
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
