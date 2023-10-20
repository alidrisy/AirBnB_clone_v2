#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy import DateTime, String, Column
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime(), nullable=False,
                        default=datetime.utcnow())
    updated_at = Column(DateTime(), nullable=False,
                        default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if kwargs:
            if 'updated_at' in kwargs.keys():
                kwargs['updated_at'] = datetime.fromisoformat(
                        kwargs['updated_at'])
            else:
                self.updated_at = datetime.utcnow()
            if 'created_at' in kwargs.keys():
                kwargs['created_at'] = datetime.fromisoformat(
                        kwargs['created_at'])
            else:
                self.created_at = datetime.utcnow()
            if 'id' not in kwargs.keys():
                self.id = str(uuid.uuid4())
            if '__class__' in kwargs.keys():
                del (kwargs['__class__'])

            self.__dict__.update(kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()

    def __str__(self):
        """Returns a string representation of the instance"""
        dict1 = dict(self.__dict__)
        if '_sa_instance_state' in dict1.keys():
            del (dict1['_sa_instance_state'])
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, dict1)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if '_sa_instance_state' in dictionary.keys():
            del (dictionary['_sa_instance_state'])
        return dictionary

    def delete(self):
        """delete the current instance from the storage"""
        from models import storage
        storage.delete(self)
